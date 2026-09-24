# Bradley-AI — Free Local Jarvis (Orchestrator Edition)

> **MEMORY.md = high-level truth. GitHub = detailed context.**  
> Bradley checks GitHub repos when he needs details, not bloating MEMORY.md.

This is Bradley — free local Jarvis that runs on your laptop (RTX 4060 8GB or MacBook Pro M3 8GB) as middle ground between chatty friend and coder-orchestrator.

Built for @ability-spec / kobiljonn — for CASMI 2026, BirOvoz, Prepl.

### What is Bradley?

- **Chatty friend:** talks like bro, remembers you called him Bradley, doesn't agree with everything if idea is bad
- **Coder orchestrator:** writes `src/scorer.py`, runs `python run_E00.py`, reads errors and fixes itself — like Claude Code / OpenHands
- **Hybrid:** 80% tasks locally free on RTX 4060 (Qwen 14B/32B Q4), 20% hard tasks — auto googles and asks cloud Bradley (Opus 5.5) via API

### Hardware Targets

**Primary: RTX 4060 8GB VRAM + 16GB RAM + i7 13th gen (recommended)**
- Qwen2.5 14B Q4_K_M: ~9GB, ~15 tok/s, 70% of cloud Bradley
- Qwen2.5 32B Q4_K_M: 6GB VRAM + 10GB RAM offload, ~8 tok/s, 80% strength

**Secondary: MacBook Pro 14" M3 8GB (from screenshot)**
- Qwen2.5 7B Q4: ~20 tok/s, light and cool
- 14B Q4: works but swaps, 6-8 tok/s, yellow memory pressure

### Quick Start (10 min)

```bash
git clone https://github.com/ability-spec/Bradley-AI.git
cd Bradley-AI
cp .env.example .env
# optional: add ANTHROPIC_API_KEY for 95% strength

docker-compose up -d ollama
# wait 30s
docker exec -it $(docker ps -q -f name=ollama) ollama pull qwen2.5:14b-instruct-q4_K_M
docker-compose up -d

# Open:
# Chat: http://localhost:3000
# Orchestrator: http://localhost:3001
```

### How Hybrid Works (what you asked: "сам гугл откроет и у тебя спросит?")

```
Local Qwen (RTX 4060) -> confidence <0.4 or 2 errors or chemistry task
  -> tools/ask_bradley.py
    -> web_search DuckDuckGo
    -> ask_bradley_cloud via ANTHROPIC_API_KEY (Opus 5.5)
  -> returns code + explanation
  -> local applies
```

See `docs/README_HYBRID.md` and `tools/ask_bradley.py`

### Repository Structure

- `MEMORY.md` — high-level truth only (who you are, hardware, main projects, preferences, links). Don't bloat to 20K tokens.
- `docker-compose.yml` — Ollama + Open WebUI + Chroma + OpenHands
- `tools/` — ask_bradley, github reader, openhands tool
- `workspace/MEMORY.md` — copy for container
- `docs/` — setup guides

**Rule:** If Bradley needs context on BirOvoz / Prepl / CASMI2026, he checks GitHub repositories, not MEMORY.md.

### Projects (high-level)

- **CASMI2026** — Kaggle mass-spec competition, 3 branches (library + structural + generation), MRR@25 by InChIKey14, 9h offline final. Detailed impl in /home/user/CASMI2026 (not in this repo, see separate).
- **BirOvoz** — Central-Asian voice benchmark, Uzbek/Kazakh voice, check GitHub for details
- **Prepl** — AI interview coach, Next.js, check GitHub

### What to Upload / Not

**Upload:** README, MEMORY.md, docker-compose, tools, docs, .env.example, .gitignore
**Don't upload:** ollama_data/ (9-20GB models), chroma_data/, .env with keys, serial numbers

### .gitignore

See .gitignore file.

---
Built with Bradley — your free Jarvis. Memory system: MEMORY.md + GitHub.
