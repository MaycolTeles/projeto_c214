"""
TODO
"""

from abc import ABC, abstractmethod

from src.domain.documents.rg import RG


class RGRepository(ABC):

    @abstractmethod
    def create(self, comprovante_residencia: RG):
        """
        TODO
        """
