"""
Logger Config Template
Ensures unified logging across modules.
"""

import logging

def configure_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(asctime)s — %(name)s: %(message)s"
    )
