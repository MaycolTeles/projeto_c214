"""
TODO
"""

from abc import ABC, abstractmethod

from src.domain.documents.comprovante_residencia import ComprovanteResidencia


class ComprovanteResidenciaRepository(ABC):

    @abstractmethod
    def create(self, comprovante_residencia: ComprovanteResidencia):
        """
        TODO
        """
