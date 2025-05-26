from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
import tempfile
import shutil
import json
from cookiecutter_smp_api.services.generator import generate_from_template
from pathlib import Path

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Cookiecutter SMP API is running"}

@router.post("/zip_from_smp")
async def generate_project(
    context_file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks()
):
    if not context_file.filename.endswith(".json"):
        raise HTTPException(status_code=400, detail="File must be a JSON file")

    tmpdir = tempfile.mkdtemp()
    zip_path, slug = generate_from_template(context_file, tmpdir)

    background_tasks.add_task(shutil.rmtree, tmpdir)

    return FileResponse(
        path=zip_path,
        media_type='application/zip',
        filename=f"{slug}.zip",
        background=background_tasks
    )