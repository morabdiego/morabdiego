.PHONY: install run export clean

install:
	uv sync

run:
	uv run reflex run --frontend-only

export:
	uv run reflex export --frontend-only --no-zip

clean:
	rm -rf .states/ .web/ frontend.zip
	find . -name "__pycache__" -type d -exec rm -rf {} +
