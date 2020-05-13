dicVt = {
    # ; { }  ( ) 不做映射
    # =  + - * / 操作符统称 运算符 o
    # => == <= 作为 判断运算符judge j
    'int': 'a',
    'float': 'b',
    'COMMON': 'c',
    'IF': 'd',
    'ELSE': 'e',
    'FOR': 'f',
    '': 'g',
    '': 'h',
    'ID': 'i',
    'ABOVE': 'j',
    'EQUAL': 'j',
    'BELOW': 'j',
    'BREAK': 'k',
    '++': 'l',
    '--': 'l',
    'main': 'm',
    'CONTINUE': 'n',
    '运算符': 'o',
    '': 'p',
    '': 'q',
    'return': 'r',
    '': 's',
    '': 't',
    '': 'u',
    'void': 'v',
    'WHILE': 'w',
    '': 'x',
    '': 'y',
    '': 'z',
}

with open('result.txt', 'r') as f:
    texts = f.readlines()

sent = ''
for text in texts:
    text = text.split(',')
    text[0] = text[0].replace('(', '')
    text[1] = text[1].replace(' ', '')
    text[1] = text[1][:-2]
    text[1] = text[1].replace('\n', '')

    if text[1] == 'int' or text[1] == 'float' or text[1] == 'void' or text[1] == 'main' or text[1] == 'return' or text[
        1] == '++' or text[1] == '--':
        sent = sent + dicVt[text[1]]
    elif text[1] == '>=' or text[1] == '==' or text[1] == '<=':
        sent = sent + 'j'
    elif text[1] == 'while':
        sent = sent + dicVt['WHILE']
    elif text[1] == 'for':
        sent = sent + dicVt['FOR']
    elif text[1] == 'if':
        sent = sent + dicVt['IF']
    elif text[1] == 'else':
        sent = sent + dicVt['ELSE']
    elif text[1] == 'break':
        sent = sent + dicVt['BREAK']
    elif text[1] == 'continue':
        sent = sent + dicVt['CONTINUE']
    elif text[0] == '标识符':
        sent = sent + dicVt['ID']
    elif text[0] == '界符':
        sent = sent + text[1]
        continue
    elif text[0] == '运算符':
        sent = sent + text[1]
        continue
    elif text[0] == '常数':
        sent = sent + dicVt['COMMON']
        continue
    elif text[0] == '其他':
        continue
    else:
        sent = sent + text[1]

print(sent)
