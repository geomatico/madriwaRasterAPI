import numpy as np
import pyproj
import rasterio
from rasterio.mask import mask
from shapely import Geometry, Point, Polygon
from shapely.ops import transform

from domain import HeatInland
from repository import RasterRepository


def calculate_aoi(point: Point, side_square: int) -> Polygon:
    """
    Calculate the area of interest (aoi) based on a point and a square side
    :param point:
    :param side_square:
    :return:
    """
    x0 = point.x - side_square / 2
    y0 = point.y + side_square / 2
    return Polygon(
        [
            (x0, y0),
            (x0, y0 - side_square),
            (x0 + side_square, y0 - side_square),
            (x0 + side_square, y0),
            (x0, y0),
        ]
    )


def transform_from_wgs84_coordinates_to_32630(geom: Geometry) -> Geometry:
    """
    Transform a point from 4326 to 32630
    :param geom:
    :return:
    """
    wgs84 = pyproj.CRS("EPSG:4326")
    utm_z30n = pyproj.CRS("EPSG:32630")

    project = pyproj.Transformer.from_crs(wgs84, utm_z30n, always_xy=True).transform
    return transform(project, geom)


def to_degrees(kelvin: float) -> float:
    return kelvin - 273.15


def calculate_heat_inland(
    repository: RasterRepository, point: Point, side_square: int
) -> HeatInland:
    """
    Calculate the heat inland
    :param repository:
    :param point:
    :param side_square:
    :return:
    """
    raster: rasterio.DatasetReader = repository.raster

    point_32630: Point = Point(transform_from_wgs84_coordinates_to_32630(point))

    aoi = calculate_aoi(point_32630, side_square)

    mask_data, mask_transform = mask(
        raster,
        [aoi],
        crop=True,
        all_touched=True,
    )
    out_meta = raster.meta

    out_meta.update(
        {
            "driver": "GTiff",
            "height": mask_data.shape[1],
            "width": mask_data.shape[2],
            "transform": mask_transform,
            "nodata": raster.profile["nodata"],
        }
    )

    # calculate the row and col of the point
    pixel_size = raster.res[0]
    col = int((point_32630.x - raster.bounds.left) / pixel_size)
    row = int((raster.bounds.top - point_32630.y) / pixel_size)
    value = raster.read(1)[row, col]

    mask_data[np.isnan(mask_data)] = 0
    the_max = np.amax(mask_data)
    the_min = np.amin(mask_data[np.nonzero(mask_data)])
    the_mean = np.mean(mask_data[np.nonzero(mask_data)])

    return HeatInland(
        inland_max=to_degrees(the_max),
        inland_mean=to_degrees(the_mean),
        inland_min=to_degrees(the_min),
        value=to_degrees(value),
        image=mask_data,
    )


def convert_image_to_base64():
    pass
