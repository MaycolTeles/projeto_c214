"""TODO"""

import os

import dotenv


dotenv.load_dotenv()


REPOSITORY = os.getenv("REPOSITORY", "inmemo")
