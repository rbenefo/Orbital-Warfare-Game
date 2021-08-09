class Planet:
    def __init__(self, x,y, s, m, img):
        self.pos = PVector(x,y)
        self.s = int(s*1.5)
        
        self.mass = m
        self.img = img
        self.img.resize(self.s, self.s)
        self.atmosphere_radius = self.s*1.2

        self.pg =createGraphics(self.s,self.s)
    def draw(self):
        noStroke()
        fill(227, 247, 255) #later, use gradient for this
        circle(self.pos[0], self.pos[1], self.atmosphere_radius)

        fill(175, 233, 255)
        circle(self.pos[0], self.pos[1], self.s)
        # self.pg.beginDraw()
        # self.pg.noStroke()
        # self.pg.background(0)
        # self.pg.fill(255)
        # self.pg.ellipse(self.s/2, self.s/2, self.s, self.s)
        # self.pg.endDraw()
        # self.img.mask(self.pg.get())
        # imageMode(CENTER)
        # image(self.img, self.pos[0],self.pos[1])
        
