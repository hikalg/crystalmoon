import player as p
import match as m

p1 = p.Player("musket")
p2 = p.Player("rifle")

p1.setRating(1500)
p2.setRating(800)
mx = m.Match(p1, p2)
mx.setScore(4, 4)
mx.setPolarity()
a = mx.calculateBaseChange()


print(f"{mx.matchAnalytics['player1']['polarity']}")
print(a)
print(mx.matchPlayers['player1']['playerRating'])
print(mx.matchPlayers['player2']['playerRating'])
print(p1.playerData['playerRating'])
