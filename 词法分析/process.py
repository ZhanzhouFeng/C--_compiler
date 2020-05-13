# K:关键字 I:标识符 C:常数 O:运算符 P:界符 L：标号

delimiters = ['{', '}', '(', ')',';']

operators = ['+', '-', '*', '/', '=', '>=', '==', '<=','++']

operators_first=['+', '-', '*', '/', '=', '>', '=', '<']

key_words = ['while', 'break', 'continue', 'for', 'if', 'else', 'float', 'int', 'void', 'return', 'main']


def process(file_name):
    try:
        #读写文件
        read = open(file_name, 'r', encoding='utf-8')          # 打开预处理之后得到的文件
        write = open('result.txt', 'w', encoding='GBK')  # 打开一个新的文件，为了将得到的二元式表输入进去

        lines = read.readlines()  # 依旧是按行读取

        for line in lines:  # 逐行遍历
            length = len(line)  # 获得当前行字符长度为了遍历每个字符
            i = -1
            while i < length - 1:
                i += 1
                #判断所有非letter字符

                # 当前字符为空格，直接跳过
                if line[i] == ' ':
                    continue
                # 当前字符在最开始定义的界符集中，那么就直接输出（界符，当前字符）
                elif line[i] in delimiters:
                    print('(界符,', line[i], ')', file=write)
                    continue
                # 当前字符在运算符集首字符中
                elif line[i] in operators_first:
                    if (line[i] == '<' or line[i] == '>' or line[i] == '=') and line[i + 1]=='=' and i < length - 1:
                            print('(运算符,',line[i], line[i + 1], ')', sep='', file=write)  # sep=''实现print连续输出不加空格，为了输出>=而不是> =
                            i+=1
                    elif line[i] == '+'  and line[i + 1] == '+' and i < length - 1:
                        print('(运算符,', line[i], line[i + 1], ')', sep='',
                              file=write)  # sep=''实现print连续输出不加空格，为了输出>=而不是> =
                        i += 1
                    elif line[i] == '-'  and line[i + 1] == '-' and i < length - 1:
                        print('(运算符,', line[i], line[i + 1], ')', sep='',
                              file=write)  # sep=''实现print连续输出不加空格，为了输出>=而不是> =
                        i += 1
                    elif line[i] in operators and line[i+1] in operators:
                        flag2=1
                        total =''
                        while flag2:
                            total+=line[i]
                            i=i+1
                            if line[i] not in operators:
                                flag2=0
                                i = i - 1
                        print('(其他,', total, ')', file=write)

                    elif line[i] in operators:
                        print('(运算符,',line[i], ')', file=write)
                    else:
                        print('(其他,', line[i], ')', file=write)

                    continue

                elif line[i].isdigit() or line[i]=='.':
                    fsign = 0
                    error_flag=0
                    str=line[i].__str__()
                    if line[i]=='.':
                        fsign=1
                    while i < length-1 and line[i+1] not in delimiters and line[i+1] not in operators_first and line[i+1]!=' ':
                        i+=1
                        str+=line[i]
                        if line[i]=='.':
                            fsign = 1
                        elif not line[i].isdigit():
                            error_flag=1


                    if fsign==1:
                        #小数点个数和开头不能为0判断
                        flag1=0
                        # print(str)
                        for i1 in str:
                            # print(i1)
                            if i1=='.':
                                flag1+=1
                        if str[0]=='0' and len(str)>1:
                            flag1=5
                        if flag1>=2:
                            print('(其他,', str, ')', file=write)
                        else:
                            print('(常数,', str,')', file=write)
                    elif error_flag==1:
                        print('(其他,', str, ')', file=write)
                    else:
                        print('(常数,',str, ')', file=write)
                    continue
                elif line[i]=='#':
                    break

                error_flag=0
                temp=''
                while True:
                    #当标识符字符串结束：
                    if line[i] == ' ' or line[i] in operators_first or line[i] in delimiters:
                        break
                    else:
                        if (not line[i].isalnum()) and line[i]!='_':
                            error_flag=1
                        temp+=line[i]

                    if i < length - 1:
                        i += 1

                i-=1
                if temp in key_words:
                    print('(关键字,', temp, ')', file=write)
                elif error_flag==1:
                    print('(其他,', temp, ')', file=write)
                else:
                    print('(标识符,', temp, ')', file=write)

    except Exception as e:
        print(e)
        print('Error')


if __name__ == '__main__':
    process('preprocess.txt')
