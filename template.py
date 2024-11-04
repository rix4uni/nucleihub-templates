"""
https://github.com/projectdiscovery/nuclei/blob/149edf12d56f47a2a3b72080de08e9d50146e307/v2/pkg/templates/templates.go
"""
# import telegram.client
from typing import List

from core.logger import getLogger
from template import model, request
from template.model import ServerityChoice
from template.options import Options


class Template(object):
    ID: str = ""
    Info: model.Info = None
    RequestsHTTP: List[request.Request]
    RequestsFile: List[request.File]
    logger = getLogger()

    def __init__(self, id, info: model.Info, requests, files):
        self.ID = id
        self.Info = info
        self.RequestsHTTP = requests
        self.RequestsFile = files

    def list_requests(self):
        for request_http in self.RequestsHTTP:
            print("method: ", request_http.Method)
            print("path: ", request_http.Path)
            print("header: ", request_http.Headers)
            print("body: ", request_http.Body)

            for matcher in request_http.Matchers:
                print("matcher type: ", matcher.Type)
                print("matcher condition: ", matcher.Condition)
                # print(matcher.)

    def log(self, request_success_url):
        if request_success_url:
            if self.Info.SeverityHolder == ServerityChoice.ServerityCritical:
                # self.logger.critical("{}".format(request_success_url))
                # self.logger.info("{}".format(request_success_url))
                self.logger.log(messages={
                    "[{}] ".format(self.Info.SeverityHolder): "red",
                    "[{}] ".format(self.ID): "green",
                    request_success_url: "white"
                })
            elif self.Info.SeverityHolder == ServerityChoice.ServerityHigh:
                # self.logger.critical("{}".format(request_success_url))
                # self.logger.info("{}".format(request_success_url))
                self.logger.log(messages={
                    "[{}] ".format(self.Info.SeverityHolder): "red",
                    "[{}] ".format(self.ID): "green",
                    request_success_url: "white"
                })
            elif self.Info.SeverityHolder == ServerityChoice.ServerityMedium:
                # self.logger.critical("{}".format(request_success_url))
                # self.logger.info("{}".format(request_success_url))
                self.logger.log(messages={
                    "[{}] ".format(self.Info.SeverityHolder): "yellow",
                    "[{}] ".format(self.ID): "green",
                    request_success_url: "white"
                })
            elif self.Info.SeverityHolder == ServerityChoice.ServerityLow:
                # self.logger.critical("{}".format(request_success_url))
                # self.logger.info("{}".format(request_success_url))
                self.logger.log(messages={
                    "[{}] ".format(self.Info.SeverityHolder): "blue",
                    "[{}] ".format(self.ID): "green",
                    request_success_url: "white"
                })
            elif self.Info.SeverityHolder == ServerityChoice.ServerityInfo:
                # self.logger.critical("{}".format(request_success_url))
                # self.logger.info("{}".format(request_success_url))
                self.logger.log(messages={
                    "[{}] ".format(self.Info.SeverityHolder): "blue",
                    "[{}] ".format(self.ID): "green",
                    request_success_url: "white"
                })

    def compile(self, options: Options):

        # 解析模板里面的requests进行请求发起
        for request_http in self.RequestsHTTP:
            request_success_url = request_http.compile(options)
            yield request_success_url
            self.log(request_success_url)

        for request_file in self.RequestsFile:
            request_success_url = request_file.compile(options)
            yield request_success_url
            self.log(request_success_url)
