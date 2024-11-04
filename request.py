import json
from typing import List, Mapping

import requests.exceptions

from template.exceptions import AnyBadException
from template.matchers import Matcher, ANDCondition, ORCondition, get_condition_from_string
import requests as httpclient

from template.options import Options


class HTTPClient(object):

    def __init__(self):
        self.base = None

    def get_instance(self):
        return httpclient

    def set_baseurl(self, url: str):
        self.base = url if url.endswith("/") else url + "/"

    def base_request(self, method: str, path: str, body=None, options: Options=None):
        # print("Request path: ", path)
        # print("Request method: ", method)
        # print("Request body: ", body)

        kwargs = {
            "proxies": options.RequestProxy,
            "headers": options.RequestHeaders,
            "allow_redirects": options.RequestAllowRedirect,
            "verify": options.RequestSSLVerify
        }

        if method.lower() == "get":
            return self.get_instance().get(path, **kwargs)
        elif method.lower() == "post":
            if isinstance(body, dict):
                body = json.dumps(body)
            return self.get_instance().post(
                path, data=body, **kwargs
            )
        elif method.lower() == "delete":
            return self.get_instance().delete(path, **kwargs)


class Request:
    Path: List[str]
    Raw: List[str]
    ID: str
    Name: str
    AttachType: str
    Method: str
    Body: str
    Payloads: Mapping[str, object]
    Headers: Mapping[str, str]
    RaceNumberRequests: int
    MaxRedirects: int
    Threads: int
    Redirects: int

    Matchers: List[Matcher]
    Matchers_Condition: bool = ANDCondition
    HTTPRequest = HTTPClient()

    def __init__(self,
                 path=None, raw=None, id=None, name=None,
                 method=None, body=None, headers=None,
                 redirects=None, matchers=None, **kwargs):
        self.Path = path
        self.Raw = raw
        self.ID = id
        self.Name = name
        self.Method = method
        self.Body = body
        self.Headers = headers
        self.Redirects = redirects

        self.Matchers = [
            Matcher(**matcher) for matcher in matchers
        ] if matchers else []
        self.Matchers_Condition = get_condition_from_string(kwargs.get("matchers-condition", "and").lower())

    def replace(self, url, path: str):
        path = path.replace("{{BaseURL}}", url)
        path = path.replace("{{RootURL}}", url)
        path = path.replace("{{interactsh-url}}", url)
        return path

    def compile(self, options: Options) -> str:
        # 临时加的
        if not all([options.Url, self.Path]):
            return

        url = self.replace(options.Url, path=self.Path[0])

        try:
            response = self.HTTPRequest.base_request(
                method=self.Method if self.Method else "GET",
                path=url, body=self.Body, options=options)
        except requests.exceptions.ProxyError as e:
            return

        # matchers-condition 判断
        if self.Matchers_Condition == ANDCondition:
            coditions = [matcher.compile(response) for matcher in self.Matchers]
            if len(coditions) and all(coditions):
                return url
        elif self.Matchers_Condition == ORCondition:
            if any([matcher.compile(response) for matcher in self.Matchers]):
                return url
        # print("STATUS: ", response.status_code)

    def get_id(self):
        return self.ID


class File:
    Extensions: List[str]           # extensions
    DenyList: List[str]             # denylist
    ID: str                         # id
    MaxSize: str                    # max-size      - value: "\"5Mb\""
    maxSize: int
    Archive: bool
    # CompiledOperators:
    extensions: Mapping[str, object]
    denyList: Mapping[str, object]
    NoRecursive: bool               # no-recursive
    allExtensions: bool

    Matchers: List[Matcher]
    Matchers_Condition: bool = ANDCondition
    HTTPRequest = HTTPClient()

    def __init__(self, extensions=None, denylist=None, id=None, extractors=None, **kwargs):
        self.Extensions = extensions
        self.DenyList = denylist
        self.ID = id
        self.MaxSize = kwargs.get("max-size")
        self.NoRecursive = kwargs.get("no-recursive")

        self.Matchers = [
            Matcher(**matcher) for matcher in extractors
        ] if extractors else []
        self.Matchers_Condition = get_condition_from_string(kwargs.get("matchers-condition", "and").lower())

    def getID(self):
        return self.ID

    def compile(self, options: Options):
        pass


defaultDenylist = {
    ".3g2", ".3gp", ".arj", ".avi", ".axd", ".bmp", ".css", ".csv", ".deb",
    ".dll", ".doc", ".drv", ".eot", ".exe", ".flv", ".gif", ".gifv", ".h264",
    ".ico", ".iso", ".jar", ".jpeg", ".jpg", ".lock", ".m4a", ".m4v", ".map",
    ".mkv", ".mov", ".mp3", ".mp4", ".mpeg", ".mpg", ".msi", ".ogg", ".ogm",
    ".ogv", ".otf", ".pdf", ".pkg", ".png", ".ppt", ".psd", ".rm", ".rpm", ".svg",
    ".swf", ".sys", ".tif", ".tiff", ".ttf", ".vob", ".wav", ".webm", ".wmv", ".woff",
    ".woff2", ".xcf", ".xls", ".xlsx"
}

defaultArchiveDenyList = {".7z", ".apk", ".gz", ".rar", ".tar.gz", ".tar", ".zip"}