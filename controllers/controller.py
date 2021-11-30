from flask import render_template, request
from app import app
from models.player import Player
from models.game import Game
import random


@app.route('/')
def index():
    return render_template('intro.html')

@app.route('/play', methods=['POST','GET'])
def play():
    return render_template('play.html')
    

@app.route('/evaluate', methods=['POST'])
def evaluate():
    player_1 = Player( request.form['name_1'], request.form['player_1'] )
    player_2 = Player( request.form['name_2'], request.form['player_2'] )
    #name = "Computer", choice = random.choice(["rock", "scissors", "paper"])

    winner, loser = Game.Evaluate(player_1, player_2)
    return render_template('result.html', winner=winner, loser=loser)
    