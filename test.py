import player as p
import match as m

p1 = p.Player("musket")
p1.setRating(1700)
p2 = p.Player("rifle")
p2.setRating(1200)

mx = m.Match(p1, p2)
x = mx.quickScore(4, 2)
mx.winner()
mx.ratingAverage()
print(mx.matchData['ratingAverage'])
print(mx.ratingMultiplier())