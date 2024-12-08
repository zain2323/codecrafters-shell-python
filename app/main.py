import sys

COMMANDS = ['echo', 'exit', 'type']

def parse_args(command: str):
    command = command.split()
    cmd, *args = command[0], *command[1:]
    return cmd, args

def stringify_args(args: list[str]):
    return ' '.join(args)

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
            if response in COMMANDS:
                sys.stdout.write(f'{response} is a shell builtin\n')
            else:
                sys.stdout.write(f"{response}: not found\n")
        else:
            sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
