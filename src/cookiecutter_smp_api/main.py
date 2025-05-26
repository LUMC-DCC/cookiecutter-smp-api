from fastapi import FastAPI
from cookiecutter_smp_api.api.routes import router

app = FastAPI(
    title="Cookiecutter SMP API",
    description="API for applying Cookiecutter templates with JSON context.",
    version="0.1.0"
)

app.include_router(router)
