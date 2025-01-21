import subprocess
import shlex
import os

def execute_command(command):
    # Split the command into parts
    parts = shlex.split(command)
    
    # Handle IO redirection
    if '>' in parts:
        idx = parts.index('>')
        command = parts[:idx]
        output_file = parts[idx + 1]
        with open(output_file, 'w') as f:
            result = subprocess.run(command, stdout=f, stderr=subprocess.PIPE, text=True)
            if result.stderr:
                print(result.stderr)
        return

    if '<' in parts:
        idx = parts.index('<')
        command = parts[:idx]
        input_file = parts[idx + 1]
        with open(input_file, 'r') as f:
            result = subprocess.run(command, stdin=f, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print(result.stderr)
        return

    # Handle piping
    if '|' in parts:
        commands = [shlex.split(cmd) for cmd in command.split('|')]
        processes = []
        for i, cmd in enumerate(commands):
            if i == 0:
                processes.append(subprocess.Popen(cmd, stdout=subprocess.PIPE))
            else:
                processes.append(subprocess.Popen(cmd, stdin=processes[-1].stdout, stdout=subprocess.PIPE))
        output, error = processes[-1].communicate()
        if output:
            print(output.decode())
        if error:
            print(error.decode())
        return

    # Execute the command normally
    try:
        result = subprocess.run(parts, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
    except FileNotFoundError:
        print(f"Command not found: {parts[0]}")

def main():
    while True:
        try:
            command = input("shell> ")
            if command.lower() in ['exit', 'quit']:
                break
            execute_command(command)
        except KeyboardInterrupt:
            print("\nExiting shell.")
            break

if __name__ == "__main__":
    main()