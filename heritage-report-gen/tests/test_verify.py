import subprocess
import sys
import unittest
from pathlib import Path

from docx import Document
from docx.enum.text import WD_COLOR_INDEX

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from verify import count_flags, split_flags, unsupported_numbers  # noqa: E402

MEMO = "정면 3칸 측면 3칸, 기둥 하부 부식 약 20cm 깊이, 조사일 2026-09-14"


class VerifyTest(unittest.TestCase):
    def test_flags_number_not_in_memo(self):
        self.assertEqual(unsupported_numbers(MEMO, "건립은 1450년경이다."), ["1450"])

    def test_memo_numbers_pass(self):
        self.assertEqual(unsupported_numbers(MEMO, "정면 3칸, 부식 깊이 20cm."), [])

    def test_numbers_inside_flag_ignored(self):
        body = "중수 시기는 [확인 필요: 1700년대 기록 원문 확인]이다."
        self.assertEqual(unsupported_numbers(MEMO, body), [])

    def test_count_and_split(self):
        text = "가 [확인 필요: A] 나 [확인 필요] 다"
        self.assertEqual(count_flags(text), 2)
        self.assertEqual([f for _, f in split_flags(text)], [False, True, False, True, False])
        self.assertEqual("".join(t for t, _ in split_flags(text)), text)


class EndToEndTest(unittest.TestCase):
    """API 없이 가짜 응답으로 .docx 생성까지 확인한다."""

    def test_full_flow_with_fake_llm(self):
        import importlib
        import tempfile
        import types

        main = importlib.import_module("main")
        fake = "- 정면 3칸이다.\n소재지는 [확인 필요: 소재지 미기재]이다.\n건립은 1450년경으로 본다."
        main.generate = lambda *a, **k: fake
        fake_anthropic = types.SimpleNamespace(Anthropic=lambda: object())
        sys.modules["anthropic"] = fake_anthropic

        out = Path(tempfile.mkdtemp()) / "t.docx"
        argv = sys.argv
        sys.argv = ["main.py", "-i", str(ROOT / "input/sample_memo.md"), "-t", "architecture_survey", "-o", str(out)]
        try:
            main.main()
        finally:
            sys.argv = argv
            sys.modules.pop("anthropic", None)

        doc = Document(out)
        highlighted = [r.text for p in doc.paragraphs for r in p.runs
                       if r.font.highlight_color == WD_COLOR_INDEX.YELLOW]
        self.assertTrue(highlighted)
        self.assertTrue(all(t.startswith("[확인 필요") for t in highlighted))
        text = "\n".join(p.text for p in doc.paragraphs)
        self.assertIn("검증 요약", text)
        self.assertIn("메모에 없는 숫자: 1450", text)


if __name__ == "__main__":
    unittest.main()
