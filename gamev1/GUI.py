class GUI:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.fuel_indicator_color = color(153, 166, 196)
        self.health_indicator_color = color(153, 196, 162)
        self.temp_indicator_color = color(196, 153, 153)
        self.indicator_border = color(176, 176, 176)
        self.indicator_thickness = 5
        
    def update_ship1_gui(self, heatpercentage, healthpercentage, fuelpercentage):
        pushMatrix()
        translate(self.width*0.8, self.height*0.8)
        #tempbar1
        stroke(self.indicator_border)
        strokeWeight(self.indicator_thickness)
        
        fill(255,255,255)
        circle(0, 0, 100)
        # kiona = createFont("Kiona-Regular.ttf", 10)
        # textFont(kiona)
        text("Temperature", -40, 70)

        angle = 2*PI*(1-heatpercentage)-PI
        rotate(angle/2)
        noStroke()
        fill(self.temp_indicator_color)
        self.tempbar1 = arc(0,0, 100,100, 0, PI-angle, OPEN);
        popMatrix()
        
        pushMatrix()
        translate(self.width*0.9, self.height*0.6)
        #healthbar1
        stroke(self.indicator_border)
        strokeWeight(self.indicator_thickness)

        fill(255,255,255)
        circle(0, 0, 100)
        text("Health", -20, 70)

        angle = 2*PI*(1-healthpercentage)-PI
        rotate(angle/2)
        noStroke()
        fill(self.health_indicator_color)
        self.healthbar1 = arc(0,0, 100,100, 0, PI-angle, OPEN);
        popMatrix()
    
        pushMatrix()
        translate(self.width*0.9, self.height*0.8)
        #healthbar1
        stroke(self.indicator_border)
        strokeWeight(self.indicator_thickness)

        fill(255,255,255)
        circle(0, 0, 100)
        text("Fuel", -12, 70)

        angle = 2*PI*(1-fuelpercentage)-PI
        rotate(angle/2)
        noStroke()
        fill(self.fuel_indicator_color)
        self.healthbar1 = arc(0,0, 100,100, 0, PI-angle, OPEN);
        popMatrix()

    def update_ship0_gui(self, heatpercentage, healthpercentage, fuelpercentage):

        pushMatrix()
        translate(self.width*0.2, self.height*0.8)
        #tempbar1
        stroke(self.indicator_border)
        strokeWeight(self.indicator_thickness)

        fill(255,255,255)
        circle(0, 0, 100)
        # kiona = createFont("Kiona-Regular.ttf", 10)
        # textFont(kiona)
        text("Temperature", -40, 70)

        angle = 2*PI*(1-heatpercentage)-PI
        rotate(angle/2)
        noStroke()
        fill(self.temp_indicator_color)
        self.tempbar1 = arc(0,0, 100,100, 0, PI-angle, OPEN);
        popMatrix()
        
        pushMatrix()
        translate(self.width*0.1, self.height*0.6)
        #healthbar1
        stroke(self.indicator_border)
        strokeWeight(self.indicator_thickness)

        fill(255,255,255)
        circle(0, 0, 100)
        text("Health", -20, 70)

        angle = 2*PI*(1-healthpercentage)-PI
        rotate(angle/2)
        noStroke()
        fill(self.health_indicator_color)
        self.healthbar1 = arc(0,0, 100,100, 0, PI-angle, OPEN);
        popMatrix()

        pushMatrix()
        translate(self.width*0.1, self.height*0.8)
        #healthbar1
        stroke(self.indicator_border)
        strokeWeight(self.indicator_thickness)

        fill(255,255,255)
        circle(0, 0, 100)
        text("Fuel", -12, 70)

        angle = 2*PI*(1-fuelpercentage)-PI
        rotate(angle/2)
        noStroke()
        fill(self.fuel_indicator_color)
        self.healthbar1 = arc(0,0, 100,100, 0, PI-angle, OPEN);
        popMatrix()
