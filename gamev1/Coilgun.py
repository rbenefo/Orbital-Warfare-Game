class CoilgunRound:
    def __init__(self, pos, vel):
        self.pos= pos
        self.vel = vel
        self.accel = PVector(0,0)
        self.type = "coilgun"
        self.s = 2
    def applyAccel(self, accel):
        self.accel = accel
        
    def draw(self):
        noStroke()
        fill(255, 255, 255)
        circle(self.pos[0], self.pos[1], self.s)
