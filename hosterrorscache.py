class Cache:
    MaxHostError: int
    verbose: bool
    failedTargets: object

    def set_verbose(self, verbose: bool):
        self.verbose = verbose

    def close(self):
        pass
