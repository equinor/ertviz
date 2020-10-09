import dash_html_components as html
import dash_core_components as dcc
from webviz_config import WebvizPluginABC

from ertviz.views import response_view, parameter_view
from ertviz.controllers import (
    response_controller,
    parameter_controller,
    link_and_brush_controller,
)


class Ensemble(WebvizPluginABC):
    def __init__(self, app):
        super().__init__()
        self.id = "Ensemble"
        self.ensemble_plot = None
        self.parameter_plot = None
        self.set_callbacks(app)

    @property
    def layout(self):
        return html.Div(
            [
                html.Div(
                    id="ensemble-content",
                    children=response_view(parent=self) + parameter_view(parent=self),
                ),
                html.Div(
                    [
                        dcc.Store(id=self.uuid("selection-store")),
                    ]
                ),
            ]
        )

    def set_callbacks(self, app):
        response_controller(self, app)
        parameter_controller(self, app)
        link_and_brush_controller(self, app)
