import cv2

#load camera to get one frame
'''
cap = cv2.VideoCapture(0)
_, frame = cap.read()
cv2.imshow("Frame",frame)
cv2.waitKey(0)
'''

'''
#to load many frames or make a video
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
while True:
    _, frame = cap.read()
    height, width, _ = frame.shape

    cx = int(width/2)
    cy =int(height/2)

    #pixel value
    pixel_center = frame[cy,cx]
    print(pixel_center)
    cv2.circle(frame, (cx, cy), 5, (255, 0, 0), 3)
    cv2.imshow("Frame", frame)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()

'''
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #here we convert BRG TO HSV (HSV BENEFITS THE colour changing as shown)
    height, width, _ = frame.shape

    cx = int(width / 2)
    cy = int(height / 2)

    # Pick pixel value
    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]#we r only going to take the 1st value in the list[66 77 101] la 66 is the value we take

    color = "Undefined"
    if hue_value < 5:
        color = "RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 145:
        color = "VIOLET"
    elif hue_value < 167:
        color = "PINK"
    else:
        color = "RED"

    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])#we are giving the text the same color as the image color
    #if the object u show is orange the image which color is recognzed and printed in the frame using the same colour
    #inovative la.........yaaa

    cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
    # cv2,putText(on frame we display so "frame", what to display - "color", co-ordinates, font (as u increase front 0 font changes), thickness, colour of the text
    cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()