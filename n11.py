from nuclei import BaseHTTP
http = BaseHTTP(method="GET")
http.set_paths(
    paths=[
        '{{BaseURL}}/Runtime/Logs/{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/Runtime/Logs/{{unix_time(10)}}-{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/Runtime/Logs/Home/{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/Runtime/Logs/Home/{{unix_time(10)}}-{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/Runtime/Logs/Common/{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/Runtime/Logs/Common/{{unix_time(10)}}-{{date_time("%Y_%M_%D")}}',

        '{{BaseURL}}/App/Runtime/Logs/{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/App/Runtime/Logs/{{unix_time(10)}}-{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/App/Runtime/Logs/Home/{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/App/Runtime/Logs/Home/{{unix_time(10)}}-{{date_time("%Y_%M_%D")}}',
        # '{{BaseURL}}/App/Runtime/Logs/Common/{{date_time("%Y_%M_%D")}}',
        # '{{BaseURL}}/App/Runtime/Logs/Common/{{unix_time(10)}}-{{date_time("%Y_%M_%D")}}',

        '{{BaseURL}}/Application/Runtime/Logs/{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/Application/Runtime/Logs/{{unix_time(10)}}-{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/Application/Runtime/Logs/Admin/{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/Application/Runtime/Logs/Admin/{{unix_time(10)}}-{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/Application/Runtime/Logs/Home/{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/Application/Runtime/Logs/Home/{{unix_time(10)}}-{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/Application/Runtime/Logs/App/{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/Application/Runtime/Logs/App/{{unix_time(10)}}-{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/Application/Runtime/Logs/Ext/{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/Application/Runtime/Logs/Ext/{{unix_time(10)}}-{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/Application/Runtime/Logs/Api/{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/Application/Runtime/Logs/Api/{{unix_time(10)}}-{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/Application/Runtime/Logs/Test/{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/Application/Runtime/Logs/Test/{{unix_time(10)}}-{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/Application/Runtime/Logs/Common/{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/Application/Runtime/Logs/Common/{{unix_time(10)}}-{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/Application/Runtime/Logs/Service/{{date_time("%Y_%M_%D")}}',
        '{{BaseURL}}/Application/Runtime/Logs/Service/{{unix_time(10)}}-{{date_time("%Y_%M_%D")}}',
    ]
)
http.set_body_word_matcher(
    patterns=[
        "INFO",
        "[ error ]"
    ]
)
http.set_matchers_condition(condition="or")
http.dump(
    id="ThinkPHP 3.x 日志泄露",
    fingers=[
        "thinkphp"
    ]
)
