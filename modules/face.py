import face_recognition

def verify_face(profile_img, login_img):
    try:
        stored = face_recognition.load_image_file(profile_img)
        login = face_recognition.load_image_file(login_img)

        stored_enc = face_recognition.face_encodings(stored)[0]
        login_enc = face_recognition.face_encodings(login_img)[0]

        result = face_recognition.compare_faces([stored_enc], login_enc)
        return result[0]
    except:
        return False
