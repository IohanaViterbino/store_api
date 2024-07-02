from typing import List
from uuid import UUID
import pytest
from store.usecases.product import product_usecase
from store.schemas.product import ProductOut, ProductUpdateOut
from store.core.exceptions import NotFoundException


@pytest.mark.asyncio
async def test_usecases_create_should_return_sucess(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Flocão Santa Clara"


@pytest.mark.asyncio
async def test_usecases_get_should_return_sucess(product_inserted):
    result = await product_usecase.get(id=product_inserted.id)

    assert isinstance(result, ProductOut)
    assert result.name == "Flocão Santa Clara"


@pytest.mark.asyncio
async def test_usecase_get_should_return_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(id=UUID("8fb0bbc8-300b-4f9c-8130-40c6eccc1a81"))

    assert (
        err.value.message
        == "Product not found with filter: 8fb0bbc8-300b-4f9c-8130-40c6eccc1a81"
    )


@pytest.mark.usefixtures("products_inserted")
async def test_usecases_query_should_return_sucess():
    result = await product_usecase.query()

    assert isinstance(result, List)
    assert len(result) > 1


@pytest.mark.asyncio
async def test_usecases_update_should_return_sucess(product_up, product_inserted):
    product_up.price = 4.50
    result = await product_usecase.update(id=product_inserted.id, body=product_up)

    breakpoint()
    assert isinstance(result, ProductUpdateOut)

@pytest.mark.asyncio
async def test_usecases_update_should_return_not_found(product_up):
    product_up.price = 4.50
    with pytest.raises(NotFoundException) as err:
        await product_usecase.update(id=UUID("8fb0bbc8-300b-4f9c-8130-40c6eccc1a81"), body=product_up)
        
    assert (
        err.value.message
        == "Product not found with filter: 8fb0bbc8-300b-4f9c-8130-40c6eccc1a81"
    )

@pytest.mark.asyncio
async def test_usecases_delete_should_return_sucess(product_inserted):
    result = await product_usecase.delete(id=product_inserted.id)

    assert result is True


@pytest.mark.asyncio
async def test_usecase_delete_should_return_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.delete(id=UUID("8fb0bbc8-300b-4f9c-8130-40c6eccc1a81"))

    assert (
        err.value.message
        == "Product not found with filter: 8fb0bbc8-300b-4f9c-8130-40c6eccc1a81"
    )
