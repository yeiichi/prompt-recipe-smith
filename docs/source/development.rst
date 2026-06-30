Development
===========

Set up the local environment:

.. code-block:: bash

   uv sync

Run the main checks:

.. code-block:: bash

   uv run pytest
   uv run ruff check .
   uv run mypy src
   uv build

Build the documentation locally:

.. code-block:: bash

   uv run sphinx-build -b html docs/source docs/build/html

The project uses Python Semantic Release for versioning and release notes.
