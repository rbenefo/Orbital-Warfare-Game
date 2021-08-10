class CoilgunRound:
    def __init__(self, pos, vel):
        self.pos= pos
        self.vel = vel
        self.accel = PVector(0,0)
        self.type = "coilgun"
        self.s = 2
        
        self.reentering = False
        self.reentry_coloring = color(255, 163, 71)
    def applyAccel(self, accel):
        self.accel = accel
        
    def draw(self):
        noStroke()
        if not self.reentering:
            fill(255, 255, 255)
        else:
            fill(lerpColor(color(255, 255, 255), self.reentry_coloring,0.5))
        circle(self.pos[0], self.pos[1], self.s)
