# Contributing

## Adding Slide Types

Edit `scripts/generate_pptx.py` and add handling for new slide types.

## Testing

```bash
pip install python-pptx
# Create a test slides.json, then:
python scripts/generate_pptx.py test-slides.json output.pptx
```

## Pull Requests

1. Fork the repo
2. Create a branch
3. Make changes
4. Test PPTX output opens correctly
5. Submit PR

## License

MIT
