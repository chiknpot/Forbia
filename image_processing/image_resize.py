import cv2
from os import listdir
from os.path import isfile, join
mypath='./blood'
destpath='./test_blood'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for f in onlyfiles:
  img = cv2.imread(join(mypath,f), cv2.IMREAD_UNCHANGED)
  try:
        dst1 = cv2.resize(img, dsize=(200, 140))
        fPath=join(destpath,f)
        cv2.imwrite(fPath,dst1)
  except Exception as e:
        print(str(e))
