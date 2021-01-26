import dash
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
from ertviz.models import (
    load_ensemble,
    ParallelCoordinates,
)


def parameter_comparison_controller(parent, app):
    @app.callback(
        [
            Output(
                {"id": parent.uuid("parallel-coor"), "type": parent.uuid("graph")},
                "figure",
            ),
            Output(parent.uuid("parameter-selector-dropdown"), "value"),
        ],
        [
            Input(parent.uuid("parameter-selector-multi"), "value"),
            Input(parent.uuid("parameter-selector-multi"), "options"),
        ],
        [
            State(parent.uuid("ensemble-selection-store"), "data"),
            State(parent.uuid("parameter-selector-dropdown"), "value"),
        ],
    )
    def _update_parallel_coor(
        parameters, parameter_options, selected_ensembles, parameters_dropdown
    ):
        if not selected_ensembles:
            raise PreventUpdate

        data = {}
        colors = {}
        ctx = dash.callback_context
        triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]

        if triggered_id == parent.uuid("parameter-selector-dropdown"):
            datas = elements
        # if no parameters selected take up to the first 5 by default
        if not bool(parameters):
            parameters = [option["value"] for option in parameter_options][:5]
        for idx, (ensemble_id, color) in enumerate(selected_ensembles.items()):
            ensemble = load_ensemble(parent, ensemble_id)
            ens_key = str(ensemble)
            df = ensemble.parameters_df(parameters)
            df["ensemble_id"] = idx
            data[ens_key] = df.copy()
            colors[ens_key] = color["color"]
        parent.parallel_plot = ParallelCoordinates(data, colors)
        return parent.parallel_plot.repr, parameters
