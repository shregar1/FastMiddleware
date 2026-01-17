.PHONY: help install dev test lint type-check format build clean publish

help:
	@echo "FastMVC Middleware - Development Commands"
	@echo ""
	@echo "Usage: make [command]"
	@echo ""
	@echo "Commands:"
	@echo "  install      Install package in development mode"
	@echo "  dev          Install with development dependencies"
	@echo "  test         Run tests with coverage"
	@echo "  lint         Run linter (ruff)"
	@echo "  type-check   Run type checker (mypy)"
	@echo "  format       Format code with ruff"
	@echo "  build        Build package for distribution"
	@echo "  clean        Remove build artifacts"
	@echo "  publish      Publish to PyPI (requires credentials)"

install:
	pip install -e .

dev:
	pip install -e ".[dev]"

test:
	pytest --cov=fastmvc_middleware --cov-report=term-missing --cov-report=html

lint:
	ruff check .

type-check:
	mypy fastmvc_middleware

format:
	ruff format .
	ruff check --fix .

build: clean
	python -m build

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +

publish: build
	twine upload dist/*

