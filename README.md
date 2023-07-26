# Readme - Key Logger

This script is a simple key logger that records the keys pressed on the keyboard and logs them into a file named 'log.txt'. The purpose of this script is to demonstrate how to use the `keyboard` library to capture keyboard events and handle them with a callback function.

## Requirements

Before running this script, you need to have Python installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Also, make sure to install the required `keyboard` library by running the following command:

`pip install keyboard `

## Use

To run this code you need to be a superuser, run the following command:

`sudo main.py`

## How the Key Logger Works

The `when_press_the_key` function is the callback function used to handle keyboard events when a key is pressed. It utilizes the `keyboard.on_press` method to capture the key press events.

### Keys to Ignore

The script ignores certain keys, as specified in the `keys_to_ignore` list. The following keys will not be logged:

```
'alt', 'delete', 'tab', 'back', 'esc', 'ctrl', 'shift', 'win', 'caps lock',
'up', 'down', 'left', 'right', 'insert', 'home', 'page up', 'page down',
'end', 'num lock', 'scroll lock', 'pause', 'print screen', 'f1', 'f2',
'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12'

```

### Logging Behavior

The key logger records the keys as follows:

- The 'enter' key is logged as a new line.
- The 'space' key is logged as a space character.
- All other keys are logged as their names.

### File Output

The logged keys are appended to the 'log.txt' file in the current directory. The file is opened in UTF-8 encoding to ensure compatibility with various characters.
