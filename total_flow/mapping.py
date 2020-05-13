def map(stack):
    file = open('推导产生式.txt','w')

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
        '变量赋值中间量': '1',
        '算术表达式中间量1': '2',
        '算术表达式中间量2': '3',
        '判断符': '4',
        '程序1': '5',
        '空': '~'
    }

    d1 = {v: k for k, v in dicVt.items()}
    d2 = {v: k for k, v in dicVn.items()}
    for str in stack:
        str = str.split('=>')
        sent = ''
        sent = sent + d2[str[0]] + ' => '
        for word in str[1]:
            if word in d1:
                sent = sent + d1[word] + ' '
            if word in d2:
                sent = sent + d2[word] + ' '
        file.write(sent+'\n')

