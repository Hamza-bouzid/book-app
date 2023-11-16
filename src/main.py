import logging
import os
import traceback

from fastapi import FastAPI
from mangum import Mangum

from api.api import router

logger = logging.getLogger()
logger.setLevel(logging.INFO)
if os.getenv("DEBUG", None) == "1":
    logger.setLevel(logging.DEBUG)

app = FastAPI()

app.include_router(router, prefix="/api/v1")

app_handler = Mangum(app)


# create_tables() #TODO remove this line if is not necessary


def lambda_handler(event, context):
    try:
        if event.get("resource"):
            return app_handler(event, context)
    except Exception:
        logger.error(traceback.format_exc())
        return {"statusCode": 500, "body": "Internal Server Error"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
