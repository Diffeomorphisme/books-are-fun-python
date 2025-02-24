# python-project-template
A Template Repository to kickstart your Python project

## Features
Includes:
- A GitHub CI workflow that lints and tests the code, as well as runs an installation check
- A setup for dealing with secrets either locally with a `.env` file or from the environment (test / prod)  

## In practice
### Installing the project

Install uv 

run `curl -LsSf https://astral.sh/uv/install.sh | sh`
(alternatives can be found here: https://docs.astral.sh/uv/getting-started/installation/)


### Running the code locally
- Create a `.env` file in the root of the folder, and populate it up with the project's secrets, as shown in the `env.example` file
- The script to execute is app/main.py, and the working directory should be the root of the project

To run the project (installations run automatically): 

run `uv run app/main.py`


### Before pushing your code
Make sure that your code is formatted properly by running the following commands:

run `uv run ruff format` & `uv run ruff check --fix`

Run the tests to make sure everything is performing as expected:

run `uv run pytest tests`
