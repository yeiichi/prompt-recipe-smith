from __future__ import annotations

from prompt_recipe_smith.models import PromptBranch, PromptRecipe, PromptTemplate


def clarify_idea_recipe() -> PromptRecipe:
    return PromptRecipe(
        name="clarify-idea",
        description="Turn a vague idea into a clearer ChatGPT prompt.",
        steps=(
            "Restate the user's rough idea.",
            "Ask for the missing context only if it matters.",
            "Produce a practical prompt the user can paste into chat.",
        ),
        branches=(
            PromptBranch(
                name="writing",
                description="Help with writing or editing tasks.",
                keyword="write",
                template=PromptTemplate(
                    "Help me turn this writing idea into a clear request:\n"
                    "{user_input}\n\n"
                    "Ask up to three plain-language clarification questions, "
                    "then draft an improved prompt."
                ),
            ),
            PromptBranch(
                name="learning",
                description="Help with learning or explanation tasks.",
                keyword="learn",
                template=PromptTemplate(
                    "I want to learn about this topic:\n"
                    "{user_input}\n\n"
                    "Create a beginner-friendly prompt that asks for a simple "
                    "explanation, examples, and next steps."
                ),
            ),
            PromptBranch(
                name="planning",
                description="Help with planning a task or project.",
                keyword="plan",
                template=PromptTemplate(
                    "Help me plan this:\n"
                    "{user_input}\n\n"
                    "Create a prompt that asks for goals, constraints, steps, "
                    "and likely risks."
                ),
            ),
        ),
        final_template=PromptTemplate(
            "Turn this rough idea into an effective ChatGPT prompt:\n"
            "{user_input}\n\n"
            "Use simple language. Identify the goal, needed context, output "
            "format, and any assumptions."
        ),
        examples=("I want to write an email but I do not know how to start.",),
    )
