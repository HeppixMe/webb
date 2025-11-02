import math
colors = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "orange": "\033[33m",
    "blue": "\033[34m",
    "purple": "\033[35m",
    "cyan": "\033[36m",
    "lightgrey": "\033[37m",
    "darkgrey": "\033[90m",
    "lightred": "\033[91m",
    "lightgreen": "\033[92m",
    "yellow": "\033[93m",
    "lightblue": "\033[94m",
    "pink": "\033[95m",
    "lightcyan": "\033[96m",
    "white": "\033[97m",
}


class canvas:

    def __init__(self, width, height, border=False, buffer=True,lightdir = [-0.7071,0.7071,0.0]):
        self.width = width * 2
        self.height = height
        self.border = border
        self.pixelSymbol = "██"
        self.pixelArray = [[False for x in range(self.width)] for y in range(self.height)]
        self.lastPixelArray = [[False for x in range(self.width)] for y in range(self.height)]
        self.buffer = buffer
        self.lightdir = lightdir
        self.colorbuffer = [[[False,False] for x in range(self.width)] for y in range(self.height)]
        self.lastColorbuffer = [[[False,False] for x in range(self.width)] for y in range(self.height)]

    def clearBuffer(self):
        self.lastPixelArray = self.pixelArray
        self.lastColorbuffer = self.colorbuffer
        self.pixelArray = [[False for x in range(self.width)] for y in range(self.height)]
        self.colorbuffer = [[[False,False] for x in range(self.width)] for y in range(self.height)]
    def clear(self):
        print("\033c")
        self.lastPixelArray = [[False for x in range(self.width)] for y in range(self.height)]
        self.lastColorbuffer = [[[False,False] for x in range(self.width)] for y in range(self.height)]

    def cursorClear(self):
        print("\033[H", end="")

    def cursorResetBottom(self):
        print(f"\033[{self.height+3};{self.width+2}H")

    def drawBorder(self):
        self.cursorClear()
        b = ""
        for x in range(self.width + 2):
            b += "─"
        print("┌" + b + "┐")

        for y in range(2,self.height + 1):
            print(f"\033[{y};{0}H", end="")
            print("│")
            print(f"\033[{y};{self.width+4}H", end="")
            print("│")


        print("└" + b + "┘")


    def point(self, x, y, color="white", buffer = True, symbol = "██"):  # █
        buffer = self.buffer and buffer
        if not buffer:
            if not color == False:
                print(colors[color])
            print(f"\033[{y+2};{x*2+2}H", end="")
            print(symbol)
            print(colors['white'])
        else:
            if color == "black":
                self.pixelArray[y+2][x+2] = False
            else:
                self.pixelArray[y+2][x+2] = True
                self.colorbuffer[y+2][x+2] = [color,symbol]

    def smile(self, x=10, y=10, low=1):
        self.point(x + 2, y + 2)
        self.point(x + 5, y + 2)
        self.point(x, y + 3 + low)
        for i in range(6):
            self.point(x + 1 + i, y + 4 + low)
        self.point(x + 7, y + 3 + low)

    def line(self, x0, y0, x1, y1, color, symbol = "██"):
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        x, y = x0, y0
        if x0 > self.width/2 or x1 > self.width/2 or x0 < 0 or x1 < 0 or y0 > self.height or y1 > self.height or y0 < 0 or y1 < 0: return

        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1

        if dx > dy:
            err = dx // 2
            while x != x1:
                if x <= max(x0,x1) and x >= min(x0,x1) and y <= max(y0,y1) and y >= min(y0,y1):
                    self.point(x, y, color, symbol=symbol)
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx 
        else:
            err = dy // 2
            while y != y1:
                if x <= max(x0,x1) and x >= min(x0,x1) and y <= max(y0,y1) and y >= min(y0,y1):
                    self.point(x, y, color, symbol=symbol)
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy

        self.point(x, y, color, symbol=symbol)  # Endpunkt setzen

    def triangle(
        self,
        p1,
        p2,
        p3,
        fill=True,
        fillColor="white",
        edgeColor="black",
        shading=True
    ):
        n = p1[3]
        symbol = self.pixelSymbol
        symbols = [
    '██', '▓▓', '▒▒', '░░', '##', '@@', '%%', '&&', 'WW', 'MM', 'BB', 'XX', 'ZZ', 'OO', 'CC',
    '||', '//', '\\', '--', '==', '++', '**', '::', ';;', ',,', '..', '((', '))', '[[',
    ']]', '>>', '<<', '``', '^^', '""', '\'\'', '::', ';;', '==', '--', '~~', '||',
    '||', 'II', 'ii', '__', '..', ',,', '::', ';;', '--', '--', '  ', '  ', '//', '\\',
    '||', '||', '--', '--'
]

        if shading:
            if self.getAngle(n,self.lightdir) > 30:
                symbol = symbols[0]+symbols[0]
            for i in range(1,len(symbols)-1):
                if self.getAngle(n,self.lightdir) > i*5+30:
                    symbol = symbols[i]+symbols[i]
        x1, y1 = round(p1[0]), round(p1[1])
        x2, y2 = round(p2[0]), round(p2[1])
        x3, y3 = round(p3[0]), round(p3[1])
    
        if p1 == p2 == p3:
            self.point(p1[0],p2[1],fillColor,symbol=symbol)
        elif x1 == x2 == x3 or y1 == y2 == y3:
            return
        elif p1 == p2 or p2 == p3 or p3 == p1 or abs(x2 - x1) < 1 and abs(y2-y1)<1 or abs(x3 - x2) < 1 and abs(y3-y2)<1 or abs(x1 - x3) < 1 and abs(y1-y3)<1:
            
            self.line(x1, y1, x2, y2,fillColor,symbol=symbol)
            self.line(x2, y2, x3, y3,fillColor,symbol=symbol)
            self.line(x3, y3, x1, y1,fillColor,symbol=symbol)
        else:
            if fill:
                xmin = min(x1,x2,x3)
                ymin = min(y1,y2,y3)
                xmax = max(x1,x2,x3)
                ymax = max(y1,y2,y3)
                for y in range(ymin,ymax):
                    for x in range(xmin,xmax):
                        if self.PointInTriangle(p1[:2], p2[:2], p3[:2], (x, y)):
                            self.point(x, y, fillColor,symbol=symbol)
            self.line(x1, y1, x2, y2,edgeColor,symbol=symbol)
            self.line(x2, y2, x3, y3,edgeColor,symbol=symbol)
            self.line(x3, y3, x1, y1,edgeColor,symbol=symbol)

    def multibleTriangle(self, points,fill = True, fillColor = "white", edgeColor="white", shading = False):
        if len(points)==3:
            self.triangle(points[0],points[1],points[2],fill,fillColor,edgeColor)
        elif len(points)>3:
            self.triangle(points[0],points[1],points[2],fill,fillColor,edgeColor)
            lastPoint=2 
            for i in range(3,len(points)):
                self.triangle(points[0],points[lastPoint],points[i],fill,fillColor,edgeColor)
                lastPoint+=i

    def DOT(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2

        return x1 * x2 + y1 * y2

    def Perpendicular(self, vec):
        x, y = vec
        return (y, -x)

    def PointOnRightSideOfLine(self, line, point):
        x1, y1, x2, y2 = line
        px, py = point
        ap = (px - x1, py - y1)
        abPerp = self.Perpendicular((x2 - x1, y2 - y1))
        return self.DOT(ap, abPerp) >= 0

    def PointInTriangle(self, a, b, c, p):
        ax, ay = a
        bx, by = b
        cx, cy = c
        sideAB = self.PointOnRightSideOfLine((ax, ay, bx, by), p)
        sideBC = self.PointOnRightSideOfLine((bx, by, cx, cy), p)
        sideCA = self.PointOnRightSideOfLine((cx, cy, ax, ay), p)
        return sideAB == sideBC == sideCA
    def rotate(self,p,a):
        return [p[0]*math.cos(a) + p[2]*math.sin(a),p[1], -p[0]*math.sin(a)+p[2]*math.cos(a)]

    def getAngle(self,a,b):
        scalar = a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
        absa = math.sqrt(a[0]**2+a[1]**2+a[2]**2)
        absb = math.sqrt(b[0]**2+b[1]**2+b[2]**2)
        return math.degrees(math.acos(scalar/(absa*absb)))

    def render(self, obj, scale = 1,offX = 0, offY = 0, rotate = False, rotationAngle = 0.0005, shading = True, color = "white"):
        cube = open(obj, "r")
        vertecies = []
        triangles = []
        normals = []
        final = []
        for line in cube:
            if line.startswith("vn"):
                line = line.removeprefix("vn").removesuffix("\n").split(" ")
                temp = []
                for i in range(len(line)):
                    if not line[i]=='':
                        temp.append(float(line[i]))
                normals.append(temp)
            elif line.startswith("v "):
                line = line.removeprefix("v ").removesuffix("\n").split(" ")
                temp = []
                for i in range(len(line)):
                    if not line[i]=='':
                        temp.append(float(line[i]))
                vertecies.append(temp)

            elif line.startswith("f"):
                line = line.removeprefix("f ").removesuffix("\n").split(" ")
                triangle = []
                for i in range(len(line)):
                    triangle.append(line[i].split("/"))
                temp2 = []
                for j in range(len(triangle)):
                    if not line[j]=='':
                        temp2.append([int(triangle[j][0]),int(triangle[j][2])])
                triangles.append(temp2)
                temp2 = []

                temp2 =[]
                c = 0
                for i in triangles:
                    temp=[]
                    for p in i:
                        j = p[0]
                        if not type(j)==list:
                            temp.append([offX - vertecies[j-1][0]*scale, offY - vertecies[j-1][1]*scale,vertecies[j-1][2],normals[p[1]-1]])
                    temp2.append(temp)
                    c+=1
        cube.close()

        def sortZ(e):
            out = 0
            for m in range(len(e)): out += e[m][2]
            return out/len(e)        

        final = temp2
        final.sort(key=sortZ)
        for f in final:
            self.multibleTriangle(f, shading=shading, fillColor=color)
        rot = 0
        if self.buffer: self.drawBuffer()
        
        while rotate:
            rot += rotationAngle
            rot %= 1
            final = temp2
            final.sort(key=sortZ)
            self.clearBuffer()
            for f in final:
                for i in range(len(f)):
                    temp = self.rotate([(offX - f[i][0])/scale, (offY - f[i][1])/scale, f[i][2]],math.pi*rot)
                    f[i] = [offX - temp[0]*scale,offY - temp[1]*scale,temp[2],f[i][3]]
                self.multibleTriangle(f,shading=shading, fillColor=color)
            if self.buffer: self.drawBuffer()


    def drawBuffer(self):
        for y in range(len(self.pixelArray)):
            for x in range(len(self.pixelArray[y])):
                if self.pixelArray[y][x] and not self.lastPixelArray[y][x]:
                    self.point(x,y,self.colorbuffer[y][x][0],symbol=self.colorbuffer[y][x][1], buffer=False)
                elif not self.pixelArray[y][x] and self.lastPixelArray[y][x]:
                    self.point(x,y,"black", buffer=False, symbol="  ")
                elif self.pixelArray[y][x] == self.lastPixelArray[y][x]:
                    if not self.colorbuffer[y][x] == self.lastColorbuffer[y][x] and self.pixelArray[y][x]:
                        self.point(x,y,self.colorbuffer[y][x][0],symbol=self.colorbuffer[y][x][1], buffer=False)
