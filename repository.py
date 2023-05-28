import os
from abc import ABC, abstractmethod

import rasterio
from dotenv import load_dotenv
from rasterio import DatasetReader

load_dotenv()

LTS_RASTER_PATH = os.environ.get("LTS_RASTER_PATH")


class RasterRepository(ABC):
    @abstractmethod
    def raster(self) -> DatasetReader:
        pass


class InMemoryRasterRepository(RasterRepository):
    def __init__(self, raster_path=LTS_RASTER_PATH):
        """
        La idea era que se abriese en memoria, pero no he conseguido que funcione

            f = open(raster_path, "rb")
            mem_file = MemoryFile(f)
            self._raster = mem_file.open()

        :param raster_path:
        """
        dataset = rasterio.open(raster_path, "r")
        self._raster = dataset

    @property
    def raster(self) -> DatasetReader:
        return self._raster
