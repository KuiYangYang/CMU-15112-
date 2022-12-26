from cmu_112_graphics import *
import math
from math import atan2, degrees, radians

class Isometric(): 
    def __init__(self,name,cx,cy,width,length,rotateCx,rotateCy,
                roomWidth,roomLength,roomWall,angle,angleYZ,objectCount):
        self.name = name
        self.cx = cx
        self.cy = cy
        self.w = width
        self.l = length
        self.angle = angle
        self.angleYZ = angleYZ
        self.count = objectCount
        self.rotateCX = rotateCx
        self.rotateCY = rotateCy    
        self.roomWidth = roomWidth
        self.roomLength = roomLength
        self.roomWall = roomWall
        self.coordinates3D = []
        self.coordinates2D = []
        self.customizeObject()

    def customizeObject(self):
        # find corner points(p1,p2,p3,p4) of the object
        if self.name == 'window' or self.name == 'door':
            x0 = int(self.rotateCX - (self.roomWidth/2)-(self.roomWall/2))
            x1 = int(self.rotateCX - (self.roomWidth/2)+(self.roomWall/2))
            x2 = int(self.rotateCX + (self.roomWidth/2)-(self.roomWall/2))
            x3 = int(self.rotateCX + (self.roomWidth/2)+(self.roomWall/2))

            y0 = int(self.rotateCY - (self.roomLength/2)-(self.roomWall/2))
            y1 = int(self.rotateCY - (self.roomLength/2)+(self.roomWall/2))
            y2 = int(self.rotateCY + (self.roomLength/2)-(self.roomWall/2))
            y3 = int(self.rotateCY + (self.roomLength/2)+(self.roomWall/2))

            #draw window
            if (self.cx in range(x0,x1) and 
                self.cy in range(int(y0+self.w/2),int(y3-self.w/2))):
                temp = self.w
                self.w = self.l
                self.l = temp
            elif (self.cx in range(x2,x3) and 
                self.cy in range(int(y0+self.w/2),int(y3-self.w/2))):
                temp = self.w
                self.w = self.l
                self.l = temp
            p1 = (self.cx-(self.w/2),self.cy-(self.l/2))
            p2 = (self.cx-(self.w/2),self.cy+(self.l/2))
            p3 = (self.cx+(self.w/2),self.cy+(self.l/2))
            p4 = (self.cx+(self.w/2),self.cy-(self.l/2)) 
        else:
            p1 = (self.cx-(self.w/2),self.cy-(self.l/2))
            p2 = (self.cx-(self.w/2),self.cy+(self.l/2))
            p3 = (self.cx+(self.w/2),self.cy+(self.l/2))
            p4 = (self.cx+(self.w/2),self.cy-(self.l/2)) 

        # change height when press 'up' and 'down'
        constant = 1-((self.angleYZ)*(self.angleYZ))
        if self.name == 'room':
            self.coordinates2D = [p1,p2,p3,p4]
            #bottom coordinates
            sub = []
            temp1 = []
            for p in self.coordinates2D:
                temp1.append(self.rotate(p[0],p[1]))
            sub.append(temp1)

            #top coordinates
            temp2 =[]
            for L in sub:
                for p in L:
                    newP = (p[0],p[1]-300*constant)
                    temp2.append(newP)
            sub.append(temp2)
            self.coordinates3D.append(sub)
        
        if self.name == 'desk':
            #colums of desk
            columns = []
            c1_x0 = self.cx-(self.w/2)
            c1_y0 = self.cy-(self.l/2)
            c1_x1 = self.cx-(self.w/2)
            c1_y1 = self.cy-(self.l/2)+10
            c1_x2 = self.cx-(self.w/2)+10
            c1_y2 = self.cy-(self.l/2)+10
            c1_x3 = self.cx-(self.w/2)+10
            c1_y3 = self.cy-(self.l/2)
            c1 = [(c1_x0,c1_y0),(c1_x1,c1_y1),(c1_x2,c1_y2),(c1_x3,c1_y3)]
            columns.append(c1)

            c2_x0 = self.cx-(self.w/2)
            c2_y0 = self.cy+(self.l/2)-10
            c2_x1 = self.cx-(self.w/2)
            c2_y1 = self.cy+(self.l/2)
            c2_x2 = self.cx-(self.w/2)+10
            c2_y2 = self.cy+(self.l/2)
            c2_x3 = self.cx-(self.w/2)+10
            c2_y3 = self.cy+(self.l/2)-10
            c2 = [(c2_x0,c2_y0),(c2_x1,c2_y1),(c2_x2,c2_y2),(c2_x3,c2_y3)]
            columns.append(c2)

            c3_x0 = self.cx+(self.w/2)-10
            c3_y0 = self.cy+(self.l/2)-10
            c3_x1 = self.cx+(self.w/2)-10
            c3_y1 = self.cy+(self.l/2)
            c3_x2 = self.cx+(self.w/2)
            c3_y2 = self.cy+(self.l/2)
            c3_x3 = self.cx+(self.w/2)
            c3_y3 = self.cy+(self.l/2)-10
            c3 = [(c3_x0,c3_y0),(c3_x1,c3_y1),(c3_x2,c3_y2),(c3_x3,c3_y3)]
            columns.append(c3)

            c4_x0 = self.cx+(self.w/2)-10
            c4_y0 = self.cy-(self.l/2)
            c4_x1 = self.cx+(self.w/2)-10
            c4_y1 = self.cy-(self.l/2)+10
            c4_x2 = self.cx+(self.w/2)
            c4_y2 = self.cy-(self.l/2)+10
            c4_x3 = self.cx+(self.w/2)
            c4_y3 = self.cy-(self.l/2)
            c4 = [(c4_x0,c4_y0),(c4_x1,c4_y1),(c4_x2,c4_y2),(c4_x3,c4_y3)]
            columns.append(c4)

            self.coordinates2D = [p1,p2,p3,p4]
            top =[]
            temp1 = []
            for p in self.coordinates2D:
                temp1.append(self.rotate(p[0],p[1]))
            top.append(temp1)        
            temp2 =[]
            for L in top:
                for p in L:
                    newP = (p[0],p[1]-60*constant)
                    temp2.append(newP)
            top.append(temp2)
            top.pop(0)
            temp3 =[]
            for L in top:
                for p in L:
                    newP = (p[0],p[1]-10*constant)
                    temp3.append(newP)
            top.append(temp3)
            self.coordinates3D.append(top)

            for L in columns:
                newColumns = []
                temp3 = []
                for p in L:
                    temp3.append(self.rotate(p[0],p[1]))
                newColumns.append(temp3)         

                temp4 =[]
                for L in newColumns:
                    for p in L:
                        newP = (p[0],p[1]-60*constant)
                        temp4.append(newP)
                newColumns.append(temp4)
                self.coordinates3D.append(newColumns)
        
        if self.name == 'chair':
            if self.count%4 == 0:
                p1 = (self.cx-(self.w/2)+5,self.cy-(self.l/2))
                p2 = (self.cx-(self.w/2)+5,self.cy+(self.l/2))
                p3 = (self.cx+(self.w/2)-5,self.cy+(self.l/2))
                p4 = (self.cx+(self.w/2)-5,self.cy-(self.l/2)) 
                self.coordinates2D = [p1,p2,p3,p4]
                #bottom coordinates
                sub = []
                temp1 = []
                for p in self.coordinates2D:
                    temp1.append(self.rotate(p[0],p[1]))
                sub.append(temp1)

                #top coordinates
                temp2 =[]
                for L in sub:
                    for p in L:
                        newP = (p[0],p[1]-40*constant)
                        temp2.append(newP)
                sub.append(temp2)
                self.coordinates3D.append(sub)

                back = []
                d1_x0 = self.cx+(self.w/2)-5
                d1_y0 = self.cy-(self.l/2)
                d1_x1 = self.cx+(self.w/2)-5
                d1_y1 = self.cy+(self.l/2)
                d1_x2 = self.cx+(self.w/2)+5
                d1_y2 = self.cy+(self.l/2)
                d1_x3 = self.cx+(self.w/2)+5
                d1_y3 = self.cy-(self.l/2)
                d1 = [(d1_x0,d1_y0),(d1_x1,d1_y1),(d1_x2,d1_y2),(d1_x3,d1_y3)]
                back.append(d1)
                for L in back:
                    newBack = []
                    temp3 = []
                    for p in L:
                        temp3.append(self.rotate(p[0],p[1]))
                    newBack.append(temp3)         

                    temp4 =[]
                    for L in newBack:
                        for p in L:
                            newP = (p[0],p[1]-80*constant)
                            temp4.append(newP)
                    newBack.append(temp4)
                    self.coordinates3D.append(newBack)
            if self.count%4 == 1:
                p1 = (self.cx-(self.w/2),self.cy-(self.l/2)+5)
                p2 = (self.cx-(self.w/2),self.cy+(self.l/2)-5)
                p3 = (self.cx+(self.w/2),self.cy+(self.l/2)-5)
                p4 = (self.cx+(self.w/2),self.cy-(self.l/2)+5) 
                self.coordinates2D = [p1,p2,p3,p4]
                #bottom coordinates
                sub = []
                temp1 = []
                for p in self.coordinates2D:
                    temp1.append(self.rotate(p[0],p[1]))
                sub.append(temp1)

                #top coordinates
                temp2 =[]
                for L in sub:
                    for p in L:
                        newP = (p[0],p[1]-40*constant)
                        temp2.append(newP)
                sub.append(temp2)
                self.coordinates3D.append(sub)

                back = []
                d1_x0 = self.cx-(self.w/2)
                d1_y0 = self.cy-(self.l/2)-5
                d1_x1 = self.cx-(self.w/2)
                d1_y1 = self.cy-(self.l/2)+5
                d1_x2 = self.cx+(self.w/2)
                d1_y2 = self.cy-(self.l/2)+5
                d1_x3 = self.cx+(self.w/2)
                d1_y3 = self.cy-(self.l/2)-5
                d1 = [(d1_x0,d1_y0),(d1_x1,d1_y1),(d1_x2,d1_y2),(d1_x3,d1_y3)]
                back.append(d1)
                for L in back:
                    newBack = []
                    temp3 = []
                    for p in L:
                        temp3.append(self.rotate(p[0],p[1]))
                    newBack.append(temp3)         

                    temp4 =[]
                    for L in newBack:
                        for p in L:
                            newP = (p[0],p[1]-80*constant)
                            temp4.append(newP)
                    newBack.append(temp4)
                    self.coordinates3D.append(newBack)
            if self.count%4 == 2:
                p1 = (self.cx-(self.w/2)+5,self.cy-(self.l/2))
                p2 = (self.cx-(self.w/2)+5,self.cy+(self.l/2))
                p3 = (self.cx+(self.w/2)-5,self.cy+(self.l/2))
                p4 = (self.cx+(self.w/2)-5,self.cy-(self.l/2)) 
                self.coordinates2D = [p1,p2,p3,p4]
                #bottom coordinates
                sub = []
                temp1 = []
                for p in self.coordinates2D:
                    temp1.append(self.rotate(p[0],p[1]))
                sub.append(temp1)

                #top coordinates
                temp2 =[]
                for L in sub:
                    for p in L:
                        newP = (p[0],p[1]-40*constant)
                        temp2.append(newP)
                sub.append(temp2)
                self.coordinates3D.append(sub)

                back = []
                d1_x0 = self.cx-(self.w/2)-5
                d1_y0 = self.cy-(self.l/2)
                d1_x1 = self.cx-(self.w/2)-5
                d1_y1 = self.cy+(self.l/2)
                d1_x2 = self.cx-(self.w/2)+5
                d1_y2 = self.cy+(self.l/2)
                d1_x3 = self.cx-(self.w/2)+5
                d1_y3 = self.cy-(self.l/2)
                d1 = [(d1_x0,d1_y0),(d1_x1,d1_y1),(d1_x2,d1_y2),(d1_x3,d1_y3)]
                back.append(d1)
                for L in back:
                    newBack = []
                    temp3 = []
                    for p in L:
                        temp3.append(self.rotate(p[0],p[1]))
                    newBack.append(temp3)         

                    temp4 =[]
                    for L in newBack:
                        for p in L:
                            newP = (p[0],p[1]-80*constant)
                            temp4.append(newP)
                    newBack.append(temp4)
                    self.coordinates3D.append(newBack)
            if self.count%4 == 3:
                p1 = (self.cx-(self.w/2),self.cy-(self.l/2)+5)
                p2 = (self.cx-(self.w/2),self.cy+(self.l/2)-5)
                p3 = (self.cx+(self.w/2),self.cy+(self.l/2)-5)
                p4 = (self.cx+(self.w/2),self.cy-(self.l/2)+5) 
                self.coordinates2D = [p1,p2,p3,p4]
                #bottom coordinates
                sub = []
                temp1 = []
                for p in self.coordinates2D:
                    temp1.append(self.rotate(p[0],p[1]))
                sub.append(temp1)

                #top coordinates
                temp2 =[]
                for L in sub:
                    for p in L:
                        newP = (p[0],p[1]-40*constant)
                        temp2.append(newP)
                sub.append(temp2)
                self.coordinates3D.append(sub)

                back = []
                d1_x0 = self.cx-(self.w/2)
                d1_y0 = self.cy+(self.l/2)+5
                d1_x1 = self.cx-(self.w/2)
                d1_y1 = self.cy+(self.l/2)-5
                d1_x2 = self.cx+(self.w/2)
                d1_y2 = self.cy+(self.l/2)-5
                d1_x3 = self.cx+(self.w/2)
                d1_y3 = self.cy+(self.l/2)+5
                d1 = [(d1_x0,d1_y0),(d1_x1,d1_y1),(d1_x2,d1_y2),(d1_x3,d1_y3)]
                back.append(d1)
                for L in back:
                    newBack = []
                    temp3 = []
                    for p in L:
                        temp3.append(self.rotate(p[0],p[1]))
                    newBack.append(temp3)         

                    temp4 =[]
                    for L in newBack:
                        for p in L:
                            newP = (p[0],p[1]-80*constant)
                            temp4.append(newP)
                    newBack.append(temp4)
                    self.coordinates3D.append(newBack)

        if self.name == 'bed':
            if self.count % 4 == 0:
                p1 = (self.cx-(self.w/2),self.cy-(self.l/2))
                p2 = (self.cx-(self.w/2),self.cy+(self.l/2))
                p3 = (self.cx+(self.w/2),self.cy+(self.l/2))
                p4 = (self.cx+(self.w/2),self.cy-(self.l/2))
                self.coordinates2D = [p1,p2,p3,p4]
                #bottom coordinates
                sub = []
                temp1 = []
                for p in self.coordinates2D:
                    temp1.append(self.rotate(p[0],p[1]))
                sub.append(temp1)

                #top coordinates
                temp2 =[]
                for L in sub:
                    for p in L:
                        newP = (p[0],p[1]-40*constant)
                        temp2.append(newP)
                sub.append(temp2)
                self.coordinates3D.append(sub)

                pillows = []
                p1_x0 = self.cx-(self.w/2)+20
                p1_y0 = self.cy-(self.l/2)+10
                p1_x1 = self.cx-(self.w/2)+20
                p1_y1 = self.cy-(self.l/2)+30
                p1_x2 = self.cx -10
                p1_y2 = self.cy-(self.l/2)+30
                p1_x3 = self.cx -10
                p1_y3 = self.cy-(self.l/2)+10
                p1 = [(p1_x0,p1_y0),(p1_x1,p1_y1),(p1_x2,p1_y2),(p1_x3,p1_y3)]
                pillows.append(p1)

                p2_x0 = self.cx+(self.w/2)-20
                p2_y0 = self.cy-(self.l/2)+10
                p2_x1 = self.cx+(self.w/2)-20
                p2_y1 = self.cy-(self.l/2)+30
                p2_x2 = self.cx +10
                p2_y2 = self.cy-(self.l/2)+30
                p2_x3 = self.cx +10
                p2_y3 = self.cy-(self.l/2)+10
                p2 = [(p2_x0,p2_y0),(p2_x1,p2_y1),(p2_x2,p2_y2),(p2_x3,p2_y3)]
                pillows.append(p2)

                for L in pillows:
                    newPillows = []
                    temp3 = []
                    for p in L:
                        temp3.append(self.rotate(p[0],p[1]))
                    newPillows.append(temp3)         

                    temp4 =[]
                    for L in newPillows:
                        for p in L:
                            newP = (p[0],p[1]-40*constant)
                            temp4.append(newP)
                    newPillows.append(temp4)
                    newPillows.pop(0)

                    temp5 =[]
                    for L in newPillows:
                        for p in L:
                            newP = (p[0],p[1]-5*constant)
                            temp5.append(newP)
                    newPillows.append(temp5)
                    self.coordinates3D.append(newPillows)

                duvet = []
                d1_x0 = self.cx-(self.w/2)
                d1_y0 = self.cy-(self.l/2)+40
                d1_x1 = self.cx-(self.w/2)
                d1_y1 = self.cy-(self.l/2)
                d1_x2 = self.cx+(self.w/2)
                d1_y2 = self.cy-(self.l/2)
                d1_x3 = self.cx+(self.w/2)
                d1_y3 = self.cy-(self.l/2)+40
                d1 = [(d1_x0,d1_y0),(d1_x1,d1_y1),(d1_x2,d1_y2),(d1_x3,d1_y3)]
                duvet.append(d1)
                for L in duvet:
                    newDuvet = []
                    temp3 = []
                    for p in L:
                        temp3.append(self.rotate(p[0],p[1]))
                    newDuvet.append(temp3)         

                    temp4 =[]
                    for L in newDuvet:
                        for p in L:
                            newP = (p[0],p[1]-40*constant)
                            temp4.append(newP)
                    newDuvet.append(temp4)
                    newDuvet.pop(0)
                    self.coordinates3D.append(newDuvet)
            if self.count % 4 == 1:
                p1 = (self.cx-(self.w/2),self.cy-(self.l/2))
                p2 = (self.cx-(self.w/2),self.cy+(self.l/2))
                p3 = (self.cx+(self.w/2),self.cy+(self.l/2))
                p4 = (self.cx+(self.w/2),self.cy-(self.l/2))
                self.coordinates2D = [p1,p2,p3,p4]
                #bottom coordinates
                sub = []
                temp1 = []
                for p in self.coordinates2D:
                    temp1.append(self.rotate(p[0],p[1]))
                sub.append(temp1)

                #top coordinates
                temp2 =[]
                for L in sub:
                    for p in L:
                        newP = (p[0],p[1]-40*constant)
                        temp2.append(newP)
                sub.append(temp2)
                self.coordinates3D.append(sub)

                pillows = []
                p1_x0 = self.cx-(self.w/2)+10
                p1_y0 = self.cy-(self.l/2)+20
                p1_x1 = self.cx-(self.w/2)+30
                p1_y1 = self.cy-(self.l/2)+20
                p1_x2 = self.cx -(self.w/2)+30
                p1_y2 = self.cy-10
                p1_x3 = self.cx-(self.w/2)+10
                p1_y3 = self.cy-10
                p1 = [(p1_x0,p1_y0),(p1_x1,p1_y1),(p1_x2,p1_y2),(p1_x3,p1_y3)]
                pillows.append(p1)

                p2_x0 = self.cx-(self.w/2)+10
                p2_y0 = self.cy+10
                p2_x1 = self.cx-(self.w/2)+30
                p2_y1 = self.cy+10
                p2_x2 = self.cx-(self.w/2)+30
                p2_y2 = self.cy+(self.l/2)-20
                p2_x3 = self.cx-(self.w/2)+10
                p2_y3 = self.cy+(self.l/2)-20
                p2 = [(p2_x0,p2_y0),(p2_x1,p2_y1),(p2_x2,p2_y2),(p2_x3,p2_y3)]
                pillows.append(p2)

                for L in pillows:
                    newPillows = []
                    temp3 = []
                    for p in L:
                        temp3.append(self.rotate(p[0],p[1]))
                    newPillows.append(temp3)         

                    temp4 =[]
                    for L in newPillows:
                        for p in L:
                            newP = (p[0],p[1]-40*constant)
                            temp4.append(newP)
                    newPillows.append(temp4)
                    newPillows.pop(0)

                    temp5 =[]
                    for L in newPillows:
                        for p in L:
                            newP = (p[0],p[1]-5*constant)
                            temp5.append(newP)
                    newPillows.append(temp5)
                    self.coordinates3D.append(newPillows)

                duvet = []
                d1_x0 = self.cx-(self.w/2)+40
                d1_y0 = self.cy-(self.l/2)
                d1_x1 = self.cx-(self.w/2)+40
                d1_y1 = self.cy+(self.l/2)
                d1_x2 = self.cx+(self.w/2)
                d1_y2 = self.cy+(self.l/2)
                d1_x3 = self.cx+(self.w/2)
                d1_y3 = self.cy-(self.l/2)
                d1 = [(d1_x0,d1_y0),(d1_x1,d1_y1),(d1_x2,d1_y2),(d1_x3,d1_y3)]
                duvet.append(d1)
                for L in duvet:
                    newDuvet = []
                    temp3 = []
                    for p in L:
                        temp3.append(self.rotate(p[0],p[1]))
                    newDuvet.append(temp3)         

                    temp4 =[]
                    for L in newDuvet:
                        for p in L:
                            newP = (p[0],p[1]-40*constant)
                            temp4.append(newP)
                    newDuvet.append(temp4)
                    newDuvet.pop(0)
                    self.coordinates3D.append(newDuvet)
            if self.count % 4 == 2:
                p1 = (self.cx-(self.w/2),self.cy-(self.l/2))
                p2 = (self.cx-(self.w/2),self.cy+(self.l/2))
                p3 = (self.cx+(self.w/2),self.cy+(self.l/2))
                p4 = (self.cx+(self.w/2),self.cy-(self.l/2))
                self.coordinates2D = [p1,p2,p3,p4]
                #bottom coordinates
                sub = []
                temp1 = []
                for p in self.coordinates2D:
                    temp1.append(self.rotate(p[0],p[1]))
                sub.append(temp1)

                #top coordinates
                temp2 =[]
                for L in sub:
                    for p in L:
                        newP = (p[0],p[1]-40*constant)
                        temp2.append(newP)
                sub.append(temp2)
                self.coordinates3D.append(sub)

                pillows = []
                p1_x0 = self.cx-(self.w/2)+20
                p1_y0 = self.cy+(self.l/2)-10
                p1_x1 = self.cx-(self.w/2)+20
                p1_y1 = self.cy+(self.l/2)-30
                p1_x2 = self.cx -10
                p1_y2 = self.cy+(self.l/2)-30
                p1_x3 = self.cx -10
                p1_y3 = self.cy+(self.l/2)-10
                p1 = [(p1_x0,p1_y0),(p1_x1,p1_y1),(p1_x2,p1_y2),(p1_x3,p1_y3)]
                pillows.append(p1)

                p2_x0 = self.cx+(self.w/2)-20
                p2_y0 = self.cy+(self.l/2)-10
                p2_x1 = self.cx+(self.w/2)-20
                p2_y1 = self.cy+(self.l/2)-30
                p2_x2 = self.cx +10
                p2_y2 = self.cy+(self.l/2)-30
                p2_x3 = self.cx +10
                p2_y3 = self.cy+(self.l/2)-10
                p2 = [(p2_x0,p2_y0),(p2_x1,p2_y1),(p2_x2,p2_y2),(p2_x3,p2_y3)]
                pillows.append(p2)

                for L in pillows:
                    newPillows = []
                    temp3 = []
                    for p in L:
                        temp3.append(self.rotate(p[0],p[1]))
                    newPillows.append(temp3)         

                    temp4 =[]
                    for L in newPillows:
                        for p in L:
                            newP = (p[0],p[1]-40*constant)
                            temp4.append(newP)
                    newPillows.append(temp4)
                    newPillows.pop(0)

                    temp5 =[]
                    for L in newPillows:
                        for p in L:
                            newP = (p[0],p[1]-5*constant)
                            temp5.append(newP)
                    newPillows.append(temp5)
                    self.coordinates3D.append(newPillows)

                duvet = []
                d1_x0 = self.cx-(self.w/2)
                d1_y0 = self.cy+(self.l/2)-40
                d1_x1 = self.cx-(self.w/2)
                d1_y1 = self.cy-(self.l/2)
                d1_x2 = self.cx+(self.w/2)
                d1_y2 = self.cy-(self.l/2)
                d1_x3 = self.cx+(self.w/2)
                d1_y3 = self.cy+(self.l/2)-40
                d1 = [(d1_x0,d1_y0),(d1_x1,d1_y1),(d1_x2,d1_y2),(d1_x3,d1_y3)]
                duvet.append(d1)
                for L in duvet:
                    newDuvet = []
                    temp3 = []
                    for p in L:
                        temp3.append(self.rotate(p[0],p[1]))
                    newDuvet.append(temp3)         

                    temp4 =[]
                    for L in newDuvet:
                        for p in L:
                            newP = (p[0],p[1]-40*constant)
                            temp4.append(newP)
                    newDuvet.append(temp4)
                    newDuvet.pop(0)
                    self.coordinates3D.append(newDuvet)
            if self.count % 4 == 3:
                p1 = (self.cx-(self.w/2),self.cy-(self.l/2))
                p2 = (self.cx-(self.w/2),self.cy+(self.l/2))
                p3 = (self.cx+(self.w/2),self.cy+(self.l/2))
                p4 = (self.cx+(self.w/2),self.cy-(self.l/2))
                self.coordinates2D = [p1,p2,p3,p4]
                #bottom coordinates
                sub = []
                temp1 = []
                for p in self.coordinates2D:
                    temp1.append(self.rotate(p[0],p[1]))
                sub.append(temp1)

                #top coordinates
                temp2 =[]
                for L in sub:
                    for p in L:
                        newP = (p[0],p[1]-40*constant)
                        temp2.append(newP)
                sub.append(temp2)
                self.coordinates3D.append(sub)

                pillows = []
                p1_x0 = self.cx+(self.w/2)-10
                p1_y0 = self.cy-(self.l/2)+20
                p1_x1 = self.cx+(self.w/2)-30
                p1_y1 = self.cy-(self.l/2)+20
                p1_x2 = self.cx +(self.w/2)-30
                p1_y2 = self.cy-10
                p1_x3 = self.cx+(self.w/2)-10
                p1_y3 = self.cy-10
                p1 = [(p1_x0,p1_y0),(p1_x1,p1_y1),(p1_x2,p1_y2),(p1_x3,p1_y3)]
                pillows.append(p1)

                p2_x0 = self.cx+(self.w/2)-10
                p2_y0 = self.cy+10
                p2_x1 = self.cx+(self.w/2)-30
                p2_y1 = self.cy+10
                p2_x2 = self.cx+(self.w/2)-30
                p2_y2 = self.cy+(self.l/2)-20
                p2_x3 = self.cx+(self.w/2)-10
                p2_y3 = self.cy+(self.l/2)-20
                p2 = [(p2_x0,p2_y0),(p2_x1,p2_y1),(p2_x2,p2_y2),(p2_x3,p2_y3)]
                pillows.append(p2)

                for L in pillows:
                    newPillows = []
                    temp3 = []
                    for p in L:
                        temp3.append(self.rotate(p[0],p[1]))
                    newPillows.append(temp3)         

                    temp4 =[]
                    for L in newPillows:
                        for p in L:
                            newP = (p[0],p[1]-40*constant)
                            temp4.append(newP)
                    newPillows.append(temp4)
                    newPillows.pop(0)

                    temp5 =[]
                    for L in newPillows:
                        for p in L:
                            newP = (p[0],p[1]-5*constant)
                            temp5.append(newP)
                    newPillows.append(temp5)
                    self.coordinates3D.append(newPillows)

                duvet = []
                d1_x0 = self.cx+(self.w/2)-40
                d1_y0 = self.cy-(self.l/2)
                d1_x1 = self.cx+(self.w/2)-40
                d1_y1 = self.cy+(self.l/2)
                d1_x2 = self.cx+(self.w/2)
                d1_y2 = self.cy+(self.l/2)
                d1_x3 = self.cx+(self.w/2)
                d1_y3 = self.cy-(self.l/2)
                d1 = [(d1_x0,d1_y0),(d1_x1,d1_y1),(d1_x2,d1_y2),(d1_x3,d1_y3)]
                duvet.append(d1)
                for L in duvet:
                    newDuvet = []
                    temp3 = []
                    for p in L:
                        temp3.append(self.rotate(p[0],p[1]))
                    newDuvet.append(temp3)         

                    temp4 =[]
                    for L in newDuvet:
                        for p in L:
                            newP = (p[0],p[1]-40*constant)
                            temp4.append(newP)
                    newDuvet.append(temp4)
                    newDuvet.pop(0)
                    self.coordinates3D.append(newDuvet)

        if self.name == 'cabinet':
            self.coordinates2D = [p1,p2,p3,p4]
            #bottom coordinates
            sub = []
            temp1 = []
            for p in self.coordinates2D:
                temp1.append(self.rotate(p[0],p[1]))
            sub.append(temp1)

            #top coordinates
            temp2 =[]
            for L in sub:
                for p in L:
                    newP = (p[0],p[1]-180*constant)
                    temp2.append(newP)
            sub.append(temp2)
            self.coordinates3D.append(sub)

        if self.name == 'window':
            self.coordinates2D = [p1,p2,p3,p4]
            top =[]
            temp1 = []
            for p in self.coordinates2D:
                temp1.append(self.rotate(p[0],p[1]))
            top.append(temp1)        
            temp2 =[]
            for L in top:
                for p in L:
                    newP = (p[0],p[1]-60*constant)
                    temp2.append(newP)
            top.append(temp2)
            top.pop(0)
            temp3 =[]
            for L in top:
                for p in L:
                    newP = (p[0],p[1]-100*constant)
                    temp3.append(newP)
            top.append(temp3)
            self.coordinates3D.append(top)
        
        if self.name == 'door':
            self.coordinates2D = [p1,p2,p3,p4]
            #bottom coordinates
            sub = []
            temp1 = []
            for p in self.coordinates2D:
                temp1.append(self.rotate(p[0],p[1]))
            sub.append(temp1)

            #top coordinates
            temp2 =[]
            for L in sub:
                for p in L:
                    newP = (p[0],p[1]-180*constant)
                    temp2.append(newP)
            sub.append(temp2)
            self.coordinates3D.append(sub)

    def rotate(self,x,y):
        d = math.sqrt((self.rotateCX-x)**2 + (self.rotateCY-y)**2)
        a = x-self.rotateCX
        b = -(y-self.rotateCY)
        angle = degrees(math.atan2(b,a))
        newX = self.rotateCX + d*math.cos(radians(angle+self.angle))
        newY = (self.rotateCY - 
            (d*math.sin(radians(angle+self.angle))*(self.angleYZ)))

        #change view direction
        #newY *= self.angleYZ
        newY += 100
        return (newX,newY)

