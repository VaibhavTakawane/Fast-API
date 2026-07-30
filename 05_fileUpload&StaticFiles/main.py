from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

# ENSURE uploads folder exists:
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# static file setup(public path) like =>
# url=> http://127.0.0.1:8000/files/<file_name>
app.mount("/files", StaticFiles(directory=UPLOAD_DIR), name="files")

# UPLOAD FILE API:
@app.post("/upload/")
def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not filename:
        raise HTTPException(status_code=400, detail="File not selected")

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

        return {
            "message": "File uploadede successfully",
            "fileName": filename,
            "file_url": f"http://127.0.0.1:8000/{filename}"
        }

# GET FILE URL API:
@app.get("/files/{filename}/")
def get_file(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return {
        "file_url": f"http://127.0.0.1:8000/{filename}",
    }

