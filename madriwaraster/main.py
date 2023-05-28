from fastapi import FastAPI
from starlette import status
from starlette.exceptions import HTTPException

from madriwaraster.domain import AOI, LTS, PointOfInterest, Values
from madriwaraster.repository import InMemoryRasterRepository
from madriwaraster.use_cases import calculate_heat_inland

API_VERSION = "v1"

app = FastAPI()

raster_repository = InMemoryRasterRepository()


@app.post(f"/api/{API_VERSION}/isladecalor/lts/", status_code=status.HTTP_201_CREATED)
async def heat_inland(aoi: AOI):
    try:
        the_inland = calculate_heat_inland(
            repository=raster_repository,
            point=aoi.to_point,
            side_square=aoi.side_square,
        )

    except ValueError as err:
        raise HTTPException(status_code=404, detail=err.args[0])

    return LTS(
        values=Values(
            max=the_inland.max,
            mean=the_inland.mean,
            min=the_inland.min,
            point=PointOfInterest(lts=the_inland.value, point=aoi.point),
        )
    )
