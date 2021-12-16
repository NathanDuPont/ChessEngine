let currentImg = 0;

let blackPlayer;
let whitePlayer;

let yellowHighlight = "rgba(251, 255, 0, 0.3)"
let blueHighlight = "rgba(0, 229, 255, 0.3)"

function isWhiteMove(){
    return (currentImg % 2 === 1)
}

function switchTurnMarkers(isWhite){
    let white = document.getElementById('whitePlayerMove')
    white.style.visibility = ''
    let black = document.getElementById('blackPlayerMove')
}

//if white, y coord needs to be reversed
function translateYCoord(y, isWhite){
    // if (isWhite){
    //     return 8 - y
    // } else {
    //     return y + 1
    // }
    return 8 - y
}

function getBordPos(move, isWhite) {
    y = parseInt(move.substring(4,5))
    y = translateYCoord(y, isWhite)

    x = move.charCodeAt(3) - 97
    return [x, y]
}

function convertCoordsToMove(x, y, isWhite){
    y_move_selection = translateYCoord(y, isWhite)

    let x_char = String.fromCharCode(97 + x)
    return x_char + y_move_selection
}

function getClickPos(client, event){
    let x = event.pageX - client.offset().left
    let y = event.pageY - client.offset().top
    //picture is 750 px by 750 px, black board edges are 30 px wide
    let x_selection = Math.floor((x - 30)/(690/8))
    let y_selection = Math.floor((y - 30)/(690/8))

    return [x_selection, y_selection]
}

function createHighlight(client, x, y, color, piecePos = false, playerColor){
    //create highlight square
    let highlight = document.createElement("div")
    highlight.className = "highlight"
    $('body').append(highlight)
    highlight.style.top = (client.offset().top + 30 + y * (690/8)) + 'px'
    highlight.style.left = (client.offset().left + 30 + x * (690/8)) + 'px'
    highlight.style.backgroundColor = color

    if (piecePos != false){
        highlight.addEventListener('click', function(event) {
            let pos = getClickPos($('#chessTable'), event) //need to convert hightlight into a jquery element
            let move = convertCoordsToMove(pos[0], pos[1], isWhiteMove())

            sendPlayerMove(playerColor + piecePos + move)
        })
    }
}

function clearTable(){
    $('#chessTable').off('click') //turn off click if it is on
    $('.highlight').remove() //removes any highlight
}

function updateGameScore(score){
    document.getElementById('boardScore').innerHTML = score.substring(("boardScore:").length + 1, score.length - 1)
}

function checkNextMove(){
    clearTable()
    getBoardScore()
    switchTurnMarkers(isWhiteMove())

    if (isWhiteMove() && whitePlayer === 'bot'){
        //white player is a bot, request next image imediately
        requestNextImg()
    } else if (!isWhiteMove() && blackPlayer === 'bot') {
        //black player is a bot, request next image imediately
        requestNextImg()
    } else {
        //player is up
        $('#chessTable').click(function(event){

            //remove previous highlight
            $('.highlight').remove()

            let pos = getClickPos($(this), event)
            let x_selection = pos[0]
            let y_selection = pos[1]

            //check if the user did not click on the margin
            if(!((x_selection < 0 || x_selection > 7) || (y_selection < 0 || y_selection > 7))){
                legalMoves = requestLegalMoves(convertCoordsToMove(x_selection, y_selection, isWhiteMove()), $(this), x_selection, y_selection, isWhiteMove())  
            }
        })
    }

}

function requestLegalMoves(piece, client, x, y, isWhite){
    player = isWhite ? 'w' : 'b';
    $.ajax({
        url: 'legalmoves',
        type: 'POST',
        data: {
            piecePos: (player + piece)
        },
        success: function(msg) { //triggers when response message of 200 is sent
            legalMoves = msg.replaceAll(' ', '').substring(("{legalmoves:[").length, msg.length - 2).split(',')
            if (legalMoves[0] === ''){ // no moves could be found
            } else {
                createHighlight(client, x, y, blueHighlight, false, null) //this is where the piece is
                legalMoves.forEach((move) => {
                    boardPos = getBordPos(move, isWhite)
                    //these are the possible moves
                    playerSymbol = isWhite ? 'w' : 'b';
                    createHighlight(client, boardPos[0], boardPos[1], yellowHighlight, piecePos=piece, playerSymbol)
                })
            }
        }               
    });
}

function requestNextImg(){
    $.ajax({
        url: 'move' + currentImg + '.svg',
        method: "GET",
        success: function(response) {
            $.when(
                $('#chessTable').html(response.substring(4))

            ).done(function(){
                if (response.substring(0,4) === 'GaOv'){
                    alert('Game Has Finished')
                }
                currentImg++
    
                checkNextMove()
            }); 
        }
    });
}

function sendPlayerMove(move){
    $.ajax({
        url: 'playerdata',
        type: 'POST',
        data: {
            playerDataField: move
        },
        success: function(msg) { //triggers when response message of 200 is sent
            requestNextImg()
        }               
    });
}

function requestStartMenue(){
    $.ajax({
        url: "startmenue.html",
        method: "GET",
        success: function(response) {
            $('#chessTable').html(response);
        }
    });
}

function getBoardScore(){
    $.ajax({
        url: "boardScore",
        method: "POST",
        success: function(response) {
            updateGameScore(response)
        }
    })
}

$(document).ready(function() {
    $(document).on('click', '#start', function() {
        player1 = $('#player1').val().split(':')
        player2 = $('#player2').val().split(':')
        $.ajax({
            url: 'start',
            type: 'POST',
            data: {
                players: player1[0] + " " + player2[0]
            },
            success: function(msg) { //triggers when response message of 200 is sent
                
                whitePlayer = player1[1]
                blackPlayer = player2[1]
                requestNextImg()
            }               
        });
    });
});


$(document).ready(function () {
    $(document).on('click', '#next', function () {
        requestNextImg()
    });
});

requestStartMenue()


