# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_first_exception.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wezhou <wezhou@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/16 13:21:47 by wezhou            #+#    #+#              #
#    Updated: 2026/06/16 13:42:05 by wezhou           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def input_temperature(temp_str: str) -> int:
    return int(temp_str)

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
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()
