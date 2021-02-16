import dash_html_components as html
import dash_core_components as dcc
import webviz_core_components as wcc
import dash_bootstrap_components as dbc


def parameter_selector_view(parent, data_type="parameter", suffix=""):
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.Label(
                            "Search (Press ENTER to select all matches):",
                            className="ert-label",
                        ),
                        align="left",
                        width="auto",
                    ),
                    dbc.Col(
                        dcc.Input(
                            id=parent.uuid(f"parameter-selector-filter-{suffix}"),
                            type="search",
                            placeholder="Substring...",
                            persistence="session",
                        ),
                        align="left",
                    ),
                    dbc.Col(
                        html.Button(
                            id=parent.uuid(f"parameter-selector-button-{suffix}"),
                            children=("Toggle selector visibility"),
                        ),
                        align="right",
                    ),
                ],
            ),
            html.Div(
                wcc.Select(
                    id=parent.uuid(f"parameter-selector-multi-{suffix}"),
                    multi=True,
                    size=10,
                    persistence="session",
                ),
                id=parent.uuid(f"container-parameter-selector-multi-{suffix}"),
                className="ert-parameter-selector-container-show",
            ),
            dcc.Dropdown(
                id=parent.uuid(f"parameter-deactivator-{suffix}"),
                multi=True,
                persistence="session",
            ),
            dcc.Store(
                id=parent.uuid(f"parameter-selection-store-{suffix}"),
                storage_type="session",
            ),
            dcc.Store(
                id=parent.uuid(f"parameter-type-store-{suffix}"),
                storage_type="session",
                data=data_type,
            ),
        ],
    )
