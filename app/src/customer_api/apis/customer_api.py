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

from customer_api.models.extra_models import TokenModel  # noqa: F401
from customer_api.models.customer import Customer
from customer_api.models.error import Error


router = APIRouter()


@router.get(
    "/customer",
    responses={
        200: {"model": Customer, "description": "The customer details"},
    },
    tags=["customer"],
)
async def customer_get(
) -> Customer:
    ...


@router.get(
    "/customer/{id}",
    responses={
        200: {"model": List[Customer], "description": "Details of customer with ID {id}"},
        404: {"model": Error, "description": "The customer could not be found"},
    },
    tags=["customer"],
)
async def customer_id_get(
    id: str = Path(None, description="The ID of the customer to be returned"),
) -> List[Customer]:
    ...


@router.post(
    "/customer",
    responses={
        200: {"model": Customer, "description": "The customer created"},
        500: {"model": Error, "description": "Internal error"},
    },
    tags=["customer"],
)
async def customer_post(
    customer: Customer = Body(None, description="Customer to be created"),
) -> Customer:
    """Add a new customer"""
    ...
