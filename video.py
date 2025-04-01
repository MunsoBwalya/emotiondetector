import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace

# Open webcam (0 is the default camera)
cap = cv2.VideoCapture(1)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break

    # Convert frame from BGR to RGB
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    try:
        # Analyze emotion in the frame
        result = DeepFace.analyze(img_rgb, actions=['emotion'], enforce_detection=False)

        # Extract dominant emotion
        if result:
            res = result[0]
            dominant_emotion = res['dominant_emotion']
            confidence = float(res['emotion'][dominant_emotion])
            
            # Display emotion on the frame
            text = f"{dominant_emotion} ({confidence:.2f}%)"
            cv2.putText(frame, text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    except Exception as e:
        print("Error:", e)

    # Show the frame with emotion detection
    cv2.imshow("Emotion Detector", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
