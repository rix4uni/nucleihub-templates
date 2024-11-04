import logging
import colorama
from typing import Dict
from termcolor import colored
from config import logging_level, logging_format


# coloredlogs.DEFAULT_FIELD_STYLES = {
#     'hostname': {'color': 'magenta'},
#     'programname': {'color': 'cyan'},
#     'name': {'color': 'blue'},
#     'levelname': {'color': 'black', 'bold': True},
#     'asctime': {'color': 'magenta'}}
#
# coloredlogs.install(
#     fmt="[%(levelname)s] %(message)s",
#     field_styles={},
#     level_styles=dict(
#         debug={"color": "yellow"},
#         info={"color": "white"},
#         warning={"color": "red"},
#         error={"color": "red"},
#     )
# )
#
# handler = colorlog.StreamHandler()
# handler.setFormatter(
#     colorlog.ColoredFormatter(
#         "%(log_color)s[%(levelname)s] %(reset)s %(blue)s%(message)s",
#         reset=True,
#         log_colors={
#             'DEBUG': 'cyan',
#             'INFO': 'green',
#             'WARNING': 'yellow',
#             'ERROR': 'red,bg_white',
#             'CRITICAL': 'red',
#         },
#         style='%'
#     ))


# def getLogger() -> logging:
#     logger = logging.getLogger()
#     logger.addHandler(handler)
#     return logger

# #
# l = getLogger()
# l.error("ok")

class getLogger(object):

    def __init__(self):
        pass

    def base_log(self, level, level_color,
                 messages: Dict[str, str], hidden_level=False):
        texts = []
        if not hidden_level and level and level_color:
            texts.append('[{}]'.format(colored(level, level_color)))

        for k, color in messages.items():
            texts.append(colored(k, color))
        return "".join(texts)

    def log(self, messages: Dict[str, str], hidden_level=False,
            level=None, level_color=None):
        print(self.base_log(
            level=level, level_color=level_color,
            messages=messages, hidden_level=hidden_level
        ))


if __name__ == '__main__':
    # print(getLogger().info({}))
    pass

