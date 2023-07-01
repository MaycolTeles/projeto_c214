"""
Module containing the RGRequest class.
"""

from typing import Any
from dataclasses import dataclass

from src.domain.interfaces import RequestModel


@dataclass
class RGRequest(RequestModel):
    """
    TODO
    """
    values: dict[str, Any]
