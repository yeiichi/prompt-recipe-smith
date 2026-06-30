class PromptRecipeSmithError(Exception):
    """Base exception for prompt-recipe-smith errors."""


class TooManyBranchesError(PromptRecipeSmithError):
    """Raised when a recipe defines more than three branches."""
