from controller.servises import Service


class ArgParser:
    def __init__(self, args):
        self.action_func = None
        self.action_args = []
        self.services = Service()
        self.args_parse(args)



    def args_parse(self, args):
        if len(args) > 1 and args[1] in self.services.SERVICES:
            if len(args) >= self.services.SERVICES[args[1]][1]:
                self.action_func = self.services.SERVICES[args[1]][0]
                self.action_args = args[2:]
        else:
            self.action_func = self.services.SERVICES["help"][0]


    def action(self):
        self.action_func(self.services, *self.action_args)