# Create three decorators: make_bold, make_italic, and make_underline,
# which will have to wrap a text returned from a function in <b></b>, <i></i> and <u></u> respectively.

def make_bold(function):
    def wrapped(*args):
        return f"<b>{function(*args)}</b>"
    return wrapped


def make_italic(function):
    def wrapped(*args):
        return f"<i>{function(*args)}</i>"
    return wrapped


def make_underline(function):
    def wrapped(*args):
        return f"<u>{function(*args)}</u>"
    return wrapped


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
