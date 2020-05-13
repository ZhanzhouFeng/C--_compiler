"""
    Created by ws
"""
"""
 文法：
    E->E+T | T
    T->T*F | F
    F->(E)|i
 消除左递归：
    E->TH
    H->+TH|e(e替代空)
    T->FY
    Y->*FY|e
    F->(E)|i
 非终结符：
    E，H，T，Y，F
 终结符:
    i,+,*,(,),#
"""

# 手动构造预测分析表
# dists = {
#     ('E', 'i'): 'TH',
#     ('E', '('): 'TH',
#     ('H', '+'): '+TH',
#     ('H', ')'): 'e',
#     ('H', '#'): 'e',
#     ('T', 'i'): 'FY',
#     ('T', '('): 'FY',
#     ('Y', '+'): 'e',
#     ('Y', '*'): '*FY',
#     ('Y', ')'): 'e',
#     ('Y', '#'): 'e',
#     ('F', 'i'): 'i',
#     ('F', '('): '(E)',
# }
dists = {
    ('A', 'a'): 'B5',
    ('A', 'b'): 'B5',
    ('A', 'v'): 'B5',
    ('5', '~'): '~',
    ('5', 'a'): 'B',
    ('5', 'b'): 'B',
    ('5', 'v'): 'B',
    ('B', 'a'): 'CX(D){E}',
    ('B', 'b'): 'CX(D){E}',
    ('B', 'v'): 'CX(D){E}',
    ('C', 'a'): 'a',
    ('C', 'b'): 'b',
    ('C', 'v'): 'v',
    ('X', 'i'): 'i',
    ('X', 'm'): 'm',
    ('D', '~'): '~',
    ('D', ')'): '~',
    ('D', 'a'): 'GX,D',
    ('D', 'b'): 'GX,D',
    ('D', 'n'): 'GX,D',
    ('D', 'k'): 'GX,D',
    ('D', 'r'): 'GX,D',
    ('D', 'd'): 'GX,D',
    ('D', 'f'): 'GX,D',
    ('D', 'w'): 'GX,D',
    ('E', '{'): 'YE',
    ('E', 'a'): 'YE',
    ('E', 'b'): 'YE',
    ('E', 'i'): 'YE',
    ('E', ';'): 'YE',
    ('E', 'n'): 'YE',
    ('E', 'k'): 'YE',
    ('E', 'r'): 'YE',
    ('E', 'd'): 'YE',
    ('E', 'f'): 'YE',
    ('E', 'w'): 'YE',
    ('Y', '{'): 'I',
    ('Y', 'a'): 'G',
    ('Y', 'b'): 'G',
    ('Y', 'i'): 'K',
    ('Y', ';'): 'H',
    ('Y', 'n'): 'G',
    ('Y', 'k'): 'G',
    ('Y', 'r'): 'G',
    ('Y', 'd'): 'G',
    ('Y', 'f'): 'G',
    ('Y', 'w'): 'G',
    ('H', ';'): ';',
    ('I', '{'): '{E}',
    ('F', 'a'): 'GK;',
    ('F', 'b'): 'GK;',
    ('F', 'n'): 'GK;',
    ('F', 'k'): 'GK;',
    ('F', 'r'): 'GK;',
    ('F', 'd'): 'GK;',
    ('F', 'f'): 'GK;',
    ('F', 'w'): 'GK;',
    ('G', 'a'): 'a',
    ('G', 'b'): 'b',
    ('G', 'n'): 'Q',
    ('G', 'k'): 'R',
    ('G', 'r'): 'S',
    ('G', 'd'): 'T',
    ('G', 'f'): 'W',
    ('G', 'w'): 'W',
    ('K', 'i'): 'i1',
    ('1', '~'): '~',
    ('1', ')'): '~',
    ('1', '{'): '~',
    ('1', '}'): '~',
    ('1', 'a'): '~',
    ('1', 'b'): '~',
    ('1', 'i'): '~',
    ('1', ';'): '~',
    ('1', '='): '=Z;',
    ('1', 'l'): 'l',
    ('1', 'n'): '~',
    ('1', 'k'): '~',
    ('1', 'r'): '~',
    ('1', 'd'): '~',
    ('1', 'f'): '~',
    ('1', 'w'): '~',
    ('Z', '('): 'M2',
    ('Z', 'i'): 'M2',
    ('Z', 'm'): 'M2',
    ('Z', 'c'): 'M2',
    ('2', '~'): '~',
    ('2', ')'): '~',
    ('2', ';'): '~',
    ('2', '+'): '+3',
    ('2', '-'): '-3',
    ('3', '('): 'M2',
    ('3', 'i'): 'M2',
    ('3', 'm'): 'M2',
    ('3', 'c'): 'M2',
    ('M', '('): 'N',
    ('M', 'i'): 'N',
    ('M', 'm'): 'N',
    ('M', 'c'): 'N',
    ('N', '('): '(Z)',
    ('N', 'i'): 'X',
    ('N', 'm'): 'X',
    ('N', 'c'): 'O',
    ('O', 'c'): 'c',
    ('P', '('): 'N4N',
    ('P', 'i'): 'N4N',
    ('P', 'm'): 'N4N',
    ('P', 'c'): 'N4N',
    ('4', 'j'): 'j',
    ('Q', 'n'): 'n;',
    ('R', 'k'): 'k;',
    ('S', 'r'): 'rZ;',
    ('T', 'd'): 'dUVgV',
    ('U', '('): '(P)',
    ('V', '{'): '{E}',
    ('W', 'f'): 'f(F;U;K)V',
    ('W', 'w'): 'wUV',
    ('E', '}'): '~',
    ('5', '#'): '~',
}
# 构造终结符集合
# -*- coding:UTF-8 -*-
Vt = [chr(i) for i in range(ord("a"), ord("z") + 1)]
temp = ['e', 'h', 'p', 'q', 's', 't', 'u', 'x', 'y']
for i in temp:
    Vt.remove(i)
temp = ['(', ')', ';', '=', '+', '-', '*', '/', ',', '{', '}']
for i in temp:
    Vt.append(i)

# 构造非终结符集合
Vh = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
Vh.append('1')


# 获取符号栈中的内容
def printstack(stack):
    rtu = ''
    for i in stack:
        rtu += i
    return rtu


# 得到输入串剩余串
def printstr(str, index):
    rtu = ''
    for i in range(index, len(str), 1):
        rtu += str[i]
    return rtu


# 定义error函数
def error():
    print('Error')
    exit()


# 总控程序
def masterctrl(str):
    stack_pro = []
    '''
    总控程序，用于进程文法的判断
    '''
    # 用列表模拟栈
    stack = []
    # 位置
    location = 0
    # 将#号入栈
    stack.append(str[location])

    # 将文法开始符入栈
    stack.append('A')

    # 将输入串第一个字符读进a中
    location += 1
    a = str[location]

    # 判断循环用标签
    flag = True
    count = 0

    print('%d\t\t%s\t\t%s' % (count, printstack(stack), printstr(str, location)))
    while flag:
        if count == 0:
            pass
        else:
            # 由于第一轮不触发此 else 所以x定义在后方  x是符号栈的栈顶
            if x in Vt:
                # Vt是终结符集 假设x是终结符，那么输出
                print('%d\t\t%s\t\t%s' % (count, printstack(stack), printstr(str, location)))

            else:
                # x是非终结符  s是产生式的右部
                print('%d\t\t%s\t\t%s\t\t%s->%s' % (count, printstack(stack), printstr(str, location), x, s))
                sttt = x + '=>' + s
                stack_pro.append(sttt)

        # 获取符号栈顶
        x = stack.pop()

        # 如果符号栈顶是终结符，那么一定是匹配字符串的当前位置的
        if x in Vt:
            # 符合条件，同时消除
            if x == str[location]:
                location += 1
                a = str[location]
            # 若不是 则报错
            else:
                error()

        # 如果 符号栈读入#且字符串当前位置也是#　结束
        elif x == '#':
            if x == a:
                flag = False
            else:
                error()

        # 判断移进-归约
        elif (x, a) in dists.keys():
            s = dists[(x, a)]
            # 反向入站
            for i in range(len(s) - 1, -1, -1):
                # 如果为空，跳过 不为空，加入符号栈
                if s[i] != '~':
                    stack.append(s[i])
                    # print(stack)
        # 错误处理
        else:
            error()
        count += 1
    return stack_pro


def main(str):
    print("步骤\t\t符号栈\t\t输入串\t\t\t所用产生式")
    str = '#' + str + '#'
    stack = masterctrl(str)
    return stack


if __name__ == '__main__':
    str = 'vm(){ai=c;ai=c;ai=c;w(iji){i=i+i;il;il;}ri;}'
    main(str)
