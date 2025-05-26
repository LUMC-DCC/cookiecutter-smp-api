from pathlib import Path
import json
import shutil
from cookiecutter.main import cookiecutter


def generate_from_template(json_file, base_tmp_dir):
    context_data = json.load(json_file.file)
    slug = context_data.get("project_slug") or context_data.get("project_name") or "project"
    language = context_data.get("language")
    if not language:
        raise ValueError("The 'language' field is required in the context JSON.")

    output_dir = Path(base_tmp_dir) / "output"
    output_dir.mkdir()

    project_path = Path(cookiecutter(
        template='https://github.com/LUMC-DCC/cc-template.git',
        directory=language,
        no_input=True,
        extra_context=context_data,
        output_dir=str(output_dir)
    ))

    zip_base = Path(base_tmp_dir) / "result"
    shutil.make_archive(
        base_name=str(zip_base),
        format='zip',
        root_dir=project_path.parent,
        base_dir=project_path.name
    )

    return zip_base.with_suffix(".zip"), slug
