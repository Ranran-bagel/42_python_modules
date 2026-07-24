import importlib


def check_package(name: str, purpose: str) -> bool:
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {name} ({version}) - {purpose} ready")
        return True
    except ImportError:
        print(f"[MISSING] {name} - {purpose} unavailable")
        return False


def check_dependencies() -> bool:
    packages = [
        ("pandas", "Data manipulation"),
        ("numpy", "Numerical computation"),
        ("matplotlib", "Visualization"),
    ]

    missing_packages: list[str] = []
    print("Checking dependencies:")
    for name, purpose in packages:
        if not check_package(name, purpose):
            missing_packages.append(name)
    if missing_packages:
        print()
        print("Missing dependencies detected:")
        for name in missing_packages:
            print(f"- {name}")
        print()
        print("Install with pip:")
        print("pip install -r requirements.txt")
        print("Or install with Poetry:")
        print("poetry install")
        return False
    return True


def show_dependency_management() -> None:
    print()
    print("Dependency management:")
    print("pip uses requirements.txt:")
    print("pip install -r requirements.txt")
    print("Poetry uses pyproject.toml:")
    print("poetry install")
    print("poetry run python loading.py")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print()
    if not check_dependencies():
        return
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    show_dependency_management()
    print()
    print("Analyzing Matrix data...")

    data = np.random.normal(loc=0, scale=1, size=1000)
    df = pd.DataFrame({"matrix_signal": data})

    print(f"Processing {len(df)} data points...")
    average = df["matrix_signal"].mean()
    maximum = df["matrix_signal"].max()
    minimum = df["matrix_signal"].min()
    print(f"Signal average: {average:.3f}")
    print(f"Signal maximum: {maximum:.3f}")
    print(f"Signal minimum: {minimum:.3f}")

    print("Generating visualization...")

    plt.hist(df["matrix_signal"], bins=30)
    plt.title("Matrix Signal Distribution")
    plt.xlabel("Signal value")
    plt.ylabel("Frequency")
    plt.savefig("matrix_analysis.png")
    plt.close()

    print()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
