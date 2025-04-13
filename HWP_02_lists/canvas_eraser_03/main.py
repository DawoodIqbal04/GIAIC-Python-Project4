import matplotlib.pyplot as plt
import numpy as np

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

CELL_SIZE = 400
ERASER_SIZE = 100

canvas = np.ones((CANVAS_HEIGHT, CANVAS_WIDTH, 3))

canvas[0:CELL_SIZE, 0:CELL_SIZE] = [0, 0, 1]

def erase_area(x, y, size=ERASER_SIZE):
    canvas[y:y+size, x:x+size] = [1, 1, 1]

plt.imshow(canvas)
plt.title("Before Erase")
plt.axis("off")
plt.show()

erase_x = 150
erase_y = 150
erase_area(erase_x, erase_y)

plt.imshow(canvas)
plt.title("After Erase")
plt.axis("off")
plt.show()
