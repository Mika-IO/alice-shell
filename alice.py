import tkinter as tk
import tkinter.ttk as ttk
from terminal.terminal import Terminal

# Define the root window and its title
root = tk.Tk()
root.title("Browser")

# Define the menu bar and its options
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New Tab", accelerator="Ctrl+N")
filemenu.add_command(label="Close Tab", accelerator="Ctrl+W")
filemenu.add_separator()
filemenu.add_command(label="Exit", accelerator="Ctrl+Q")
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

# Define the tab control and its initial tab
notebook = ttk.Notebook(root)
terminal = Terminal(notebook, pady=5, padx=5)
terminal.shell = True

terminal.pack(expand=True, fill="both")
notebook.add(terminal, text="$h&ll")
notebook.pack(fill="both", expand=True)

# Handle keyboard shortcuts using bindings
def handle_keyboard_shortcuts(event):
    if event.keysym == "n" and event.state == 12:  # Ctrl+N on Windows
        terminal = Terminal(notebook, pady=5, padx=5)
        terminal.shell = True
        notebook.add(terminal, text=f"$h&ll")
        notebook.select(notebook.index("end"))
    elif event.keysym == "w" and event.state == 12:  # Ctrl+W on Windows
        index = notebook.index(notebook.select())
        if index > 0:
            notebook.forget(index)
            notebook.select(index - 1)
        elif index == 0 and notebook.index("end") == 1:
            root.destroy()
        else:
            notebook.forget(index)
            notebook.select(index)
        print(notebook.index("end"))
    elif event.keysym == "q" and event.state == 12:  # Ctrl+Q on Windows
        root.destroy()


# Bind keyboard shortcuts to the root window
root.bind("<Control-n>", handle_keyboard_shortcuts)
root.bind("<Control-N>", handle_keyboard_shortcuts)  # Ctrl+N on Windows
root.bind("<Control-w>", handle_keyboard_shortcuts)
root.bind("<Control-W>", handle_keyboard_shortcuts)  # Ctrl+W on Windows
root.bind("<Control-q>", handle_keyboard_shortcuts)
root.bind("<Control-Q>", handle_keyboard_shortcuts)  # Ctrl+Q on Windows


# Start the main event loop
root.mainloop()
