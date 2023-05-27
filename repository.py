import os
from abc import ABC, abstractmethod

from dotenv import load_dotenv
from rasterio import DatasetReader, MemoryFile

load_dotenv()

LTS_RASTER_PATH = os.environ.get("LTS_RASTER_PATH")


class RasterRepository(ABC):
    @abstractmethod
    def raster(self) -> DatasetReader:
        pass


class InMemoryRasterRepository(RasterRepository):
    def __init__(self, raster_path=LTS_RASTER_PATH):
        f = open(raster_path, "rb")
        mem_file = MemoryFile(f)
        self._raster = mem_file.open()

    @property
    def raster(self) -> DatasetReader:
        return self._raster
