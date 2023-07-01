"""
Module containing the CPFRequest class.
"""

from typing import Any
from dataclasses import dataclass

from src.domain.interfaces import ResponseModel


@dataclass
class CPFRequest(ResponseModel):
    """
    Class containing the request model for the CPFRequest class.
    """
    values: dict[str, Any]
