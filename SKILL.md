---
slug: slide-deck-generator
name: slide-deck-generator
displayName: Slide Deck Generator
version: 1.1.0
summary: 把笔记、文本、代码变成演示文稿
description: "Use when the user wants to create slides or a presentation. Triggers on 'make slides', 'create presentation', 'turn this into slides'."
license: MIT
---

# Slide Deck Generator

Converts content into structured slide decks and generates actual PowerPoint files using a bundled Python script.

## When to use

- Create presentation slides from notes
- Convert markdown to slide deck
- Build pitch decks

## When NOT to use

- Creating video content
- Designing visual layouts (colors, fonts)
- Building interactive demos

## Workflow

### Step 1: Understand the content

Use `read` tool to examine the input:

```
read <file_path>
```

Or work with the content the user pasted directly.

### Step 2: Generate slide structure

Create a JSON array of slides. Each slide has: type, title, content (array), speaker_notes.

```json
[
  {"type": "title", "title": "My Deck", "content": [], "speaker_notes": "Opening remarks"},
  {"type": "content", "title": "Key Point", "content": ["Bullet 1", "Bullet 2"], "speaker_notes": "Explain..."},
  {"type": "closing", "title": "Summary", "content": ["Takeaway 1"], "speaker_notes": "Wrap up"}
]
```

### Step 3: Save JSON

```bash
write slides.json <json_content>
```

### Step 4: Generate PPTX

```bash
pip install python-pptx
python <skill_dir>/scripts/generate_pptx.py slides.json output.pptx
```

### Step 5: Deliver

Tell the user the PPTX file is ready at the output path.

## Slide types

| Type | Use for |
|------|---------|
| title | Opening slide |
| section | Topic divider |
| content | Bullet points (max 5) |
| code | Code with annotation |
| closing | Summary + CTA |

## Output

- **JSON**: Structured slide definition (always generated)
- **PPTX**: Editable PowerPoint file (when python-pptx is installed)
- **Markdown**: Fallback slide list (when no Python available)

## Error handling

- **No content provided**: Ask user for the topic or paste their notes
- **Content too vague**: Generate a template deck with placeholders, ask for specifics
- **python-pptx not installed**: Output JSON + Markdown instead, tell user how to install
- **Script fails**: Output the JSON directly, user can paste into any presentation tool

## Known limitations

- No visual design (colors, fonts, images) — user styles the PPTX manually
- Chart slides are text descriptions only, not actual charts
- Speaker notes are brief — not full scripts
- Fixed slide layout (16:9)
