import dash
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State, MATCH
import plotly.graph_objects as go
from ertviz.models import EnsembleModel, MultiHistogramPlotModel, load_ensemble
import ertviz.assets as assets


def multi_parameter_controller(parent, app):
    @app.callback(
        Output({"index": MATCH, "type": parent.uuid("bincount-store")}, "data"),
        [Input({"index": MATCH, "type": parent.uuid("hist-bincount")}, "value")],
        [State({"index": MATCH, "type": parent.uuid("bincount-store")}, "data")],
    )
    def update_bincount(hist_bincount, store_bincount):
        if hist_bincount == store_bincount:
            raise PreventUpdate
        return hist_bincount

    @app.callback(
        [
            Output(
                {
                    "index": MATCH,
                    "id": parent.uuid("parameter-scatter"),
                    "type": parent.uuid("graph"),
                },
                "figure",
            ),
            Output({"index": MATCH, "type": parent.uuid("hist-bincount")}, "value"),
        ],
        [
            Input({"index": MATCH, "type": parent.uuid("hist-check")}, "value"),
            Input(
                {"index": MATCH, "type": parent.uuid("bincount-store")},
                "modified_timestamp",
            ),
            Input(parent.uuid("ensemble-selection-store"), "modified_timestamp"),
            Input(parent.uuid("param-label-check"), "value"),
        ],
        [
            State(parent.uuid("ensemble-selection-store"), "data"),
            State({"index": MATCH, "type": parent.uuid("parameter-id-store")}, "data"),
            State({"index": MATCH, "type": parent.uuid("bincount-store")}, "data"),
        ],
    )
    def update_histogram(
        hist_check_values, _, __, legend, selected_ensembles, parameter, bin_count
    ):
        if not selected_ensembles:
            raise PreventUpdate

        data = {}
        colors = {}
        names = {}
        priors = {}
        for ensemble_id, color in selected_ensembles.items():
            ensemble = load_ensemble(parent, ensemble_id)
            if parameter in ensemble.parameters:
                key = str(ensemble)
                parameter_model = ensemble.parameters[parameter]
                data[key] = parameter_model.data_df()
                colors[key] = color["color"]
                names[key] = repr(ensemble) if "label" in legend else ""

                if parameter_model.priors and "prior" in hist_check_values:
                    priors[names[key]] = (parameter_model.priors, colors[key])

        parent.parameter_plot = MultiHistogramPlotModel(
            data,
            names=names,
            colors=colors,
            hist="hist" in hist_check_values,
            kde="kde" in hist_check_values,
            priors=priors,
            bin_count=bin_count,
        )
        return parent.parameter_plot.repr, parent.parameter_plot.bin_count

    @app.callback(
        Output({"index": MATCH, "type": parent.uuid("hist-check")}, "options"),
        [
            Input({"index": MATCH, "type": parent.uuid("parameter-id-store")}, "data"),
        ],
        [
            State({"index": MATCH, "type": parent.uuid("hist-check")}, "options"),
            State(parent.uuid("ensemble-selection-store"), "data"),
        ],
    )
    def set_parameter_from_btn(parameter, plotting_options, selected_ensembles):
        has_priors = False
        for ensemble_id, _ in selected_ensembles.items():
            ensemble = load_ensemble(parent, ensemble_id)
            if parameter in ensemble.parameters:
                parameter_model = ensemble.parameters[parameter]
                if parameter_model.priors:
                    has_priors = True
                    break
        prior_option = {"label": "prior", "value": "prior"}
        if has_priors and prior_option not in plotting_options:
            plotting_options.append(prior_option)
        if not has_priors and prior_option in plotting_options:
            plotting_options.remove(prior_option)
        return plotting_options
