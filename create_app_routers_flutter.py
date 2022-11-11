import os
import sys


def get_arguments():
    print(len(sys.argv))
    # if len(sys.argv) > 1:
    #     path = sys.argv[1]
    #     if os.path.exists(path):
    #         names:list[str] = []
    #         walk = os.walk(path, topdown=True)
    #         for minipath in walk:
    #             splitted = str(minipath[0]).split('/')
    #             if (len(path.split('/')) + 1) == len(splitted):
    #                 names.append(splitted[len(splitted) - 1])
    #         return names
    #     else:
    #         print('The path does not exists')
    #         sys.exit(1)
    # else:
    #     print('Introduce the argunemnt.')
    #     sys.exit(1)


def main():
    # names = get_arguments()
    # print(names)
    pass


if __name__ == '__main__':
    main()