"""
https://github.com/projectdiscovery/nuclei/blob/149edf12d56f47a2a3b72080de08e9d50146e307/v2/pkg/protocols/dns/dns.go#L21
"""

from typing import Mapping, List

from template.operators import Operators
from template.interactsh import Client


class Request:
    ID: str = None
    Name: str = None
    RequestType: str = None
    Class: str
    Retries: int
    Trace: bool
    TraceMaxRecursion: int
    CompiledOperators: Operators
    dnsClient: Client
    options: object
    clazz: int
    question: int
    Recursion: bool
    Resolvers: [str]

    def get_compile_operators(self) -> List[Operators]:
        return []

    def get_id(self):
        return self.ID

    def compile(request, options):
        if request.Retries == 0:
            request.Retries = 3

        if request.Recursion is None:
            recusion = True
            request.Recursion = recusion




RequestPartDefinitions: Mapping[str, str] = {
    "template-id": "ID of the template executed",
    "template-info": "Info Block of the template executed",
    "template-path": "Path of the template executed",
    "host": "Host is the input to the template",
    "matched": "Matched is the input which was matched upon",
    "request": "Request contains the DNS request in text format",
    "type": "Type is the type of request made",
    "rcode": "Rcode field returned for the DNS request",
    "question": "Question contains the DNS question field",
    "extra": "Extra contains the DNS response extra field",
    "answer": "Answer contains the DNS response answer field",
    "ns": "NS contains the DNS response NS field",
    "raw,body,all": "Raw contains the raw DNS response (default)",
    "trace": "Trace contains trace data for DNS request if enabled",
}
