from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
from ertviz.models import (
    load_ensemble,
    ParalellCoordinates,
)


def parameter_comparison_controller(parent, app):
    @app.callback(
        Output(
            {"id": parent.uuid("paralell-coor"), "type": parent.uuid("graph")},
            "figure",
        ),
        [
            Input(parent.uuid("parameter-selector-multi"), "value"),
        ],
        [State(parent.uuid("ensemble-selection-store"), "data")],
    )
    def _update_paralell_coor(parameters, selected_ensembles):
        if not selected_ensembles:
            raise PreventUpdate

        data = {}
        colors = []
        for idx, (ensemble_id, color) in enumerate(selected_ensembles.items()):
            ensemble = load_ensemble(parent, ensemble_id)
            ens_key = str(ensemble)
            df = ensemble.parameters_df(parameters)
            df["ensemble_id"] = idx
            data[ens_key] = df.copy()
            colors.append([idx / len(selected_ensembles), color["color"]])
            colors.append([(idx + 1) / len(selected_ensembles), color["color"]])
        parent.parallel_plot = ParalellCoordinates(data, colors)
        return parent.parallel_plot.repr
