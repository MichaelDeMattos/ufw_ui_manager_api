# -*- coding: utf-8 -*-

import sentry_sdk
from fastapi import FastAPI
from contextlib import asynccontextmanager
from ufw_ui_manager_api.api.routes import api_router
from ufw_ui_manager_api.router import app_routes
from fastapi.middleware.cors import CORSMiddleware
from ufw_ui_manager_api.api.settings import get_settings
from ufw_ui_manager_api.api.repository.db import sessionmanager
from prometheus_fastapi_instrumentator import Instrumentator


settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Function that handles startup and shutdown events.
    To understand more, read https://fastapi.tiangolo.com/advanced/events/
    """
    yield
    if sessionmanager._engine is not None:
        # Close the DB connection
        await sessionmanager.close()


sentry_sdk.init(
    dsn=settings.SENTRY_DSN,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

# fastapi
app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app_routes.include_router(api_router)
app.include_router(app_routes)

# prometheus
Instrumentator().instrument(app).expose(app)
