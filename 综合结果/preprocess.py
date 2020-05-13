# 预处理函数，对例程进行预处理，去掉多余的空格、注释
def preprocess(file_name):
    # try:  # try except 使程序不会因为异常而中断
        fp_read = open(file_name, 'r',encoding='GBK')  # 打开需要分析的文件
        fp_write = open('preprocess.txt', 'w')
        sign = 0  # 每当上一个字符为空格时，将sign变为1，通过这样来保证每个需要空格的地方不会有多余的空格
        signl=0
        while True:
            read = fp_read.readline()  # 循环读取每一行字符
            if not read:
                break  # 如果没有读取到任何东西直接结束循环
            length = len(read)  # 获得当前字符串的长度
            i = -1
            while i < length - 1:  # 循环读取每个字符
                i += 1
                #判断 /* and */ 组成的注释
                if signl==1:
                    try :
                        if read[i-1]=='*' and read[i]=='/':
                            i +=1
                            signl=0
                        else:
                            continue
                    except:
                        continue
                #空字符处理
                if read[i] == ' ':
                    if sign == 1:  # 读取到空格，如果sign为1说明上一个字符也是空格，那个可以忽略当前空格
                        continue
                    else:  # 如果sign不为1，说明上一个字符不是空格，那么就输出当前空格
                        sign = 1
                        fp_write.write(' ')
                elif read[i] == '\t':  # 同上读取到空格的操作，对于水平制表符（tab）同样输出为一个空格，如果已经输出过一个空格了那就选择跳过
                    if sign == 1:
                        continue
                    else:
                        sign = 1
                        fp_write.write('')
                elif read[i] == '\n':  # 同上读取到水平制表符（tab）的操作
                    if sign == 1:
                        continue
                    else:
                        sign = 1
                        fp_write.write(' ')
                #注释处理
                elif read[i] == '/' and read[i + 1] == '*':  # 如果读取到/* 即注释
                    signl=1
                    # i = i + 2  # 从星号之后的第一个字符开始遍历直到读取到下一对注释
                    # while True:
                    #     if read[i] == '*' and read[i + 1] == '/':
                    #         break
                    #     i = i + 1
                    # i = i + 1  # 遍历完之后i停留在左斜杠，所以需要+1达到下一个字符
                elif read[i]=='/' and read[i+1]=='/':
                    break

                #存疑 这个我没用过呀
                elif read[i] == '\\':  # 如果读取到续行符，之所以是双斜杠因为右斜杠是转义字符，双右斜杠等于单右斜杠，即续行符
                    break
                else:  # 除了以上这些就直接输出字符就好
                    fp_write.write(read[i])
                    sign = 0
        #存疑，这＃会不会影响include
        fp_write.write('#')  # 在最后输出一个井号
    # except Exception:
    #     # print(Exception)
    #     print('Errors')

if __name__=='__main__':
    preprocess('file.txt')
    # preprocess('error.txt')
    _=1