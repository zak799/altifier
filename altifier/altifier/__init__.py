def alty_text(text):
    output = []
    switchy = True
    for char in text:
        if char.isalpha():
            if switchy:
                output.append(char.upper())
            else:
                output.append(char.lower())
            switchy = not switchy
        else:
            output.append(char)
    return ''.join(output)
