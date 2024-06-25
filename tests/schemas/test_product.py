from pydantic import ValidationError
import pytest
from store.schemas.product import ProductIn
from tests.factories import product_data


def test_schemas_return_sucess():
    data = product_data()
    product = ProductIn.model_validate(data)

    assert product.name == "Flocão Santa Clara"


def test_schemas_return_raise():
    data = {"name": "Flocão Santa Clara", "quantity": 30, "price": 3.25}

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "Flocão Santa Clara", "quantity": 30, "price": 3.25},
        "url": "https://errors.pydantic.dev/2.7/v/missing",
    }
