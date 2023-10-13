import cv2
import matplotlib as plt
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont






def main():
    
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


    while True:
        ret, frame = cap.read()

        # writer.write(frame)
        
        cv2.imshow("device read", frame)

        if (cv2.waitKey(30) == 27): # break with escape key
            break
            
    cap.release()
    cv2.destroyAllWindows()
    plt.plot()
    
if __name__ == "__main__":
    main()