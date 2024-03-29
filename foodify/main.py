from fastapi import FastAPI, HTTPException
from application.auth.oauth_errors import http_error_handler
from starlette.middleware.cors import CORSMiddleware
from application.database.database import init_db
from application.routes.api import router as api_router
from core.config import get_app_settings
from core.logging import logger


def get_application() -> FastAPI:
    settings = get_app_settings()
    logger.info(f"Foodify is in {settings.app_env} environment")

    # Load app
    application = FastAPI(**settings.fastapi_kwargs)

    # Init the database
    init_db()

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_exception_handler(HTTPException, http_error_handler)

    application.include_router(api_router, prefix=settings.api_prefix)

    return application


app = get_application()

# @app.on_event("startup")
# async def init_data():
#     scheduler = BackgroundScheduler()
#     # Esta función, sirve para pasarle el parámetro TRUE a update_prices
#     update_prices_with_argument = functools.partial(foodify_man.update_prices, True)
#     scheduler.add_job(update_prices_with_argument, "interval", hours=1)
#     scheduler.start()

#
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=7080)
