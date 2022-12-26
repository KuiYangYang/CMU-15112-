class room:
    def __init__(self,width,height):
        self.roomLength = 0
        self.roomWidth = 0
        self.cx = width/2
        self.cy = height/2
        self.wallWidth = 20
        self.dimensionStep = 50
        self.dimensionSE = 10

    def drawRoom(self,canvas):
        l = int(self.roomLength)/2
        w = int(self.roomWidth)/2
        canvas.create_rectangle(self.cx-w,self.cy-l, self.cx+w,self.cy+l,
            outline='black', width = self.wallWidth)

    def drawRuler(self,canvas):
        dwX0 = self.cx - (self.roomWidth/2) 
        dwX1 = self.cx + (self.roomWidth/2)
        dwY = self.cy - (self.roomLength/2) - self.dimensionStep
        canvas.create_line(dwX0,dwY, dwX1,dwY, fill='black')
        canvas.create_line(dwX0,dwY-self.dimensionSE, dwX0,dwY+self.dimensionSE, 
                            fill='black')
        canvas.create_line(dwX1,dwY-self.dimensionSE, dwX1,dwY+self.dimensionSE, 
                            fill='black')
        canvas.create_text(self.cx, dwY-15, text=f'{self.roomWidth} cm', 
                            font='Arial 12', fill='black')

        dlX = self.cx - (self.roomWidth/2) - self.dimensionStep
        dlY0 = self.cx - (self.roomLength/2) 
        dlY1 = self.cy + (self.roomLength/2) 
        canvas.create_line(dlX,dlY0, dlX, dlY1, fill='black')
        canvas.create_line(dlX-self.dimensionSE,dlY0, dlX+self.dimensionSE,dlY0, 
                            fill='black')
        canvas.create_line(dlX-self.dimensionSE,dlY1, dlX+self.dimensionSE,dlY1, 
                            fill='black')
        canvas.create_text(dlX-30, self.cy, text=f'{self.roomLength} cm', 
                            font='Arial 12', fill='black')

class Object:
    def __init__(self,width,height,name,roomCX,roomCY):
        self.width = width
        self.length = height
        self.name = name
        self.cx = roomCX
        self.cy = roomCY
        self.chairCount = 0
        self.bedCount = 0
        self.doorCount = 0

    def dragObject(self,x,y):
        self.cx = x
        self.cy = y

    def objectDimension(self):
        #(width,length) of obj
        if self.name == 'desk':
            self.width = 100
            self.length = 50 
        if self.name == 'chair':
            self.width = 60
            self.length = 50 
        if self.name == 'bed':
            self.width = 160
            self.length = 180
        if self.name == 'cabinet':
            self.width = 100
            self.length = 50
        if self.name == 'window':
            self.width = 100
            self.length = 20
        if self.name == 'door':
            self.width = 90
            self.length = 20

    def getObjectBoundary(self):
        return (self.width,self.length) 

    # count rotating direction
    def objectDirection(self):
        if self.name == 'chair':
            self.chairCount += 1
        if self.name == 'bed':
            self.bedCount += 1
    
    def objectCount(self):
        if self.name == 'chair':
            return self.chairCount
        if self.name == 'bed':
            return self.bedCount
        else:
            return 0

    def drawObject(self,canvas):
        if self.name == 'desk':
            canvas.create_rectangle(self.cx-(self.width/2),
            self.cy-(self.length/2),self.cx+(self.width/2),
            self.cy+(self.length/2), outline='black')      

        if self.name == 'chair':
            #set up conditions for different angle
            if self.chairCount % 4 == 1:
                canvas.create_rectangle(self.cx-25, self.cy-25, 
                                        self.cx+25,self.cy+25, outline='black')
    
                canvas.create_rectangle(self.cx-25,self.cy-35, 
                                        self.cx+25,self.cy-25, outline='black')
            elif self.chairCount % 4 == 2:
                canvas.create_rectangle(self.cx-25, self.cy-25, 
                                        self.cx+25,self.cy+25, outline='black')
    
                canvas.create_rectangle(self.cx-35,self.cy-25, 
                                        self.cx-25,self.cy+25, outline='black')
            elif self.chairCount % 4 == 3:
                canvas.create_rectangle(self.cx-25, self.cy-25, 
                                        self.cx+25,self.cy+25, outline='black')
    
                canvas.create_rectangle(self.cx-25,self.cy+25, 
                                        self.cx+25,self.cy+35, outline='black')
            elif self.chairCount % 4 == 0:
                canvas.create_rectangle(self.cx-25, self.cy-25, 
                                        self.cx+25,self.cy+25, outline='black')
    
                canvas.create_rectangle(self.cx+25,self.cy-25, 
                                        self.cx+35,self.cy+25, outline='black')

        if self.name == 'bed':
            #set up conditions for different angle
            if self.bedCount % 4 == 0:
                canvas.create_rectangle(self.cx-80,self.cy-90, 
                                        self.cx+80,self.cy+90, outline='black')
                canvas.create_rectangle(self.cx-60,self.cy-80, 
                                        self.cx-10,self.cy-60, outline='black')
                canvas.create_rectangle(self.cx+10,self.cy-80, 
                                        self.cx+60,self.cy-60, outline='black')
                canvas.create_rectangle(self.cx-80,self.cy-50, 
                                        self.cx+80,self.cy-90, outline='black')
            elif self.bedCount % 4 == 1:
                canvas.create_rectangle(self.cx-90,self.cy-80, 
                                        self.cx+90,self.cy+80, outline='black')
                canvas.create_rectangle(self.cx-80,self.cy-60, 
                                        self.cx-60,self.cy-10, outline='black')
                canvas.create_rectangle(self.cx-80,self.cy+10, 
                                        self.cx-60,self.cy+60, outline='black')
                canvas.create_rectangle(self.cx-50,self.cy-80, 
                                        self.cx-90,self.cy+80, outline='black')
            elif self.bedCount % 4 == 2:
                canvas.create_rectangle(self.cx-80,self.cy-90, 
                                        self.cx+80,self.cy+90, outline='black')
                canvas.create_rectangle(self.cx-60,self.cy+60, 
                                        self.cx-10,self.cy+80, outline='black')
                canvas.create_rectangle(self.cx+10,self.cy+60, 
                                        self.cx+60,self.cy+80, outline='black')
                canvas.create_rectangle(self.cx-80,self.cy+50, 
                                        self.cx+80,self.cy+50, outline='black')
            if self.bedCount % 4 == 3:
                canvas.create_rectangle(self.cx-90,self.cy-80, 
                                        self.cx+90,self.cy+80, outline='black')
                canvas.create_rectangle(self.cx+60,self.cy-60, 
                                        self.cx+80,self.cy-10, outline='black')
                canvas.create_rectangle(self.cx+60,self.cy+10, 
                                        self.cx+80,self.cy+60, outline='black')
                canvas.create_rectangle(self.cx+50,self.cy-80, 
                                        self.cx+50,self.cy+80, outline='black')
        if self.name == 'cabinet':
            canvas.create_rectangle(self.cx-(self.width/2),
                        self.cy-(self.length/2),self.cx+(self.width/2),
                        self.cy+(self.length/2), outline='black')        
        if self.name == 'door':
            canvas.create_rectangle(self.cx-1,self.cy-90, 
                                        self.cx+1,self.cy, outline='black')
            canvas.create_arc(self.cx-90, self.cy-90, self.cx+90, self.cy+90,
                            outline="black", width = 1, style="arc",extent=90)
    
    def drawWindow(app,canvas,x,y,objX,objY,rCx,rCy,
                    roomWidth,roomLength,wallWidth):
        x0 = int(rCx - (roomWidth/2)-(wallWidth/2))
        x1 = int(rCx - (roomWidth/2)+(wallWidth/2))
        x2 = int(rCx + (roomWidth/2)-(wallWidth/2))
        x3 = int(rCx + (roomWidth/2)+(wallWidth/2))

        y0 = int(rCy - (roomLength/2)-(wallWidth/2))
        y1 = int(rCy - (roomLength/2)+(wallWidth/2))
        y2 = int(rCy + (roomLength/2)-(wallWidth/2))
        y3 = int(rCy + (roomLength/2)+(wallWidth/2))

        #draw window
        if (x in range(x0,x1) and y in range(int(y0+objX/2),int(y3-objX/2))):
            cx = rCx
            cy = y
            canvas.create_rectangle(cx-(roomWidth/2)-(objY/2),cy-(objX/2),
                                    cx-(roomWidth/2)+(objY/2),cy+(objX/2),
                                    fill = "light gray" ,outline='black')
        elif (x in range(x2,x3) and y in range(int(y0+objX/2),int(y3-objX/2))):
            cx = rCx
            cy = y
            canvas.create_rectangle(cx+(roomWidth/2)-(objY/2),cy-(objX/2),
                                    cx+(roomWidth/2)+(objY/2),cy+(objX/2),
                                    fill = "light gray" ,outline='black')
        elif (x in range(int(x0+objX/2),int(x3-objX/2)) and y in range(y0,y1)):
            cx = x
            cy = rCy
            canvas.create_rectangle(cx-(objX/2),cy-(objY/2)-(roomLength/2),
                                    cx+(objX/2),cy+(objY/2)-(roomLength/2),
                                    fill = "light gray" ,outline='black')
        elif (x in range(int(x0+objX/2),int(x3-objX/2)) and y in range(y2,y3)):
            cx = x
            cy = rCy
            canvas.create_rectangle(cx-(objX/2),cy-(objY/2)+(roomLength/2),
                                    cx+(objX/2),cy+(objY/2)+(roomLength/2),
                                    fill = "light gray" ,outline='black')
 
    def drawDoor(app,canvas,x,y,objX,objY,rCx,rCy,
                    roomWidth,roomLength,wallWidth):
        x0 = int(rCx - (roomWidth/2)-(wallWidth/2))
        x1 = int(rCx - (roomWidth/2)+(wallWidth/2))
        x2 = int(rCx + (roomWidth/2)-(wallWidth/2))
        x3 = int(rCx + (roomWidth/2)+(wallWidth/2))

        y0 = int(rCy - (roomLength/2)-(wallWidth/2))
        y1 = int(rCy - (roomLength/2)+(wallWidth/2))
        y2 = int(rCy + (roomLength/2)-(wallWidth/2))
        y3 = int(rCy + (roomLength/2)+(wallWidth/2))

        #draw window
        if (x in range(x0,x1) and y in range(int(y0+objX/2),int(y3-objX/2))):
            cx = rCx
            cy = y
            canvas.create_rectangle(cx-(roomWidth/2)-(objY/2),cy-(objX/2),
                                    cx-(roomWidth/2)+(objY/2),cy+(objX/2),
                                    fill = "white" ,outline='black')
        elif (x in range(x2,x3) and y in range(int(y0+objX/2),int(y3-objX/2))):
            cx = rCx
            cy = y
            canvas.create_rectangle(cx+(roomWidth/2)-(objY/2),cy-(objX/2),
                                    cx+(roomWidth/2)+(objY/2),cy+(objX/2),
                                    fill = "white" ,outline='black')
        elif (x in range(int(x0+objX/2),int(x3-objX/2)) and y in range(y0,y1)):
            cx = x
            cy = rCy
            canvas.create_rectangle(cx-(objX/2),cy-(objY/2)-(roomLength/2),
                                    cx+(objX/2),cy+(objY/2)-(roomLength/2),
                                    fill = "white" ,outline='black')
        elif (x in range(int(x0+objX/2),int(x3-objX/2)) and y in range(y2,y3)):
            cx = x
            cy = rCy
            canvas.create_rectangle(cx-(objX/2),cy-(objY/2)+(roomLength/2),
                                    cx+(objX/2),cy+(objY/2)+(roomLength/2),
                                    fill = "white" ,outline='black')