# app.py

import os
import uuid
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from models import image_to_array, result_waifu_generate

app = FastAPI()

# Serve static files from 'templates/static'
app.mount("/static", StaticFiles(directory="app/templates/static"), name="static")

# Serve uploaded images from 'uploads' directory
app.mount("/uploads", StaticFiles(directory="app/uploads"), name="uploads")

templates = Jinja2Templates(directory="app/templates")

class ImageUploadService:
    def __init__(self, upload_directory):
        self.upload_directory = upload_directory

    def save_image(self, file: UploadFile):
        # Generate a random filename using uuid
        random_filename = str(uuid.uuid4())
        file_extension = os.path.splitext(file.filename)[1]  # Get the original file extension
        image_path = os.path.join(self.upload_directory, f"{random_filename}{file_extension}")
        with open(image_path, "wb") as image_file:
            image_file.write(file.file.read())
        return image_path

image_upload_service = ImageUploadService("app/uploads/")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload/")
async def upload_images(request: Request, image: UploadFile = File(...)):
    image_filename = image_upload_service.save_image(image)
    image_arr = image_to_array(image_filename)
    prediction = result_waifu_generate(image_arr)
    return JSONResponse(content={"prediction": prediction, "image_filename": f"/uploads/{os.path.basename(image_filename)}"})
