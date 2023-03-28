import tkinter as tk
import os
import platform
import getpass
import subprocess
import cmd


INTRO_TEXT = """
Welcome to AliceShell, the simple multitab terminal
Type shortcuts or help for instructions on how to use AliceShell
"""


class Terminal(tk.Text, cmd.Cmd):
    def __init__(self, parent, **kwargs):
        tk.Text.__init__(self, parent, **kwargs)
        self.bind("<Key>", self.on_key)  # setup handler to process pressed keys
        self.cmd = None  # hold the last command issued
        self.os_type = platform.system().lower()
        self.insert_text(INTRO_TEXT, end="")
        self.show_prompt()

    # to append given text at the end of Text box
    def insert_text(self, txt="", end="\n"):
        self.insert(tk.END, txt + end)
        self.see(tk.END)  # make sure it is visible

    def show_prompt(self):
        currenty_dir = str(os.popen("cd").read()).strip()
        user_name = str(getpass.getuser())
        self.insert_text(f"@{user_name} {currenty_dir}>> ", end="")
        self.mark_set(tk.INSERT, tk.END)  # make sure the input cursor is at the end
        self.cursor = self.index(tk.INSERT)  # save the input position

    # handler to process keyboard input
    def on_key(self, event):
        # print(event)
        if event.keysym == "Up":
            if self.cmd:
                # show the last command
                self.delete(self.cursor, tk.END)
                self.insert(self.cursor, self.cmd)
            return "break"  # disable the default handling of up key
        if event.keysym == "Down":
            return "break"  # disable the default handling of down key
        if event.keysym in ("Left", "BackSpace"):
            current = self.index(
                tk.INSERT
            )  # get the current position of the input cursor
            if self.compare(current, "==", self.cursor):
                # if input cursor is at the beginning of input (after the prompt), do nothing
                return "break"
        if event.keysym == "Return":
            # extract the command input
            cmd = self.get(self.cursor, tk.END).strip()
            self.insert_text()  # advance to next line
            self.run(cmd)
            self.show_prompt()
            return "break"  # disable the default handling of Enter key
        if event.keysym == "Escape":
            self.master.destroy()  # quit the shell

    def run(self, cmd):
        self.cmd = cmd
        if cmd == "cls" or cmd == "clear":
            self.delete("1.0", tk.END)
            return
        if self.os_type == "windows":
            if cmd == "ls":
                cmd = "dir"

            if cmd == "pwd":
                cmd = "cd"
        try:
            if cmd.startswith("cd "):
                path = cmd[3:].strip()
                os.chdir(path)
                result = f"Changed directory to {os.getcwd()}\n"
            if cmd == "vim":
                os.system("vim")
                return
            else:

                result = subprocess.run(
                    cmd,
                    shell=True,
                    capture_output=True,
                    text=True,
                    stdin=subprocess.PIPE,
                ).stdout.strip()

            if result:
                self.insert_text(str(result))
            else:
                self.insert_text(f"Error: '{cmd}' command not found")
        except Exception as e:
            self.insert_text(str(e))
