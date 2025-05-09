.PHONY: build run clean static

build:
	python -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

run:
	. .venv/bin/activate && reflex run

static: build
	. .venv/bin/activate && reflex export --frontend-only
	rm -rf public/
	mkdir -p public/
	unzip -o frontend.zip -d public/
	rm frontend.zip
	echo "Static site generated in the public/ directory"

clean:
	rm -rf .venv/
	rm -rf .states/
	rm -rf .web/
	rm -rf public/
	find . -name "__pycache__" -type d -exec rm -rf {} +
