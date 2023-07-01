"""
Module containing the ComprovanteResidenciaResponse class.
"""

from typing import Any
from dataclasses import dataclass

from src.domain.interfaces import ResponseModel


@dataclass
class ComprovanteResidenciaResponse(ResponseModel):
    """
    TODO
    """
    success: bool
    response: dict[str, Any]
