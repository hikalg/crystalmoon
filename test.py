import player as p
import match as m

p1 = p.Player("musket")
p1.adjustRating(1500)
p2 = p.Player("rifle")
p2.adjustRating(800)
mx = m.Match(p1, p2)
mx.setScore(2, 0)
mx.winner()
mx.setPolarity()

# one = mx.returnOnePlus()
print(f"{mx.matchAnalytics['player1']['polarity']}")
# print(one)

