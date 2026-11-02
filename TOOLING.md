# 개발 도구 연결 가이드

이 저장소에서 Claude Code와 함께 쓰는 도구 목록입니다.
`.claude/settings.json`과 `.mcp.json`은 커밋되어 있으므로 저장소를 열면 자동으로 제안됩니다.

| 도구 | 방식 | 상태 |
|---|---|---|
| Agent-skills (addyosmani) | 플러그인 `agent-skills@addy-agent-skills` | settings.json에 등록 |
| Matt Pocock skills | 플러그인 `mattpocock-skills@claude-plugins-official` | settings.json에 등록, 최초 1회 `/setup-matt-pocock-skills` 실행 |
| diagram-design | 플러그인 `diagram-design@diagram-design` | settings.json에 등록 |
| graphify | 프로젝트 스킬 + 훅 | `.claude/skills/graphify`, CLAUDE.md, 훅 설치됨 |
| 21st.dev Magic | HTTP MCP 서버 `21st` | `.mcp.json`, API 키 필요 |
| strix | 독립 CLI (Claude Code 연결 아님) | 아래 참고 |

## 개인 환경에서 한 번만 할 일

1. **플러그인 신뢰**: Claude Code에서 `/plugin`으로 마켓플레이스 설치를 승인합니다.
2. **graphify CLI** (훅이 호출함): `uv tool install graphifyy` (PyPI 이름이 `graphifyy`). 이후 `/graphify .`로 그래프를 생성합니다.
3. **Magic MCP 키**: https://21st.dev/mcp 에서 새 키를 발급받고 환경변수로 설정합니다. 키를 파일에 커밋하지 않습니다.
   `export TWENTY_FIRST_API_KEY="..."`
4. **Matt Pocock skills**: `/setup-matt-pocock-skills` (이슈 트래커, 라벨, 문서 저장 위치 선택).

## strix (보안 점검 에이전트)

- 본인 소유이거나 서면 허가를 받은 대상에만 사용합니다.
- 요구사항: 실행 중인 Docker, LLM API 키.
- 설치: `curl -sSL https://strix.ai/install | bash`
- 설정: `export STRIX_LLM="<model>"`, `export LLM_API_KEY="<key>"`
- 실행: `strix --target ./heritage-report-gen` (결과는 `strix_runs/`)
- `strix_runs/`와 `graphify-out/`은 커밋하지 않습니다.
