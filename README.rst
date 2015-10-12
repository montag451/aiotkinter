This module provide an asyncio API for the the Tkinter event loop

License: MIT (see LICENSE)

Requirements
============

-  Unix platform (it doesn't work on Windows because of the lack of
   **Tcl\_CreateFileHandler** on this platform)
-  Python 3.3 + asyncio or Python >= 3.4

Installation
============

.. code:: sh

    python setup.py install

Usage
=====

**aiotkinter** expose an event loop policy (which based on the default
event loop policy of **asyncio**) so the only thing you have to do is to
set the global event loop policy with an instance of
**TkinterEventLoopPolicy**:

.. code:: python

    import asyncio
    import aiotkinter

    asyncio.set_event_loop_policy(aiotkinter.TkinterEventLoopPolicy())
    loop = asyncio.get_event_loop()
    loop.run_forever()
