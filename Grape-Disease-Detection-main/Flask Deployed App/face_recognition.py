import cv2
import face_recognition
import numpy as np
import os
import pandas as pd
from datetime import datetime

# Folder containing known images
KNOWN_FACES_DIR = "C:\\Users\\user\\Downloads"
ATTENDANCE_CSV = "attendance_log.csv"

# Step 1: Load known faces
known_encodings = []
known_names = []

for filename in os.listdir(KNOWN_FACES_DIR):
    image_path = os.path.join(KNOWN_FACES_DIR, sanika.jpg)
    image = face_recognition.load_image_file("C:\\Users\\user\\Downloads\\sanika.jpg")
    encoding = face_recognition.face_encodings(image)

    if encoding:
        known_encodings.append(encoding[0])
        name = os.path.splitext(filename)[0]
        known_names.append(name)
        print(f"[+] Loaded encoding for {name}")

# Step 2: Initialize webcam or CCTV feed
# Use 0 for webcam or replace with CCTV IP stream like 'rtsp://username:pass@ip_address'
video_capture = cv2.VideoCapture(0)

# Step 3: Track attendance
marked_names = []
attendance_data = []

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Resize for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]  # BGR to RGB

    # Detect faces and encodings
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_names[best_match_index]

            if name not in marked_names:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                attendance_data.append({"Name": name, "Time": now})
                marked_names.append(name)
                print(f"[✓] Marked attendance for {name} at {now}")

        # Show name on the video frame
        top, right, bottom, left = [v * 4 for v in face_location]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # Display the resulting image
    cv2.imshow('Attendance System', frame)

    # Quit with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Step 4: Save attendance log to CSV
df = pd.DataFrame(attendance_data)
df.to_csv(ATTENDANCE_CSV, index=False)
print(f"[✓] Attendance saved to {ATTENDANCE_CSV}")

video_capture.release()
cv2.destroyAllWindows()


