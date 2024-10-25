"""This module contains the Core class that is responsible for storing and analyzing
CPU Core data.

Example Usage:
.. code-block:: python
    from temps import Core

    core = Core(CORE_NUMBER)
    core.add_reading((TIME, TEMPERATURE))
    print(core)
    core.write_to_file()
"""

from .core import Core

__all__ = [
    "Core",
]
