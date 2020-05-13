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
    '': 'l',
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

dicVn={
    '程序':'A',
    '外部声明':'B',
    '函数类型':'C',
    '形参列表':'D',
    '函数体语句':'E',
    '声明语句':'F',
    '控制语句':'G',
    '空语句':'H',
    '复合语句':'I',
    '数据类型':'G',
    '变量赋值':'K',
    '算数表达式':'L',
    '乘除项':'M',
    '元素':'N',
    '常量':'O',
    '判断':'P',
    'continue语句':'Q',
    'break语句':'R',
    'return语句':'S',
    '条件判断语句':'T',
    '判断条件':'U',
    '条件执行':'V',
    '循环语句':'W',
    '标识符':'X',
    '语句':'Y',
    '算术表达式':'Z',
}
with open('产生式.txt','r',encoding='UTF-8') as f:
    texts = f.readlines()

for text in texts:
    # print(text)
    text = text.split(' ')
    text[-1] = text[-1].split('\n')[0]
    sent = ''
    count =0
    for word in text:
        count+=1
        if word.replace('$','') in dicVt:
            sent = sent +' '+dicVt[word.replace('$','')]
        elif word in dicVn:
            sent = sent+' '+dicVn[word]
        elif count==2:
            sent = sent + ' =>'
        else:
            sent = sent+' '+word

    print(sent)
