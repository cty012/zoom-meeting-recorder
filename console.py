from console.command_parser import CommandParser
import console.commands as cmds
from console.config_reader import ConfigReader


config = ConfigReader()

while True:
    command_str = input('>>> ')
    command = CommandParser.parse(command_str)
    config.decorate(command)
    if command.cmd == 'quit':
        cmds.quit_(command)
    elif command.cmd == 'join':
        cmds.join(command)
    elif command.cmd == 'join_by_name':
        cmds.join_by_name(command)
