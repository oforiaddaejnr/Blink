import sys
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QPoint, QTimer


class Face(QWidget):

  def __init__(self):
    super().__init__()
    self.setGeometry(50, 50, 500, 500)
    self.setWindowTitle('Face')
    self.__x = -1
    self.__y = -1
    self.__timer = QTimer()
    self.__timer.timeout.connect(self.blink)
    self.show()

  def blink(self):
    self.__timer.stop()
    self.__x = -1
    self.__y = -1
    print('twinkle')
    self.update()


  def paintEvent(self, event):
    qp = QPainter()
    qp.begin(self)
    # draw eye sockets
    qp.drawEllipse(100, 100, 100, 100)
    qp.drawEllipse(300, 100, 100, 100)
    # draw mouth
    qp.setPen(QPen(Qt.red, 8))
    qp.drawLine(150, 300, 250, 400)
    qp.drawLine(250, 400, 350, 300)
    # draw nose
    qp.setPen(QPen(Qt.blue, 1))
    qp.setBrush(Qt.blue)
    qp.drawPolygon(QPoint(250,175), QPoint(200, 275), QPoint(300, 275))
    # draw eyeballs
    qp.setPen(QPen(Qt.black, 5))
    qp.setBrush(Qt.black)
    if self.__x < 0 and self.__y < 0:
        qp.drawEllipse(125, 125, 50, 50)
        qp.drawEllipse(325, 125, 50, 50)
    qp.end()

  def mousePressEvent(self, event):
    self.__x = event.x()
    self.__y = event.y()
    self.__timer.start(100)
    self.update()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = Face()
  sys.exit(app.exec_())
