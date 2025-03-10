import re


class Utils:
    @staticmethod
    def detect_summary(text: str) -> bool:
        pattern = r"\bSummary(?:\sread)?\b"
        matches = re.findall(pattern, text)
        return bool(matches)

    @staticmethod
    def format_ddl_and_examples(
        ddl_commands: list[str], examples: list[dict[str, str]]
    ) -> tuple[str, str]:
        ddl_commands_str = "\n".join(ddl_commands)
        examples_str = "\n".join(
            [f"{i + 1}. {example['text']}\n" for i, example in enumerate(examples)]
        )
        return ddl_commands_str, examples_str
