from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlalchemy import text
from config import engine
from app.routers.detection_router import router as detection_router
from app.routers.web_router import router as web_router

app = FastAPI(
    title="Safety Helmet Object Detection System",
    description="Sistem deteksi penggunaan helm keselamatan berbasis FastAPI",
    version="1.0.0"
)

# Servis direktori statis (CSS & File Upload Gambar)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include Routers
app.include_router(detection_router)
app.include_router(web_router)

@app.get("/health/database")
def check_database():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"status": "success", "message": "Koneksi ke db_helmet_detection berhasil"}
    except Exception as e:
        return {"status": "error", "message": f"Koneksi PostgreSQL gagal: {str(e)}"}