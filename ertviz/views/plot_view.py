import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from .selector_view import parameter_selector_view


def plot_view_header(parent):
    return [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Label("Responses", className="ert-label"),
                        parameter_selector_view(
                            parent, data_type="response", suffix="resp"
                        ),
                        dcc.Checklist(
                            id=parent.uuid("response-observations-check"),
                            options=[
                                {
                                    "label": "Show only responses with observations",
                                    "value": "obs",
                                },
                                {
                                    "label": "Remove all key-names ending with 'H' ( "
                                    "probably historical vectors )",
                                    "value": "historical",
                                },
                            ],
                            value=[],
                        ),
                    ],
                    width=6,
                ),
                dbc.Col(
                    [
                        html.Label("Parameters", className="ert-label"),
                        parameter_selector_view(
                            parent, data_type="parameter", suffix="param"
                        ),
                    ],
                    width=6,
                ),
            ]
        ),
        dcc.Store(id=parent.uuid("plot-selection-store"), storage_type="session"),
    ]


def plot_view_body(parent):
    return [
        html.Div(id=parent.uuid("plotting-content")),
        dcc.Store(id=parent.uuid("plotting-content-store"), storage_type="session"),
    ]
