from store.models.base import CreateBaseModel, UpdateModel
from store.schemas.product import ProductIn, ProductUpdate


class ProductModel(ProductIn, CreateBaseModel):
    ...

class ProductUpdateModel(ProductUpdate, UpdateModel):
    ...
