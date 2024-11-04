import re
from enum import Enum
from typing import Mapping
from requests import Response


class MatcherType(Enum):
    WordsMatcher = 1
    RegexMatcher = 2
    BinaryMatcher = 3
    StatusMatcher = 4
    SizeMatcher = 5
    DSLMatcher = 6
    limit = 7

#
# class MatcherTypeHolder(MatcherType):
#
#     def __init__(self):
#         self.MatcherType = self


class Matcher:

    Type: MatcherType
    Condition: str
    Part: str
    Negative: bool
    Name: str
    Status: [int]
    Size: [int]
    Words: [str]
    Regex: [str]
    Binary: [str]
    DSL: [str]
    Encoding: str
    CaseInsensitive: str

    condition: int
    matcherType: int
    binaryDecoded: [str]
    regexCompiled: []
    dslCompiled: []

    def __init__(self, type=None, condition=None,
                 part=None, negative=None,
                 name=None, status=None,
                 size=None, words=None,
                 regex=None, binary=None,
                 dsl=None, **kwargs):
        self.Type = get_matchertype_from_string(type)
        self.Condition = get_condition_from_string(condition)
        self.Part = part
        self.Negative = negative
        self.Name = name
        self.Status = status
        self.Size = size
        self.Words = words
        self.Regex = regex
        self.Binary = binary
        self.DSL = dsl

    def get_type(self):
        return self.Type.MatcherType

    def compile(self, response: Response):
        # print(self.Condition, self.Type, response.status_code, self.Status)
        if not response:
            return False

        if self.Words and self.Type == MatcherType.WordsMatcher:
            if self.Condition == ANDCondition:
                if all([word in response.text for word in self.Words]):
                    return True
            elif self.Condition == ORCondition:
                if any([word in response.text for word in self.Words]):
                    return True
        elif self.Type == MatcherType.StatusMatcher:
            """
            这里要改一下
            """
            if self.Condition == ANDCondition:
                if all([status == response.status_code for status in self.Status]):
                    return True
            elif self.Condition == ORCondition:
                if any([status == response.status_code for status in self.Status]):
                    return True
        elif self.Type == MatcherType.RegexMatcher:
            try:
                if self.Condition == ANDCondition:
                    if all([re.search(r'{}'.format(regx), response.text) for regx in self.Regex]):
                        return True
                elif self.Condition == ORCondition:
                    if any([re.search(r'{}'.format(regx), response.text) for regx in self.Regex]):
                        return True
            except re.error as e:
                return False


ConditionType = int
MatcherTypes = {
    MatcherType.StatusMatcher: 'status',
    MatcherType.SizeMatcher: "size",
    MatcherType.WordsMatcher: "word",
    MatcherType.RegexMatcher: "regex",
    MatcherType.BinaryMatcher: "binary",
    MatcherType.DSLMatcher: "dsl",
}


def get_matchertype_from_string(string):
    for k, v in MatcherTypes.items():
        if v == string:
            return k
    return MatcherType.WordsMatcher


def get_condition_from_string(string: str):
    if string is None:
        return ConditionTypes.get("and")
    return ConditionTypes.get(string.lower(), None)


ANDCondition: int = 1
ORCondition: int = 2
ConditionTypes: Mapping[str, int] = {
    "and": ANDCondition,
    "or": ORCondition
}



