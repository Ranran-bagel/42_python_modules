def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise Exception(f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise Exception(f"{temp}°C is too cold for plants (min 0°C)")
    return temp

def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    print("Input data is '25'")
    try:
        result = input_temperature("25")
        print(f"Temperature is now {result}°C")
    except Exception as error:
        print(f"Caught input_temperature error: {error}")
    print()
    print("Input data is 'abc'")
    try:
        result = input_temperature("abc")
    except Exception as error:
        print(f"Caught input_temperature error: {error}")
    print()
    print("Input data is '100'")
    try:
        result = input_temperature("100")
    except Exception as error:
        print(f"Caught input_temperature error: {error}")
    print()
    print("Input data is '-50'")
    try:
        result = input_temperature("-50")
    except Exception as error:
        print(f"Caught input_temperature error: {error}")
    print()
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()
