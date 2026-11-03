from sqlalchemy import Column, Integer, String, Text, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config import Base

class ObjectClass(Base):
    __tablename__ = "object_classes"

    id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String(100), nullable=False)
    description = Column(Text)

    results = relationship("DetectionResult", back_populates="object_class")

class DetectionImage(Base):
    __tablename__ = "detection_images"

    id = Column(Integer, primary_key=True, index=True)
    original_filename = Column(String(255), nullable=False)
    stored_filename = Column(String(255), nullable=False)
    image_path = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())

    results = relationship("DetectionResult", back_populates="image", cascade="all, delete-orphan")

class DetectionResult(Base):
    __tablename__ = "detection_results"

    id = Column(Integer, primary_key=True, index=True)
    image_id = Column(Integer, ForeignKey("detection_images.id", ondelete="CASCADE"), nullable=False)
    class_id = Column(Integer, ForeignKey("object_classes.id", ondelete="CASCADE"), nullable=False)
    confidence_score = Column(Numeric(5, 4), nullable=False)
    x_min = Column(Integer, nullable=False)
    y_min = Column(Integer, nullable=False)
    x_max = Column(Integer, nullable=False)
    y_max = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())

    image = relationship("DetectionImage", back_populates="results")
    object_class = relationship("ObjectClass", back_populates="results")