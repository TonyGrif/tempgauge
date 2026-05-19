"""This module contains the Core class that is responsible for storing and analyzing
CPU Core data.

Example Usage:
.. code-block:: python
    from tempgauge import Core

    core = Core(CORE_NUMBER)
    core.add_reading((TIME, TEMPERATURE))
    print(core)
    core.write_to_file()
"""

from .core import Core
from .parse_temps import parse_raw_temps

__all__ = [
    "Core",
    "parse_raw_temps",
]
