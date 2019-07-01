from PyQt5.QtCore import QDir, QPoint, QRect, QSize, Qt
from PyQt5.QtGui import QImage, QImageWriter, QPainter, QPen, qRgb, QColor, QBrush, QPainterPath
from PyQt5.QtWidgets import (QAction, QApplication, QColorDialog, QFileDialog, QStackedWidget,
        QInputDialog, QMainWindow, QMenu, QMessageBox, QWidget)
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog,QGraphicsView,QGraphicsScene,QVBoxLayout, QFrame

from PyQt5.QtWidgets import QApplication, QLabel, QWidget ,QDialog, QGraphicsView, QGraphicsScene, QGridLayout, QPushButton
from collections import deque


class ScribbleArea(QWidget):
    def __init__(self, parent=None):
        super(ScribbleArea, self).__init__(parent)

        self.setAttribute(Qt.WA_StaticContents)
        self.modified = False
        self.scribbling = False
        self.myPenWidth = 3
        self.myPenColor = Qt.white
        self.image = QImage()
        self.lastPoint = QPoint()
        global clicked
        clicked = False
        global drawcolor
        drawcolor = qRgb(255,255,255)
        global red
        red = 255
        global green
        green = 255
        global blue
        blue = 255 
        self.current = QFrame(self)
        self.current.setGeometry(QtCore.QRect(80, 830, 70, 70))
        self.current.setStyleSheet("background-color: #ffffff")
        self.current.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.current.setFrameShadow(QtWidgets.QFrame.Raised)

        btn1 = QPushButton('sky', self)
        btn1.setStyleSheet("background-color: rgb(163, 255, 238)")
        btn1.setGeometry(QtCore.QRect(190, 830, 150, 80))
        font = QtGui.QFont()
        font.setFamily("AppleGothic")
        font.setPointSize(24)
        btn1.setFont(font)
        btn1.clicked.connect(self.btn1_clicked)

        btn2 = QPushButton('tree', self)
        btn2.setStyleSheet("background-color: #b1d627")
        btn2.setGeometry(QtCore.QRect(350, 830, 150, 80))
        btn2.clicked.connect(self.btn2_clicked)
        btn2.setFont(font)

        btn3 = QPushButton('cloud', self)
        btn3.setStyleSheet("background-color: #686868")
        btn3.setGeometry(QtCore.QRect(510, 830, 150, 80))
        btn3.clicked.connect(self.btn3_clicked)
        btn3.setFont(font)

        btn4 = QPushButton('mountain', self)
        btn4.setStyleSheet("background-color: #899c61")
        btn4.setGeometry(QtCore.QRect(670, 830, 150, 80))
        btn4.clicked.connect(self.btn4_clicked)
        btn4.setFont(font)

        btn5 = QPushButton('grass', self)
        btn5.setStyleSheet("background-color: #7dd700")
        btn5.setGeometry(QtCore.QRect(830, 830, 150, 80))
        btn5.clicked.connect(self.btn5_clicked)
        btn5.setFont(font)

        btn6 = QPushButton('sea', self)
        btn6.setStyleSheet("background-color: #a1d3ec")
        btn6.setGeometry(QtCore.QRect(990, 830, 150, 80))
        btn6.clicked.connect(self.btn6_clicked)
        btn6.setFont(font)

        btn7 = QPushButton('river', self)
        btn7.setStyleSheet("background-color: #9862d6")
        btn7.setGeometry(QtCore.QRect(1150, 830, 150, 80))
        btn7.clicked.connect(self.btn7_clicked)
        btn7.setFont(font)

        btn8 = QPushButton('rock', self)
        btn8.setStyleSheet("background-color: #9c6228")
        btn8.setGeometry(QtCore.QRect(1310, 830, 150, 80))
        btn8.clicked.connect(self.btn8_clicked)
        btn8.setFont(font)

        btn9 = QPushButton('plant', self)
        btn9.setStyleSheet("background-color: #92fa10")
        btn9.setGeometry(QtCore.QRect(1470, 830, 150, 80))
        btn9.clicked.connect(self.btn9_clicked)
        btn9.setFont(font)

        btn10 = QPushButton('sand', self)
        btn10.setStyleSheet("background-color: #9f9f00")
        btn10.setGeometry(QtCore.QRect(1630, 830, 150, 80))
        btn10.clicked.connect(self.btn10_clicked)
        btn10.setFont(font)

        btn11 = QPushButton('snow', self)
        btn11.setStyleSheet("background-color: #a6a5b3")
        btn11.setGeometry(QtCore.QRect(190, 930, 150, 80))
        btn11.clicked.connect(self.btn11_clicked)
        btn11.setFont(font)

        btn12 = QPushButton('water', self)
        btn12.setStyleSheet("background-color: #bcd6ff")
        btn12.setGeometry(QtCore.QRect(350, 930, 150, 80))
        btn12.clicked.connect(self.btn12_clicked)
        btn12.setFont(font)

        btn13 = QPushButton('hill', self)
        btn13.setStyleSheet("background-color: #80d663")
        btn13.setGeometry(QtCore.QRect(510, 930, 150, 80))
        btn13.clicked.connect(self.btn13_clicked)
        btn13.setFont(font)

        btn14 = QPushButton('dirt', self)
        btn14.setStyleSheet("background-color: #6b6e1c")
        btn14.setGeometry(QtCore.QRect(670, 930, 150, 80))
        btn14.clicked.connect(self.btn14_clicked)
        btn14.setFont(font)

        btn15 = QPushButton('road', self)
        btn15.setStyleSheet("background-color: #9a6d1c")
        btn15.setGeometry(QtCore.QRect(830, 930, 150, 80))
        btn15.clicked.connect(self.btn15_clicked)
        btn15.setFont(font)

        btn16 = QPushButton('flower', self)
        btn16.setStyleSheet("background-color: #770000")
        btn16.setGeometry(QtCore.QRect(990, 930, 150, 80))
        btn16.clicked.connect(self.btn16_clicked)
        btn16.setFont(font)

        btn17 = QPushButton('stone', self)
        btn17.setStyleSheet("background-color: #a9a85c")
        btn17.setGeometry(QtCore.QRect(1150, 930, 150, 80))
        btn17.clicked.connect(self.btn17_clicked)
        btn17.setFont(font)

        btn18 = QPushButton('bush', self)
        btn18.setStyleSheet("background-color: #5e6e28")
        btn18.setGeometry(QtCore.QRect(1310, 930, 150, 80))
        btn18.clicked.connect(self.btn18_clicked)
        btn18.setFont(font)

        btn19 = QPushButton('wood', self)
        btn19.setStyleSheet("background-color: #c17f09")
        btn19.setGeometry(QtCore.QRect(1470, 930, 150, 80))
        btn19.clicked.connect(self.btn19_clicked)
        btn19.setFont(font)

        btn20 = QPushButton('gravel', self)
        btn20.setStyleSheet("background-color: #7f28d7")
        btn20.setGeometry(QtCore.QRect(1630, 930, 150, 80))
        btn20.clicked.connect(self.btn20_clicked)
        btn20.setFont(font)

        self.pencil = QPushButton('Pencil', self)
        self.pencil.setStyleSheet("background-color: #4b5b55")
        self.pencil.setGeometry(QtCore.QRect(50, 110, 100, 100))
        self.pencil.clicked.connect(self.setPaint)
        self.pencil.setFont(font)

        self.pen = QPushButton('Pen', self)
        self.pen.setStyleSheet("background-color: #4b5b55")
        self.pen.setGeometry(QtCore.QRect(50, 250, 100, 100))
        self.pen.clicked.connect(self.setPenWidth10)
        self.pen.setFont(font)

        self.paint = QPushButton('Painting', self)
        self.paint.setStyleSheet("background-color: #4b5b55")
        self.paint.setGeometry(QtCore.QRect(50, 380, 100, 100))
        self.paint.clicked.connect(self.setPenWidth1)
        self.paint.setFont(font)

        clear = QPushButton('clear', self)
        clear.setStyleSheet("background-color: #4b5b55")
        clear.setGeometry(QtCore.QRect(50, 530, 100, 100))
        clear.clicked.connect(self.clearframe)
        clear.setFont(font)

        cur = QLabel('current', self)
        cur.setStyleSheet("color: #ffffff")
        cur.setGeometry(50,650,100,100)
        cur.setFont(font)


        self.stat = QLabel('Pen', self)
        self.stat.setStyleSheet("color: #ffffff")
        self.stat.setGeometry(50,700,100,100)
        self.stat.setFont(font)


    def openImage(self, fileName):
        loadedImage = QImage()
        if not loadedImage.load(fileName):
            return False

        newSize = loadedImage.size().expandedTo(self.size())
        self.resizeImage(loadedImage, newSize)
        self.image = loadedImage
        self.modified = False
        self.update()
        return True

    def saveImage(self, fileName, fileFormat):
        visibleImage = self.image
        rect = QtCore.QRect(280, 120, 660, 660)

        visibleImage = visibleImage.copy(rect)

        self.resizeImage(visibleImage, self.size())

        if visibleImage.save(fileName, fileFormat):
            self.modified = False
            return True
        else:
            return False

    def setPaint(self, event) :
        global clicked
        clicked = False
        self.stat.setText("Pencil")
        self.myPenWidth = 3
        self.pencil.setStyleSheet("background-color: #ffffff")
        self.pen.setStyleSheet("background-color: #4b5b55")
        self.paint.setStyleSheet("background-color: #4b5b55")

    def setPenColor(self, newColor):
        self.myPenColor = newColor

    def setPenWidth1(self, newWidth):
        self.myPenWidth = 0
        self.stat.setText("Paint")
    
        global clicked
        clicked = True
        self.pencil.setStyleSheet("background-color: #4b5b55")
        self.pen.setStyleSheet("background-color: #4b5b55")
        self.paint.setStyleSheet("background-color: #ffffff")

    def setPenWidth10(self, newWidth):
        global clicked
        clicked = False
        self.stat.setText("Pen")
        self.myPenWidth = 10
        self.pencil.setStyleSheet("background-color: #4b5b55")
        self.pen.setStyleSheet("background-color: #ffffff")
        self.paint.setStyleSheet("background-color: #4b5b55")

    def setPenWidth(self, newWidth):
        self.myPenWidth = newWidth

    def clearImage(self):
        self.image.fill(qRgb(0, 0, 0))
        self.modified = True
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()

            self.xpos = event.pos().x()
            self.ypos = event.pos().y()
            global clicked
            if clicked == True and self.xpos < 970 and self.xpos > 270 and self.ypos < 800 and self.ypos > 100 : #Painting을 눌렀을때!
          
              x = self.xpos
              y = self.ypos

              global red
              global green
              global blue

              xq = deque()
              xq.append(x)
              yq = deque()
              yq.append(y)
              self.image.setPixel(x,y,drawcolor)
              while xq:
                xpos = xq.popleft()
                ypos = yq.popleft() 
                # 970 270 800 100
                rgb = self.image.pixel(xpos+1,y)
                if QtGui.qRed(rgb) != red and QtGui.qGreen(rgb) != green and QtGui.qBlue(rgb) != blue and xpos < 960 and xpos > 280 and ypos < 790 and ypos > 110 :
                    self.image.setPixel(xpos+1,ypos,drawcolor)
                    xq.append(xpos+1)
                    yq.append(ypos)

                rgb = self.image.pixel(xpos,ypos+1)
                if QtGui.qRed(rgb) != red and QtGui.qGreen(rgb) != green and QtGui.qBlue(rgb) != blue and xpos < 960 and xpos > 280 and ypos < 790 and ypos > 110 :
                    self.image.setPixel(xpos,ypos+1,drawcolor)
                    xq.append(xpos)
                    yq.append(ypos+1)

                rgb = self.image.pixel(xpos-1,ypos)
                if QtGui.qRed(rgb) != red and QtGui.qGreen(rgb) != green and QtGui.qBlue(rgb) != blue and xpos < 960 and xpos > 280 and ypos < 790 and ypos > 110 :
                    self.image.setPixel(xpos-1,ypos,drawcolor)
                    xq.append(xpos-1)
                    yq.append(ypos)

                rgb = self.image.pixel(xpos,ypos-1)
                if QtGui.qRed(rgb) != red and QtGui.qGreen(rgb) != green and QtGui.qBlue(rgb) != blue and xpos < 960 and xpos > 280 and ypos < 790 and ypos > 110 : 
                    self.image.setPixel(xpos,ypos-1,drawcolor)
                    xq.append(xpos)
                    yq.append(ypos-1)
            
            self.update()
            clicked = False
            self.paint.setStyleSheet("background-color: #4b5b55")
            '''
                #뒤에 재귀로 해야할듯
              while(x > 270): # - - 이니까 왼쪽 위로 다 색칠하는거
                while(y > 100):
                  rgb = self.image.pixel(x, y)
                  if QtGui.qRed(rgb) != red and QtGui.qGreen(rgb) != green and QtGui.qBlue(rgb) != blue :
                    self.image.setPixel(x,y,drawcolor)
                    y = y - 1 
                    cnt = cnt + 1
                  else:
                    break
                if cnt == 0 :
                  break
                x = x - 1
                y = self.ypos
                cnt = 0

              cnt = 0
              x = self.xpos
              y = self.ypos

              while(x < 970): # + + 이니까 오른쪽 밑으로
                while(y < 800):
                  rgb = self.image.pixel(x, y)
                  if QtGui.qRed(rgb) != red and QtGui.qGreen(rgb) != green and QtGui.qBlue(rgb) != blue :
                    self.image.setPixel(x,y,drawcolor)
                    y = y + 1 
                    cnt = cnt + 1
                  else:
                    break
                if cnt == 0 : 
                  break
                x = x + 1
                y = self.ypos
                cnt = 0
              
              x = self.xpos+1
              y = self.ypos
              cnt = 0

              while(x > 270): # - + 왼쪽 아래
                while(y < 800):
                  rgb = self.image.pixel(x, y)
                  if QtGui.qRed(rgb) != red and QtGui.qGreen(rgb) != green and QtGui.qBlue(rgb) != blue :
                    self.image.setPixel(x,y,drawcolor)
                    y = y + 1 
                    cnt = cnt + 1
                  else:
                    break
                if cnt == 0 :
                  break
                x = x - 1
                y = self.ypos+1
                cnt = 0

              cnt = 0
              x = self.xpos
              y = self.ypos

              while(x < 970): # + - 오른쪽 위
                while(y > 100):
                  rgb = self.image.pixel(x, y)
                  if QtGui.qRed(rgb) != red and QtGui.qGreen(rgb) != green and QtGui.qBlue(rgb) != blue :
                    self.image.setPixel(x,y,drawcolor)
                    y = y - 1 
                    cnt = cnt + 1
                  else:
                    break
                if cnt == 0 : 
                  break
                x = x + 1
                y = self.ypos-1
                cnt = 0
            '''
            self.scribbling = True   

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) and self.scribbling:
            self.drawLineTo(event.pos())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.scribbling:
            self.drawLineTo(event.pos())
            self.scribbling = False

    def paintEvent(self, event):
        painter = QPainter(self)
        dirtyRect = event.rect()
        painter.drawImage(dirtyRect, self.image, dirtyRect)
        painter.setPen(QPen(Qt.white,  40, Qt.SolidLine))
        painter.drawRect(270, 100, 700, 700)
        painter.drawRect(1070, 100, 700, 700)



    def resizeEvent(self, event):
        if self.width() > self.image.width() or self.height() > self.image.height():
            newWidth = max(self.width() + 128, self.image.width())
            newHeight = max(self.height() + 128, self.image.height())
            self.resizeImage(self.image, QSize(newWidth, newHeight))
            self.update()

        super(ScribbleArea, self).resizeEvent(event)

    def drawLineTo(self, endPoint):
        painter = QPainter(self.image)
        painter.setPen(QPen(self.myPenColor, self.myPenWidth, Qt.SolidLine,
                Qt.RoundCap, Qt.RoundJoin))
        
        i = str(self.lastPoint)
        value_x = int(i[20:22])
        value_y = int(i[25:27])

        if value_x < 96 and value_x > 26 and value_y > 10 and value_y < 79: 
          painter.drawLine(self.lastPoint, endPoint)
          self.modified = True

          rad = self.myPenWidth / 2 + 2

          self.update(QRect(self.lastPoint, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))
          self.lastPoint = QPoint(endPoint)

    def resizeImage(self, image, newSize):
        if image.size() == newSize:
            return

        newImage = QImage(newSize, QImage.Format_RGB32)
        newImage.fill(qRgb(0, 0, 0))
        painter = QPainter(newImage)
        painter.drawImage(QPoint(0, 0), image)
        self.image = newImage

    def print_(self):
        printer = QPrinter(QPrinter.HighResolution)

        printDialog = QPrintDialog(printer, self)
        if printDialog.exec_() == QPrintDialog.Accepted:
            painter = QPainter(printer)
            rect = painter.viewport()
            size = self.image.size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image.rect())
            painter.drawImage(0, 0, self.image)
            painter.end()

    def isModified(self):
        return self.modified

    def penColor(self):
        return self.myPenColor

    def penWidth(self):
        return self.myPenWidth

    def btn1_clicked(self):
        self.myPenColor = QColor('#a3ffee')
        self.current.setStyleSheet("background-color: #a3ffee")
        global drawcolor
        global red
        global green
        global blue
        red = 163
        green = 255
        blue = 238
        drawcolor = qRgb(163,255,238)

    def btn2_clicked(self):
        self.myPenColor = QColor('#b1d627')
        self.current.setStyleSheet("background-color: #b1d627")
        global drawcolor
        global red
        global green
        global blue
        red = 177
        green = 214
        blue = 39
        drawcolor = qRgb(177,214,39)

    def btn3_clicked(self):
        self.myPenColor = QColor('#686868')
        self.current.setStyleSheet("background-color: #686868")
        global drawcolor
        global red
        global green
        global blue
        red = 104
        green = 104
        blue = 104
        drawcolor = qRgb(104,104,104)

    def btn4_clicked(self):
        self.myPenColor = QColor('#899c61')
        self.current.setStyleSheet("background-color: #899c61")
        global drawcolor
        global red
        global green
        global blue
        red = 137
        green = 156
        blue = 97
        drawcolor = qRgb(137,156,97)

    def btn5_clicked(self):
        self.myPenColor = QColor('#7dd700')
        self.current.setStyleSheet("background-color: #7dd700")
        global drawcolor
        global red
        global green
        global blue
        red = 125
        green = 215
        blue = 0
        drawcolor = qRgb(125,215,0)

    def btn6_clicked(self):
        self.myPenColor = QColor('#a1d3ec')
        self.current.setStyleSheet("background-color: #a1d3ec")
        global drawcolor
        global red
        global green
        global blue
        red = 161
        green = 211
        blue = 236
        drawcolor = qRgb(161,211,236)
        
    def btn7_clicked(self):
        self.myPenColor = QColor('#9862d6')
        self.current.setStyleSheet("background-color: #9862d6")
        global drawcolor
        global red
        global green
        global blue
        red = 152
        green = 98
        blue = 214
        drawcolor = qRgb(152,98,214)

    def btn8_clicked(self):
        self.myPenColor = QColor('#9c6228')
        self.current.setStyleSheet("background-color: #9c6228")
        global drawcolor
        global red
        global green
        global blue
        red = 156
        green = 98
        blue = 40
        drawcolor = qRgb(156,98,40)

    def btn9_clicked(self):
        self.myPenColor = QColor('#92fa10')
        self.current.setStyleSheet("background-color: #92fa10")
        global drawcolor
        global red
        global green
        global blue
        red = 146
        green = 250
        blue = 16
        drawcolor = qRgb(146,250,16)

    def btn10_clicked(self):
        self.myPenColor = QColor('#9f9f00')
        self.current.setStyleSheet("background-color: #9f9f00")
        global drawcolor
        global red
        global green
        global blue
        red = 159
        green = 159
        blue = 0
        drawcolor = qRgb(159,159,0)

    def btn11_clicked(self):
        self.myPenColor = QColor('#a6a5b3')
        self.current.setStyleSheet("background-color: #a6a5b3")
        global drawcolor
        global red
        global green
        global blue
        red = 166
        green = 165
        blue = 179
        drawcolor = qRgb(166,165,179)

    def btn12_clicked(self):
        self.myPenColor = QColor('#bcd6ff')
        self.current.setStyleSheet("background-color: #bcd6ff")
        global drawcolor
        global red
        global green
        global blue
        red = 188
        green = 214
        blue = 255
        drawcolor = qRgb(188,214,255)

    def btn13_clicked(self):
        self.myPenColor = QColor('#80d663')
        self.current.setStyleSheet("background-color: #80d663")
        global drawcolor
        global red
        global green
        global blue
        red = 128
        green = 214
        blue = 99
        drawcolor = qRgb(128,214,99)

    def btn14_clicked(self):
        self.myPenColor = QColor('#6b6e1c')
        self.current.setStyleSheet("background-color: #6b6e1c")
        global drawcolor
        global red
        global green
        global blue
        red = 107
        green = 110
        blue = 28
        drawcolor = qRgb(107,110,28)

    def btn15_clicked(self):
        self.myPenColor = QColor('#9a6d1c')
        self.current.setStyleSheet("background-color: #9a6d1c")
        global drawcolor
        global red
        global green
        global blue
        red = 154
        green = 109
        blue = 28
        drawcolor = qRgb(154,109,28)

    def btn16_clicked(self):
        self.myPenColor = QColor('#770000')
        self.current.setStyleSheet("background-color: #770000")
        global drawcolor
        global red
        global green
        global blue
        red = 119
        green = 0
        blue = 0
        drawcolor = qRgb(119,0,0)

    def btn17_clicked(self):
        self.myPenColor = QColor('#a9a85c')
        self.current.setStyleSheet("background-color: #a9a85c")
        global drawcolor
        global red
        global green
        global blue
        red = 169
        green = 168
        blue = 92
        drawcolor = qRgb(169,168,92)

    def btn18_clicked(self):
        self.myPenColor = QColor('#5e6e28')
        self.current.setStyleSheet("background-color: #5e6e28")
        global drawcolor
        global red
        global green
        global blue
        red = 94
        green = 110
        blue = 40
        drawcolor = qRgb(94,110,40)

    def btn19_clicked(self):
        self.myPenColor = QColor('#c17f09')
        self.current.setStyleSheet("background-color: #c17f09")
        global drawcolor
        global red
        global green
        global blue
        red = 193
        green = 127
        blue = 9
        drawcolor = qRgb(193,127,9)

    def btn20_clicked(self):
        self.myPenColor = QColor('#7f28d7')
        self.current.setStyleSheet("background-color: #7f28d7")
        global drawcolor
        global red
        global green
        global blue
        red = 127
        green = 40
        blue = 215
        drawcolor = qRgb(127,40,215)

    def clearframe(self):
        self.image.fill(qRgb(0, 0, 0))
        self.modified = True
        self.update()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.saveAsActs = []

        self.scribbleArea = ScribbleArea()
        self.setCentralWidget(self.scribbleArea)

        self.createActions()
        self.createMenus()

        self.setWindowTitle("DeepLearing")
        self.resize(1920, 1080)


    def closeEvent(self, event):
        if self.maybeSave():
            event.accept()
        else:
            event.ignore()

    def open(self):
        if self.maybeSave():
            fileName, _ = QFileDialog.getOpenFileName(self, "Open File",
                    QDir.currentPath())
            if fileName:
                self.scribbleArea.openImage(fileName)

    def save(self):
        action = self.sender()
        fileFormat = action.data()
        self.saveFile(fileFormat)

    def penColor(self):
        newColor = QColorDialog.getColor(self.scribbleArea.penColor())
        if newColor.isValid():
            self.scribbleArea.setPenColor(newColor)

    def penWidth(self):
        newWidth, ok = QInputDialog.getInt(self, "Scribble",
                "Select pen width:", self.scribbleArea.penWidth(), 1, 50, 1)
        if ok:
            self.scribbleArea.setPenWidth(newWidth)

    def createActions(self):
        self.openAct = QAction("&Open...", self, shortcut="Ctrl+O",
                triggered=self.open)

        for format in QImageWriter.supportedImageFormats():
            aaaaa = bytes(format)
            #format = str(format)
            format = aaaaa.decode('utf-8')
            text = format.upper() + "..."

            action = QAction(text, self, triggered=self.save)
            action.setData(format)
            self.saveAsActs.append(action)

        self.printAct = QAction("&Print...", self,
                triggered=self.scribbleArea.print_)

        self.exitAct = QAction("E&xit", self, shortcut="Ctrl+Q",
                triggered=self.close)

        self.penColorAct = QAction("&Pen Color...", self,
                triggered=self.penColor)

        self.penWidthAct = QAction("Pen &Width...", self, shortcut="Ctrl+J",
                triggered=self.penWidth)

        self.clearScreenAct = QAction("&Clear Screen", self, shortcut="Ctrl+L",
                triggered=self.scribbleArea.clearImage)


        self.aboutQtAct = QAction("About &Qt", self,
                triggered=QApplication.instance().aboutQt)

    def createMenus(self):
        self.saveAsMenu = QMenu("&Save As", self)
        for action in self.saveAsActs:
            self.saveAsMenu.addAction(action)

        fileMenu = QMenu("&File", self)
        fileMenu.addAction(self.openAct)
        fileMenu.addMenu(self.saveAsMenu)
        fileMenu.addAction(self.printAct)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAct)

        optionMenu = QMenu("&Options", self)
        optionMenu.addAction(self.penColorAct)
        optionMenu.addAction(self.penWidthAct)
        optionMenu.addSeparator()
        optionMenu.addAction(self.clearScreenAct)

        helpMenu = QMenu("&Help", self)
        helpMenu.addAction(self.aboutQtAct)

        self.menuBar().addMenu(fileMenu)
        self.menuBar().addMenu(optionMenu)
        self.menuBar().addMenu(helpMenu)

    def maybeSave(self):
        if self.scribbleArea.isModified():
            ret = QMessageBox.warning(self, "Save",
                        "Do you want save image?",
                        QMessageBox.Save | QMessageBox.Discard |
                        QMessageBox.Cancel)
            if ret == QMessageBox.Save:
                return self.saveFile('png')
            elif ret == QMessageBox.Cancel:
                return False

        return True

    def saveFile(self, fileFormat):

        initialPath = QDir.currentPath() + '/untitled.' + fileFormat

        fileName, _ = QFileDialog.getSaveFileName(self, "Save As", initialPath,
                "%s Files (*.%s);;All Files (*)" % (fileFormat.upper(), fileFormat))

        if fileName:
            return self.scribbleArea.saveImage(fileName, fileFormat)

        return False


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())