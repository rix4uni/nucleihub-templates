"""
https://github.com/projectdiscovery/nuclei/blob/149edf12d56f47a2a3b72080de08e9d50146e307/v2/pkg/operators/operators.go#L13
"""
from typing import List, Mapping
from template.matchers import Matcher, ConditionType
from template.extractors import Extractor


class Operators:

    Matchers: List[Matcher] = []
    Extractors: List[Extractor] = []
    MatchersCondition: str
    matchersCondition: ConditionType

    def get_matchers_condition(self) -> ConditionType:
        return self.matchersCondition


class Result:
    Matched: bool
    Extracted: bool
    # Mapping[str, List[str]]
    Matches: {}
    # Mapping[str, List[str]]
    Extracts: {}
    OutputExtracts: [str]
    outputUnique: Mapping[str, object]
    DynamicValues: Mapping[str, List[str]]
    PayloadValues: Mapping[str, object]

    def merge(self, result):
        if not self.Matched and result.Matched:
            self.Matched = result.Matched

        if not self.Extracted and result.Extracted:
            self.Extracted = result.Extracted

        for k, v in result.Matches.items():
            self.Matches[k] = v

        for k, v in result.Extracts.items():
            self.Extracts[k] = v

