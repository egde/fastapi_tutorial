# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)
from customer_api.impl.health import is_everything_ok

from customer_api.models.extra_models import TokenModel  # noqa: F401


router = APIRouter()


@router.get(
    "/",
    responses={
        200: {"model": str, "description": "Everything is OK"},
        500: {"description": "Something is wrong"},
    },
    tags=["health"],
)
async def root_get(
) -> str:
    return is_everything_ok()
