---
slug: slide-deck-generator
name: slide-deck-generator
displayName: Slide Deck Generator
version: 1.2.0
summary: 把笔记、文本、代码变成演示文稿
description: "Use when the user wants to create slides or a presentation. Triggers on 'make slides', 'create presentation', 'turn this into slides'."
license: MIT
---

# Slide Deck Generator

Converts content into slide decks and generates actual PowerPoint files.

## When to use

- Create presentation slides
- Convert notes to deck
- Build pitch decks

## When NOT to use

- Creating video
- Designing visual layouts
- Building interactive demos

## Workflow (follow these exact steps)

### Step 1: Get the content

Ask user for content OR read their file:

```
read <file_path>
```

### Step 2: Create slide structure

Generate a JSON array. Each slide needs: type, title, content (array), speaker_notes.

Save the JSON:

```
write slides.json <json_content>
```

### Step 3: Generate PPTX

```
bash: pip install python-pptx
bash: python <skill_dir>/scripts/generate_pptx.py slides.json output.pptx
```

### Step 4: Deliver

Tell user: "PPTX saved to output.pptx. You can open it in PowerPoint or WPS."

## Error handling

- **No content**: Ask user for topic or paste notes
- **python-pptx not installed**: Output JSON + Markdown, tell user how to install
- **Script fails**: Output JSON directly, user can paste into any tool
