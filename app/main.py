import sys
import os

PATH = os.environ.get('PATH')
BINARIES = []


def _init():
    global BINARIES
    dirs = PATH.split(':')
    for dir in dirs:
        BINARIES += os.listdir(dir)


def parse_args(command: str):
    command = command.split()
    cmd, *args = command[0], *command[1:]
    return cmd, args


def stringify_args(args: list[str]):
    return ' '.join(args)


def check_presence_of_command(cmd: str):
    return cmd in BINARIES


def main():
    # start repl
    while True:
        # Wait for user input
        sys.stdout.write("$ ")
        command = input()
        cmd, args = parse_args(command)
        if cmd == 'exit' and args == ['0']:
            break
        elif cmd == 'echo':
            response = stringify_args(args)
            sys.stdout.write(f'{response}\n')
        elif cmd == 'type':
            response = stringify_args(args)
            if check_presence_of_command(response):
                sys.stdout.write(f'{response} is a shell builtin\n')
            else:
                sys.stdout.write(f"{response}: not found\n")
        else:
            sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    _init()
    main()
