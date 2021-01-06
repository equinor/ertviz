import dash
import dash_html_components as html
import dash_core_components as dcc
import ertviz.assets as assets
import webviz_core_components as wcc


def paralell_coordinates_view(parent):
    return [
        html.H5("Parameters in parallel coordinates"),
        html.Div(
            className="ert-dropdown-container",
            children=[
                wcc.Select(
                    id=parent.uuid("parameter-selector-multi"),
                    multi=True,
                    size=10,
                    # style={
                    #     # "width": "700px",
                    #     "fontSize": "8pt",
                    # },
                    persistence=True,
                    persistence_type="session",
                    className="ert-dropdown",
                ),
            ],
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Label("ParCoor:"),
                    ],
                    className="ert-graph-options",
                ),
                dcc.Graph(
                    id={
                        "id": parent.uuid("paralell-coor"),
                        "type": parent.uuid("graph"),
                    },
                    className="ert-graph",
                    config={"responsive": True},
                ),
            ],
            className="ert-graph-container",
        ),
    ]
