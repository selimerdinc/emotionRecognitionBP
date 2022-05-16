import re
import glob
import os
import cv2
import logging
import tqdm

filePath = 'z:/Bora/B/Crop/DATA/'
fileNames = os.listdir(filePath)
numClasses = 12

for fName in fileNames:
    print(fName)
    newpath = r'{}/{}/CROPPED'.format(filePath, fName)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    for i in range(numClasses):
        if not os.path.exists(newpath + r'/{}'.format(i)):
            os.makedirs(newpath + r'/{}'.format(i))

    textFiles = [f for f in os.listdir(filePath + "/" + fName) if f.endswith('.txt')]
    jpgFiles = [f for f in os.listdir(filePath + "/" + fName) if f.endswith('.jpg')]

    for jpg in jpgFiles:
        if not jpg[:-4] + ".txt" in textFiles:
            logging.warning("There is no text file for {}/{}".format(fName, jpg))

    # print(textFiles)
    for textFile in tqdm.tqdm(textFiles, position=0, leave=True):
        # print(textFile)
        path = filePath + "/" + fName + "/" + textFile
        myfile = open(path, 'r')
        lines = myfile.readlines()
        for line in lines:
            if (line == ''):
                logging.warning(path + " has no label in it...")
                continue

            Cord_Raw = line
            Cord = Cord_Raw.split(" ")[1:]

            x_min = float(Cord[0]) - float(Cord[2]) / 2
            x_max = x_min + float(Cord[2])
            y_min = float(Cord[1]) - float(Cord[3]) / 2
            y_max = y_min + float(Cord[3])

            img = cv2.imread(filePath + "/" + fName + "/" + textFile[:-4] + ".jpg")
            try:
                height, width, channels = img.shape
            except:
                logging.warning("Image file is currepted{}/{}".format(fName, jpg))
                continue

            x_min = int(x_min * width)
            x_max = int(x_max * width)
            y_min = int(y_min * height)
            y_max = int(y_max * height)

            crop_img = img[y_min:y_max, x_min:x_max]
            cropped_path = newpath + "/{}/{}_cropped.jpg".format(line[0], textFile[:-4])
            cropped_path = r'{}'.format(cropped_path.replace('/', '\\'))

            if not cv2.imwrite(cropped_path, crop_img):
                logging.warning(cropped_path + " couldn't be saved...")

print("Job ended.")



