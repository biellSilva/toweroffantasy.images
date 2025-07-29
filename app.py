from pathlib import Path

from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/{image:path}")
async def get_image(image: str) -> FileResponse:
    image_path = (
        Path(image)
        if image.startswith("Hotta/Content")
        else Path("./Hotta/Content", image)
    )
    if not image_path.exists() or not image_path.is_file():
        raise HTTPException(
            status_code=404,
            detail="Image not found, please check the path.",
        )
    return FileResponse(image_path)
