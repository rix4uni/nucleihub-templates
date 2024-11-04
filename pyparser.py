import pyparsing
from ast import literal_eval
from asteval import Interpreter

import requests

identifier = pyparsing.QuotedString('"')
operator = (
    pyparsing.Literal("=") |
    pyparsing.Literal("≠") |
    pyparsing.Literal("≥") |
    pyparsing.Literal("≤") |
    pyparsing.Literal("<") |
    pyparsing.Literal(">")
)
value = pyparsing.QuotedString('"')
match_format = identifier + operator + value

print(
    match_format.parseString("\"a\" = \"1\"")
)

a = 1
import os
print(eval("os.listdir('.')", {"__builtins__": {}}))


class Response:
    status_code = 201


interpreter = Interpreter()
interpreter.symtable['response'] = Response

print(interpreter.eval("response.status_code == 200"))
# print(interpreter.eval("a = 1"))
