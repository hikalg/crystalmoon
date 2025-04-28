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
            "playerScore" : 0,
            "playerPerformance" : 0,
        },
        
        "player2" : {
            "playerScore" : 0,
            "playerPerformance" : 0,
        }
    }
    
    matchAnalytics = {
        
        "player1" : {

            "baseChange" : 0,
            "polarity": 0,
            "ratioToMedian": 0,
        },
        
        "player2" : {

            "baseChange" : 0,
            "polarity": 0,
            "ratioToMedian": 0,
        },
    }
    
    matchAnalyticsGeneral = {
        "averageRating" : 0,
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
        
        scoreOne = self.matchInformation['player1']['playerScore']
        scoreTwo = self.matchInformation['player2']['playerScore']
        if (scoreOne > scoreTwo): return self.matchPlayers['player1']
        elif (scoreOne < scoreTwo): return self.matchPlayers['player2']
        elif (scoreOne == scoreTwo): return "Tie"
        else: return 0
                
        
    def setPolarity(self):
        playerOne = self.matchPlayers['player1']
        playerTwo = self.matchPlayers['player2']
        
        ratingOne = self.matchPlayers['player1']['playerRating']
        ratingTwo = self.matchPlayers['player2']['playerRating']
        
        if (self.winner() == playerOne): 
            self.matchAnalytics['player1']['polarity'] = 1
            self.matchAnalytics['player2']['polarity'] = -1
            
        if (self.winner() == playerTwo): 
            self.matchAnalytics['player1']['polarity'] = -1
            self.matchAnalytics['player2']['polarity'] = 1
            
        if (self.winner() == "Tie"):
            
            if (ratingOne > ratingTwo):
                self.matchAnalytics['player1']['polarity'] = -0.5
                self.matchAnalytics['player2']['polarity'] = 0.5
                
            if (ratingOne < ratingTwo):
                self.matchAnalytics['player1']['polarity'] = 0.5
                self.matchAnalytics['player2']['polarity'] = -0.5
                
            if (ratingOne == ratingTwo):
                self.matchAnalytics['player1']['polarity'] = 0.25
                self.matchAnalytics['player2']['polarity'] = 0.25
            
    def calculateRatio(self):
        
        ratingOne = self.matchPlayers['player1']['playerRating']
        ratingTwo = self.matchPlayers['player2']['playerRating']
        ratingAvg = (ratingOne + ratingTwo) / 2
        
        self.matchAnalytics['player1']['ratioToMedian'] = ratingOne / ratingAvg
        self.matchAnalytics['player2']['ratioToMedian'] = ratingTwo / ratingAvg
        
    def calculateBaseChange(self):
        
        playerOne = self.matchPlayers['player1']
        playerTwo = self.matchPlayers['player2']
        
        ratingOne = self.matchPlayers['player1']['playerRating']
        ratingTwo = self.matchPlayers['player2']['playerRating']
        ratingDifference = ratingOne - ratingTwo
        
        if (ratingDifference <= 100):
            return 1
        elif (ratingDifference > 100 and ratingDifference <= 200):
            return 2
        else: return 3