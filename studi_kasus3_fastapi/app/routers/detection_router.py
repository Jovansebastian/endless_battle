from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from config import get_db
from app.schemas.detection_schema import DetectionImageResponse
from app.services import detection_service as service

router = APIRouter(prefix="/api", tags=["Detection API"])

@router.post("/upload", response_model=DetectionImageResponse)
async def api_upload_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    return service.process_image_upload(db, contents, file.filename)

@router.get("/history", response_model=list[DetectionImageResponse])
def api_get_history(db: Session = Depends(get_db)):
    return service.get_all_images(db)

@router.get("/result/{image_id}", response_model=DetectionImageResponse)
def api_get_result(image_id: int, db: Session = Depends(get_db)):
    img = service.get_image_by_id(db, image_id)
    if not img:
        raise HTTPException(status_code=404, detail="Gambar tidak ditemukan.")
    return img

@router.delete("/delete/{image_id}")
def api_delete_image(image_id: int, db: Session = Depends(get_db)):
    success = service.delete_image_record(db, image_id)
    if not success:
        raise HTTPException(status_code=404, detail="Gambar tidak ditemukan.")
    return {"status": "success", "message": "Data deteksi berhasil dihapus."}