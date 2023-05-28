# Madriwa Raster API

El proyecto está creado con FastAPI, para arrancarlo se necesario tener uvicorn instalado:

```bash
pip install uvicorn
```

para arrancar el proyecto:

```bash
uvicorn madriwaraster.main:app --reload
```

Para probar el proyecto:

**POST** http://localhost:8000/api/v1/isladecalor/lts/

```json
{
  "side_square": 7000,
  "point": {
    "type": "Point",
    "coordinates": {"coordinates": [-3.7060583, 40.4169019]}
  }
}
```