"""생성 본문 사후 검증: 메모에 없는 숫자 탐지, [확인 필요] 구간 분리."""
import re

NUM = re.compile(r"\d+(?:[.,]\d+)?")
FLAG = re.compile(r"\[확인 필요[^\]]*\]")


def _numbers(text: str) -> set[str]:
    return {n.replace(",", "") for n in NUM.findall(text)}


def unsupported_numbers(memo: str, body: str) -> list[str]:
    """본문에 있으나 메모에 없는 숫자(정렬, 중복 제거). [확인 필요] 안은 제외."""
    stripped = FLAG.sub(" ", body)
    return sorted(_numbers(stripped) - _numbers(memo), key=lambda s: (len(s), s))


def count_flags(body: str) -> int:
    return len(FLAG.findall(body))


def split_flags(text: str) -> list[tuple[str, bool]]:
    """텍스트를 (조각, 확인필요 여부) 목록으로 분리한다."""
    parts, pos = [], 0
    for m in FLAG.finditer(text):
        if m.start() > pos:
            parts.append((text[pos:m.start()], False))
        parts.append((m.group(0), True))
        pos = m.end()
    if pos < len(text):
        parts.append((text[pos:], False))
    return parts
