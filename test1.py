import readline
import rlcompleter

# enable tab completion
readline.parse_and_bind("tab: complete")

# define a list of possible tab completions
options = ["apple", "banana", "cherry", "date", "elderberry"]

# define a function to provide tab completion
def tab_complete(text, state):
    options = [option for option in options if option.startswith(text)]
    try:
        return options[state]
    except IndexError:
        return None


# set the tab completion function
readline.set_completer(tab_complete)
