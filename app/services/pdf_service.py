import hashlib
import os
from fastapi import UploadFile

UPLOAD_DIR = "uploads"


async def upload_pdf(file: UploadFile):
    contents = await file.read()
    file_hash = hashlib.sha256(contents).hexdigest()

    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    file_path = os.path.join(UPLOAD_DIR, f"{file_hash}.pdf")

    with open(file_path, "wb") as f:
        f.write(contents)

    return {"hash": file_hash, "filename": file.filename}


def get_pdf_path(hash: str):
    file_path = os.path.join(UPLOAD_DIR, f"{hash}.pdf")
    if os.path.exists(file_path):
        return file_path
    return None
