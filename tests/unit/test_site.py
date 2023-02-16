import pytest

URL_test_data = [
]

@pytest.mark.parametrize("URL, response", URL_test_data)
def test_is_valid(URL, response):
   return True