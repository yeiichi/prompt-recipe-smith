Quickstart
==========

Command line
------------

Run the CLI with a rough idea. The command asks up to three clarification
questions, then prints a final prompt you can paste into a chat agent.

.. code-block:: bash

   prompt-recipe-smith I want to plan a small workshop

One-shot builder
----------------

Use ``PromptBuilder`` when you already have enough context to build a prompt in
one step.

.. code-block:: python

   from prompt_recipe_smith import PromptBuilder
   from prompt_recipe_smith.output import to_json, to_plain_text
   from prompt_recipe_smith.recipes import clarify_idea_recipe

   recipe = clarify_idea_recipe()
   result = PromptBuilder().build(
       recipe,
       "I want to write a polite follow-up email",
   )

   print(to_plain_text(result))
   print(to_json(result))

Layered questions
-----------------

Use ``PromptSessionRunner`` when your app should collect the built-in
clarification answers before rendering the final prompt.

.. code-block:: python

   from prompt_recipe_smith import PromptBuilder
   from prompt_recipe_smith.recipes import clarify_idea_recipe
   from prompt_recipe_smith.session import PromptSessionRunner

   runner = PromptSessionRunner(
       recipe=clarify_idea_recipe(),
       builder=PromptBuilder(),
   )
   session = runner.start("I want to plan a small workshop")

   session = runner.answer(session, "A one-day facilitation agenda")
   session = runner.answer(session, "First-time team leads")
   session = runner.answer(session, "Keep it practical and under six hours")

   result = runner.finish(session)
   print(result.prompt)

The built-in clarification questions are written in English, but answers can be
provided in any language. The CLI, API, and JSON output preserve Unicode text.

Colab notebook
--------------

Open the `prompt-recipe-smith Colab notebook <https://colab.research.google.com/github/yeiichi/prompt-recipe-smith/blob/main/examples/prompt_recipe_smith_colab_demo.ipynb>`_
to try the same flow in a browser without setting up a local environment.
