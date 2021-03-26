from typing import List, Union, Optional, TYPE_CHECKING
import datetime
import dateutil.parser


def indexes_to_axis(
    indexes: Optional[List[Union[int, str, datetime.datetime]]]
) -> Optional[List[Union[int, str, datetime.datetime]]]:
    try:
        if indexes and type(indexes[0]) is str:
            return list(map(lambda dt: dateutil.parser.isoparse(str(dt)), indexes))
        return indexes
    except ValueError as e:
        raise ValueError("Could not parse indexes as either int or dates", e)


if TYPE_CHECKING:
    from .ensemble_model import EnsembleModel
    from ertviz.plugins._webviz_ert import WebvizErtPluginABC


def load_ensemble(
    parent_page: "WebvizErtPluginABC", ensemble_id: int
) -> "EnsembleModel":
    ensemble = parent_page.ensembles.get(
        ensemble_id,
        EnsembleModel(
            ensemble_id=int(ensemble_id), project_id=parent_page.project_identifier
        ),
    )
    parent_page.ensembles[ensemble_id] = ensemble
    return ensemble


from .observation import Observation
from .realization import Realization
from .response import Response
from .plot_model import (
    PlotModel,
    ResponsePlotModel,
    HistogramPlotModel,
    MultiHistogramPlotModel,
    BoxPlotModel,
    ParallelCoordinatesPlotModel,
    BarChartPlotModel,
)
from .parameter_model import PriorModel, ParametersModel
from .ensemble_model import EnsembleModel
