def createEmptyPicture():
  emptyPicture = makeEmptyPicture(600, 300)
  show(emptyPicture)
  
def drawRectangle():
  pic = makeEmptyPicture(600, 300)
  addRect(pic, 50, 100, 200, 50, red)
  addRectFilled(pic, 100, 200, 200, 50, red)
  show(pic)
  
def drawCircle():
  pic = makeEmptyPicture(600, 300)
  addOval(pic, 100, 100, 50, 100, red)
  addOvalFilled(pic, 200, 100, 50, 100, red) 
  addOval(pic, 350, 100, 50, 50, red)
  addOvalFilled(pic, 450, 100, 50, 50, red)
  show(pic)
  
def drawLine():
  pic = makeEmptyPicture(600, 300)
  addLine(pic, 50, 200, 250, 200, red)
  show(pic)
  


  


