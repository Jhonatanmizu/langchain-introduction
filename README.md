# LangChain Introduction

A hands-on learning repository for exploring and understanding LangChain framework.

## Overview

This repository is dedicated to learning LangChain, a framework for building applications powered by language models. It contains practical examples, experiments, and implementations of various LangChain concepts and features.

## Technologies & Dependencies

- **Python 3.14+**
- **Package Manager**: [uv](https://github.com/astral-sh/uv) - Fast Python package installer and resolver
- **Type Checking**: mypy with pydantic plugin

### Core Dependencies

- `langchain` - Core LangChain framework
- `langchain-openai` - OpenAI integrations (ChatOpenAI)
- `langchain-google-genai` - Google Generative AI integrations
- `python-dotenv` - Environment variable management
- `pypdf` - PDF processing capabilities
- `beautifulsoup4` - Web scraping and HTML parsing

## Project Structure

```
langchain-introduction/
├── main.py                    # Basic LangChain examples
├── fundamentals/
│   └── prompt-template.py    # Prompt template examples
├── pyproject.toml            # Project configuration and dependencies
└── README.md
```

## Getting Started

1. **Install uv** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Sync dependencies**:
   ```bash
   uv sync
   ```

3. **Activate virtual environment**:
   - Bash/Zsh: `source .venv/bin/activate`
   - Fish: `source .venv/bin/activate.fish`

4. **Run examples**:
   ```bash
   python main.py
   ```

## Type Checking

Run mypy to check type hints:
```bash
uv run mypy main.py
```

## Environment Variables

Create a `.env` file in the root directory with your API keys:
```
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_key
```

## License

This project is for educational purposes.
