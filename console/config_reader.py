import json


class ConfigReader:
    def __init__(self, path='./resources/config.json'):
        self.path = path
        self.config = json.load(open(path, 'r'))

    def decorate(self, command):
        if '-abbr' in self.config:
            command.cmd = self.config['-abbr'].get(command.cmd, command.cmd)
        if command.cmd not in self.config:
            return
        for arg in self.config[command.cmd]['args']:
            if arg not in command.args:
                command.args.append(arg)
        for kwarg in self.config[command.cmd]['kwargs']:
            if kwarg not in command.kwargs:
                command.kwargs[kwarg] = self.config[command.cmd]['kwargs'][kwarg]
