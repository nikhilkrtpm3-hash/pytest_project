from api.endpoints import brand_list
from utils.logger import logger


def test_brandlist(api_client):
    logger.debug("Fetching brand list with endpoint: %s", brand_list)
    response = api_client.get(brand_list)
    response_data = response.json()
    logger.debug("Brand-list response status: %s", response.status_code)
    logger.debug("Brand-list response code: %s", response_data.get("responseCode"))

    assert response.status_code == 200
    logger.info("Brand list fetched successfully")

def test_brands_with_wrong_method(api_client):
    logger.debug("Fetching brands with wrong method: %s", brand_list)
    response = api_client.put(brand_list)
    response_data = response.json()
    assert response.status_code == 200
    assert response_data.get("responseCode") == 405