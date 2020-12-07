import shlex


class Command:
    def __init__(self, cmd=None, values=None, args=None, kwargs=None):
        self.cmd = cmd
        self.values = [] if values is None else values
        self.args = [] if args is None else args
        self.kwargs = {} if kwargs is None else kwargs

    def __str__(self):
        args_str = ' '.join([f'-{arg}' for arg in self.args])
        kwargs_str = ' '.join([f'-{key}={value}' for key, value in self.kwargs.items()])
        values_str = ' '.join(self.values)
        return f'{self.cmd} {args_str} {kwargs_str} {values_str}'

    __repr__ = __str__


class CommandParser:
    @classmethod
    def parse(cls, command_str):
        command_list = shlex.split(command_str)
        command = Command(command_list[0])
        for item in command_list[1:]:
            if not item.startswith('-'):
                command.values.append(item)
                continue
            items = item[1:].split('=')
            if len(items) == 1:
                command.args.append(items[0])
            elif len(items) == 2:
                command.kwargs[items[0]] = items[1]
        return command

    @classmethod
    def _split(cls, command_str):
        buffer_str, command_list = '', []
        back_slash = False
        for char in (command_str + ' '):
            if char == '\\':
                back_slash = True
                continue
            back_slash = False
            if char != ' ':
                buffer_str += char
                continue
            elif back_slash:
                buffer_str += char
            elif len(buffer_str) > 0:
                command_list.append(buffer_str)
                buffer_str = ''
        return command_list
