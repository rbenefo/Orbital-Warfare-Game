class Planet:
    def __init__(self, x,y, s, m, img):
        self.pos = PVector(x,y)
        self.s = int(s*1.5)
        
        self.mass = m
        self.img = img.PLANET
        self.img.resize(self.s, self.s)
        self.atmosphere_radius = int(self.s*1.3)
        
    def draw(self):
        noStroke()
        h = self.atmosphere_radius - self.s
        for i in range(self.atmosphere_radius, 0, -1):
            if i < self.s-10:
                fill(color(3,3,22))
            else:
                fill(lerpColor(color(252, 82, 255),color(3,3,22), float(i-self.s)/float(h)))

            circle(self.pos[0], self.pos[1], i)

        imageMode(CENTER)
        image(self.img, self.pos[0],self.pos[1])
