# Slide Deck Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.txt)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-D97757)](SKILL.md)
[![Codex](https://img.shields.io/badge/Codex-Skill-000000)](SKILL.md)
[![Version](https://img.shields.io/badge/Version-1.0.0-blue)]()

> Convert notes, text, and code into structured presentation slide decks.

## What it does

Takes markdown notes, technical outlines, or code walkthroughs and generates a complete slide deck with titles, content bullets, code slides, and speaker notes. Output is structured JSON ready for any presentation tool.

## Why this exists

Creating slides from scratch is time-consuming. Most people spend more time on formatting than content. This skill generates the structure instantly — you get the right number of slides, proper flow, and speaker notes for every slide. Focus on your message, not the tool.

## Quick start

```text
# In Claude Code or Codex
Use the slide-deck-generator skill
```

```bash
cp -r slide-deck-generator ~/.claude/skills/
```

## What you get

| Input | Output |
|-------|--------|
| Markdown outline | 10-15 slide JSON deck with speaker notes |
| Technical notes | Slide deck with code slides + explanations |
| Meeting summary | Presentation with agenda, content, summary |
| Feature list | Pitch deck with problem, solution, demo flow |

## Slide types

- **Title** — Opening slide
- **Section** — Topic divider
- **Content** — Bullet points (max 5 per slide)
- **Code** — Code block with annotation
- **Chart** — Data description
- **Closing** — Summary + call to action

## Output format

```json
[
  {"type": "title", "title": "My Presentation", "content": [], "speaker_notes": "..."},
  {"type": "content", "title": "Key Point", "content": ["Bullet 1", "Bullet 2"], "speaker_notes": "..."}
]
```

## Acknowledgments

README structure inspired by [sovereign-skills](https://github.com/AlexZio00/sovereign-skills), [claude-code-skills](https://github.com/levnikolaevich/claude-code-skills), and [html-to-editable-pptx](https://github.com/Hasasasa/html-to-editable-pptx). All referenced projects are MIT licensed.

## License

MIT
