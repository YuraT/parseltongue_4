def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, "42")
            print(s1)
        print('\n')

print_format_table()

def write_colorful_text(string, style, background, foreground):
    s1 = ''
    format = ";".join([str(style), str(foreground), str(background)])
    s1 += '\x1b[%sm %s \x1b[0m' % (format, string)
    return s1

print(write_colorful_text("R", 0, 47, 31), end = " ")
print(write_colorful_text("A", 2, 47, 30), end = " ")
print(write_colorful_text("I", 1, 47, 33), end = " ")
print(write_colorful_text("N", 3, 47, 32), end = " ")
print(write_colorful_text("B", 4, 47, 36), end = " ")
print(write_colorful_text("O", 5, 47, 34), end = " ")
print(write_colorful_text("W", 6, 47, 35), end = " ")