"""
TODO
"""

from .contants import REPOSITORY
from src.application.infra.repositories import InMemoRepository
from src.application.infra.repositories import MySQLRepository


repository = InMemoRepository()

if REPOSITORY == "inmemo":
    repository = InMemoRepository()

elif REPOSITORY == "mysql":
    repository = MySQLRepository()


def get_repository():
    """
    Function to get the repository.
    """
    return repository
