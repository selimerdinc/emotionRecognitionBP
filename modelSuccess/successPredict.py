import datetime
import os
import numpy as np
from keras.models import load_model
from keras_applications.resnet50 import preprocess_input
from keras_preprocessing.image import load_img, img_to_array


def load_images_from_folder(folder, m_dict, m_class):
    for filename in os.listdir(folder):
        full_path = os.path.join(folder, filename)
        if full_path.split(".")[-1] == "jpg" or full_path.split(".")[-1] == "jpeg":
            if full_path not in m_dict:
                m_dict[full_path] = m_class
    return m_dict


def classify(img_path):
    img = load_img(img_path, target_size=(224, 224))
    img_array = img_to_array(img)


    img_batch = np.expand_dims(img_array, axis=(0))


    img_preprocessed = preprocess_input(img_batch)


    model = load_model(r'C:\Users\selimerdinc\PycharmProjects\realTimeEmotionRecognation\models\model.h5')

    start = datetime.datetime.now()
    prediction = model.predict(img_preprocessed)
    end = datetime.datetime.now()
    pred_time = (end - start).total_seconds() * 1000
    classes = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
    m_label = classes[np.argmax((prediction))]
    print("preds: {}, \nEmotion Prediction ==> {}".format(prediction, m_label))
    print("Elapsed for Prediction time :  ", pred_time, "ms")
    return m_label


# read images from directory
# get class names as pre defined target source (hedef sınıf sonucu)
# classify each of them and return class_name for current input image
# calculate average accuracy for input images for selected directory

m_dict = {}

m_dict = load_images_from_folder(r'C:\Users\selimerdinc\PycharmProjects\realTimeEmotionRecognation\dataset\train\angry', m_dict, "Angry")
# m_dict = load_images_from_folder(r'C:\Users\selimerdinc\PycharmProjects\realTimeEmotionRecognation\dataset\train\disgust', m_dict, "Disgust")
# m_dict = load_images_from_folder(r'C:\Users\selimerdinc\PycharmProjects\realTimeEmotionRecognation\dataset\train\fear', m_dict, "Fear")
# m_dict = load_images_from_folder(r'C:\Users\selimerdinc\PycharmProjects\realTimeEmotionRecognation\dataset\train\happy', m_dict, "Happy")
# m_dict = load_images_from_folder(r'C:\Users\selimerdinc\PycharmProjects\realTimeEmotionRecognation\dataset\train\neutral', m_dict, "Neutral")
# m_dict = load_images_from_folder(r'C:\Users\selimerdinc\PycharmProjects\realTimeEmotionRecognation\dataset\train\sad', m_dict, "Sad")
# m_dict = load_images_from_folder(r'C:\Users\selimerdinc\PycharmProjects\realTimeEmotionRecognation\dataset\train\surprise', m_dict, "Surprise")

for img in m_dict:
    print("m_path: {} => class: {}".format(img, m_dict[img]))




correct_found = 0
for img in m_dict:
    cur_label = classify(img)
    if cur_label == m_dict[img]:
        correct_found += 1

print("total_img_ct: {}, correct_found: {}, avg_acc: {}".format(len(m_dict), correct_found, (correct_found / float(len(m_dict)))))







