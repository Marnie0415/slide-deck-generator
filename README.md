# Slide Deck Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.txt)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-D97757)](SKILL.md)
[![Codex](https://img.shields.io/badge/Codex-Skill-000000)](SKILL.md)
[![Version](https://img.shields.io/badge/Version-1.1.0-blue)]()

> Convert notes, text, and code into structured presentation slide decks.

## What it does

Takes markdown notes, technical outlines, or code walkthroughs and generates a complete slide deck with titles, content bullets, code slides, and speaker notes. Output is structured JSON ready for any presentation tool.

## Why this exists

Creating slides from scratch is time-consuming. Most people spend more time on formatting than content. This skill generates the structure instantly — you get the right number of slides, proper flow, and speaker notes for every slide. Focus on your message, not the tool.

## Prerequisites

- Claude Code, Codex, or any LLM agent that supports SKILL.md
- Git (to clone the repository)
- Python 3.8+ (for PPTX generation)
- `pip install python-pptx` (for PPTX generation)

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/Marnie0415/slide-deck-generator.git
```

### Step 2: Copy to your skills directory

**macOS / Linux:**

```bash
# For Claude Code
cp -r slide-deck-generator ~/.claude/skills/

# For Codex
cp -r slide-deck-generator ~/.codex/skills/
```

**Windows (PowerShell):**

```powershell
# For Claude Code
Copy-Item -Path "slide-deck-generator" -Destination "$env:USERPROFILE\.claude\skills\slide-deck-generator" -Recurse

# For Codex
Copy-Item -Path "slide-deck-generator" -Destination "$env:USERPROFILE\.codex\skills\slide-deck-generator" -Recurse
```

### Step 3: Restart your agent

Restart Claude Code or Codex to pick up the new skill.

## Usage

In Claude Code or Codex, simply ask:

```text
Generate slides from my notes
```

The agent will automatically detect and use this skill.

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
