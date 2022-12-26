from cmu_112_graphics import *
from isometric import *
from roomAndObject import *
        
def appStarted(app):
    app.r = None
    app.numButton = 7
    app.stepButton = int(app.width / app.numButton)
    app.buttonHeight = 50
    app.desk = None
    app.chair = None
    app.bed = None
    app.cabinet =None
    app.window = None
    app.door = None
    app.objects = []
    app.x = None
    app.y = None
    app.isometricView = 0
    app.isometricAngle = 45
    app.angleYZ = 0.5
    app.start = False
    app.onTheEdge = False
    app.windowXY = []
    app.doorXY= []
    app.helper = 0
    app.instruction = (''' 
    Builder is a design interface for architecture. Users can create a room
    and configure the position for furniture, windows and doors. The user
    experience allows all objects except the room to be moved, rotated and 
    deleted. When completing 2D design, users can transfer to isometric 
    view and navigate the space by rotating the view.

    Instruction
    Step1: create a room
    1.click 'Create Room' to create room and set up scale of the room

    Step2: create furnitures
    1.Click 'desk', 'chair', 'cabinet' or 'bed' to create objects for the room.
    2.The object will pop up in the center,
        you can drag the object within the room.
    3.Click the object and press 'r' to rotate.
    4.Click the object and press 'd' to delete.
    
    Step3: create windows and doors
    1.Click 'window' or 'door' and click the wall of the room.

    Step4: change to isometric view
    1.Click 'Isometric', the 2D plan will change to 2.5D. 
    2.Press 'Right','Left','Up' or 'Down' to adjust isometric view.
    3.Click 'Isometric' again, the 2.5D view will change to 2D.

    Step5: reset
    1.Click 'Reset' to remove all the objects in the board.
''')

def mousePressed(app,event):
    app.x = event.x
    app.y = event.y
    isStart(app)
    if (event.x in range(0,app.stepButton) and 
        event.y in range(0,app.buttonHeight)):
        app.r = room(app.width,app.height)
        l = app.getUserInput('''What is the length of the room?
        (input 200-600 Unit:cm)''')
        app.r.roomLength = isValidRoomDimension(app,l)

        w = app.getUserInput('''What is the width of the room?
        (input 200-600 Unit:cm)''')
        app.r.roomWidth = isValidRoomDimension(app,w)
    
    if (event.x in range(50,150) and 
        event.y in range(app.height-100,app.height-50)):
        app.helper += 1
        if app.helper%2 == 1:
            app.showMessage(app.instruction)
    
    if app.r != None:
        if (event.x in range(app.stepButton,app.stepButton*2) and 
            event.y in range(0,app.buttonHeight)):
            app.desk = Object(app.width,app.height,'desk',app.r.cx,app.r.cy)
            app.desk.objectDimension()
            app.objects.append(app.desk)
            checkNewObjectIntersection(app,app.desk)
                        
        if (event.x in range(app.stepButton*2,app.stepButton*3) and 
            event.y in range(0,app.buttonHeight)):
            app.chair = Object(app.width,app.height,'chair',app.r.cx,app.r.cy)
            app.chair.objectDimension()
            app.objects.append(app.chair)
            checkNewObjectIntersection(app,app.chair)
        
        if (event.x in range(app.stepButton*3,app.stepButton*4) and 
            event.y in range(0,app.buttonHeight)):
            app.bed = Object(app.width,app.height,'bed',app.r.cx,app.r.cy)
            app.bed.objectDimension()
            app.objects.append(app.bed)
            checkNewObjectIntersection(app,app.bed)
        
        if (event.x in range(app.stepButton*4,app.stepButton*5) and 
            event.y in range(0,app.buttonHeight)):
            app.cabinet = Object(app.width,app.height,'cabinet',
                                    app.r.cx,app.r.cy)
            app.cabinet.objectDimension()
            app.objects.append(app.cabinet)
            checkNewObjectIntersection(app,app.cabinet)
        
        if (event.x in range(app.stepButton*5,app.stepButton*6) and 
            event.y in range(0,app.buttonHeight)):
            app.window = Object(app.width,app.height,'window',app.r.cx,app.r.cy)
            app.window.objectDimension()
            app.objects.append(app.window)

        if (event.x in range(app.stepButton*6,app.stepButton*7) and 
            event.y in range(0,app.buttonHeight)):
            app.door = Object(app.width,app.height,'door',app.r.cx,app.r.cy)
            app.door.objectDimension()
            app.objects.append(app.door)

        if (event.x in range(app.width-150,app.width-50) and 
            event.y in range(app.height-100,app.height-50)):
            app.isometricView += 1
        
        if (event.x in range(app.width-350,app.width-250) and 
            event.y in range(app.height-100,app.height-50)):
            reset(app)

        
        if len(app.objects) > 0 and app.objects[-1].name == 'window':
            generateWindowCenter(app)
        elif len(app.objects) > 0 and app.objects[-1].name == 'door':
            generateDoorCenter(app)

def checkNewObjectIntersection(app,obj):
    result = intersection(app,obj,obj.cx,obj.cy)
    if result[0] == True:
        (newCx,newCy) = moveNewObject(app,obj,app.r.cx,app.r.cy)
        if withinRoom(app,int(newCx),int(newCy),obj.width,obj.length):
            obj.cx = newCx
            obj.cy = newCy
        else:
            app.objects.pop()
            app.showMessage("The room is too small!")

def moveNewObject(app,obj,cx,cy):
    result = intersection(app,obj,cx,cy)
    if result[0] == False:
        return (cx,cy)
    else:
        (x,y) = result[1]
        return moveNewObject(app,obj,x,y)

# remove all object
def reset(app):
    app.r = None
    app.objects = []

#create window.cx and window.cy 
def generateWindowCenter(app):
    windowCount = 0
    #create set to prevent duplicate 
    windowSet = set()
    for obj in app.objects:
        #click edge to generate window
        if (obj != None and obj.name == 'window'):
            windowCount+=1
            pt = onTheEdgeOfRoom(app,app.x,app.y,obj.width,obj.length)
            if app.onTheEdge == True:
                windowSet.add(pt)
    for i in windowSet:
        app.windowXY.append(i)
    if len(app.windowXY) >windowCount:
        app.windowXY.pop(windowCount-1) 
    if len(app.windowXY) > 0:
        index = 0
        for obj in app.objects:
            if (windowCount == len(app.windowXY) and obj.name == 'window'):
                (x,y) = app.windowXY[index]
                obj.cx = x
                obj.cy = y
                index+=1

def generateDoorCenter(app):
    doorCount = 0
    #create set to prevent duplicate 
    doorSet = set()
    for obj in app.objects:
        #click edge to generate window
        if (obj != None and obj.name == 'door'):
            doorCount+=1
            pt = onTheEdgeOfRoom(app,app.x,app.y,obj.width,obj.length)
            if app.onTheEdge == True:
                doorSet.add(pt)
    for i in doorSet:
        app.doorXY.append(i)
    if len(app.doorXY) >doorCount:
        app.doorXY.pop(doorCount-1) 
    if len(app.doorXY) > 0:
        index = 0
        for obj in app.objects:
            if (doorCount == len(app.doorXY) and obj.name == 'door'):
                (x,y) = app.doorXY[index]
                obj.cx = x
                obj.cy = y
                index+=1

def isValidRoomDimension(app,n):
        if (n == None or len(n)==0):
            app.showMessage('Use default length 400')
            return 400 #default
        elif n != None and (int(n)<200 or int(n)>600):
            app.showMessage('Invalid Number, input again!')
            n = app.getUserInput('What is width?\ninput 200-600')
            return isValidRoomDimension(app,n)
        else:
            return int(n)

def mouseDragged(app, event):
    for obj in app.objects:
        if obj != None:
            (x,y) = obj.getObjectBoundary()
            x0 = int(obj.cx - (x/2))
            x1 = int(obj.cx + (x/2))
            y0 = int(obj.cy - (y/2))
            y1 = int(obj.cy + (y/2))
            if (event.x in range(x0,x1) and event.y in range(y0,y1) 
            and withinRoom(app,event.x,event.y,x,y) and obj.name != 'window'
            and obj.name != 'door'):
                result = intersection(app,obj,event.x,event.y)
                if result[0] == False:
                    obj.dragObject(event.x,event.y)

def intersection(app,obj,x,y):
    if len(app.objects) >1:
        for i in range(len(app.objects)):
            if obj == app.objects[i]:
                continue
            (nX,nY) = obj.getObjectBoundary()
            nX1 = int(x - (nX/2))
            nX2 = int(x + (nX/2))
            nY1 = int(y - (nY/2))
            nY2 = int(y + (nY/2))   
            nX = [i for i in range(nX1,nX2)]        
            nY = [i for i in range(nY1,nY2)]
            old = app.objects[i]
            (oX,oY) = old.getObjectBoundary()
            oX1 = int(old.cx - (oX/2))
            oX2 = int(old.cx + (oX/2))
            oY1 = int(old.cy - (oY/2))
            oY2 = int(old.cy + (oY/2))
            oX = [i for i in range(oX1,oX2)]
            oY = [i for i in range(oY1,oY2)]
            for tx in nX:
                for ty in nY:
                    if (tx in oX) and (ty in oY):
                        newCX = x
                        newCY = (oY1 - obj.length/2)
                        pt = (newCX,newCY)
                        # when intersect, move object
                        if x < oX1:
                            obj.cx = oX1 - (obj.width/2)
                        elif x > oX2:
                            obj.cx = oX2 + (obj.width/2)
                        elif y < oY1:
                            obj.cy = oY1 - (obj.length/2)
                        elif y > oY2:
                            obj.cy = oY2 + (obj.length/2)
                        return (True,pt)
    pt = (x,y)
    return (False,pt)

#check whether the object inside room
def withinRoom(app,cx,cy,objX,objY):
    x0 = int(app.r.cx - (app.r.roomWidth/2)+(objX/2)+(app.r.wallWidth/2))
    x1 = int(app.r.cx + (app.r.roomWidth/2)-(objX/2)-(app.r.wallWidth/2))
    y0 = int(app.r.cy - (app.r.roomLength/2)+(objY/2)+(app.r.wallWidth/2))
    y1 = int(app.r.cy + (app.r.roomLength/2)-(objY/2)-(app.r.wallWidth/2))
    
    if cx in range(x0,x1) and cy in range(y0,y1):
        return True
    return False

#check window on the wall
def onTheEdgeOfRoom(app,x,y,objX,objY):
    x0 = int(app.r.cx - (app.r.roomWidth/2)-(app.r.wallWidth/2))
    x1 = int(app.r.cx - (app.r.roomWidth/2)+(app.r.wallWidth/2))
    x2 = int(app.r.cx + (app.r.roomWidth/2)-(app.r.wallWidth/2))
    x3 = int(app.r.cx + (app.r.roomWidth/2)+(app.r.wallWidth/2))

    y0 = int(app.r.cy - (app.r.roomLength/2)-(app.r.wallWidth/2))
    y1 = int(app.r.cy - (app.r.roomLength/2)+(app.r.wallWidth/2))
    y2 = int(app.r.cy + (app.r.roomLength/2)-(app.r.wallWidth/2))
    y3 = int(app.r.cy + (app.r.roomLength/2)+(app.r.wallWidth/2))

    if (x in range(x0,x1) and y in range(int(y0+objX/2),int(y3-objX/2))):
        app.onTheEdge = True
        return (app.r.cx - (app.r.roomWidth/2),y)

    elif (x in range(x2,x3) and y in range(int(y0+objX/2),int(y3-objX/2))):
        app.onTheEdge = True
        return (app.r.cx + (app.r.roomWidth/2),y)

    elif (x in range(int(x0+objX/2),int(x3-objX/2)) and y in range(y0,y1)):
        app.onTheEdge = True
        return (x,app.r.cy - (app.r.roomLength/2))

    elif (x in range(int(x0+objX/2),int(x3-objX/2)) and y in range(y2,y3)):
        app.onTheEdge = True
        return (x,app.r.cy + (app.r.roomLength/2))
    else:
        app.onTheEdge = False

def rotateRoom(app):
    temp = app.r.roomWidth
    app.r.roomWidth = app.r.roomLength
    app.r.roomLength = temp

def rotateObject(app,obj):
    tempCx = obj.cx
    tempCy = obj.cy
    tempWidth = obj.width
    tempLength = obj.length
    obj.length = obj.width
    obj.width = tempLength
    result = intersection(app,obj,obj.cx,obj.cy)
    if ((not withinRoom(app,obj.cx,obj.cy,obj.width,obj.length)) or
        (not withinRoom(app,obj.cx,obj.cy,obj.width,obj.length) and 
        result[0] == True)):
        obj.cx = tempCx
        obj.cy = tempCy
        obj.width = tempWidth
        obj.length = tempLength
        app.showMessage("Can not rotate. The space is too small!")

def keyPressed(app,event):
    #rotate object
    if event.key == 'r':
        for obj in app.objects: 
            (x,y) = obj.getObjectBoundary()
            x0 = int(obj.cx - (x/2))
            x1 = int(obj.cx + (x/2))
            y0 = int(obj.cy - (y/2))
            y1 = int(obj.cy + (y/2))
            if app.x in range(x0,x1) and app.y in range(y0,y1):
                # add count to isometric
                obj.objectDirection()
                rotateObject(app,obj)
        #rotateRoom(app)

    #delete object
    if event.key == 'd':
        for obj in app.objects:
            if obj != None:
                (x,y) = obj.getObjectBoundary()
                x0 = int(obj.cx - (x/2))
                x1 = int(obj.cx + (x/2))
                y0 = int(obj.cy - (y/2))
                y1 = int(obj.cy + (y/2))
                if app.x in range(x0,x1) and app.y in range(y0,y1):
                    app.objects.remove(obj)
    
    if app.isometricView %2 ==1:
        if event.key == 'Right':
            app.isometricAngle+=1
        if event.key == 'Left':
            app.isometricAngle-=1
        if event.key == 'Up':
            app.angleYZ -= 0.1 
        if event.key == 'Down':
            app.angleYZ += 0.1
        
        if app.angleYZ < -1:
            app.angleYZ = -1
        if app.angleYZ > 1:
            app.angleYZ = 1 

def isStart(app):
    cx = int(app.width/2)
    cy = int(app.height-200)
    w = 50
    h = 25
    if app.x in range(cx-w,cx+w) and app.y in range(cy-h,cy+h):
        app.start = True

def drawInstruction(app,canvas):
    canvas.create_text(app.width/2, app.height/2 ,
                       text=app.instruction, font='Arial 12', fill='black')
    canvas.create_rectangle(app.width/2-50,app.height-225, 
                        app.width/2+50,app.height-175 , outline = 'black')
    canvas.create_text(app.width/2,app.height-200,
                    text='Start', font='Arial 24', fill='black')
    canvas.create_text(app.width/2,200,
                    text='Builder', font='Arial 24', fill='black')

def redrawAll(app, canvas):
    if app.start == False:
        drawInstruction(app,canvas)
    else:
        #draw buttons
        for i in range(app.numButton):
            canvas.create_rectangle(i*app.stepButton,0, (i+1)*app.stepButton ,
                                    app.buttonHeight , outline = 'black')
            if i == 0:
                canvas.create_text((i+0.5)*app.stepButton, app.buttonHeight/2 ,
                        text='Create Room', font='Arial 12', fill='black')
            if i == 1:
                canvas.create_text((i+0.5)*app.stepButton, app.buttonHeight/2 ,
                        text='Desk', font='Arial 12', fill='black')
            if i == 2:
                canvas.create_text((i+0.5)*app.stepButton, app.buttonHeight/2 ,
                        text='Chair', font='Arial 12', fill='black')
            if i == 3:
                canvas.create_text((i+0.5)*app.stepButton, app.buttonHeight/2 ,
                        text='Bed', font='Arial 12', fill='black')
            if i == 4:
                canvas.create_text((i+0.5)*app.stepButton, app.buttonHeight/2 ,
                        text='Cabinet', font='Arial 12', fill='black')
            if i == 5:
                canvas.create_text((i+0.5)*app.stepButton, app.buttonHeight/2 ,
                        text='Window', font='Arial 12', fill='black')
            if i == 6:
                canvas.create_text((i+0.5)*app.stepButton, app.buttonHeight/2 ,
                        text='Door', font='Arial 12', fill='black')
        
        #isometric button
        canvas.create_rectangle(app.width-150, app.height-100, app.width-50,
                            app.height-50, outline = 'black')
        canvas.create_text(app.width-100, app.height-75,
                            text='Isometric', font='Arial 12', fill='black')
        
        #reset button
        canvas.create_rectangle(app.width-350, app.height-100, app.width-250,
                            app.height-50, outline = 'black')
        canvas.create_text(app.width-300, app.height-75,
                            text='Reset', font='Arial 12', fill='black')
        
        #helper button
        canvas.create_rectangle(50, app.height-100, 150,
                            app.height-50, outline = 'black')
        canvas.create_text(100, app.height-75,
                            text='Helper', font='Arial 12', fill='black')
        
        if app.isometricView %2 ==0:
            #draw room
            if app.r != None:
                app.r.drawRoom(canvas)
                app.r.drawRuler(canvas)
            #draw objects
            for obj in app.objects:
                #click edge to generate window
                if (obj != None and obj.name == 'window' 
                    and len(app.windowXY)>0):
                    for (x,y) in app.windowXY:
                        obj.drawWindow(canvas,x,y,obj.width,obj.length,
                        app.r.cx,app.r.cy,app.r.roomWidth,
                        app.r.roomLength,app.r.wallWidth)
                elif (obj != None and obj.name == 'door' 
                    and len(app.doorXY)>0):
                    for (x,y) in app.doorXY:
                        obj.drawDoor(canvas,x,y,obj.width,obj.length,
                        app.r.cx,app.r.cy,app.r.roomWidth,
                        app.r.roomLength,app.r.wallWidth)

                elif obj != None and obj.name != 'window' and obj.name!= 'door':
                    obj.drawObject(canvas)         
        else:
            if app.r != None:
                outerRoom = Isometric('room',app.r.cx,app.r.cy,
                app.r.roomWidth+(app.r.wallWidth),
                app.r.roomLength+(app.r.wallWidth),app.r.cx,app.r.cy,
                app.r.roomWidth,
                app.r.roomLength,app.r.wallWidth,
                app.isometricAngle,app.angleYZ,0)
                
                innerRoom = Isometric('room',app.r.cx,app.r.cy,
                app.r.roomWidth-(app.r.wallWidth),
                app.r.roomLength-(app.r.wallWidth),app.r.cx,app.r.cy,
                app.r.roomWidth,
                app.r.roomLength,app.r.wallWidth,
                app.isometricAngle,app.angleYZ,0)
                
                isometricRoom = [outerRoom,innerRoom]

                #draw floor
                a = isometricRoom[0].coordinates3D[0][0][0]
                b = isometricRoom[0].coordinates3D[0][0][1]
                c = isometricRoom[0].coordinates3D[0][0][2]
                d = isometricRoom[0].coordinates3D[0][0][3]
                canvas.create_polygon(a[0],a[1],b[0],b[1],c[0],c[1],d[0],d[1],
                                fill = 'light gray')

                for isoRoom in isometricRoom:
                    # connect 2d plan
                    for s in isoRoom.coordinates3D:
                        for L in s:
                            for i in range(len(L)-1):
                                a = L[i]
                                b = L[i+1]
                                canvas.create_line(a[0],a[1],b[0],b[1], 
                                                fill='black')
                                if i == len(L)-2:
                                    a = L[i+1]
                                    b = L[0]
                                    canvas.create_line(a[0],a[1],b[0],b[1],
                                                fill='black')      
                    # connect vertical points
                    for s in isoRoom.coordinates3D:
                        for col in range(len(s[0])):
                            for row in range(len(s)-1):
                                a = s[row][col]
                                b = s[row+1][col]
                                canvas.create_line(a[0],a[1],b[0],b[1], 
                                                fill='black')
            
                for obj in app.objects:     
                    iso = Isometric(obj.name,obj.cx,obj.cy,obj.width,obj.length,
                    app.r.cx,app.r.cy,app.r.roomWidth,
                    app.r.roomLength,app.r.wallWidth,
                    app.isometricAngle,app.angleYZ,obj.objectCount())
                    if(((obj.name == 'window' or obj.name == 'door') and 
                        obj.cx == app.r.cx and obj.cy == app.r.cy)):
                        return
                    # connect 2d plan
                    for s in iso.coordinates3D:
                        for L in s:
                            for i in range(len(L)-1):
                                a = L[i]
                                b = L[i+1]
                                canvas.create_line(a[0],a[1],b[0],b[1], 
                                fill='black')
                                if i == len(L)-2:
                                    a = L[i+1]
                                    b = L[0]
                                    canvas.create_line(a[0],a[1],b[0],b[1],
                                    fill='black')      
                    # connect vertical points
                    for s in iso.coordinates3D:
                        for col in range(len(s[0])):
                            for row in range(len(s)-1):
                                a = s[row][col]
                                b = s[row+1][col]
                                canvas.create_line(a[0],a[1],b[0],b[1], 
                                fill='black')

runApp(width=1000, height=1000)
