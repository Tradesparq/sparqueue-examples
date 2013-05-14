class ExampleException(Exception):
    pass


class FailDependency():
    def __init__(self, fail):
        self.fail = fail

    def conditionalFail(self):
        if self.fail:
            raise ExampleException('configured to fail')


class ExampleJob():

    def __init__(self, injected):
        self.injected = injected

    # we have an unused *args and **kwargs just to collect extraneous arguments
    def perform(self, reporter, string, *args, **kwargs):
        reporter.step('count length of %s' % string)
        length = len(string)

        reporter.step('iterate %s' % string, length)
        chars = []
        for i in string:
            reporter.increment()
            chars.append(i)

        reporter.step('check for failure')
        self.injected.conditionalFail()

        return {
            'chars': chars
        }

    @staticmethod
    def instantiate(config, parameters=None):
        dependency = FailDependency(False)

        return ExampleJob(dependency)
