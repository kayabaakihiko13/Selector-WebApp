from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class ImageUploadService:
    def __init__(self, upload_directory):
        self.upload_directory = upload_directory

    def save_image(self, file: UploadFile):
        with open(self.upload_directory + file.filename, "wb") as image_file:
            image_file.write(file.file.read())
        return file.filename

image_upload_service = ImageUploadService("uploads/")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload/", response_class=HTMLResponse)
async def upload_images(request: Request, image: UploadFile = File(...)):
    image_filename = image_upload_service.save_image(image)
    return templates.TemplateResponse("index.html", {"request": request, "message": f"Gambar {image_filename} berhasil diunggah"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
