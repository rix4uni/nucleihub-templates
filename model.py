"""
v2/pkg/model/model.go
"""


class Info(object):

    Name: str = None
    Authors: str = None
    Tags: str = None
    Description: str = None
    Reference: str = None
    SeverityHolder: str = None

    def __init__(self,
                 name=None, auther=None, tags=None,
                 description=None, reference=None,
                 severity=None, **kwargs):
        self.Name = name
        self.Authors = auther
        self.Tags = tags
        self.Description = description
        self.Reference = reference
        self.SeverityHolder = severity


class ServerityChoice:
    ServerityCritical = "critical"
    ServerityHigh = "high"
    ServerityMedium = "medium"
    ServerityLow = "low"
    ServerityInfo = "info"
