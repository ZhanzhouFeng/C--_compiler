import total_flow.LL1 as LL1
import total_flow.get_result as get_result
import total_flow.mapping as mapping


def gram_main():
    str = get_result.get_result()
    stack = LL1.main(str)
    mapping.map(stack)


if __name__ == '__main__':
    gram_main()
