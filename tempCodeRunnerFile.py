        # Check if face landmarks are detected
        if face_landmarks:
            face_encodings = []

            for landmarks in face_landmarks:
                try:
                    # Convert landmarks to a flat list of (x, y) coordinates
                    flattened_landmarks = [coord for sublist in landmarks.values() for coord in sublist]

                    encoding = face_recognition.face_encodings(rgb_small_frame, [flattened_landmarks])[0]
                    face_encodings.append(encoding)
                except IndexError:
                    print("Warning: IndexError occurred. Skipping face.")
        else:
            face_encodings = []