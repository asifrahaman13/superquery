from src.helper.utils import Utils


def test_detect_summary():
    assert Utils.detect_summary("This is a Summary of the report.") is True
    assert Utils.detect_summary("Summary read is available.") is True
    assert Utils.detect_summary("This is a detailed report.") is False


def test_format_ddl_and_examples():
    ddl_commands = ["CREATE TABLE users;", "DROP TABLE orders;"]
    examples = [{"text": "Example 1"}, {"text": "Example 2"}]
    ddl_str, examples_str = Utils.format_ddl_and_examples(ddl_commands, examples)
    assert ddl_str == "CREATE TABLE users;\nDROP TABLE orders;"
    assert examples_str == "1. Example 1\n\n2. Example 2\n"
    ddl_commands = []
    examples = []
    ddl_str, examples_str = Utils.format_ddl_and_examples(ddl_commands, examples)
    assert ddl_str == ""
    assert examples_str == ""
