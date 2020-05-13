def get_result(text='result.txt'):
    dicVt = {
        # ; { }  ( ) 不做映射
        # =  + - * / 操作符统称 运算符 o
        # => == <= 作为 判断运算符judge j
        'int': 'a',
        'float': 'b',
        'COMMON': 'c',
        'IF': 'd',
        '出现错误': 'e',
        'FOR': 'f',
        'ELSE': 'g',
        '出现错误': 'h',
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
        '出现错误': 'p',
        '出现错误': 'q',
        'return': 'r',
        '出现错误': 's',
        '出现错误': 't',
        '出现错误': 'u',
        'void': 'v',
        'WHILE': 'w',
        '出现错误': 'x',
        '出现错误': 'y',
        '出现错误': 'z',
    }

    dicVn = {
        '程序': 'A',
        '外部声明': 'B',
        '函数类型': 'C',
        '形参列表': 'D',
        '函数体语句': 'E',
        '声明语句': 'F',
        '控制语句': 'G',
        '空语句': 'H',
        '复合语句': 'I',
        '数据类型': 'G',
        '变量赋值': 'K',
        '算数表达式': 'L',
        '乘除项': 'M',
        '元素': 'N',
        '常量': 'O',
        '判断': 'P',
        'continue语句': 'Q',
        'break语句': 'R',
        'return语句': 'S',
        '条件判断语句': 'T',
        '判断条件': 'U',
        '条件执行': 'V',
        '循环语句': 'W',
        '标识符': 'X',
        '语句': 'Y',
        '算术表达式': 'Z',
        '变量赋值中间量': '1\'',
        '算术表达式中间量1': '2',
        '算术表达式中间量2': '3',
        '判断符': '4',
        '程序1': '5'
    }

    with open(text, 'r') as f:
        texts = f.readlines()

    sent = ''
    for text in texts:
        text = text.split(',')
        text[0] = text[0].replace('(', '')
        text[1] = text[1].replace(' ', '')
        text[1] = text[1][:-2]
        text[1] = text[1].replace('\n', '')

        if text[1] == 'int' or text[1] == 'float' or text[1] == 'void' or text[1] == 'main' or text[1] == 'return' or \
                text[
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
    return sent


if __name__ == '__main__':
    print(get_result())
