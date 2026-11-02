# Graph Report - First-PR  (2026-11-02)

## Corpus Check
- 24 files · ~2,850 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 97 nodes · 109 edges · 22 communities (7 shown, 15 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6ef00c16`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- main.py
- First Pull Request - Learn by Doing
- Step-by-Step Guide
- Contributors List
- 개발 도구 연결 가이드
- CLAUDE.md
- .claude/CLAUDE.md
- sample_memo.md
- artifacts.md
- condition.md
- environment.md
- evaluation.md
- history.md
- layout.md
- overview.md
- stratigraphy.md
- structure.md
- .mcp.json
- unsupported_numbers
- test_verify.py
- 명세: 생성 본문 사후 검증과 확인 필요 항목 강조

## God Nodes (most connected - your core abstractions)
1. `main()` - 10 edges
2. `First Pull Request - Learn by Doing` - 10 edges
3. `unsupported_numbers()` - 9 edges
4. `Step-by-Step Guide` - 8 edges
5. `add_body()` - 6 edges
6. `split_flags()` - 6 edges
7. `명세: 생성 본문 사후 검증과 확인 필요 항목 강조` - 6 edges
8. `VerifyTest` - 5 edges
9. `count_flags()` - 5 edges
10. `load_template()` - 4 edges

## Surprising Connections (you probably didn't know these)
- `main()` --calls--> `count_flags()`  [EXTRACTED]
  heritage-report-gen/main.py → heritage-report-gen/verify.py
- `main()` --calls--> `unsupported_numbers()`  [EXTRACTED]
  heritage-report-gen/main.py → heritage-report-gen/verify.py
- `add_body()` --calls--> `split_flags()`  [EXTRACTED]
  heritage-report-gen/main.py → heritage-report-gen/verify.py

## Import Cycles
- None detected.

## Communities (22 total, 15 thin omitted)

### Community 0 - "main.py"
Cohesion: 0.21
Nodes (7): add_body(), build_prompt(), generate(), load_template(), main(), set_font(), split_flags()

### Community 1 - "First Pull Request - Learn by Doing"
Cohesion: 0.20
Nodes (9): About Pull Requests, Best Practices, Code of Conduct, First Pull Request - Learn by Doing, Need Help?, Optional: Add Yourself as a Contributor, Prerequisites, What You'll Learn (+1 more)

### Community 2 - "Step-by-Step Guide"
Cohesion: 0.25
Nodes (8): 1. Fork This Repository, 2. Clone Your Fork, 3. Create a New Branch, 4. Make Your Changes, 5. Commit Your Changes, 6. Push to GitHub, 7. Create a Pull Reest, Step-by-Step Guide

### Community 3 - "Contributors List"
Cohesion: 0.50
Nodes (3): Contributors, Contributors List, Example

### Community 4 - "개발 도구 연결 가이드"
Cohesion: 0.50
Nodes (3): strix (보안 점검 에이전트), 개발 도구 연결 가이드, 개인 환경에서 한 번만 할 일

### Community 19 - "unsupported_numbers"
Cohesion: 0.25
Nodes (4): VerifyTest, count_flags(), _numbers(), unsupported_numbers()

### Community 21 - "명세: 생성 본문 사후 검증과 확인 필요 항목 강조"
Cohesion: 0.29
Nodes (6): 명세: 생성 본문 사후 검증과 확인 필요 항목 강조, 배경, 범위 밖, 수용 기준, 요구사항, 한계

## Knowledge Gaps
- **15 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `unsupported_numbers()` connect `unsupported_numbers` to `main.py`, `test_verify.py`?**
  _High betweenness centrality (0.030) - this node is a cross-community bridge._
- **Why does `First Pull Request - Learn by Doing` connect `First Pull Request - Learn by Doing` to `Step-by-Step Guide`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **Why does `Step-by-Step Guide` connect `Step-by-Step Guide` to `First Pull Request - Learn by Doing`?**
  _High betweenness centrality (0.020) - this node is a cross-community bridge._