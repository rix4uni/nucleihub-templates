from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import LiteralScalarString
import re

class HTTP:
    def __init__(self):
        self.matchers = []
        self.matchers_condition = "or"
        self.stop_at_first = True
        self.extractors = []
        self.cookie_reuse = False
        self.paylaods = {}

    def set_stop_at_first_match(self,flag=True):
        self.stop_at_first = flag

    def set_matchers_condition(self,condition:str="or"):
        self.matchers_condition = condition

    def set_sleep_time_matcher(self,time=3):
        self.set_matcher(
            type="dsl",
            patterns=[
                f"duration>={time} && duration<={time + 1}"
            ]
        )
    def dump(self,id:str="poc",fingers=[]):
        template = Template(
            id=id
        )
        if len(fingers) > 0:
            template.finger = fingers
        template.set_http(http=self)
        template.dump()

        
    def set_cookie_reuse(self,reuse=False):
        self.cookie_reuse = reuse

    def set_dnslog_matcher(self):
        self.set_matcher(type="word",part="interactsh_protocol",patterns=["dns"])
        
    def set_httplog_matcher(self):
        self.set_matcher(type="word",part="interactsh_protocol",patterns=["http"])

    def set_status_matcher(self,status=[200],condition="or",negative=False):
        self.set_matcher(type="status",patterns=status,condition=condition,negative=negative)
    
    def set_body_word_matcher(self,patterns=[],condition="or",negative=False):
        self.set_matcher(
            type = "word",
            part = "body",
            patterns=patterns,
            condition=condition,
            negative=negative
        )
    
    def set_matcher(self,type="word",part:str=None,patterns=["a","b"],condition:str="or",negative=False):
        matcher = {
            "type":type,
        }
        if part and re.match("^(body|header|status)(_\\d+)?$|server|answer|raw|interactsh_request|interactsh_protocol|cipher|issuer_cn",part):
            matcher["part"] = part

        if type == "word":
            matcher["words"] = patterns
        elif type == "regex":
            matcher["regex"] = patterns
        elif type == "status":
            matcher["status"] = patterns
            if "part" in matcher:
                if "status" not in part:
                    del matcher["part"]
        elif type == "dsl":
            matcher["dsl"] = patterns
        elif type == "binary":
            matcher["binary"] = patterns
        else:
            return

        if condition == "or" or condition == "and" and len(patterns) > 1:
            matcher["condition"] = condition
        if negative:
            matcher["negative"] = negative

        self.matchers.append(matcher)

    def set_extractor(self,type="regex",part:str=None,patterns=["a","b"],group=None,name=None,internal=True):
        extractor = {
            "type":type
        }
        if name:
            extractor["name"] = name
        if part:
            extractor["part"] = part
        if type == "regex":
            extractor["regex"] = patterns
            if group:
                extractor["group"] = group
        elif type == "kval":
            extractor["kval"] = patterns
        elif type == "json":
            extractor["json"] = patterns
        elif type == "xpath":
            extractor["xpath"] = patterns
        else:
            return
        
        extractor["internal"] = internal
        
        self.extractors.append(extractor)
    
    def set_payload(self,name="path",values=["/wms","/geoserver/wms"]):
        self.paylaods[name] = values
    


class BaseHTTP(HTTP):
    def __init__(self,method="GET"):
        super().__init__()
        self.method = method
        self.body = None
        self.headers = None
        self.path = []

    def set_path(self,path:str="{{BaseURL}}/index.php"):
        self.path.append(path)

    def set_paths(self,paths:list):
        self.path = paths

    def set_headers(self,headers={"Cookie":"id=1"}):
        self.headers = headers

    def set_body(self,body:str):
        self.body = LiteralScalarString(body)

class RawHTTP(HTTP):
    def __init__(self,unsafe=False):
        super().__init__()
        self.unsafe = unsafe
        self.raw = []
    def set_raw(self,raw:str):
        self.raw.append(LiteralScalarString(raw))


class Template:
    def __init__(self,id:str="模板名",name="描述模板本身做了什么",author="inhann",severity="high",description="核弹级漏洞"):
        self.id = id
        self.info = {}
        self.metadata = {}
        self.http = []
        self.finger = []
        self.set_info(name=name,author=author,severity=severity,description=description)
    def set_info(self,name="描述模板本身做了什么",author="inhann",severity="high",description="核弹级漏洞"):
        self.info = {
            "name":name,
            "author":author,
            "severity":severity,
            "description":description,
        }
    def fofa_query(self,fofa_query=[
        'app="满客宝后台管理系统"'
    ]):
        self.metadata["fofa-query"] = fofa_query

    def cnvd(self,company="华为",website="https://www.huawei.com/cn/",product="华为14promax",version="全版本"):
        self.info["metadata"] = {
            
        }
        self.info["metadata"]["company"] = company
        self.info["metadata"]["website"] = website
        self.info["metadata"]["product"] = product
        self.info["metadata"]["version"] = version

    def tag(self,*tags):
        self.tags = list(tags)

    def set_http(self,http:HTTP):
        o = {}
        if isinstance(http,BaseHTTP):
            o = {
                "method":http.method,
                "path":http.path,
            }
            if http.body:
                o["body"] = http.body
            if http.headers:
                o["headers"] = http.headers

        elif isinstance(http,RawHTTP):
            o = {
                "raw":http.raw,
                "unsafe":http.unsafe,
            }
        
        o["cookie-reuse"] = http.cookie_reuse
        
        if http.matchers_condition:
            o["matchers-condition"] = http.matchers_condition
        if http.matchers:
            o["matchers"] = http.matchers
        if http.extractors:
            o["extractors"] = http.extractors
        
        if len(http.paylaods) > 0:
            o["payloads"] = http.paylaods
        
        self.http.append(o)

    def dump(self,dir="."):
        metadata = {}

        if "company" in self.metadata:
            metadata["company"] = self.metadata["company"]

        if "website" in self.metadata:
            metadata["website"] = self.metadata["website"]

        if "product" in self.metadata:
            metadata["product"] = self.metadata["product"]

        if "version" in self.metadata:
            metadata["version"] = self.metadata["version"]

        if "fofa-query" in self.metadata:
            metadata["fofa-query"] =  self.metadata["fofa-query"]

        if len(self.http) == 0:
            raise Exception("please set BaseHTTP or RawHTTP")
        
        if len(metadata) > 0:
            o = {
                "id":self.id,
                "info":self.info,
                "metadata":metadata,
                "http":self.http
            }
        else:
            o = {
                "id":self.id,
                "info":self.info,
                "http":self.http
            }
        if len(self.finger) >0:
            o["finger"] = self.finger
        with open(f"{self.id}.yaml", "w",encoding="utf-8") as f:
            yaml = YAML()
            yaml.dump(o,f)
            #default_flow_style=False,allow_unicode=True,sort_keys=False