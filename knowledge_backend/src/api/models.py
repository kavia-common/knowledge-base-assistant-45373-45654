from pydantic import BaseModel, Field
from typing import Optional
import datetime

# PUBLIC_INTERFACE
class FileMetadata(BaseModel):
    """Metadata for an uploaded file."""
    filename: str = Field(..., description="Original name of the uploaded file")
    content_type: str = Field(..., description="MIME type detected for the file")
    size: int = Field(..., description="Byte size of the uploaded file")
    upload_time: str = Field(..., description="UTC ISO8601 upload time")
    path: Optional[str] = Field(None, description="Path where the file is stored on server")

# PUBLIC_INTERFACE
def metadata_from_upload(filename: str, content_type: str, size: int, upload_time: datetime.datetime, path: str = None) -> FileMetadata:
    """Helper to create FileMetadata from upload attributes."""
    return FileMetadata(
        filename=filename,
        content_type=content_type,
        size=size,
        upload_time=upload_time.replace(microsecond=0).isoformat() + "Z",
        path=path,
    )
