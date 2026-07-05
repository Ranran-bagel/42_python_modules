import typing
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self, name: str) -> None:
        self._name = name
        self._data: list[tuple[int, str]] = []
        self._rank: int = 0

    def get_name(self) -> str:
        return self._name

    def get_total_processed(self) -> int:
        return self._rank

    def get_remaining_count(self) -> int:
        return len(self._data)

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
    def __init__(self) -> None:
        super().__init__("Numeric Processor")

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
    def __init__(self) -> None:
        super().__init__("Text Processor")

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
    def __init__(self) -> None:
        super().__init__("Log Processor")

    def _validate_log(self, data: dict[typing.Any, typing.Any]) -> bool:
        if "log_level" not in data or "log_message" not in data:
            return False
        for key in data:
            if not isinstance(key, str):
                return False
            if not isinstance(data[key], str):
                return False
        return True

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return self._validate_log(data)
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False
                if not self._validate_log(item):
                    return False
            return True
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


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExporter:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        res = ",".join(str(d[1]) for d in data)
        print("CSV Output:")
        print(res)


class JSONExporter:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        items: list[str] = []
        for rank, value in data:
            items.append(f'"item_{rank}": "{value}"')
        print("JSON Output:")
        print("{" + ", ".join(items) + "}")

class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            processed = False
            for proc in self._processors:
                if proc.validate(item):
                    proc.ingest(item)
                    processed = True
                    break
            if not processed:
                print(f"DataStream error - Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        has_any_processor = False
        for proc in self._processors:
            print(f"{proc.get_name()}: total {proc.get_total_processed()} "
                  "items processed, remaining "
                  f"{proc.get_remaining_count()} on processor")
            has_any_processor = True
        if not has_any_processor:
            print("No processor found, no data")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        nb_origin = nb
        for proc in self._processors:
            collected = []
            if proc.get_remaining_count() < nb_origin:
                nb_cur = proc.get_remaining_count()
            else:
                nb_cur = nb_origin
            for i in range(nb_cur):
                collected.append(proc.output())
            if collected:
                plugin.process_output(collected)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print()
    print("Initialize Data Stream...")
    data_stream = DataStream()
    print()
    print("== DataStream statistics ==")
    data_stream.print_processors_stats()
    print()
    print("Registering Processors")
    numeric_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()
    data_stream.register_processor(numeric_processor)
    data_stream.register_processor(text_processor)
    data_stream.register_processor(log_processor)
    print()
    print("Send first batch of data on stream: "
          "['Hello world', [3.14, -1, 2.71], [{'log_level': 'WARNING', '"
          "log_message': 'Telnet access! Use ssh instead'}, {'log_level': "
          "'INFO', 'log_message': 'User wil is "
          "connected'}], 42, ['Hi', 'five']]")
    data_stream.process_stream(['Hello world', [3.14, -1, 2.71],
                               [{'log_level': 'WARNING', 'log_message': 
                                   'Telnet access! Use ssh instead'},
                                {'log_level': 'INFO', 'log_message':
                                    'User wil is connected'}], 42, ['Hi', 'five']])
    print()
    print("== DataStream statistics ==")
    data_stream.print_processors_stats()
    print()
    csv_plugin = CSVExporter()
    json_plugin = JSONExporter()
    print("Send 3 processed data from each processor to a CSV plugin:")
    data_stream.output_pipeline(3, csv_plugin)
    print()
    print("== DataStream statistics ==")
    data_stream.print_processors_stats()
    print()
    print("Send another batch of data: [21, "
          "['I love AI', 'LLMs are wonderful', 'Stay healthy'], [{'log_level': "
          "'ERROR', 'log_message': '500 server crash'}, {'log_level': 'NOTICE',"
          " 'log_message': 'Certificate expires in 10 days'}],"
          " [32, 42, 64, 84, 128, 168], 'World hello']")
    data_stream.process_stream([21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
                                [{'log_level': 'ERROR', 'log_message': '500 server crash'},
                                 {'log_level': 'NOTICE', 'log_message':
                                     'Certificate expires in 10 days'}],
                                [32, 42, 64, 84, 128, 168], 'World hello'])
    print()
    print("== DataStream statistics ==")
    data_stream.print_processors_stats()
    print()
    print("Send 5 processed data from each processor to a JSON plugin:")
    data_stream.output_pipeline(5, json_plugin)
    print()
    print("== DataStream statistics ==")
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
