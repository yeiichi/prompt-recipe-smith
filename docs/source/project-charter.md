# Project Charter

`prompt-recipe-smith` helps users convert vague ideas into effective chat prompts.

The project favors simple language, understandable flows, and small typed
building blocks. The core package should remain independent of web frameworks
and external LLM APIs.

Initial goals:

- Provide a reusable `PromptRecipe` concept.
- Support ChatGPT-oriented prompt formatting first.
- Export plain text and JSON results.
- Keep the package PyPI-ready with tests, typing, linting, and semantic release.
