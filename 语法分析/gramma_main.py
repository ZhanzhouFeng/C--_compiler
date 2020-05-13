import LL1
import get_result
import mapping


def gram_main():
    str = get_result.get_result()
    stack = LL1.main(str)
    mapping.map(stack)


if __name__ == '__main__':
    gram_main()
