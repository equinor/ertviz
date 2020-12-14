import dash_html_components as html
import dash_core_components as dcc
from .paremeter_view import parameter_view
from .ensemble_selector_view import ensemble_selector_view


def response_view(parent, index=0):
    return [
        html.H5("Response plots"),
        html.Div(
            className="ert-dropdown-container",
            children=[
                html.Label("Response", className="ert-label"),
                dcc.Dropdown(
                    id={"index": index, "type": parent.uuid("response-selector")},
                    className="ert-dropdown",
                ),
            ],
        ),
        html.Div(
            [
                html.Div(
                    className="ert-graph-options",
                    children=[
                        html.Label("Graph Type:"),
                        dcc.RadioItems(
                            options=[
                                {"label": key, "value": key}
                                for key in ["Function plot", "Statistics"]
                            ],
                            value="Function plot",
                            id={"index": index, "type": parent.uuid("plot-type")},
                        ),
                    ],
                ),
                dcc.Graph(
                    id={
                        "index": index,
                        "id": parent.uuid("response-graphic"),
                        "type": parent.uuid("graph"),
                    },
                    config={"responsive": True},
                    className="ert-graph",
                ),
            ],
            className="ert-graph-container",
        ),
    ]


def response_obs_view(parent):
    return [
        html.H5("Observation/Misfits plots"),
        html.Div(
            className="ert-dropdown-container",
            children=[
                html.Label("Response", className="ert-label"),
                dcc.Dropdown(
                    id=parent.uuid("response-selector"),
                    className="ert-dropdown",
                ),
            ],
        ),
        html.Div(
            [
                html.Div(
                    className="ert-graph-options",
                    children=[
                        html.Label("Y-axis type:"),
                        dcc.RadioItems(
                            options=[
                                {"label": key, "value": key}
                                for key in ["linear", "log"]
                            ],
                            value="linear",
                            id=parent.uuid("yaxis-type"),
                        ),
                        html.Label("Misfits Type:"),
                        dcc.RadioItems(
                            options=[
                                {"label": key, "value": key}
                                for key in ["Univariate", "Summary"]
                            ],
                            value="Univariate",
                            id=parent.uuid("misfits-type"),
                        ),
                    ],
                ),
                dcc.Graph(
                    id={
                        "id": parent.uuid("response-graphic"),
                        "type": parent.uuid("graph"),
                    },
                    className="ert-graph",
                ),
            ],
            className="ert-graph-container",
        ),
    ]