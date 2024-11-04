from template.exceptions import AnyBadException
from template.request import Request, File
from template.model import Info
from template.options import Options as OptionsType
import yaml

from template.template import Template


class Runner(object):

    Options: OptionsType

    def __init__(self, options: OptionsType):
        self.Options = options

    def yaml_parse(self, file) -> Template:
        poc_yaml_text = yaml.load(open(file), Loader=yaml.FullLoader)
        id = poc_yaml_text.get("id") or poc_yaml_text.get("name")
        info = Info(**poc_yaml_text.get("info"))
        requests = []
        files = []

        # 临时加的
        # if not poc_yaml_text.get("requests"):
        #     raise AnyBadException()

        if poc_yaml_text.get("requests"):
            for request in poc_yaml_text.get("requests"):
                requests.append(Request(**request))

        if poc_yaml_text.get("file"):
            for file in poc_yaml_text.get("file"):
                files.append(File(**file))

        return Template(id=id, info=info, requests=requests, files=files)
        # template.list_requests()
        # template.compile(url)

    def run(self, callback=None):
        templates = self.Options.Templates

        for poc_template in templates:
            # print("load {}".format(poc_template))
            try:
                template = self.yaml_parse(poc_template)
            except KeyError as e:
                print("error in run {}".format(poc_template), e)
                continue

            # poc模板处理options参数
            for result in template.compile(self.Options):
                if callback and result:
                    yield callback(template, result)
                # print(template.Info.SeverityHolder, self.Options.Url)
            # print(template.Info.SeverityHolder)
