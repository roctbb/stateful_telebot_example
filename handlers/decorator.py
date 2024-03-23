handlers = {}

def state_handler(event):
    def decorator(func):
        handlers[event] = func
        return func

    return decorator