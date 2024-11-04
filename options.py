from typing import List


class Options(object):
    Url: str
    RequestProxy: dict
    RequestAllowRedirect: bool = True
    RequestHeaders: dict = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/72.0.3626.121 Safari/537.36"
    }
    Templates: List[str] = []
    RequestSSLVerify: bool = False

    def __init__(self, url=None, request_proxy=None,
                 request_allow_redirect=True,
                 request_headers: dict={},
                 templates=[], **kwargs):
        self.Url = url
        self.RequestProxy = request_proxy
        self.RequestAllowRedirect = request_allow_redirect
        self.RequestHeaders = dict(self.RequestHeaders, **request_headers)
        self.Templates = templates

