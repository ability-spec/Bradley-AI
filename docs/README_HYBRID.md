# Как сделать чтобы локальный тупил -> сам гуглил -> спрашивал Bradley

Да, бро, можно и это как раз то что делает из простого чата — оркестратор как я.

### Схема которую ты хочешь:

```
[Твой ноут RTX 4060]
   Qwen 14B (локально, бесплатно, 80% задач)
       |
       | confidence < 0.4 или 2 ошибки подряд
       v
   [ask_bradley_when_stuck тул]
       |
       +---> web_search (DuckDuckGo) — гуглит доку по RDKit/DreaMS
       |
       +---> ask_bradley_cloud — спрашивает меня через API
                |
                +---> если есть ANTHROPIC_API_KEY -> спрашивает Opus 5.5 (95% как я)
                +---> если нет -> fallback с гуглом + локальным Qwen
```

### Что я тебе уже собрал:

В `tools/ask_bradley.py` — готовый тул:
- `web_search()` — гуглит через DuckDuckGo
- `ask_bradley_cloud()` — спрашивает облачного меня через Anthropic/OpenAI API
- `should_ask_bradley()` — логика когда звать (если confidence низкий, ошибки, или химия сложная)

В `tools/openhands_tool.py` — обертка для OpenHands чтобы он сам вызывал когда тупит.

### Как подключить в твой LocalJarvis:

1. В `docker-compose.yml` уже есть `ANTHROPIC_API_KEY` и `OPENAI_API_KEY` из `.env` — вставь туда ключ если хочешь 95% силы.

2. В Open WebUI:
   - Settings -> Tools -> Add Tool -> вставь код из `tools/openhands_tool.py`
   - Теперь когда Qwen тупит, в чате появится кнопка "Ask Bradley"

3. В OpenHands:
   - В `config.toml` добавь:
```toml
[tools]
ask_bradley_when_stuck = { module = "tools.openhands_tool", function = "ask_bradley_when_stuck" }
```

### Пример как это работает на CASMI:

Локальный Qwen пытается посчитать InChIKey14:
```
Qwen: пробую MolToInchiKey... ошибка, не знаю про таутомеры
Qwen: confidence 0.3, error_count 2 -> вызываю ask_bradley_when_stuck
Tool: гуглю "RDKit 2026.03.3 tautomer canonicalization InChIKey14"
Tool: спрашиваю Bradley: "Как правильно каноникализировать таутомеры для CASMI?"
Bradley (я в облаке): "Используй rdMolStandardize.TautomerEnumerator().Canonicalize(mol), не делай salt removal, вот код..."
Qwen: а, понял, применяю код от Bradley
```

Итого: 80% задач — локально бесплатно на 4060, 20% сложных — спрашивает меня, гуглит, и решает.

Хочешь я еще добавлю голосовой триггер — скажешь "Брадли, помогай" и он сам меня зовет?
