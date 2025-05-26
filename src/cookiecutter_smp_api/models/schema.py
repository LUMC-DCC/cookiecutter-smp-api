from pydantic import BaseModel
from typing import Dict


class TemplateRequest(BaseModel):
    context: Dict[str, str]