#TODO: this is a test for the following function
def find_tasks(source_code):
    """Find tasks in source code (TODO, FIXME, XXX, ...)"""
    results = []
    for line, text in enumerate(source_code.splitlines()):
        for todo in re.findall(TASKS_PATTERN, text):
            results.append((todo[-1].strip().capitalize(), line+1))
    return results
