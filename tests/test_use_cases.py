import pytest
from shapely import Point

from repository import InMemoryRasterRepository
from use_cases import (
    calculate_aoi,
    calculate_heat_inland,
    transform_from_wgs84_coordinates_to_32630,
)

in_memory_repository = InMemoryRasterRepository(raster_path="./test_raster.tif")


def test_calculate_aoi():
    sideSquare = 100
    point = Point(0, 0)

    aoi = calculate_aoi(point, sideSquare)

    assert aoi.area == 10000
    assert aoi.length == 400
    assert aoi.bounds == (-50.0, -50.0, 50.0, 50.0)


def test_transform_coordinates_to_32630():
    point = Point(-7.4842644, 0.0090194)

    point = Point(transform_from_wgs84_coordinates_to_32630(point))

    assert point.x == pytest.approx(500, 0.003)
    assert point.y == pytest.approx(1000, 0.003)


def test_in_memory_repository():
    raster = in_memory_repository.raster
    assert raster.count == 1


def test_in_memory_repository_again_without_open():
    raster = in_memory_repository.raster
    assert raster.count == 1


def test_calculate_heat_inland():
    heat_inland = calculate_heat_inland(
        in_memory_repository, Point(-7.48847, 0.00026), 5
    )

    assert heat_inland.max == 6.0
    assert heat_inland.mean == 5.0
    assert heat_inland.min == 4.0
    assert heat_inland.value == 6.0
