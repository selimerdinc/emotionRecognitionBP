import numpy as np
from keras.models import load_model
import datetime
import os
from keras_preprocessing.image import load_img, img_to_array

def predictionScore(output):
    my_file = open(output, "r", encoding="utf-8")
    outputs = my_file.read().lower()

    happyCount = outputs.count("happy")
    sadCount = outputs.count("sad")
    angryCount = outputs.count("angry")
    fearCount = outputs.count("fear")
    disgustCount = outputs.count("disgust")
    neutralCount = outputs.count("neutral")
    surpriseCount = outputs.count("surprise")

    toplam = happyCount + sadCount + angryCount + fearCount + disgustCount + neutralCount + surpriseCount
    ortHappy = float((happyCount / toplam) * 100).__round__(2)
    ortSad = float((sadCount / toplam) * 100).__round__(2)
    ortAngry = float((angryCount / toplam) * 100).__round__(2)
    ortFear = float((fearCount / toplam) * 100).__round__(2)
    ortDisgust = float((disgustCount / toplam) * 100).__round__(2)
    ortNeutral = float((neutralCount / toplam) * 100).__round__(2)
    ortSurprise = float((surpriseCount / toplam) * 100).__round__(2)

    list = ["Happy", "Sad", "Angry", "Fear", "Disgust", "Neutral", "Surprise"]
    dataList = [happyCount, sadCount, angryCount, fearCount, disgustCount, neutralCount, surpriseCount]
    ortList = [ortHappy, ortSad, ortAngry, ortFear, ortDisgust, ortNeutral, ortSurprise]

    for i in range(0, 7):
        score = open("predictionSurprise/surpriseScore.txt", "a", encoding="utf-8")
        print(list[i], " = ", dataList[i], "// Oran : %", ortList[i], file=score)





def load_images_from_folder(folder, m_dict, m_class):
    for filename in os.listdir(folder):
        full_path = os.path.join(folder, filename)
        if full_path.split(".")[-1] == "jpg" or full_path.split(".")[-1] == "jpeg":
            if full_path not in m_dict:
                m_dict[full_path] = m_class
    return m_dict

model =load_model(r'C:\Users\selimerdinc\PycharmProjects\realTimeEmotionRecognation\models\model.h5')
m_dict = {}

m_dict = load_images_from_folder(r'/content/test/angry', m_dict, "Angry")
m_dict = load_images_from_folder(r'/content/test/disgust', m_dict, "Disgust")
m_dict = load_images_from_folder(r'/content/test/fear', m_dict, "Fear")
m_dict = load_images_from_folder(r'/content/test/happy', m_dict, "Happy")
m_dict = load_images_from_folder(r'/content/test/neutral', m_dict, "Neutral")
m_dict = load_images_from_folder(r'/content/test/sad', m_dict, "Sad")
m_dict = load_images_from_folder(r'/content/test/surprise', m_dict, "Surprise")
for img in m_dict:
    print("m_path: {} => class: {}".format(img, m_dict[img]))
    img = load_img(img, target_size=(224, 224))
    ia = img_to_array(img) / 255
    input_arr = np.array([ia])
    start = datetime.datetime.now()
    prediction = model.predict(input_arr)
    end = datetime.datetime.now()
    pred_time = (end - start).total_seconds() * 1000
    classes = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
    m_label = classes[np.argmax((prediction))]
    f = open("/content/surprise.txt", "a", encoding="utf-8")
    f2 = open("/content/surpriseTime.txt", "a", encoding="utf-8")
    print("preds: {}, \nEmotion Predict ==> {}".format(prediction, m_label), file=f)
    print("Elapsed for Prediction time :  ", pred_time, "ms", file=f2)
