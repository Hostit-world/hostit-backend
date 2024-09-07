from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from app.services import pdf_service

router = APIRouter()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    return await pdf_service.upload_pdf(file)


@router.get("/pdf/{hash}")
async def get_pdf(hash: str):
    file_path = pdf_service.get_pdf_path(hash)
    if file_path:
        return FileResponse(
            file_path, media_type="application/pdf", filename=f"{hash}.pdf"
        )
    raise HTTPException(status_code=404, detail="PDF not found")
