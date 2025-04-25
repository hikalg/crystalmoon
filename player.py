class Player:
    playerData = {
        "playerName": "unknown",
        "playerRating": 1000.00
    }
    
    # Initialises player object
    def __init__(self, playerName):
        self.playerData['playerName'] = playerName
        
    # String format of object
    def __str__(self):
        return f"This is {self.playerData["playerName"]} with a rating of {self.playerData["playerRating"]}"
    
    # Manually sets rating
    def setRating(self, rating):
        self.playerData["playerRating"] = rating
        print(f"Rating successfully set to {self.playerData["playerRating"]}")
        return 1
    
    # Manually changes player name
    def changeName(self, name):
        self.playerData['playerName'] = name
        print(f"Name changed successfully to {self.playerData["playerRating"]}")
        return 1
    
    # Changes rating by value
    def adjustRating(self, value):
        self.playerData['playerRating'] += value
        
    