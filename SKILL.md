---
name: slide-deck-generator
version: "1.0.0"
description: "Use when the user wants to create slides, generate a presentation, turn notes into a deck, or build pitch materials. Triggers on 'make slides', 'create a presentation', 'turn this into slides', 'generate a deck', 'build a pitch deck', or when the user uploads content and wants presentation output."
---

# Slide Deck Generator

Converts markdown notes, text content, and code into structured, export-ready presentation slide decks.

## When to use

- Create presentation slides from notes or outlines
- Convert markdown content into slide format
- Generate code walkthrough presentations
- Build pitch decks or proposal decks

## When NOT to use

- Creating actual PowerPoint/PPTX files (this generates structure, not files)
- Designing visual layouts or choosing color schemes
- Generating speaker scripts or full narration text
- Creating video content or animations
- Building interactive demos or live presentations

## Workflow

1. Parse the input to identify topics, key points, and structure.
2. Map content to slide types.
3. Generate slide sequence following the deck flow.
4. Add speaker notes for each slide.
5. Output as JSON array or Markdown slide list.

## Slide types

1. **Title Slide**: Title + subtitle + date
2. **Section Divider**: Topic transition with section number
3. **Content Slide**: Heading + 3 to 5 bullet points
4. **Code Slide**: Heading + code block with annotation
5. **Chart Slide**: Heading + data description
6. **Closing Slide**: Summary + call to action + contact

## Deck flow

Always follow this sequence:
- Title slide
- Agenda / overview (3 to 5 items)
- Content sections (3 to 7 slides each)
- Summary slide
- Q&A or next steps slide

## Style rules

- One idea per slide. If you need two ideas, use two slides.
- Bullet points: max 5 per slide, max 8 words per bullet.
- No paragraphs on slides. Prose goes in speaker notes.
- Headings are verbs or questions, not nouns. "Reduce latency" not "Latency reduction."
- Code slides: max 15 lines. Highlight the key lines.
- Transitions: each slide should answer "why am I seeing this now?"

## Handling different inputs

- **Markdown**: Parse headings as slide titles, bullets as content.
- **Prose**: Extract key points, group into logical slides.
- **Code**: Create a code slide + explanation slide pair.
- **Thin source**: Generate a template deck with placeholder sections and ask for more detail.

## Error handling

- **Input too short** (under 20 words): Ask for more content or specify the topic.
- **No clear structure**: Generate a generic template and ask user to fill in sections.
- **Too many topics** (more than 7): Ask user to pick top 3-5, or split into multiple decks.
- **Code-only input**: Create code walkthrough deck with explanation slides between code slides.
- **Non-technical content**: Adapt slide types (remove code slides, add more content slides).

## Examples

### Example 1: Meeting notes to pitch deck
Input: Notes from a product planning meeting with 5 feature ideas
Output: 12-slide deck with title, problem, solution, features, timeline, team, ask.

### Example 2: Markdown outline to tutorial deck
Input: Markdown with 3 sections about Docker basics
Output: 15-slide deck with title, agenda, 3 sections (4 slides each), summary, Q&A.

### Example 3: Code to walkthrough deck
Input: A Python class with 3 methods
Output: 8-slide deck with title, overview, method explanations, usage example, summary.

## Known limitations

- Does not generate actual PPTX/PPT files — output is structured data only
- No visual design, themes, or styling applied
- Cannot include images or embedded media
- Chart slides are descriptive only (no actual charts generated)
- Speaker notes are brief — not full scripts

## Output format

JSON array of slide objects:
```json
[
  {"type": "title", "title": "Presentation", "content": [], "speaker_notes": ""},
  {"type": "content", "title": "Section 1", "content": ["Point 1", "Point 2"], "speaker_notes": "Context..."}
]
```

Also supports Markdown slide list format for quick sharing.
