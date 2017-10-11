from scanner import Scanner

import sys

if __name__ == "__main__":
    file_ = open(sys.argv[1], 'r')
    content_ = file_.read()
    scanner_ = Scanner(content_)
    file_.close()
    scanner_.analyze()
    scanner_.PrintLexical()
