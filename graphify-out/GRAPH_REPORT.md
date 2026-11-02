# Graph Report - First-PR  (2026-11-02)

## Corpus Check
- 21 files · ~2,254 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 3)

## Summary
- 70 nodes · 63 edges · 19 communities (5 shown, 14 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `4202dd16`
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

## God Nodes (most connected - your core abstractions)
1. `First Pull Request - Learn by Doing` - 10 edges
2. `main()` - 8 edges
3. `Step-by-Step Guide` - 8 edges
4. `add_body()` - 5 edges
5. `load_template()` - 4 edges
6. `set_font()` - 3 edges
7. `Contributors List` - 3 edges
8. `개발 도구 연결 가이드` - 3 edges
9. `build_prompt()` - 2 edges
10. `generate()` - 2 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (19 total, 14 thin omitted)

### Community 0 - "main.py"
Cohesion: 0.20
Nodes (6): add_body(), build_prompt(), generate(), load_template(), main(), set_font()

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

## Knowledge Gaps
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `First Pull Request - Learn by Doing` connect `First Pull Request - Learn by Doing` to `Step-by-Step Guide`?**
  _High betweenness centrality (0.046) - this node is a cross-community bridge._
- **Why does `Step-by-Step Guide` connect `Step-by-Step Guide` to `First Pull Request - Learn by Doing`?**
  _High betweenness centrality (0.039) - this node is a cross-community bridge._