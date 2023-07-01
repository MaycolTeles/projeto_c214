"""
TODO
"""

import os

from dotenv import load_dotenv


load_dotenv()


UI_INJECTION = os.getenv("UI_INJECTION", "Flask")
