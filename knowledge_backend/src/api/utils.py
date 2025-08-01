import os
from fastapi import UploadFile

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "../../uploaded_files")

# PUBLIC_INTERFACE
def ensure_upload_dir_exists():
    """Ensure the upload directory exists."""
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    return UPLOAD_DIR

# PUBLIC_INTERFACE
async def save_upload_file(file: UploadFile) -> str:
    """
    Save an uploaded file and return the absolute disk path.
    """
    directory = ensure_upload_dir_exists()
    file_path = os.path.join(directory, file.filename)
    # Avoid overwriting files: append a number if file exists
    base, ext = os.path.splitext(file.filename)
    i = 1
    while os.path.exists(file_path):
        file_path = os.path.join(directory, f"{base}_{i}{ext}")
        i += 1

    with open(file_path, "wb") as buffer:
        while chunk := await file.read(1024 * 1024):
            buffer.write(chunk)

    await file.seek(0)  # Reset for any future use
    return os.path.abspath(file_path)
