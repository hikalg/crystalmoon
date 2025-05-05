import player as p
import numpy as np
class Match:
    # Players (Player objects)
    players : list
    
    # Match score (Empty dict)
    matchScore = {
        
    }
    
    # Match data (Empty dict)
    matchData = {
        
    }
    
    # Match analytics (Empty dict)
    ratingCalc = {
        
    }
    
    def __init__(self, player1 : p.Player, player2 : p.Player):
        self.players = [player1, player2]
        self.matchScore = {
            "player1" : 0,
            "player2" : 0,
        }
        self.matchData = {
            "winner": None,
            "ratingDifference" : 0,
            "ratingAverage" : 0,
        }
        self.ratingCalc = {
            "player1" : {
                "baseChange" : 0,
                "polarity" : 0,
                "multiplier" : 0,
            },
             "player2" : {
                "baseChange" : 0,
                "polarity" : 0,
                "multiplier" : 0,
            },
            
        }
    
    # Scoring functions
    
    # Instantly set game score
    def quickScore(self, score1 : int, score2 : int):
        self.matchScore = {
            "player1" : score1,
            "player2" : score2,
        }
        
        print ((self.matchScore['player1'], self.matchScore['player2']))
        return 0
    
    # Set game score of each player
    def setScore(self, playerNumber : int, score : int):
        
        # Prints error is playerNumber is not a number
        if (not isinstance(playerNumber, int)):
            print('Player is not a number')
            return -1
        
        # Prints error if score is not a number
        if (not isinstance(score, int)):
            print('Score is not a number')
            return -1
        
        match playerNumber:
            case 1:
                self.matchScore['player1'] = score
                return 0
            case 2:
                self.matchScore['player2'] = score
                return 0
            case _:
                print (f"Player not found")
                return -1
            
    # Sets winning player
    def winner(self):
        score1 = self.matchScore['player1']
        score2 = self.matchScore['player2']
        
        if (score1 > score2):
            print (f"Winner is {self.players[0].playerData["playerName"]}")
            self.matchData['winner'] = self.players[0]
            return self.players[0]
            
        if (score1 < score2):
            print (f"Winner is {self.players[1].playerData["playerName"]}")
            self.matchData['winner'] = self.players[1]
            return self.players[1]
        
        print("There is a tie")
        return (self.players[0], self.players[1])

    # Finds difference in rating
    def ratingAverage(self):
        rating1 = self.players[0].playerData['playerRating']
        rating2 = self.players[1].playerData['playerRating']
        
        ratingAverage = (rating1 + rating2) / 2
        
        self.matchData["ratingAverage"] = ratingAverage
        
        return ratingAverage
        
    # Calculates multiplier of both players
    def ratingMultiplier(self):
        rating1 = self.players[0].playerData['playerRating']
        rating2 = self.players[1].playerData['playerRating']
        
        ratingAverage = self.ratingAverage()
        
        multiplier1 = np.round(rating1 / ratingAverage, 2)
        multiplier2 = np.round(rating2 / ratingAverage, 2)
        
        self.ratingCalc['player1']['multiplier'] = multiplier1
        
        self.ratingCalc['player2']['multiplier'] = multiplier2
        
        return multiplier1, multiplier2