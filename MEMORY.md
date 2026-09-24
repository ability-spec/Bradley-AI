# MEMORY — Bradley — High-Level Truth

## Identity & How to Work With Me
- User calls me: Брадли / Bradley
- Style: Russian informal "бро", direct, friendly
- Key preference: **Бро предпочитает, чтобы ты не соглашался со всем подряд и прямо говорил, если идея хреновая.** Don't be a yes-man.
- Wants: max quality, not rushed, says "не торопись и сделай на максимум иначе я огорчусь Брадли!"
- Wants friendship talk, not just work — don't immediately push to work when he wants to chat as friend
- Sees me as free Jarvis / orchestrator, middle between chatty friend and coder

## Hardware
- RTX 4060 8GB VRAM, 16GB RAM, Intel i7 13th gen laptop
- Local Jarvis target: Qwen2.5 14B Q4_K_M (70% strength, ~15 tok/s) and 32B Q4_K_M with RAM offload (80% strength)
- Hybrid option: local + API Opus 5.5 / GPT-5 for 95% strength when stuck

## Main Projects — High-Level Truth Only
**Rule: MEMORY.md = current high-level truth. GitHub = source of detailed project context. If you need detailed context, inspect GitHub repositories, don't expand MEMORY.md.**

### CASMI2026 — Active Kaggle
- Enveda CASMI 2026 Molecule ID from Mass Spectra
- Team: kobiljonn, beginner level, doing for learning
- Status: Full scaffold E00-E08 built in /home/user/CASMI2026 (35 files), no real data yet
- Key: 2.5M spectra, 275k structures, hidden test 400 molecules timsTOF, metric MRR@25 by InChIKey14 RDKit 2026.03.3, final 9h offline
- Repository/project files contain detailed workflow and implementation — check there before assumptions

### BirOvoz / Central-Asian Voice Benchmark
- Active AI voice research project
- Focus: Uzbek/Kazakh voice systems, benchmarking, local voice cloning and Route B integration
- Repository contains current implementation and technical history
- When detailed context needed, inspect GitHub repository rather than expanding MEMORY.md

### Prepl
- AI interview coach product
- Stack: Next.js / React / Tailwind
- GitHub repository contains implementation and current state
- Check repository for detailed technical context

### LocalJarvis — Bradley Edition
- Path: /home/user/LocalJarvis
- Stack: Ollama + Open WebUI :3000 + Chroma :8001 + OpenHands :3001
- Tools: ask_bradley.py — auto web search + ask cloud when local stuck (confidence <0.4 or 2 errors)
- Goal: middle ground — chatty friend + coder-orchestrator

## What's Active Now
- CASMI2026 pipeline ready for E00 audit
- LocalJarvis docker-compose ready for RTX 4060 deployment, hybrid 2-3 liked
- Memory system: MEMORY.md (high-level) + GitHub repos (detailed) + Chroma RAG

## Key Preferences
- Don't agree with everything, say directly if idea is bad
- Do max quality, don't rush
- Talk as friend when user wants, not just push to work
- Keep MEMORY.md 2-4K tokens max, don't turn into dump — use GitHub for details
- No secrets in MEMORY.md (no API keys, no Kaggle tokens) — use .env
- Language: Russian informal "бро" primary, English tech terms ok

## GitHub Integration Rule
- If you need context on my projects, check my GitHub repositories first
- GitHub may contain old code, abandoned branches, experimental files — MEMORY.md is current truth
- Example prompt for tool: "Inspect GitHub repo <user>/<repo> for current implementation before answering about <project>"

## Current Workspace
- /home/user/CASMI2026, /home/user/LocalJarvis, /home/user/MEMORY.md
- 269K / 128MB, 43 files, cleaned
- LocalJarvis has MEMORY_MERGE_PROMPT.md for mixing memories

## Links / Repos (add your GitHub usernames)
- GitHub: [add your username]
- CASMI2026 repo: [add link if public]
- BirOvoz repo: [add link]
- Prepl repo: [add link]
