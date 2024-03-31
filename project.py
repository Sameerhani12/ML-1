import cv2

# Function for updating
def upd_brightness(value):
    global brightness
    brightness = value - 100

def upd_contrast(value):
    global contrast
    contrast = value / 100

# for camera opening 
video = cv2.VideoCapture(0)

# Create a window for the camera feed
cv2.namedWindow('Camera')  

# Create trackbars for adjusting brightness and contrast
cv2.createTrackbar('Brightness', 'Camera', 100, 200, upd_brightness)    
cv2.createTrackbar('Contrast', 'Camera', 100, 200, upd_contrast)

# Initializiation
brightness = 0  #brightness
contrast = 1.0  #contrast 

# Infinite loop to process frames
while True:
    ret, frame = video.read()
    if not ret:
        break

    # Adjusting brightness and contrast using built in function 
    adjusted_frame = cv2.convertScaleAbs(frame, alpha=contrast, beta=brightness)

    # Display the processed frame with sliders
    cv2.imshow('Camera', adjusted_frame)

    #wait until key is pressed 
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()