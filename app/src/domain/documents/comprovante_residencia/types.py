"""
Class containing the "ComprovanteDeResidenciaType" Enum.
"""

from enum import Enum


class ComprovanteResidenciaType(Enum):
    """
    Enum containing all the available types for a "ComprovanteDeResidencia".
    Types are listed below:

    * AGUA = "agua"
    * LUZ = "luz"
    * TELEFONE = "telefone"
    * INTERNET = "internet"
    """
    AGUA = "agua"
    LUZ = "luz"
    TELEFONE = "telefone"
    INTERNET = "internet"
