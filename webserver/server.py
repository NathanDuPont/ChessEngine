# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
from os import truncate
import time
import re
from os.path import exists
import time

# from chess import engine
# from engine import Engine

import sys

import chess
from chess.svg import board

# from chess import engine
sys.path.insert(1, '../src')
from util import get_piece_utility

from agents import CustomAgent
from base_agent import BaseAgent
from player_agent import PlayerAgent

from web_engine_adaper import WebEngine
# from agents import CustomAgent

hostName = "localhost"
serverPort = 8080

#hardcoding files into the file to make my life easier
files = {"/": "index.html", "/script.js": "script.js", "/style.css": "style.css", "/index": "index.html", "/startmenue.html": "startmenue.html"}
files_types = {"index.html": "text/html", "script.js": "text/javascript", "style.css": "text/css", "startmenue.html": "text/html"}
player_choices = ['player:player', 'CustomAgent:bot', 'BaseAgent:bot'] #first part is the title, the second part tells the js what the choice is

#had to declare these variables as global
img_location =""
engine = None
player_white = None
player_black = None

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        global engine
        global img_location

        def createHeader(content_type):
            self.send_response(200)
            if content_type != None: self.send_header("Content-type", content_type)
            self.end_headers()

        def sendContent(content_type, filename):
            createHeader(content_type)
            with open(filename, 'r') as data:
                self.wfile.write(bytes(data.read(), "utf-8"))
        
        def sendStringContent(content_type, data):
            createHeader(content_type)
            self.wfile.write(bytes(data, "utf-8"))

        if self.path in files:
            file = files[self.path]

            if file == "startmenue.html":
                html_options = ""
                for choice in player_choices:
                    html_options += '<option value="' + choice + '">' + choice + '</option>'
                
                with open(file, 'r') as startMenu:
                    data = startMenu.read()
                    data = re.sub('<-P->', html_options, data)
                    sendStringContent(files_types[file], data)
            else:
                sendContent(files_types[file], file)

        elif ".svg" in self.path:
            img_number = self.path[5:-4]  # [5, -4] removes /move and .svg from file

            if exists(img_location + 'move' + img_number + '.svg'):
                sendContent(None, img_location + self.path[1:])
            
            elif img_number == "0" or exists(img_location + 'move' + str( int(img_number) - 1) + '.svg'):
                print('getting next img')
                print(img_location)

                engine.next()

                for x in range(5 * 600): # wait a maximum of 5 minutes
                    time.sleep(0.1)
                    if exists(img_location + 'move' + img_number + '.svg'):
                        break
                    
                if (img_location + 'move' + img_number + '.svg'):
                    sendContent(None, img_location + self.path[1:])
                else:
                    print('error')
                    sendContent(400) #error occurred
            
                
        else:
            self.send_response(404)
    
    def do_POST(self):
        global engine

        def getBotChoice(choice, isWhite):
            if choice == "CustomAgent":
                return CustomAgent(isWhite)
            elif choice == "BaseAgent":
                return BaseAgent(isWhite)
            elif choice == "player":
                return PlayerAgent(isWhite)
            else:
                return None

        def startChess(white_choice, black_choice):
            global player_white
            global player_black

            player_white = getBotChoice(white_choice, True)
            player_black = getBotChoice(black_choice, False)

            #this is not ideal
            global engine
            global img_location

            engine = WebEngine(player_white, player_black)
            img_location = engine.get_img_location() + '/'
            print('game_started')
            print(img_location)

        def makeMove(next_move):
            isWhite = True if next_move[:1] == 'w' else False
            player = engine.get_player(isWhite)
            player.set_next_move(next_move[1:])
            

        def sendResponce(responce_code):
            self.send_response(responce_code)
            self.end_headers()

        #repeat from above
        def createHeader(content_type):
            self.send_response(200)
            if content_type != None: self.send_header("Content-type", content_type)
            self.end_headers()

        #repeat from above
        def sendContent(content_type, filename):
            createHeader(content_type)
            with open(filename, 'r') as data:
                self.wfile.write(bytes(data.read(), "utf-8"))
        
        #repeat from above
        def sendStringContent(content_type, data):
            createHeader(content_type)
            self.wfile.write(bytes(data, "utf-8"))

        post_headers = self.headers.as_string().split('\n')

        content_lenght = -1
        for header in post_headers:
            if 'Content-Length:' in header:
                content_lenght = int(header.replace("Content-Length: ", ""))
                break
        
        if content_lenght == -1:
            sendResponce(400)

        request = self.requestline.split(' ')[1]

        if(request == '/playerdata'):
            data = self.rfile.read(content_lenght).decode('ASCII')[16:] # remove the data tag
            move = data.split('+')[0]
            print(move)
            print(type(move))
            makeMove(move)
            print('next move ' + str(move))
            sendResponce(200)

        elif(request == '/start'):
            data = self.rfile.read(content_lenght).decode('ASCII')
            players = data[len('players='):].split('+')
            startChess(players[0], players[1])
            sendResponce(200)

        elif(request == '/legalmoves'):
            data = self.rfile.read(content_lenght).decode('ASCII')
            piece = data[len('piecePos='):]
            print(piece)
            legalMoves = None
            if piece[:1] == 'b':
                legalMoves = player_black.get_legal_moves(engine.board)
            else:
                legalMoves = player_white.get_legal_moves(engine.board)
            print(legalMoves)
            legalPieceMoves = [move for move in legalMoves if move[:2] == piece[1:]]
            print(legalPieceMoves)

            sendStringContent(None, "{legalmoves:" + str(legalPieceMoves) + "}")
        
        elif(request =='/boardScore'):
            def getScore(board):
                value = sum(
                get_piece_utility(board.piece_at(square))
                if board.piece_at(square) is not None
                else 0
                for square in chess.SQUARES)
                return value
            
            #return score
            score = getScore(engine.board)
            print(engine.board)
            print("board score is " + str(score))
            sendStringContent(None, "{boardScore:" + str(score) + "}")

            

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")