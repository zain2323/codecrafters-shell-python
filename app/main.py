import sys


def main():

    # start repl
    while True:
        # Wait for user input
        sys.stdout.write("$ ")
        command = input()
        if command == 'exit 0':
            break
        sys.stdout.write(f"{command}: command not found\n")


if __name__ == "__main__":
    main()
