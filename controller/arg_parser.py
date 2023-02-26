from controller.servises import SERVICES


class ArgParser:
    def __init__(self, args):
        self.action_func = None
        self.args_parse(args)

    def args_parse(self, args):
        if len(args) <= 1:
            self.action_func = SERVICES[0]
        for item in args:
            print(item)

    def action(self):
        return self.action_func()
