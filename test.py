import os
import subprocess

while True:
    cmd = input("$ ")

    if cmd == "exit":
        break

    try:
        if cmd.startswith("cd "):
            # Change directory using os.chdir()
            new_dir = cmd.split(" ")[1]
            os.chdir(new_dir)
        else:
            # Execute the command in the terminal using subprocess.run()
            subprocess.run(cmd, shell=True)
    except Exception as e:
        print(f"Error: {e}")
