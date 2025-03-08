import re


def detect_summary(text):
    pattern = r"\bSummary(?:\sread)?\b"
    matches = re.findall(pattern, text)
    return bool(matches)
