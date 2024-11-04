

class ExtractorTypeHolder():
    def __init__(self):
        self.ExtractorType = self


class Extractor:
    Name: str
    Type: int
    extractorType: int
    Regex: [str]
    RegexGroup: int
    regexCompiled: []
    KVal: [str]
    JSON: [str]
    XPath: [str]
    Attribute: str
    jsonCompiled: []
    Part: str
    Internal: bool
    CaseInsensitive: bool
