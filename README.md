# Cookiecutter SMP API

⚠️ ***This project is under active development***


A FastAPI-powered service that applies a multi-language 
[cookiecutter](https://cookiecutter.readthedocs.io/) 
template and returns a zipped project.

This API is designed to work with the 
[LUMC-DCC cookiecutter templates](https://github.com/LUMC-DCC/cookiecutter-templates) repository, 
which provides subdirectory-based language templates (e.g., Python, R).

## Endpoints

- **GET /**  
  Health check endpoint.

- **POST /zip_from_smp**  
  Upload a JSON context file (with at least `language` and `project_slug`).  
  Example JSON:
  ```json
  {
    "language": "python",
    "project_name": "My Awesome Project",
    "project_slug": "awesome_project",
    "include_docs": "yes"
  }

## Running locally

Install dependencies with
```bash
poetry install
```

Run the API (hot reload for dev)
```bash
poetry run uvicorn cookiecutter_smp_api.main:app --reload --port 8000
```

Then visit http://127.0.0.1:8000/docs for the interactive API docs.

## Notes

* This API uses cookiecutter under the hood.
* The language in your JSON must match a subdirectory in the template repo (e.g., `python`, `r`).


---
## License
This project is licensed under the Apache 2.0. See the [LICENSE](LICENSE.txt) file for details.