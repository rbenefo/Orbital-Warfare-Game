from Coilgun import CoilgunRound
import math


class SpaceCraftPrimitive(object):
    def __init__(self, pos, vel, rgb, sounds):
        self.pos= pos
        self.theta = 0
        self.vel = vel
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
        
        self.health = 2
        self.max_health = 2
        
        self.alive = True #alive
        self.crashed = False
        self.type = "spacecraft"
        
        self.fuel_level = 2
        self.max_fuel = 2
        self.angular_vel = 0
        
        self.reentry_coloring = color(255, 163, 71)
        # self.reentering = False
        
        self.sounds = sounds
    def fire(self):
        coilgun_pos = self.pos.copy()
        currHeadingVec = PVector.fromAngle(self.theta)
        currHeadingVec.rotate(PI)
        shift = PVector.mult(currHeadingVec, self.w/2+10)
        coilgun_pos.add(shift)
        coilgun_vel = currHeadingVec.mult(0.04)
        coilgun_vel.add(self.vel)
        coilgun_round = CoilgunRound(coilgun_pos, coilgun_vel)
        self.coilgun_id += 1
        self.coilgun_rounds[self.coilgun_id] = coilgun_round
        self.sounds.CANNON.play()

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
        self.sounds.LASER.play()
        return laser_beginning_pos, laser_ending_pos
        
    def applyAccel(self, accel):
        self.accel = accel

    def draw(self):
        if not self.crashed:
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
                if not self.reentering:
                    fill(225, 226,227)
                else:
                    fill(lerpColor(color(225, 226,22), self.reentry_coloring, 0.5))
            else:
                fill(self.hit_color)
            translate(-self.w/2, 0)
            circle(0, 0, self.h)
            popMatrix()
    
            if not self.hit and self.alive:
                if not self.reentering:
                    fill(self.color)
                else:
                    fill(lerpColor(self.color, self.reentry_coloring, 0.5))
            elif not self.hit and not self.alive:
                if not self.reentering:
                    fill(color(222, 222, 222))
                else:
                    fill(lerpColor(color(222, 222, 222), self.reentry_coloring, 0.5))
            else:
                fill(self.hit_color)
            rect(-self.w/2,-self.h/2, self.w, self.h)
            # rect(self.pos[0], self.pos[1], self.w, self.h)
            popMatrix()
    

class SpaceCraft(SpaceCraftPrimitive):
    def __init__(self, maxthrust, m, x, y, rgb, sounds):
        super(SpaceCraft, self).__init__(x, y, rgb, sounds)
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
            self.sounds.THRUST.play()

        else:
            accel_vec = PVector(0,0)
        return accel_vec
    
    def turnOffThrust(self):
        self.thrusting = False
 
    def turnRight(self):
        if self.fuel_level >= 0:
            # self.theta += 0.02
            self.angular_vel += 0.00003
            self.sounds.HISS.play()
        
    def turnLeft(self):
        # print("turning left")
        if self.fuel_level >= 0:
            # self.theta -= 0.02
            self.angular_vel -= 0.00003
            self.sounds.HISS.play()
            
