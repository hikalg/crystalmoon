import player as p
import match as m

p1 = p.Player("musket")
p2 = p.Player("rifle")

mx = m.Match(p1, p2)
x = mx.score(4, 4)
print(x)
