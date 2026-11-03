from fastapi import APIRouter, Depends, File, Request, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from config import get_db
from app.services import detection_service as service

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def dashboard(request: Request, db: Session = Depends(get_db)):
    stats = service.get_dashboard_stats(db)
    recent = service.get_all_images(db)[:5]
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"active_page": "dashboard", "stats": stats, "recent": recent}
    )

@router.get("/upload", response_class=HTMLResponse)
def upload_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="upload.html",
        context={"active_page": "upload"}
    )

@router.post("/upload", response_class=HTMLResponse)
async def upload_submit(request: Request, file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename:
        return RedirectResponse(url="/upload?error=empty", status_code=303)
    
    contents = await file.read()
    image_record = service.process_image_upload(db, contents, file.filename)
    return RedirectResponse(url=f"/result/{image_record.id}", status_code=303)

@router.get("/result/{image_id}", response_class=HTMLResponse)
def result_page(image_id: int, request: Request, db: Session = Depends(get_db)):
    record = service.get_image_by_id(db, image_id)
    if not record:
        return RedirectResponse(url="/history?notice=notfound", status_code=303)
    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={"active_page": "upload", "record": record}
    )

@router.get("/history", response_class=HTMLResponse)
def history_page(request: Request, db: Session = Depends(get_db)):
    records = service.get_all_images(db)
    return templates.TemplateResponse(
        request=request,
        name="history.html",
        context={"active_page": "history", "records": records}
    )

@router.get("/detail/{image_id}", response_class=HTMLResponse)
def detail_page(image_id: int, request: Request, db: Session = Depends(get_db)):
    record = service.get_image_by_id(db, image_id)
    if not record:
        return RedirectResponse(url="/history?notice=notfound", status_code=303)
    return templates.TemplateResponse(
        request=request,
        name="detail.html",
        context={"active_page": "history", "record": record}
    )

@router.post("/delete/{image_id}")
def delete_submit(image_id: int, db: Session = Depends(get_db)):
    service.delete_image_record(db, image_id)
    return RedirectResponse(url="/history?notice=deleted", status_code=303)