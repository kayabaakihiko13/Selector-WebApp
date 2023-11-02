# main.py

import uvicorn

app_name = "app:app"  # Specify the correct path to your FastAPI app

if __name__ == "__main__":
    uvicorn.run(app_name, host="127.0.0.1", port=8000,reload=True,workers=2)
