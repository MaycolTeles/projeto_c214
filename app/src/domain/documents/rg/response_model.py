"""
Module containing the RGResponse class.
"""

from typing import Any
from dataclasses import dataclass

from src.domain.interfaces import ResponseModel


@dataclass
class RGResponse(ResponseModel):
    """
    TODO
    """
    success: bool
    response: dict[str, Any]
