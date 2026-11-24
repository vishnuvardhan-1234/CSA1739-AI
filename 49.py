import face_recognition

img = face_recognition.load_image_file("person.jpg")

faces = face_recognition.face_locations(img)

print("Number of Faces:", len(faces))

for face in faces:
    print("Face Location:", face)
