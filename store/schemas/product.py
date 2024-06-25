from decimal import Decimal
from typing import Annotated, Optional
from bson import Decimal128
from pydantic import AfterValidator, BaseModel, Field
from store.schemas.base import BaseSchemaMixin, OutSchema


class ProductBase(BaseModel):
    name: str = Field(..., description="product name")
    quantity: int = Field(..., description="product qunatity")
    price: Decimal = Field(..., description="product price")
    status: bool = Field(..., description="product status")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn, OutSchema):
    ...


def convert_decimal_128(v):
    return Decimal128(str(v))


Decimal_ = Annotated[Decimal, AfterValidator(convert_decimal_128)]


class ProductUpdate(BaseSchemaMixin):
    quantity: Optional[int] = Field(None, description="product qunatity")
    price: Optional[Decimal_] = Field(None, description="product price")
    status: Optional[bool] = Field(None, description="product status")


class ProductUpdateOut(ProductOut):
    ...
