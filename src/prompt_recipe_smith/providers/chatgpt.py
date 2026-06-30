from __future__ import annotations

from prompt_recipe_smith.providers.base import PromptProvider


class ChatGPTProvider(PromptProvider):
    """Small ChatGPT-oriented prompt adapter."""

    name = "chatgpt"

    def adapt(self, prompt: str) -> str:
        return prompt.strip()
