# imported two libraries pandas and openCv
import pandas as pd
import cv2

img_path = 'pic1.jpg'
csv_path = 'colors.csv'

# to read csv file create data frame here named as df
index = ['colour', 'colour_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv(csv_path, names=index, header=None)

img = cv2.imread(img_path)
img = cv2.resize(img, (900, 700))

clicked = False
r = g = b = xpos = ypos = 0

#  define function for open cv
#  color recognition function
def colour_name(R, G, B):
    minimum = 1000
    for i in range(len(df)):
        d = abs(R-int(df.loc[i, 'R'])) + abs(G-int(df.loc[i, 'G'])) + abs(B-int(df.loc[i, 'B']))
        if d <= minimum:
            minimum = d
            cname = df.loc[i, 'colour_name']
    return cname

def draw_function(event, x, y, flags, params):

    if event == cv2.EVENT_LBUTTONDBLCLK:
        global clicked, r, g, b, xpos, ypos
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

# create a window

cv2.namedWindow('window')
cv2.setMouseCallback('window', draw_function)

while True:
    cv2.imshow('window', img)
    if clicked:
        cv2.rectangle(img, (20, 20), (600, 60), (b, g, r), -1)
        text = colour_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

    if cv2.waitKey(20) & 0xFF == 27:
        break

# print(clicked, r, g, b, xpos, ypos)
# cv2.imshow('window', img)

cv2.destroyAllWindows()










