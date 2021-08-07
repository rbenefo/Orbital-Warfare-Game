class Planet:
    def __init__(self, x,y, s, m):
        self.pos = PVector(x,y)
        self.s = s
        
        self.mass = m
    def draw(self):
        fill(0, 102, 204)
        noStroke()
        circle(self.pos[0], self.pos[1], self.s)
