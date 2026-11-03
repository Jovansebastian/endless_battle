from datetime import datetime
from pydantic import BaseModel, ConfigDict

class ObjectClassResponse(BaseModel):
    id: int
    class_name: str
    description: str | None = None
    model_config = ConfigDict(from_attributes=True)

class DetectionResultResponse(BaseModel):
    id: int
    image_id: int
    class_id: int
    confidence_score: float
    x_min: int
    y_min: int
    x_max: int
    y_max: int
    created_at: datetime
    object_class: ObjectClassResponse | None = None
    model_config = ConfigDict(from_attributes=True)

class DetectionImageResponse(BaseModel):
    id: int
    original_filename: str
    stored_filename: str
    image_path: str
    created_at: datetime
    results: list[DetectionResultResponse] = []
    model_config = ConfigDict(from_attributes=True)