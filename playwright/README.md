# Playwright Testing

This folder contains all the end-to-end (E2E) tests for the project, using [Playwright](https://playwright.dev/) in Python.
The tests cover both the front-end (GUI) and back-end (API) functionality.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

1. [Python](https://www.python.org/) (v3.12 or later) - for creating Playwright tests
2. [pip](https://pypi.org/project/pip/) (v24.2 or later) - for installing and managing python packages

Install the [Pytest plugin](https://pypi.org/project/pytest-playwright/):

### Install Dependencies

Start the virtual environment, if not already happened because of the [Backend Setup](../backend/README.md):

```bash
# On linux/macOS
python -m venv path/to/venv
source path/to/venv/bin/activate

# On windows
python -m venv path/to/venv
source path/to/venv/Scripts/activate
```

After creating and/or activating the virtual environment you need to install the needed dependencies:

```bash
cd playwright
pip install -r requirements.txt
```

Install the required browsers:

```bash
playwright install
```

This will download and install the necessary browsers (Chromium, Firefox, and WebKit) used for testing.

## Usage

Once everything is set up, you can run all the tests using the `pytest` command.

```bash
pytest
```

### Common Commands

...
