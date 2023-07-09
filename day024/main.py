# Be careful. With VSCode, it doesn’t matter where you’re writing your python
# file in. VSCode derives their file path from where the IDE opened the folder.
# Other IDEs like Jupyter Lab will derive their file path from the file you are
# working with.
# But this default behavior can be overridden by setting
# python.terminal.executeInFileDir to true in settings.
# https://stackoverflow.com/questions/69769139/relative-file-path-is-not-recognized-by-python-in-vscode

with open('Names/invited_names.txt') as names:
# with open('day024/Names/invited_names.txt') as names:
    with open('Letters/starting_letter.txt') as starting_letter:
    # with open('day024/Letters/starting_letter.txt') as starting_letter:
        first_line = starting_letter.readline()
        rest_lines = starting_letter.read()
    for name in names.readlines():
        name = name.strip()
        with open(f'ReadyToSend/letter_to_{name.replace(" ", "_")}.txt', 'w+') as new_letter:
        # with open(f'day024/ReadyToSend/letter_to_{name.replace(" ", "_")}.txt', 'w+') as new_letter:
            new_letter.write(first_line.replace('[name]', name))
            new_letter.write(rest_lines)