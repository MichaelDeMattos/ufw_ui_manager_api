# -*- coding: utf-8 -*-

import logging
from fastapi import APIRouter
from ufw_ui_manager_api.api.routes import api_router


routes = APIRouter(tags=["ufw_rules"])
logger = logging.getLogger(__file__)
level = logging.DEBUG
logging.basicConfig(encoding="utf-8", level=level)


@routes.get("/ufw_rules/inbound")
async def list_ufw_rules_inbound():
    ...


api_router.include_router(routes)
