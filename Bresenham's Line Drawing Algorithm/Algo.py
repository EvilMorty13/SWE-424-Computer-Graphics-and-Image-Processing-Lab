import matplotlib.pyplot as plt
import os

imgCounter = 1

def draw_line(x1, y1, x2, y2):
    global imgCounter

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = dy / dx
    points = []
    decision = []

    if slope < 1:
        # Case 1: 0 < slope < 1
        p = 2 * dy - dx  # Decision Parameter
        x = x1
        y = y1

        while x <= x2:
            points.append((x, y))
            decision.append(p)
            x += 1

            if p < 0:
                p += 2 * dy
            else:
                y += 1
                p += 2 * dy - 2 * dx
    else:
        # Case 2: slope >= 1
        p = 2 * dx - dy  # Decision Parameter
        x = x1
        y = y1

        while y <= y2:
            points.append((x, y))
            decision.append(p)
            y += 1

            if p < 0:
                p += 2 * dx
            else:
                x += 1
                p += 2 * dx - 2 * dy

    x_values, y_values = zip(*points)
    plt.plot(x_values, y_values, marker='o')
    plt.title("Bresenham's Line Drawing Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)

    if not os.path.exists('images'):
        os.makedirs('images')

    file_name = f'images/bresenham_line_{imgCounter}.png'
    plt.savefig(file_name)
    plt.show()

    print('Endpoints :', f'[{x1}, {y1}]', f'[{x2}, {y2}]')
    print('Intermediate Points :', points)
    print('Decision Parameters :', decision)


    imgCounter += 1


x1, y1 = 1, 1
x2, y2 = 8, 4
draw_line(x1, y1, x2, y2)

x1, y1 = 1, 1
x2, y2 = 4, 8
draw_line(x1, y1, x2, y2)
