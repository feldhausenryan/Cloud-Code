# backwards compatible interface
def tokenize_loop(readline, tokeneater):
    for token_info in generate_tokens(readline):
        tokeneater(*token_info)
