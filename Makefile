.PHONY: help install dev test lint type-check format build clean publish publish-test check

help:
	@echo "FastMVC Middleware - Development Commands"
	@echo ""
	@echo "Usage: make [command]"
	@echo ""
	@echo "Commands:"
	@echo "  install       Install package in development mode"
	@echo "  dev           Install with development dependencies"
	@echo "  test          Run tests with coverage"
	@echo "  lint          Run linter (ruff)"
	@echo "  type-check    Run type checker (mypy)"
	@echo "  format        Format code with ruff"
	@echo "  build         Build package for distribution"
	@echo "  check         Check package before publishing"
	@echo "  clean         Remove build artifacts"
	@echo "  publish-test  Publish to TestPyPI"
	@echo "  publish       Publish to PyPI (requires credentials)"

install:
	pip install -e .

dev:
	pip install -e ".[dev]"

test:
	pytest --cov=fastMiddleware --cov-report=term-missing --cov-report=html

lint:
	ruff check fastMiddleware tests

type-check:
	mypy fastMiddleware

format:
	ruff format fastMiddleware tests
	ruff check --fix fastMiddleware tests

build: clean
	python -m build

check: build
	twine check dist/*

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
	find . -type d -name "*.egg-info" -exec rm -rf {} +

publish-test: build
	twine upload --repository testpypi dist/*

publish: check
	twine upload dist/*
