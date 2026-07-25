---
slug: slide-deck-generator
name: slide-deck-generator
displayName: Slide Deck Generator
version: 1.3.0
summary: 把笔记、文本、代码变成演示文稿
description: "Use when the user wants to create slides or a presentation. Triggers on 'make slides', 'create presentation', 'turn this into slides'."
license: MIT
---

# Slide Deck Generator

Converts content into presentations with intelligent adaptation.

## When to use

- Create presentation slides
- Convert notes to deck
- Build pitch decks

## When NOT to use

- Creating video
- Designing visual layouts
- Building interactive demos

## Workflow

### Step 1: Detect content type and audience

Read the content and classify:

```
read <file_path>
```

Then ask the user:
- "Who is the audience?" (technical team / executives / students)
- "How long is the presentation?"
- "What style?" (formal / casual / tutorial)

Adapt based on answers:

| Audience | Style |
|----------|-------|
| Technical team | Code examples, architecture diagrams, detailed specs |
| Executives | High-level, metrics, business impact |
| Students | Step-by-step, examples, exercises |

### Step 2: Generate structure

Create JSON with slides tailored to the audience:

```
write slides.json <json_content>
```

### Step 3: Generate PPTX

```
bash: pip install python-pptx
bash: python <skill_dir>/scripts/generate_pptx.py slides.json output.pptx
```

### Step 4: Multi-turn iteration

After first draft, support refinement:

- User says "Add more detail to slide 3" → regenerate with more content
- User says "Make it shorter" → reduce to key points
- User says "Change style to formal" → adjust tone
- User says "Add a slide about X" → insert new slide
- User says "Remove the conclusion" → delete slide

Regenerate PPTX after each change:

```
bash: python <skill_dir>/scripts/generate_pptx.py slides.json output.pptx
```

### Step 5: Deliver

Tell user: "PPTX saved to output.pptx"

## Error handling

- **No content**: Ask for topic or paste notes
- **python-pptx not available**: Output JSON + Markdown
- **Script fails**: Output JSON directly
