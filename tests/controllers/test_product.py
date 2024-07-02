from typing import List

import pytest
from tests.factories import product_data
from fastapi import status


async def test_controller_create_should_return_sucess(client, products_url):
    response = await client.post(products_url, json=product_data())
    content = response.json()

    del content["id"]
    del content["created_at"]
    del content["updated_at"]

    assert response.status_code == status.HTTP_201_CREATED
    assert content == {
        "name": "Flocão Santa Clara",
        "quantity": 30,
        "price": "3.25",
        "status": True,
    }


async def test_controller_get_should_return_sucess(
    client, products_url, product_inserted
):
    response = await client.get(f"{products_url}{product_inserted.id}")
    content = response.json()

    del content["created_at"]
    del content["updated_at"]

    assert content == {
        "id": str(product_inserted.id),
        "name": "Flocão Santa Clara",
        "quantity": 30,
        "price": "3.25",
        "status": True,
    }


async def test_controller_get_should_return_not_found(client, products_url):
    response = await client.get(f"{products_url}8fb0bbc8-300b-4f9c-8130-40c6eccc1a81")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "Product not found with filter: 8fb0bbc8-300b-4f9c-8130-40c6eccc1a81"
    }


@pytest.mark.usefixtures("products_inserted")
async def test_controller_query_should_return_sucess(client, products_url):
    response = await client.get(products_url)

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), List)
    assert len(response.json()) > 0


async def test_controller_update_should_return_sucess(
    client, products_url, product_inserted
):
    response = await client.patch(
        f"{products_url}{product_inserted.id}", json={"price": "5.15"}
    )
    content = response.json()

    del content["created_at"]
    del content["updated_at"]

    assert response.status_code == status.HTTP_200_OK
    assert content == {
        "id": str(product_inserted.id),
        "name": "Flocão Santa Clara",
        "quantity": 30,
        "price": "5.15",
        "status": True,
    }

async def test_controller_update_should_return_not_found(client, products_url):
    response = await client.patch(
        f"{products_url}4fd7cd35-a3a0-4c1f-a78d-d24aa81e7dca", json={"price": "5.15"}
    )
    
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "Product not found with filter: 4fd7cd35-a3a0-4c1f-a78d-d24aa81e7dca"
    }

async def test_controller_delete_should_return_no_content(
    client, products_url, product_inserted
):
    response = await client.delete(f"{products_url}{product_inserted.id}")

    assert response.status_code == status.HTTP_204_NO_CONTENT


async def test_controller_delete_should_return_not_found(client, products_url):
    response = await client.delete(
        f"{products_url}4fd7cd35-a3a0-4c1f-a78d-d24aa81e7dca"
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "Product not found with filter: 4fd7cd35-a3a0-4c1f-a78d-d24aa81e7dca"
    }
