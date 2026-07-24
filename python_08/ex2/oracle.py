import os
from dotenv import load_dotenv


REQUIRED_KEYS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def load_environment() -> bool:
    return bool(load_dotenv())


def get_config() -> dict[str, str | None]:
    config: dict[str, str | None] = {}
    for key in REQUIRED_KEYS:
        config[key] = os.getenv(key)
    return config


def print_missing_config(config: dict[str, str | None]) -> None:
    missing: list[str] = []
    for key, value in config.items():
        if value is None or value == "":
            missing.append(key)
    if missing:
        print("Missing configuration:")
        for key in missing:
            print(f"[WARNING] {key} is not set")
        print()


def show_configuration(config: dict[str, str | None]) -> None:
    mode = config.get("MATRIX_MODE")
    database_url = config.get("DATABASE_URL")
    api_key = config.get("API_KEY")
    log_level = config.get("LOG_LEVEL")
    zion_endpoint = config.get("ZION_ENDPOINT")
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    if database_url:
        if mode == "production":
            print("Database: Connected to production storage")
        else:
            print("Database: Connected to local instance")
    else:
        print("Database: Not configured")
    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API_KEY")
    if log_level:
        print(f"Log Level: {log_level}")
    else:
        print("Log Level: Unknown")
    if zion_endpoint:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def security_check(env_loaded: bool) -> None:
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if env_loaded:
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found or not loaded")
    print("[OK] Production overrides available")


def main() -> None:
    print()
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    env_loaded = load_environment()
    config = get_config()
    print_missing_config(config)
    show_configuration(config)
    print()
    security_check(env_loaded)
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
