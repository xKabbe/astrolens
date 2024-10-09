# Backend

Coming soon...

## Set Up The Backend

1. Set up and activate a virtual environment:

    ```bash
    # On linux/macOS
    python -m venv path/to/venv
    source path/to/venv/bin/activate
    
    # On windows
    python -m venv path/to/venv
    source path/to/venv/Scripts/activate
    ```

2. Install project in editable mode:

    ```bash
    pip install -e .
    ```

3. Install the production required dependencies:

    ```bash
    pip install -r requirements/prod.txt
    ```

4. Install the dev/testing required dependencies:

    ```bash
    pip install -r requirements/dev.txt
    ```

## Run The Backend

```bash
fastapi dev backend/main.js
```

Execute this command to run the `FastAPI` backend on `localhost:8000`.
