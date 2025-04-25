import player as p
import numpy as np

class Match:
    matchPlayers = {
        "player1" : {
            "playerObject" : p.Player,
            "playerRating" : float,
        },
        
        "player2" : {
            "playerObject" : p.Player,
            "playerRating" : float,
        },
    }
    
    matchInformation = {
        "player1" : {
            "playerRating" : matchPlayers["player1"]["playerRating"],
            "playerScore" : 0,
        },
        
        "player2" : {
            "playerRating" : matchPlayers["player2"]["playerRating"],
            "playerScore" : 0,
        }
    }
    
    matchAnalytics = {
        
        "player1" : {
            "playerRating" : matchPlayers["player1"]["playerRating"],
            "playerScore" : matchInformation["player1"]["playerScore"],
            "baseChange" : 0,
            "polarity": 0,
            
        },
        
        "player2" : {
            "playerRating" : matchPlayers["player2"]["playerRating"],
            "playerScore" : matchInformation["player2"]["playerScore"],
            "baseChange" : 0,
            "polarity": 0,
        },
    }
    
    
    # Initialises match object
    def __init__(self, player1: p.Player, player2: p.Player):
        
        # Player objects provided - initialises match based on existing player parameters
        
        # Player 1
        self.matchPlayers['player1']['playerObject'] = player1
        self.matchPlayers['player1']['playerRating'] = player1.playerData['playerRating']
        
        # Player 2
        self.matchPlayers['player2']['playerObject'] = player2
        self.matchPlayers['player2']['playerRating'] = player2.playerData['playerRating']
        
    def setScore(self, x, y):
        self.matchInformation['player1']['playerScore'] = x
        self.matchInformation['player2']['playerScore'] = y
            
    def findBottom(self):
        
        if (self.matchInformation['player1']['playerRating'] == self.matchInformation['player1']['playerRating']): 
            return "Tie"
        
        if (self.matchInformation['player1']['playerRating'] < self.matchInformation['player1']['playerRating']):
            return self.matchPlayers['player1']
        else: return self.matchPlayers['player2']
        
    def winner(self):
        
        # if (self.matchInformation['player1']['playerScore'] == self.matchInformation['player1']['playerScore']): 
        #     return "Tie", "Tie"
        
        if (self.matchInformation['player1']['playerScore'] > self.matchInformation['player2']['playerScore']):
            print(f"The winner is {self.matchPlayers['player1']['playerObject'].playerData['playerName']}")
            return self.matchPlayers['player1']['playerObject']
        else: return self.matchPlayers['player2']
        
    def setPolarity(self):
        
        if (self.winner() == self.matchPlayers['player1']['playerObject']): 
            self.matchAnalytics['player1']['polarity'] = 1
            self.matchAnalytics['player2']['polarity'] = -1