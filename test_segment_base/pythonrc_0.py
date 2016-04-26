# Set up history saving on exit.
def save(history=history, readline=readline, application=application):
    readline.write_history_file(history)
