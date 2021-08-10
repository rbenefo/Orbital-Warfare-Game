class GUI:
    def __init__(self, width, height, img):
        self.width = width
        self.height = height
        self.indicator_img = img.INDICATOR
        self.indicator_base = img.INDICATOR_BASE
        self.indicator_ellipse = img.INDICATOR_ELLIPSE
        self.indicator_img.resize(100,100)
        self.indicator_base.resize(100,100)
        self.indicator_ellipse.resize(102,102)
        self.fuel_indicator_color = color(153, 166, 196)
        self.health_indicator_color = color(196, 255, 228)
        self.temp_indicator_color = color(196, 153, 153)
        self.indicator_border = color(253, 150, 115)
        self.indicator_thickness = 5
        self.indicator_transparency = 200
        kiona = createFont("Kiona-Regular.ttf", 10)
        textFont(kiona)

        
    def update_ship1_gui(self, heatpercentage, healthpercentage, fuelpercentage):
        pushMatrix()
        translate(self.width*0.8, self.height*0.8)
        #tempbar1
        imageMode(CENTER)
        image(self.indicator_base, 0,0)
        fill(255,255,255)
        text("Temperature", -40, 70)

        angle = 2*PI*(1-heatpercentage)-PI
        
        rotate(angle/2)
        noStroke()
        fill(self.temp_indicator_color, self.indicator_transparency)
        self.tempbar1 = arc(0,0, 100,100, 0, PI-angle, OPEN);
        rotate(-angle/2)
        imageMode(CENTER)
        image(self.indicator_ellipse, 0,0)
        popMatrix()
        
        pushMatrix()
        translate(self.width*0.9, self.height*0.6)
        #healthbar1
        imageMode(CENTER)
        image(self.indicator_base, 0,0)

        fill(255,255,255)
        text("Health", -20, 70)

        angle = 2*PI*(1-healthpercentage)-PI
        rotate(angle/2)
        noStroke()
        fill(self.health_indicator_color, self.indicator_transparency)
        self.healthbar1 = arc(0,0, 100,100, 0, PI-angle, OPEN);
        rotate(-angle/2)
        imageMode(CENTER)
        image(self.indicator_ellipse, 0,0)

        popMatrix()
    
        pushMatrix()
        translate(self.width*0.9, self.height*0.8)
        #healthbar1
        imageMode(CENTER)
        image(self.indicator_base, 0,0)
        fill(255,255,255)
        text("Fuel", -12, 70)

        angle = 2*PI*(1-fuelpercentage)-PI
        rotate(angle/2)
        noStroke()
        fill(self.fuel_indicator_color, self.indicator_transparency)
        self.healthbar1 = arc(0,0, 100,100, 0, PI-angle, OPEN);
        rotate(-angle/2)
        imageMode(CENTER)
        image(self.indicator_ellipse, 0,0)

        popMatrix()

    def update_ship0_gui(self, heatpercentage, healthpercentage, fuelpercentage):

        pushMatrix()
        translate(self.width*0.2, self.height*0.8)
        #tempbar1
        imageMode(CENTER)
        image(self.indicator_base, 0,0)

        fill(255,255,255)
        text("Temperature", -40, 70)

        angle = 2*PI*(1-heatpercentage)-PI
        rotate(angle/2)
        noStroke()
        fill(self.temp_indicator_color,self.indicator_transparency)
        self.tempbar1 = arc(0,0, 100,100, 0, PI-angle, OPEN);
        rotate(-angle/2)
        imageMode(CENTER)
        image(self.indicator_ellipse, 0,0)

        popMatrix()
        
        pushMatrix()
        translate(self.width*0.1, self.height*0.6)
        #healthbar1
        imageMode(CENTER)
        image(self.indicator_base, 0,0)

        fill(255,255,255)
        text("Health", -20, 70)

        angle = 2*PI*(1-healthpercentage)-PI
        rotate(angle/2)
        noStroke()
        fill(self.health_indicator_color,self.indicator_transparency)
        self.healthbar1 = arc(0,0, 100,100, 0, PI-angle, OPEN);
        rotate(-angle/2)
        imageMode(CENTER)
        image(self.indicator_ellipse, 0,0)

        popMatrix()

        pushMatrix()
        translate(self.width*0.1, self.height*0.8)
        #healthbar1
        imageMode(CENTER)
        image(self.indicator_base, 0,0)

        fill(255,255,255)
        text("Fuel", -12, 70)

        angle = 2*PI*(1-fuelpercentage)-PI
        rotate(angle/2)
        noStroke()
        fill(self.fuel_indicator_color,self.indicator_transparency)
        self.healthbar1 = arc(0,0, 100,100, 0, PI-angle, OPEN);
        rotate(-angle/2)
        imageMode(CENTER)
        image(self.indicator_ellipse, 0,0)

        popMatrix()
    
    def draw_indicator(self):
        imageMode(CENTER)
        image(self.indicator_img, 0,0)
