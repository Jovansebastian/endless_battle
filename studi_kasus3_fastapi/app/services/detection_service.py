import os
import uuid
from pathlib import Path
from sqlalchemy.orm import Session
from app.models.detection_model import DetectionImage, DetectionResult, ObjectClass
from app.model_ai.detector import run_object_detection

UPLOAD_DIR = Path("static/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

def process_image_upload(db: Session, file_bytes: bytes, original_filename: str) -> DetectionImage:
    # Simpan file asli
    ext = Path(original_filename).suffix or ".jpg"
    unique_name = f"{uuid.uuid4().hex}{ext}"
    input_path = UPLOAD_DIR / unique_name
    output_path = UPLOAD_DIR / f"det_{unique_name}"

    with open(input_path, "wb") as f:
        f.write(file_bytes)

    # Jalankan Deteksi Objek
    detections = run_object_detection(str(input_path), str(output_path))

    # Simpan ke Database
    db_image = DetectionImage(
        original_filename=original_filename,
        stored_filename=f"det_{unique_name}",
        image_path=f"/static/uploads/det_{unique_name}"
    )
    db.add(db_image)
    db.commit()
    db.refresh(db_image)

    # Simpan Hasil Bounding Box & Class
    for item in detections:
        result = DetectionResult(
            image_id=db_image.id,
            class_id=item["class_id"],
            confidence_score=item["confidence_score"],
            x_min=item["x_min"],
            y_min=item["y_min"],
            x_max=item["x_max"],
            y_max=item["y_max"]
        )
        db.add(result)
    
    db.commit()
    db.refresh(db_image)
    return db_image

def get_all_images(db: Session):
    return db.query(DetectionImage).order_by(DetectionImage.created_at.desc()).all()

def get_image_by_id(db: Session, image_id: int):
    return db.query(DetectionImage).filter(DetectionImage.id == image_id).first()

def delete_image_record(db: Session, image_id: int) -> bool:
    image = get_image_by_id(db, image_id)
    if not image:
        return False
    
    # Hapus file fisik jika ada
    try:
        file_p = Path(image.image_path.lstrip("/"))
        if file_p.exists():
            os.remove(file_p)
    except Exception:
        pass

    db.delete(image)
    db.commit()
    return True

def get_dashboard_stats(db: Session):
    total_images = db.query(DetectionImage).count()
    helmet_count = db.query(DetectionResult).filter(DetectionResult.class_id == 1).count()
    no_helmet_count = db.query(DetectionResult).filter(DetectionResult.class_id == 2).count()
    
    return {
        "total_images": total_images,
        "helmet_count": helmet_count,
        "no_helmet_count": no_helmet_count
    }