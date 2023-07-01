"""
Module containing the CPFResponse class.
"""

from typing import Any
from dataclasses import dataclass

from src.domain.interfaces import ResponseModel


@dataclass
class CPFResponse(ResponseModel):
    """
    Class containing the request model for the CPFResponse class.
    """
    success: bool
    response: dict[str, Any]
