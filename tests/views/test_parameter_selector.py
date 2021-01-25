import dash
import ertviz
from unittest import mock
from ertviz.plugins._parameter_comparison import ParameterComparison
from tests.conftest import (
    mocked_requests_get,
    mocked_read_csv,
    mocked_get_info,
    mocked_get_ensemble_url,
)


@mock.patch("ertviz.data_loader.requests.get", side_effect=mocked_requests_get)
@mock.patch("ertviz.data_loader.pandas.read_csv", side_effect=mocked_read_csv)
@mock.patch("ertviz.data_loader.get_info", side_effect=mocked_get_info)
@mock.patch(
    "ertviz.models.ensemble_model.get_ensemble_url", side_effect=mocked_get_ensemble_url
)
def test_parameter_selector(
    mock_get,
    mock_get_csv,
    mock_get_info,
    mock_get_ensemble_url,
    dash_duo,
):
    app = dash.Dash(__name__)

    plugin = ParameterComparison(app, project_identifier=None)
    layout = plugin.layout
    app.layout = layout
    dash_duo.start_server(app)

    parameter_selector_input = dash_duo.find_element(
        "#" + plugin.uuid("parameter-selector-filter")
    )

    assert parameter_selector_input.text == ""
    parameter_selector_input.click()
    paremeter_selector_multi = dash_duo.find_element(
        "#" + plugin.uuid("parameter-selector-multi")
    )
    assert paremeter_selector_multi is not None
    paremeter_selector_multi.click()

    assert dash_duo.get_logs() == []
