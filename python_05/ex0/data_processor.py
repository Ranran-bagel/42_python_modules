# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    data_processor.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wezhou <wezhou@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/22 11:07:27 by wezhou            #+#    #+#              #
#    Updated: 2026/06/22 14:35:10 by wezhou           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import typing
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def  __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._rank:int = 0
    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if self._data:
            res = self._data[0]
            del self._data[0]
            return res
        else:
            raise Exception("No data to output")


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
            return True
        else:
            return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for item in data:
                    self._data.append((self._rank, str(item)))
                    self._rank += 1
            else:
                self._data.append((self._rank, str(data)))
                self._rank += 1
        else:
            raise Exception("Improper numeric data")

   
class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for item in data:
                    self._data.append((self._rank, item))
                    self._rank += 1
            else:
                self._data.append((self._rank, data))
                self._rank += 1
        else:
            raise Exception("Improper text data")


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            for key in data:
                if not isinstance(key, str):
                    return False
                if not isinstance(data[key], str):
                    return False
            return True 
        elif isinstance(data, list):
            for item in data:
                for key in item:
                    if not isinstance(key, str):
                        return False
                    if not isinstance(item[key], str):
                        return False
                return True 
        else:
            return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for item in data:
                    message = item["log_level"] + ": " + item["log_message"]
                    self._data.append((self._rank, message))
                    self._rank += 1
            else:
                message = data["log_level"] + ": " + data["log_message"]
                self._data.append((self._rank, message))
                self._rank += 1
        else:
            raise Exception("Improper log data")


def main() -> None:
    numericprocessor = NumericProcessor()
    textprocessor = TextProcessor()
    logprocessor = LogProcessor()
    print("=== Code Nexus - Data Processor ===")
    print()
    print("Testing Numeric Processor...")
    print(f"Trying to validate input '42': {numericprocessor.validate(42)}")
    print(f"Trying to validate input 'Hello': {numericprocessor.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numericprocessor.ingest("foo")
    except Exception as error:
        print(f"Got exception: {error}")
    print("Processing data: [1, 2, 3, 4, 5]")
    is_validated = numericprocessor.validate([1, 2, 3, 4, 5])
    if is_validated:
        try:
            numericprocessor.ingest([1, 2, 3, 4, 5])
        except Exception as error:
            print(f"Got exception: {error}")
    print("Extracting 3 values...")
    rank, value = numericprocessor.output()
    print(f"Numeric value {rank}: {value}")
    rank, value = numericprocessor.output()
    print(f"Numeric value {rank}: {value}")
    rank, value = numericprocessor.output()
    print(f"Numeric value {rank}: {value}")
    print()
    print("Testing Text Processor...")
    print(f"Trying to validate input '42': {textprocessor.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    is_validated = textprocessor.validate(['Hello', 'Nexus', 'World'])
    if is_validated:
        try:
            textprocessor.ingest(['Hello', 'Nexus', 'World'])
        except Exception as error:
            print(f"Got exception: {error}")
    print("Extracting 1 values...")
    print(f"Text value {textprocessor.output()}")
    print()
    print("Testing Log Processor...")
    print(f"Trying to validate input 'Hello': {logprocessor.validate('Hello')}")
    print("Processing data: [{'log_level': "
          "'NOTICE', 'log_message': 'Connection to server'}, "
          "{'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]")
    is_validated = logprocessor.validate([{'log_level': 'NOTICE',
                                            'log_message': 'Connection to server'},
                                           {'log_level': 'ERROR', 'log_message':
                                               'Unauthorized access!!'}])
    if is_validated:
        try:
            logprocessor.ingest([{'log_level': 'NOTICE',
                                            'log_message': 'Connection to server'},
                                           {'log_level': 'ERROR', 'log_message':
                                               'Unauthorized access!!'}])
        except Exception as error:
            print(f"Got exception: {error}")
    print("Extracting 2 values...")
    rank, value = logprocessor.output()
    print(f"Log entry {rank}: {value}")
    rank, value = logprocessor.output()
    print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
