import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from image_classification import image_to_array, result_waifu_generate

app = FastAPI()
# this code for adding di
app.mount("/static", StaticFiles(directory="templates/static"), name="static")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
templates = Jinja2Templates(directory="templates")

class ImageUploadService:
    def __init__(self, upload_directory):
        self.upload_directory = upload_directory

    def save_image(self, file: UploadFile):
        image_path = os.path.join(self.upload_directory, file.filename)
        with open(image_path, "wb") as image_file:
            image_file.write(file.file.read())
        return image_path

image_upload_service = ImageUploadService("uploads/")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload/")
async def upload_images(request: Request, image: UploadFile = File(...)):
    image_filename = image_upload_service.save_image(image)
    image_arr = image_to_array(image_filename)
    prediction = result_waifu_generate(image_arr)
    return JSONResponse(content={"prediction": prediction, "image_filename": f"/uploads/{os.path.basename(image_filename)}"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
