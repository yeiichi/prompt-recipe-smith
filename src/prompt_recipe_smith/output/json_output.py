from __future__ import annotations

import json

from prompt_recipe_smith.models import PromptResult


def to_json(result: PromptResult) -> str:
    return json.dumps(result.to_dict(), ensure_ascii=False, indent=2)
