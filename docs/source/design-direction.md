# Design Direction

The prompt-building flow should stay small and explainable.

Recipes may branch, but the first design intentionally supports at most three
branches. This keeps user-facing decisions manageable and avoids turning recipes
into a full rules engine.

Plain text is the primary output. JSON is available for integrations. JSONL is
reserved for future batch-oriented workflows.

Provider support starts with ChatGPT-oriented formatting. Future providers such
as Gemini and Anthropic should fit behind the provider abstraction without
changing the core recipe model.

Django support should remain optional and outside the core package.
