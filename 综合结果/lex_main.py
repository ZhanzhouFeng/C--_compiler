from total_flow import preprocess, process

def lex_main():
    preprocess.preprocess('file.txt')
    process.process('preprocess.txt')

if __name__=='__main__':
    lex_main()