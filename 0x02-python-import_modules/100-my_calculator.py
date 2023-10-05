#!/usr/bin/python3
if __name__ == "__main__":

    import calculator_1
    import sys


    if len(sys.argv) < 4:
      print("Usage: ./100-my_calculator.py <a> <operator> <b>")
      exit(1)

    oplist = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[3] not in list(oplist.keys()):
      print("Unknown operator. Available operators: +, -, * and /")
      exit(1)

    print("{} {} {} = {}".format(sys.argv[2],sys.argv[3],sys.argv[4],oplist[sys.argv[3]](sys.argv[2],sys.argv[4])))
