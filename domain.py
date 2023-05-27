import numpy as np


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
        image: np.ndarray,
    ):
        self._max = inland_max
        self._mean = inland_mean
        self._min = inland_min
        self._value = value
        self._image = None

    @property
    def max(self) -> float:
        return self._max

    @property
    def mean(self) -> float:
        return self._mean

    @property
    def min(self) -> float:
        return self._min

    @property
    def value(self) -> float:
        return self._value

    @property
    def image(self) -> np.ndarray:
        return self._image
