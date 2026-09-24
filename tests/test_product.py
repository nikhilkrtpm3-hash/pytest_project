from api.endpoints import all_product
from utils.logger import logger


def test_getproductlist(api_client):
    logger.debug("Fetching product list with endpoint: %s", all_product)
    response = api_client.get(all_product)
    response_data = response.json()
    logger.debug("Product-list response status: %s", response.status_code)
    logger.debug("Product-list response code: %s", response_data.get("responseCode"))

    assert response.status_code == 200
    logger.info("Product list fetched successfully")


def test_productlistwithwrongmethod(api_client):
    logger.debug("Sending POST request to product-list endpoint: %s", all_product)
    response = api_client.post(all_product)
    response_data = response.json()
    logger.debug("Wrong-method response status: %s", response.status_code)
    logger.debug("Wrong-method response code: %s", response_data.get("responseCode"))
    logger.debug("Wrong-method response message: %s", response_data.get("message"))

    logger.info("Product-list endpoint returned the expected HTTP response")
    assert response.status_code == 200
    assert response_data['responseCode'] == 405
