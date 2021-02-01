import dash_html_components as html
import dash_core_components as dcc
import dash_cytoscape as cyto
import ertviz.assets as assets


cyto.load_extra_layouts()


def ensemble_selector_view(parent):
    return [
        html.Div(
            [
                cyto.Cytoscape(
                    id=parent.uuid("ensemble-selector"),
                    layout={"name": "grid"},
                    className="ert-ensemble-selector-large",
                    stylesheet=assets.ERTSTYLE["ensemble-selector"]["stylesheet"],
                    responsive=False,
                ),
                html.Button(
                    id=parent.uuid("ensemble-selector-button"),
                    className="ert-ensemble-selector-view-toggle",
                    children=("Minimize"),
                ),
            ],
            id=parent.uuid("ensemble-selector-container"),
            className="ert-ensemble-selector-container-large",
        ),
        dcc.Store(id=parent.uuid("ensemble-selection-store"), storage_type="session"),
        dcc.Store(
            id=parent.uuid("ensemble-view-store"), storage_type="session", data=True
        ),
    ]
