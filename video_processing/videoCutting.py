import cv2
print(cv2.__version__)
vidcap = cv2.VideoCapture('./test.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
    if(int(vidcap.get(1)) % 20 == 0):
        print('Saved frame number : ' + str(int(vidcap.get(1))))
        cv2.imwrite("frame%d.png" % count, image)  
 
    success,image = vidcap.read()
    print ('Read a new frame: ', success)
    count += 1
