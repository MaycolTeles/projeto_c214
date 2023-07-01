"""
Module containing the ComprovanteResidenciaRequest class.
"""

from typing import Any
from dataclasses import dataclass

from src.domain.interfaces import RequestModel


@dataclass
class ComprovanteResidenciaRequest(RequestModel):
    """
    TODO
    """
    values: dict[str, Any]
