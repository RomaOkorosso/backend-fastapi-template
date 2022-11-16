import requests
from urllib.parse import urljoin


class APIRequest(object):
    """
    Can be instantiated with a base URL for an API.
    Subsequent calls can be made with the usual arguments for :meth:`requests.request`, specifying only the API route::
        >>> api_request = APIRequest('http://example.com/api/v3')
        >>> response = api_request('POST', '/login', data={'username': 'foo', 'password': 'bar'})
    etc.
    """

    def __init__(self, base_url, headers=None):
        if not base_url.endswith("/"):
            base_url += "/"
        self._base_url = base_url

        if headers is not None:
            self._headers = headers
        else:
            self._headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"
                " AppleWebKit/537.36 (KHTML, like Gecko)"
                " Chrome/51.0.2704.103"
                " Safari/537.36"
            }

    def __call__(self, method, route, **kwargs):

        if route.startswith("/"):
            route = route[1:]

        url = urljoin(self._base_url, route, allow_fragments=False)

        headers = kwargs.pop("headers", {})
        headers.update(self._headers)

        return requests.request(
            method=method, url=url, headers=headers, timeout=10, **kwargs
        )
