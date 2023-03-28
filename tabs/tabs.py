import tkinter as tk
import tkinter.ttk as ttk
from terminal.terminal import Terminal
import platform
import sv_ttk


class Tabs:
    def __init__(self):
        # Define the root window and its title
        self.root = tk.Tk()
        self.root.title("AliceShell")
        self.root.geometry("800x600")

        # Define the menu bar and its options
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.root.config(menu=self.menubar)

        # Define the tab control and its initial tab
        self.notebook = ttk.Notebook(self.root)
        self.terminal = [
            Terminal(self.root, width=100, height=50, font=("Consolas", 10))
        ]
        self.terminal[0].pack(fill=tk.BOTH, expand=1)
        self.terminal[0].focus_set()
        self.os_type = platform.system().lower()

        if self.os_type == "windows":
            self.text = "cmd"
        elif self.os_type == "darwin":
            self.text = "zsh"
        else:
            self.text = "shell"
        self.notebook.add(self.terminal[0], text=self.text)
        self.notebook.pack(fill="both", expand=True)

        # Handle keyboard shortcuts using bindings
        def handle_keyboard_shortcuts(event):

            if event.keysym == "n" and event.state == 12:  # Ctrl+N on Windows
                self.terminal.append(
                    Terminal(self.root, width=100, height=50, font=("Consolas", 10))
                )
                self.terminal[self.notebook.index("end")].pack(fill=tk.BOTH, expand=1)
                self.notebook.add(
                    self.terminal[self.notebook.index("end")], text=self.text
                )
                self.notebook.select(self.notebook.index("end") - 1)
                self.terminal[self.notebook.index("end") - 1].focus_set()
            elif event.keysym == "b" and event.state == 12:  # Ctrl+W on Windows
                index = self.notebook.index(self.notebook.select())
                if index > 0:
                    self.notebook.forget(index)
                    self.notebook.select(index - 1)
                elif index == 0 and self.notebook.index("end") == 1:
                    self.root.destroy()
                else:
                    self.notebook.forget(index)
                    self.notebook.select(index)

            elif event.keysym == "m" and event.state == 12:  # Ctrl+N on Windows
                if self.notebook.index("current") != self.notebook.index("end") - 1:
                    self.notebook.select(self.notebook.index("current") + 1)
                    self.notebook.focus_set()
                    self.terminal[self.notebook.index("current")].focus_set()
                else:
                    self.notebook.select(0)
                    self.notebook.focus_set()
                    self.terminal[0].focus_set()

            elif event.keysym == "q" and event.state == 12:  # Ctrl+Q on Windows
                self.root.destroy()

        # Bind keyboard shortcuts to the root window
        self.root.bind("<Control-n>", handle_keyboard_shortcuts)
        self.root.bind("<Control-N>", handle_keyboard_shortcuts)  # Ctrl+N on Windows
        self.root.bind("<Control-b>", handle_keyboard_shortcuts)
        self.root.bind("<Control-B>", handle_keyboard_shortcuts)  # Ctrl+W on Windows
        self.root.bind("<Control-q>", handle_keyboard_shortcuts)
        self.root.bind("<Control-Q>", handle_keyboard_shortcuts)  # Ctrl+Q on Windows
        self.root.bind("<Control-m>", handle_keyboard_shortcuts)
        self.root.bind("<Control-M>", handle_keyboard_shortcuts)

        # Add custom styles for a more visually appealing interface
        self.style = ttk.Style()
        sv_ttk.set_theme("dark")
        # Start the main event loop
        self.root.mainloop()
