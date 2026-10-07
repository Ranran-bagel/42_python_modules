# 42_python_modules

*This project has been created as part of the 42 curriculum by wezhou.*

## Description

This repository contains my solutions to the **Python Modules** from the 42 curriculum.

The project introduces Python progressively, from basic syntax and data structures to more advanced concepts such as object-oriented programming, type safety, decorators, environment management, and data validation.

Main topics covered include:

- Python syntax, functions, and data structures
- File I/O and command-line arguments
- Exception handling
- Object-oriented programming
- Type hints and static type checking with `mypy`
- Iterators, generators, and decorators
- Generic typing with `TypeVar` and `ParamSpec`
- Virtual environments and dependency management
- `pip`, `requirements.txt`, and Poetry
- Environment variables and `.env` files
- Data validation with Pydantic
- Nested models, enums, and custom validation

## Instructions

Clone the repository:

```bash
git clone <repository-url>
cd python_modules
```

Navigate to the module and exercise you want to run:

```bash
cd PythonXX/ex00
python3 <script_name>.py
```

Some modules require additional dependencies or an isolated Python environment.

### Virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Dependencies

When a `requirements.txt` file is provided:

```bash
pip install -r requirements.txt
```

When Poetry is used:

```bash
poetry install
```

### Code checking

Depending on the module, the code can be checked with:

```bash
flake8 .
mypy --strict .
```

Exact execution and dependency requirements may differ between modules. Check the corresponding module directory before running an exercise.

## AI Usage

AI tools were used as a learning and debugging aid during this project.

They were used to:

- clarify unfamiliar Python concepts and syntax;
- explain type annotations and `mypy` errors;
- understand tools such as Poetry, virtual environments, `.env`, and Pydantic;
- analyze error messages and suggest debugging approaches;
- review code structure and identify possible improvements;
- explain concepts such as decorators, `ParamSpec`, validation, and dependency management.
- assist in drafting and structuring this README.

AI-generated suggestions were reviewed and adapted before use. The final implementation was written, tested, and verified according to the requirements of the 42 curriculum.
