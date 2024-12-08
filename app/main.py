import sys
import os
import subprocess

PATH = os.environ.get('PATH')
BINARIES = {}
BUILTIN_BINARIES = ['type', 'echo', 'exit', 'pwd']


def _init():
    global BINARIES
    dirs = PATH.split(':')
    for dir in dirs:
        if not os.path.exists(dir):
            continue
        if dir in BINARIES:
            BINARIES[dir] += os.listdir(dir)
        else:
            BINARIES[dir] = os.listdir(dir)


def parse_args(command: str):
    command = command.split()
    cmd, *args = command[0], *command[1:]
    return cmd, args


def stringify_args(args: list[str]):
    return ' '.join(args)


def check_presence_of_command(cmd: str) -> tuple[bool, str]:
    for dir, binaries in BINARIES.items():
        if cmd in binaries:
            return True, dir
    return False, ''


def _construct_subprocess_command(cmd, args) -> [str]:
    command = [cmd]
    for arg in args:
        command.append(arg)
    return command

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
            status, dir = check_presence_of_command(response)
            if response in BUILTIN_BINARIES:
                sys.stdout.write(f"{response} is a shell builtin\n")
            elif status and dir != '':
                sys.stdout.write(f'{response} is {dir}/{response}\n')
            else:
                sys.stdout.write(f"{response}: not found\n")
        else:
            # if command is not in the PATH variable then it is and invalid command
            status, dir = check_presence_of_command(cmd)
            if not (status and dir != ''):
                sys.stdout.write(f"{command}: command not found\n")
                continue
            # else executing the binary located in the PATH variable
            else:
                posix_path = f'{dir}/{cmd}'
                args = _construct_subprocess_command(posix_path, args)
                completed_process = subprocess.run(args, capture_output=True)
                if completed_process.returncode == 0 and completed_process.stdout:
                    sys.stdout.write(completed_process.stdout.decode())
                else:
                    sys.stderr.write(completed_process.stderr.decode())
if __name__ == "__main__":
    _init()
    main()
