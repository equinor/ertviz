import dash
from ertviz.plugins._response_correlation import ResponseCorrelation


def test_response_correlation_view(
    mock_data,
    dash_duo,
):
    app = dash.Dash(__name__)

    plugin = ResponseCorrelation(app, project_identifier=None)
    layout = plugin.layout
    app.layout = layout
    dash_duo.start_server(app)
    windowsize = (630, 1200)
    dash_duo.driver.set_window_size(*windowsize)
    ensemble_elements = dash_duo.find_element(".ert-ensemble-selector-large")

    # The position is hard coded coordinates normalized to the extent of the
    # ensemble-selector
    x, y = (0.5, 0.15)
    dash_duo.click_at_coord_fractions(ensemble_elements, x, y)
    resp_select = dash_duo.find_element(
        "#" + plugin.uuid("parameter-selector-multi-resp")
    )

    x, y = (0.5, 0.1)
    dash_duo.click_at_coord_fractions(resp_select, x, y)

    param_select = dash_duo.find_element(
        "#" + plugin.uuid("parameter-selector-multi-param")
    )
    param_select.click()

    x, y = (0.5, 0.1)
    # double click's for the sake if other parameter comes first
    dash_duo.click_at_coord_fractions(param_select, x, y)

    response_views = dash_duo.find_elements(".ert-view-cell")
    assert len(response_views) == 4

    assert dash_duo.get_logs() == [], "browser console should contain no error"
