"""Minimal YAML 1.1 subset for wiki/data and eval files. Stdlib only."""

from __future__ import annotations

from typing import Any


def loads(text: str) -> Any:
    lines: list[tuple[int, str]] = []
    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        if "\t" in raw[: len(raw) - len(raw.lstrip())]:
            raise ValueError("tabs are not allowed")
        content = _strip_comment(raw.strip())
        lines.append((indent, content))
    if not lines:
        return None
    value, idx = _parse(lines, 0, lines[0][0])
    if idx != len(lines):
        raise ValueError(f"unparsed YAML starting at {lines[idx][1]!r}")
    return value


def dumps(data: Any) -> str:
    return _dump(data, 0).rstrip() + "\n"


def _strip_comment(content: str) -> str:
    in_single = in_double = False
    for i, ch in enumerate(content):
        if ch == "'" and not in_double:
            in_single = not in_single
        elif ch == '"' and not in_single:
            in_double = not in_double
        elif ch == "#" and not in_single and not in_double and i > 0 and content[i - 1].isspace():
            return content[:i].rstrip()
    return content


def _parse(lines: list[tuple[int, str]], i: int, indent: int) -> tuple[Any, int]:
    if i >= len(lines):
        return None, i
    if lines[i][1].startswith("- "):
        return _parse_list(lines, i, indent)
    return _parse_map(lines, i, indent)


def _parse_map(lines: list[tuple[int, str]], i: int, indent: int) -> tuple[dict[str, Any], int]:
    result: dict[str, Any] = {}
    while i < len(lines):
        level, content = lines[i]
        if level < indent:
            break
        if level > indent:
            raise ValueError(f"bad indent near {content!r}")
        if content.startswith("- "):
            break
        key, value, i = _parse_key_line(lines, i, indent)
        result[key] = value
    return result, i


def _parse_list(lines: list[tuple[int, str]], i: int, indent: int) -> tuple[list[Any], int]:
    result: list[Any] = []
    while i < len(lines):
        level, content = lines[i]
        if level < indent or not content.startswith("- "):
            break
        if level > indent:
            raise ValueError(f"bad list indent near {content!r}")
        item_text = content[2:]
        i += 1
        if item_text == "":
            if i < len(lines) and lines[i][0] > indent:
                value, i = _parse(lines, i, lines[i][0])
            else:
                value = None
            result.append(value)
            continue
        if _looks_like_key(item_text):
            key, remainder = _split_key(item_text)
            mapping: dict[str, Any] = {}
            if remainder == "":
                if i < len(lines) and lines[i][0] > indent:
                    mapping[key], i = _parse(lines, i, lines[i][0])
                else:
                    mapping[key] = None
            else:
                mapping[key] = _scalar(remainder)
            while i < len(lines) and lines[i][0] > indent and not lines[i][1].startswith("- "):
                nested, i = _parse_map(lines, i, lines[i][0])
                mapping.update(nested)
            while i < len(lines) and lines[i][0] > indent and lines[i][1].startswith("- "):
                # orphan nested list after a scalar key belongs to last empty key? unsupported
                break
            result.append(mapping)
            continue
        result.append(_scalar(item_text))
    return result, i


def _parse_key_line(lines: list[tuple[int, str]], i: int, indent: int) -> tuple[str, Any, int]:
    _, content = lines[i]
    key, remainder = _split_key(content)
    i += 1
    if remainder == "":
        if i < len(lines) and lines[i][0] > indent:
            value, i = _parse(lines, i, lines[i][0])
        else:
            value = None
        return key, value, i
    return key, _scalar(remainder), i


def _looks_like_key(text: str) -> bool:
    if text[:1] in {"'", '"'}:
        return False
    if ": " in text or text.endswith(":"):
        return True
    return False


def _split_key(text: str) -> tuple[str, str]:
    if text.endswith(":") and (": " not in text):
        return text[:-1].strip(), ""
    key, _, rest = text.partition(": ")
    return key.strip(), rest.strip()


def _scalar(text: str) -> Any:
    if text in {"", "null", "~"}:
        return None
    if text == "true":
        return True
    if text == "false":
        return False
    if text == "[]":
        return []
    if text == "{}":
        return {}
    if len(text) >= 2 and text[0] == text[-1] and text[0] in {"'", '"'}:
        return text[1:-1]
    if _is_int(text):
        return int(text)
    if _is_float(text):
        return float(text)
    return text


def _is_int(text: str) -> bool:
    if text.startswith("-"):
        return text[1:].isdigit() and bool(text[1:])
    return text.isdigit()


def _is_float(text: str) -> bool:
    if text.count(".") != 1:
        return False
    left, _, right = text.partition(".")
    if left.startswith("-"):
        left = left[1:]
    return left.isdigit() and right.isdigit()


def _dump(data: Any, indent: int) -> str:
    pad = "  " * indent
    if isinstance(data, list):
        if not data:
            return f"{pad}[]\n"
        chunks = []
        for item in data:
            if isinstance(item, dict):
                if not item:
                    chunks.append(f"{pad}- {{}}\n")
                    continue
                keys = list(item.items())
                first_k, first_v = keys[0]
                if isinstance(first_v, (dict, list)):
                    chunks.append(f"{pad}- {first_k}:\n{_dump(first_v, indent + 2)}")
                else:
                    chunks.append(f"{pad}- {first_k}: {_fmt_scalar(first_v)}\n")
                rest = dict(keys[1:])
                if rest:
                    chunks.append(_dump(rest, indent + 1))
            elif isinstance(item, list):
                chunks.append(f"{pad}-\n{_dump(item, indent + 1)}")
            else:
                chunks.append(f"{pad}- {_fmt_scalar(item)}\n")
        return "".join(chunks)
    if isinstance(data, dict):
        if not data:
            return f"{pad}{{}}\n"
        chunks = []
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                chunks.append(f"{pad}{key}:\n{_dump(value, indent + 1)}")
            else:
                chunks.append(f"{pad}{key}: {_fmt_scalar(value)}\n")
        return "".join(chunks)
    return f"{pad}{_fmt_scalar(data)}\n"


def _fmt_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    if text == "" or text in {"true", "false", "null"} or any(ch in text for ch in ":#\n'"):
        escaped = text.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    return text
