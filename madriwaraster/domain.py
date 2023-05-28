import numpy as np
from geojson import Point
from pydantic import BaseModel
from shapely import Point as ShapelyPoint

DECIMAL_PLACES = 2


class HeatInland:
    """
    Heat inland
    """

    def __init__(
        self,
        inland_max: float,
        inland_mean: float,
        inland_min: float,
        value: float,
        image: np.ndarray | None,
    ):
        self._max = inland_max
        self._mean = inland_mean
        self._min = inland_min
        self._value = value
        self._image = image

    @property
    def max(self) -> float:
        return round(self._max, DECIMAL_PLACES)

    @property
    def mean(self) -> float:
        return round(self._mean, DECIMAL_PLACES)

    @property
    def min(self) -> float:
        return round(self._min, DECIMAL_PLACES)

    @property
    def value(self) -> float:
        return round(self._value, DECIMAL_PLACES)

    @property
    def image(self) -> np.ndarray:
        return self._image


class AOI(BaseModel):
    side_square: int
    point: Point

    @property
    def to_point(self) -> ShapelyPoint:
        return ShapelyPoint(self.point["coordinates"]["coordinates"])


class PointOfInterest(BaseModel):
    lts: float
    point: Point


class Values(BaseModel):
    max: float
    mean: float
    min: float
    point: PointOfInterest


class LTS(BaseModel):
    values: Values
    image: str | None
