"""
Module containing the "DesktopController" Class.
"""

from src.application.adapters.presenters.desktop import DesktopPresenter


class DesktopController:
    """
    TODO
    """
    _presenter: DesktopPresenter

    def __init__(self) -> None:
        """
        TODO
        """
        self._presenter = DesktopPresenter()
