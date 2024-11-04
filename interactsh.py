from template.hosterrorscache import Cache


class Client:
    interactsh: object
    requests: Cache
    interactions: Cache
    matchedTemplates: Cache
    options: object
    eviction: int
    pollDuration: int
    cooldownDuration: int

    hostname: str
    firstTimeGroup: str
    generated: int
    matched: bool
