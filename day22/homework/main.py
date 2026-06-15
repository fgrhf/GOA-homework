#დავალება1
def string_to_integer(text):
    if not text:
        return "invalid input"
    check_text = text
    if text[0] == '-':
        check_text = text[1:]
        if not check_text:
            return 'invalid input'
    if check_text.isdigit():
        return int(text)
    else:
        return "invalid input"