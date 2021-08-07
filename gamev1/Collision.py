class Collision:
    def __init__(self):
        #further optimization-- implement quad trees 
        pass
        
    
    def laser_coilgun_check(self, laser, coilgun_round):
        x1 = laser[0][0]
        y1 = laser[0][1]
        x2 = laser[1][0]
        y2 = laser[1][0]
        x0 = coilgun_round.pos[0]
        y0 = coilgun_round.pos[1]
        distance = abs((x2 - x1)*(y1-y0)-(x1-x0)*(y2-y1))/sqrt((x2-x1)**2+(y2-y1)**2)
        collision = False
        if distance < coilgun_round.s*2:
            collision = True
        return collision
    
    def line_line(self, line1, line2):
        """line is a tuple of PVectors
        copied from http://jeffreythompson.org/collision-detection/line-line.php"""
        x4 = line2[1][0]
        y4 = line2[1][1]
        x3 = line2[0][0]
        y3 = line2[0][1]
        
        x2 = line1[1][0]
        y2 = line1[1][1]
        x1 = line1[0][0]
        y1 = line1[0][1]
        
        uA = ((x4 - x3)*(y1-y3)-(y4-y3)*(x1-x3))/((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
        uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
        collision = False
        if uA >= 0 and uA <= 1 and uB >= 0 and uB <= 1:
            collision = True
        return collision
    
    def laser_spacecraft_check(self, laser, space_craft):
        x1 = laser[0][0]
        y1 = laser[0][1]
        x2 = laser[1][0]
        y2 = laser[1][1]
        rect_centerX =  space_craft.pos[0]
        rect_centerY =  space_craft.pos[1]
        theta = space_craft.theta
        #rotated coilgun_round coords
        
        cx1 = cos(theta)*(x1-rect_centerX) - sin(theta)*(y1-rect_centerY)+rect_centerX
        cy1 = sin(theta)*(x1-rect_centerX) + cos(theta)*(y1-rect_centerY)+rect_centerY
        cx2 = cos(theta)*(x2-rect_centerX) - sin(theta)*(y2-rect_centerY)+rect_centerX
        cy2 = sin(theta)*(x2-rect_centerX) + cos(theta)*(y2-rect_centerY)+rect_centerY
        
        line0 = (PVector(cx1, cy1), PVector(cx2, cy2))
        #top left to top right
        line1 = (PVector(rect_centerX-space_craft.w/2, rect_centerY - space_craft.h/2), \
                  PVector(rect_centerX+space_craft.w/2, rect_centerY - space_craft.h/2))
        #bottom left to bottom right
        line2 = (PVector(rect_centerX-space_craft.w/2, rect_centerY + space_craft.h/2), \
        PVector(rect_centerX+space_craft.w/2, rect_centerY + space_craft.h/2))

        #top left to bottom left
        line3 = (PVector(rect_centerX-space_craft.w/2, rect_centerY - space_craft.h/2), \
        PVector(rect_centerX-space_craft.w/2, rect_centerY + space_craft.h/2))

        #top right to bottom right
        line4 = (PVector(rect_centerX+space_craft.w/2, rect_centerY - space_craft.h/2), \
        PVector(rect_centerX+space_craft.w/2, rect_centerY + space_craft.h/2))
        rect_lines = [line1, line2, line3, line4]
        for rect_line in rect_lines:
            collision = self.line_line(line0, rect_line)
            if collision:
                print("laser hit!")
                return collision
            
    def coilgun_spacecraft_collision_check(self, coilgun_round, space_craft):
        rect_centerX =  space_craft.pos[0]
        rect_centerY =  space_craft.pos[1]
        theta = space_craft.theta
        #rotated coilgun_round coords
        cx = cos(theta)*(coilgun_round.pos[0]-rect_centerX) - sin(theta)*(coilgun_round.pos[1]-rect_centerY)+rect_centerX
        cy = sin(theta)*(coilgun_round.pos[0]-rect_centerX) + cos(theta)*(coilgun_round.pos[1]-rect_centerY)+rect_centerY
        
        #find unrotated closest x point from center of unrotated circle
        rect_x = rect_centerX-space_craft.w/2
        rect_y = rect_centerY-space_craft.h/2
        if cx < rect_x:
            x = rect_x
        elif cx > rect_x + space_craft.w:
            x = rect_x+space_craft.w
        else:
            x = cx
        if cy < rect_y:
            
            y = rect_y
        elif cy > rect_y + space_craft.h:
            y = rect_y+space_craft.h
        else:
            y = cy
        collision = False
        v = PVector(x,y)
        c = PVector(cx, cy)
        distance = PVector.dist(v, c)
        
        
        if distance < coilgun_round.s:
            print("hesdfm")
            collision = True
            
        return collision

        
