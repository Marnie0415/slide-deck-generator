#!/usr/bin/env python3
"""Tests for generate_pptx.py"""

import sys
import os
import json
import tempfile
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

def test_generate_pptx():
    try:
        from generate_pptx import generate_pptx
    except ImportError:
        print("python-pptx not installed, skipping")
        return

    slides = [
        {"type": "title", "title": "Test Deck", "content": [], "speaker_notes": "Opening"},
        {"type": "content", "title": "Key Point", "content": ["Bullet 1"], "speaker_notes": "Details"},
    ]
    with tempfile.NamedTemporaryFile(suffix='.pptx', delete=False) as f:
        name = f.name
    try:
        result = generate_pptx(slides, name)
        assert os.path.exists(result)
        assert os.path.getsize(result) > 0
    finally:
        os.unlink(name)

def test_json():
    slides = [{"type": "title", "title": "Test", "content": [], "speaker_notes": ""}]
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(slides, f)
        name = f.name
    try:
        with open(name, 'r') as rf:
            loaded = json.load(rf)
        assert len(loaded) == 1
    finally:
        os.unlink(name)

if __name__ == "__main__":
    test_generate_pptx()
    test_json()
    print("All tests passed!")
