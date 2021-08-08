from Coilgun import CoilgunRound
import math

class SpaceCraftPrimitive(object):
    def __init__(self, x, y, rgb):
        self.pos= PVector(x,y)
        self.theta = 0
        self.vel = PVector(0,0.02)
        self.accel = PVector(0,0)
        self.h = 8
        self.w = 20
        self.color = rgb
        self.thrusting = False
        
        self.coilgun_rounds = {}
        self.coilgun_id = -1
        self.hit = False
        self.hit_color = color(255, 0, 0)
        self.laserLen = 300
        
        self.heat = 0.01
        self.max_heat = 1
        self.disappation_constant = 0.003
        self.heating_constant = 0.01
        
        self.health = 1
        self.max_health = 1
        
        self.alive = True #alive
        self.type = "spacecraft"
        
        self.fuel_level = 1
        self.max_fuel = 1
    
    def fire(self):
        coilgun_pos = self.pos.copy()
        currHeadingVec = PVector.fromAngle(self.theta)
        currHeadingVec.rotate(PI)
        shift = PVector.mult(currHeadingVec, self.w/2+4)
        coilgun_pos.add(shift)
        coilgun_vel = currHeadingVec.mult(0.05)
        coilgun_vel.add(self.vel)
        coilgun_round = CoilgunRound(coilgun_pos, coilgun_vel)
        self.coilgun_id += 1
        self.coilgun_rounds[self.coilgun_id] = coilgun_round

    def fireLaser(self):
        laser_beginning_pos = self.pos.copy()
        currHeadingVec = PVector.fromAngle(self.theta)
        currHeadingVec.rotate(PI)
        shift = PVector.mult(currHeadingVec, self.w/2+3)
        laser_beginning_pos.add(shift)
        laserVec = PVector.mult(currHeadingVec, self.laserLen)
        laser_ending_pos = PVector.add(laser_beginning_pos, laserVec)
        stroke(0, 255, 0)
        strokeWeight(4)
        #strokeCap(SQUARE)
        line(laser_beginning_pos[0], laser_beginning_pos[1], laser_ending_pos[0], laser_ending_pos[1]);
        self.heat += self.heating_constant
        return laser_beginning_pos, laser_ending_pos
        
    def applyAccel(self, accel):
        self.accel = accel

    def draw(self):
        self.heat -= self.disappation_constant*self.heat
        if self.heat >= self.max_heat or self.health <= 0:
            self.alive = False
        pushMatrix()
        translate(self.pos[0], self.pos[1])
        rotate(self.theta)
        noStroke()
        
        #Thruster burn
        if self.thrusting:
            pushMatrix()
            fill(225, 165, 0)
            translate(self.w/2, 0)
            ellipse(0, 0, self.h*2, self.h)
            popMatrix()
        
        pushMatrix()
        if not self.hit:
            fill(225, 226,227)
        else:
            fill(self.hit_color)
        translate(-self.w/2, 0)
        circle(0, 0, self.h)
        popMatrix()

        if not self.hit and self.alive:
            fill(self.color)
        elif not self.hit and not self.alive:
            fill(color(222, 222, 222))
        else:
            fill(self.hit_color)
        rect(-self.w/2,-self.h/2, self.w, self.h)
        # rect(self.pos[0], self.pos[1], self.w, self.h)
        popMatrix()

    def turnOffThrust(self):
        self.thrusting = False

class SpaceCraft(SpaceCraftPrimitive):
    def __init__(self, maxthrust, m, x, y, rgb):
        super(SpaceCraft, self).__init__(x, y, rgb)
        self.maxthrust = maxthrust
        self.m  = m
        self.fuel_burn = 0.002
        # self.I = 10 #todo-- make inertia into function of m
        
    def thrust(self):
        if self.fuel_level >= 0:
            currHeadingVec = PVector.fromAngle(self.theta)
            # currHeadingVec.rotate(HALF_PI)
            # print(currHeadingVec)
            thrust_vec = currHeadingVec.mult(self.maxthrust) #to change later
            accel_vec = thrust_vec.div(-self.m)
            self.thrusting = True
            self.heat += self.heating_constant*0.5
            self.fuel_level -= self.fuel_burn
        else:
            accel_vec = PVector(0,0)
        return accel_vec
            
    def turnRight(self):
        self.theta += 0.05
        
    def turnLeft(self):
        # print("turning left")
        self.theta -= 0.05
            
