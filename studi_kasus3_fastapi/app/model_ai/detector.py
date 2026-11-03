import cv2
import numpy as np
import random
from pathlib import Path

def run_object_detection(input_image_path: str, output_image_path: str):
    """
    Simulasi/Inference engine deteksi objek helm pada gambar.
    Menggunakan OpenCV untuk menggambar Bounding Box dan mengembalikan koordinat deteksi.
    """
    image = cv2.imread(input_image_path)
    if image is None:
        raise ValueError("Gambar tidak dapat dibaca.")

    height, width, _ = image.shape
    detections = []

    # Membuat deteksi otomatis berdasarkan dimensi gambar
    num_objects = random.randint(1, 3)
    for _ in range(num_objects):
        # Menentukan kelas acak (1: helmet, 2: no_helmet)
        class_id = random.choice([1, 2])
        label = "helmet" if class_id == 1 else "no_helmet"
        color = (0, 255, 0) if class_id == 1 else (0, 0, 255) # Hijau untuk helm, Merah untuk tanpa helm

        # Bounding Box acak yang proporsional
        w_box = random.randint(int(width * 0.15), int(width * 0.35))
        h_box = random.randint(int(height * 0.15), int(height * 0.35))
        x_min = random.randint(0, max(1, width - w_box))
        y_min = random.randint(0, max(1, height - h_box))
        x_max = x_min + w_box
        y_max = y_min + h_box
        confidence = round(random.uniform(0.75, 0.98), 4)

        # Gambar Bounding Box & Label pada file output
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color, 3)
        caption = f"{label} {confidence:.2f}"
        cv2.putText(image, caption, (x_min, max(y_min - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        detections.append({
            "class_id": class_id,
            "confidence_score": confidence,
            "x_min": x_min,
            "y_min": y_min,
            "x_max": x_max,
            "y_max": y_max
        })

    # Simpan hasil pemrosesan gambar
    cv2.imwrite(output_image_path, image)
    return detections