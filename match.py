import player as p
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
        return self.matchScore['player1'], self.matchScore['player2']
    
    # Set game score of each player
    def score(self, playerNumber : int, score : int):
        
        # Prints error is playerNumber is not a number
        if (not isinstance(playerNumber, int)):
            print('Player is not a number')
            return -1
        
        # Prints error if score is not a number
        if (not isinstance(score, int)):
            print('Score is not a number')
        
        match playerNumber:
            case 1:
                self.matchScore['player1'] = score
            case 2:
                self.matchScore['player2'] = score
            case _:
                print (f"Player not found")
                return -1