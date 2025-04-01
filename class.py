# import the required modules 
import cv2 
import matplotlib.pyplot as plt
from deepface import DeepFace
import json

img= cv2.imread("sad.jpg")
img_rgb = img[:, :, ::-1]#change from BGR to RGB
plt.imshow(img_rgb)#adds image to plot
plt.axis('off') #takes axis off plot
#plt.show()#displays image

result = DeepFace.analyze(img_rgb, actions=['emotion'])
print(result)
for res in result:
    print(f"Dominant Emotion: {res['dominant_emotion']} (Confidence: {float(res['emotion'][res['dominant_emotion']]):.2f}%)")
    print(f"Face Confidence: {float(res['face_confidence']):.2f}")
    print("Emotion Scores:")
    for emotion, score in res['emotion'].items():
        print(f"  {emotion.capitalize()}: {float(score):.4f}")
    print("-" * 40)


