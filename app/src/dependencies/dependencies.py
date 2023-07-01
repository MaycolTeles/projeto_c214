"""
TODO: FIX MODULE
"""

from .constants import UI_INJECTION
from src.application.infra.ui.interfaces import UI


def ui_factory() -> UI:
    """
    """
    from src.application.infra.ui.rest.web.flask_ui import FlaskUI
    from src.application.infra.ui.desktop.tkinter_ui import TkinterUI

    if UI_INJECTION == "Tkinter":
        return TkinterUI()
    
    if UI_INJECTION == "Flask":
        return FlaskUI()

    return FlaskUI()
