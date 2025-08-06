from fastapi import FastAPI, UploadFile, File, Form
from modules.behavior import verify_behavior
from modules.face import verify_face
import shutil

app = FastAPI()

@app.post("/verify-behavior")
def behavior_api(user_id: str):
    result = verify_behavior(user_id)
    return result

@app.post("/verify-face")
async def face_api(user_id: str = Form(...), login_image: UploadFile = File(...)):
    path = f"data/temp_login_images/{user_id}.jpg"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(login_image.file, buffer)

    profile_path = f"data/profile_images/{user_id}.jpg"
    result = verify_face(profile_path, path)
    return {"verified": result}
