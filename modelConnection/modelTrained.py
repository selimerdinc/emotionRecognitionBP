
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import cv2
import numpy as np
import datetime

from outputControl.parseOutput import returnResult

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
classifier =load_model(r'C:\Users\selimerdinc\PycharmProjects\realTimeEmotionRecognation\models\model.h5')

emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']

cap = cv2.VideoCapture(0)



while True:
    _, frame = cap.read()
    labels = []
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(250,10,80),3)
        roi_gray = gray[y:y+h,x:x+w]
        roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)
        roi_color = frame[y:y + h, x:x + w]

        if np.sum([roi_gray])!=0:
            roi = roi_gray.astype('float')/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi,axis=0)

            start = datetime.datetime.now()
            prediction = classifier.predict(roi)[0]
            end = datetime.datetime.now()
            pred_time = (end - start).total_seconds() * 1000
            label=emotion_labels[prediction.argmax()]
            label_position = (x,y)
            cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1.8,(0,255,0),2)
            f = open("../outputControl/output.txt", "a", encoding="utf-8")
            a = open("../outputControl/predictMs.txt", "a", encoding="utf-8")
            print(label,file=f)
            print("{} Tahmin Süresi = ".format(label),pred_time," ms",file=a)
        else:
            cv2.putText(frame,'Yüz Bulunumadı',(30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow('Emotion-Detector',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
output="../outputControl/angryElapsedforPredictionTime.txt"
returnResult(output)
cap.release()
cv2.destroyAllWindows()
