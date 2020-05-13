from 词法分析 import preprocess, process

if __name__=='__main__':
    preprocess.preprocess('file.txt')
    process.process('preprocess.txt')