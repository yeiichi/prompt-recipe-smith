from __future__ import annotations

from abc import ABC, abstractmethod


class PromptProvider(ABC):
    """Provider-specific prompt adapter."""

    name: str

    @abstractmethod
    def adapt(self, prompt: str) -> str:
        """Return a provider-oriented prompt string."""
