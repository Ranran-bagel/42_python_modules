# 42_python_modules

*This project has been created as part of the 42 curriculum by wezhou.*

## Description

This repository contains my solutions to the **Python Modules** from the 42 curriculum.

The modules introduce Python progressively, from basic syntax and data structures to object-oriented programming, type safety, decorators, dependency management, and data validation.

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
git clone https://github.com/Ranran-bagel/42_python_modules.git
cd 42_python_modules
```

Each module is organized in its own directory:

```text
python_00/
python_01/
python_02/
...
```

Navigate to the module and exercise you want to run. For example:

```bash
cd python_00/ex00
python3 <script_name>.py
```

Exact execution and dependency requirements differ between modules. Check the corresponding module directory before running an exercise.

### Virtual Environment

For exercises that require an isolated Python environment:

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

### Code Checking

Depending on the module, code can be checked with:

```bash
flake8 .
mypy --strict .
```

## AI Usage

AI tools were used as a learning and debugging aid during this project.

They were used to:

- clarify unfamiliar Python concepts and syntax;
- explain type annotations and `mypy` errors;
- understand tools such as Poetry, virtual environments, `.env`, and Pydantic;
- analyze error messages and suggest debugging approaches;
- review code structure and identify possible improvements;
- explain concepts such as decorators, `ParamSpec`, validation, and dependency management;
- assist in drafting and structuring this README.

AI-generated suggestions were reviewed and adapted before use. The final implementation was written, tested, and verified according to the requirements of the 42 curriculum.
