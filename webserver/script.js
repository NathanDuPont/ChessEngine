let currentImg = 0;

let blackPlayer;
let whitePlayer;

function isWhiteMove(){
    return currentImg % 2 === 1
}

function checkNextMove(){
    if (isWhiteMove() && whitePlayer === 'bot'){
        //white player is a bot, request next image imediately
        requestNextImg()
    } else if (!isWhiteMove() && blackPlayer === 'bot') {
        //black player is a bot, request next image imediately
        requestNextImg()
    } else {
        //player is up
        $('#chessTable').click(function(event){
            let x = event.pageX - $(this).offset().left
            let y = event.pageY - $(this).offset().top
            //picture is 750 px by 750 px, black board edges are 30 px wide
            let x_selection = Math.floor((x - 30)/(690/8))
            let y_selection = Math.floor((y - 30)/(690/8))
            // let x_char = String.fromCharCode(97 + x_selection)
            // alert(x_selection + "" + y_selection)

            //check if the user did not click on the margin
            if(!((x_selection < 0 || x_selection > 7) || (y_selection < 0 || y_selection > 7))){
                y_move_selection = 0

                if (!isWhiteMove()) {
                    y_move_selection = 8 - y_selection
                } else {
                    y_move_selection = y_selection + 1
                }

                let x_char = String.fromCharCode(97 + x_selection)

                //create highlight square
                let highlight = document.createElement("div")
                highlight.className = "highlight"
                $('body').append(highlight)
                highlight.style.top = ($(this).offset().top + 30 + y_selection * (690/8)) + 'px'
                highlight.style.left = ($(this).offset().left + 30 + x_selection * (690/8)) + 'px'

                legalMoves = requestLegalMoves(x_char + y_move_selection)
                
            }
        })
    }

}

function requestLegalMoves(piece){
    $.ajax({
        url: 'legalmoves',
        type: 'POST',
        data: {
            piecePos: piece
        },
        success: function(msg) { //triggers when response message of 200 is sent
            legalMoves = msg.replace(' ', '').substring(("{legalmoves:[").length, msg.length - 2).split(',')
            if (legalMoves[0] === ''){ // no moves could be found
                alert('no moves')
            } else {
                legalMoves.forEach((move, index) => {
                    alert(move + '\n' + move.substring(3,5))
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
            $('#chessTable').html(response);
        }
    });
    // wait until the chess table has loaded
    $('#chessTable').promise().done(function () {
        currentImg++
    
        checkNextMove()
    })
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

$(document).ready(function() {
    $(document).on('click', '#test', function() {
        $.ajax({
            url: 'playerdata',
            type: 'POST',
            data: {
                playerDataField: "1 2 1 4"
            },
            success: function(msg) { //triggers when response message of 200 is sent
                requestNextImg()
            }               
        });
    });

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
                alert("game starting")

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


