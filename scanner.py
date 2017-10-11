#! -*- coding:utf-8 -*-
from util import CharType
from util import KeyWord
from util import TKType


class Scanner(object):

    def __init__(self, content):
        self.__content = content
        self.__lexical = []  # (Type, Word)
        self.__index = 0
    def GetLex(self):
        return self.__lexical

    def PrintLexical(self):
        idx = 0
        for x, y in self.__lexical:
            if x == TKType.TK_IDENT:
                print idx, y
                idx += 1
                continue
            v = TKType.TSTWDMAP.get(x, None)
            if v is not None:
                if y is not None:
                    print idx, v, y
                else:
                    print idx, v
            else:
                if y is None:
                    print idx, x
                else:
                    print idx, x, y
            idx += 1

    def __analyze_word(self):
        start_idx = self.__index
        self.__index += 1
        while self.__content[self.__index] in CharType.ALPHABET or self.__content[self.__index] in CharType.UNDERLINE or self.__content[self.__index] in CharType.DIGIT:
            self.__index += 1
        word = self.__content[start_idx : self.__index]
        if word in KeyWord.SKIP_WD:
            return True
        elif word in KeyWord.WD:
            ty = TKType.WDMAP[word]
            self.__lexical.append((ty, None))
        else:
            self.__lexical.append((TKType.TK_IDENT, word))
        return True

    def __analyze_digit(self):
        start_idx = self.__index
        if self.__content[self.__index] == "0":
            self.__index += 1
            is_float = False
            if self.__content[self.__index] == ".":
                is_float = True
            elif self.__content[self.__index] in CharType.DEXFLAG:
                self.__index += 1
                while self.__content[self.__index] in CharType.DEXDIGIT:
                    self.__index += 1
                num = self.__content[start_idx : self.__index]
                self.__lexical.append((TKType.TK_CINT, num))
            else:
                while self.__content[self.__index] in CharType.DIGIT:
                    self.__index += 1
                num = self.__content[start_idx : self.__index]
                if is_float:
                    self.__lexical.append((TKType.TK_CFLOAT, num))
                else:
                    self.__lexical.append((TKType.TK_CINT, num))
        else:
          self.__index += 1
          is_float = False
          if self.__content[self.__index] == ".":
              is_float = True
              self.__index += 1
          while self.__content[self.__index] in CharType.DIGIT:
              self.__index += 1

          num = self.__content[start_idx : self.__index]
          if is_float:
              self.__lexical.append((TKType.TK_CFLOAT, num))
          else:
              self.__lexical.append((TKType.TK_CINT, num))
        return True

    def __analyze_string(self):
        start_idx = self.__index
        idx = self.__content.find('"', start_idx + 1)
        if idx < 0:
            return False
        str_ = self.__content[start_idx : idx + 1]
        self.__lexical.append((TKType.TK_CSTR, str_))
        self.__index = idx + 1
        return True

    def __analyze_char(self):
        start_idx = self.__index
        idx = self.__content.find("'", start_idx + 1)
        if idx < 0:
            return False
        str_ = self.__content[start_idx : idx + 1]
        self.__lexical.append((TKType.TK_CCHAR, str_))
        self.__index = idx + 1
        return True

    def __analyze_macro(self):
        self.__index += 1
        cnt = 0 # num of '\'
        while True:
            if self.__content[self.__index] in CharType.DIVIDE:
                self.__index += 1
                self.__analyze_comment()
            elif self.__content[self.__index] in CharType.CNT:
                cnt += 1
            elif self.__content[self.__index] in CharType.NL:
                if cnt > 0:
                    cnt -= 1
                    self.__index += 1
                else:
                    return True
            self.__index += 1
            if self.__index >= len(self.__content):
                return True

    def __analyze_comment(self):
        if self.__content[self.__index] in CharType.DIVIDE:
            idx = self.__content.find('\n', self.__index)
            if idx < 0:
                return False
            self.__index = idx
        elif self.__content[self.__index] in CharType.STAR:
            idx = self.__content.find('*/', self.__index)
            if idx < 0:
                return False
            self.__index = idx + 2
        else:
            return False
        return True

    def __analyze_div(self):
        start_idx = self.__index
        self.__index += 1
        if self.__analyze_comment():
            return True
        elif self.__content[self.__index] in CharType.EQUAL:
            self.__lexical.append((TKType.TK_DE, None))
            self.__index += 1
        elif self.__content[self.__index] == '-':
            self.__lexical.append((TKType.TK_MM, None))
            self.__index += 1
        else:
            self.__lexical.append((TKType.TK_DIVIDE, None))
        return True
    def __analyze_bracket(self):
        if self.__content[self.__index] == '(':
            self.__lexical.append((TKType.TK_PTHSL, None))
        elif self.__content[self.__index] == ')':
            self.__lexical.append((TKType.TK_PTHSR, None))
        elif self.__content[self.__index] == '[':
            self.__lexical.append((TKType.TK_BRCTL, None))
        elif self.__content[self.__index] == ']':
            self.__lexical.append((TKType.TK_BRCTR, None))
        elif self.__content[self.__index] == '{':
            self.__lexical.append((TKType.TK_BEGIN, None))
        elif self.__content[self.__index] == '}':
            self.__lexical.append((TKType.TK_END, None))
        self.__index += 1

    def analyze(self):
        length = len(self.__content)
        while self.__index < length:
            if self.__content[self.__index] in CharType.SPACE:
                self.__index += 1
            elif self.__content[self.__index] in CharType.MACRO:
                # macro not parse
                self.__analyze_macro()
            elif self.__content[self.__index] in CharType.ALPHABET or self.__content[self.__index] in CharType.UNDERLINE:
                if not self.__analyze_word():
                    break
            elif self.__content[self.__index] in CharType.DIGIT:
                if not self.__analyze_digit():
                    break
            elif self.__content[self.__index] in CharType.STR:
                if not self.__analyze_string():
                    break
            elif self.__content[self.__index] in CharType.CHAR:
                if not self.__analyze_char():
                    break
            elif self.__content[self.__index] in CharType.DIVIDE:
                if not self.__analyze_div():
                    break
            elif self.__content[self.__index] in CharType.PLUS:
                self.__index += 1
                if self.__content[self.__index] == '=':
                    self.__lexical.append((TKType.TK_PE, None))
                    self.__index += 1
                elif self.__content[self.__index] == '+':
                    self.__lexical.append((TKType.TK_PP, None))
                    self.__index += 1
                else:
                    self.__lexical.append((TKType.TK_PLUS, None))

            elif self.__content[self.__index] in CharType.MINUS:
                self.__index += 1
                if self.__content[self.__index] == '=':
                    self.__lexical.append((TKType.TK_ME, None))
                    self.__index += 1
                else:
                    self.__lexical.append((TKType.TK_MINUS, None))
            elif self.__content[self.__index] in CharType.STAR:
                self.__index += 1
                if self.__content[self.__index] == '=':
                    self.__lexical.append((TKType.TK_SE, None))
                    self.__index += 1
                else:
                    self.__lexical.append((TKType.TK_STAR, None))
            elif self.__content[self.__index] in CharType.MOD:
                self.__index += 1
                if self.__content[self.__index] == '=':
                    self.__lexical.append((TKType.TK_MDE, None))
                    self.__index += 1
                else:
                    self.__lexical.append((TKType.TK_MOD, None))
            elif self.__content[self.__index] in CharType.EQUAL:
                self.__index += 1
                if self.__content[self.__index] == '=':
                    self.__lexical.append((TKType.TK_EQ, None))
                    self.__index += 1
                else:
                    self.__lexical.append((TKType.TK_ASSIGN, None))
            elif self.__content[self.__index] in CharType.EXCLA:
                self.__index += 1
                if self.__content[self.__index] == '=':
                    self.__lexical.append((TKType.TK_NEQ, None))
                    self.__index += 1
                else:
                    self.__lexical.append((TKType.TK_NOT, None))
            elif self.__content[self.__index] in CharType.BTBT:
                self.__index += 1
                if self.__content[self.__index] == '=':
                    self.__lexical.append((TKType.TK_BTE, None))
                    self.__index += 1
                else:
                    self.__lexical.append((TKType.TK_BT, None))
            elif self.__content[self.__index] in CharType.MT:
                self.__index += 1
                if self.__content[self.__index] == '=':
                    self.__lexical.append((TKType.TK_MET, None))
                    self.__index += 1
                elif self.__content[self.__index] == '>':
                    self.__lexical.append((TKType.TK_MOVR, None))
                    self.__index += 1
                else:
                    self.__lexical.append((TKType.TK_MT, None))
            elif self.__content[self.__index] in CharType.LT:
                self.__index += 1
                if self.__content[self.__index] == '=':
                    self.__lexical.append((TKType.TK_LET, None))
                    self.__index += 1
                elif self.__content[self.__index] == '<':
                    self.__lexical.append((TKType.TK_MOVL, None))
                    self.__index += 1
                else:
                    self.__lexical.append((TKType.TK_LT, None))
            elif self.__content[self.__index] in CharType.AND:
                self.__index += 1
                if self.__content[self.__index] == '=':
                    self.__lexical.append((TKType.TK_ANDE, None))
                    self.__index += 1
                elif self.__content[self.__index] == '&':
                    self.__lexical.append((TKType.TK_AND, None))
                    self.__index += 1
                else:
                    self.__lexical.append((TKType.TK_ADDR, None))
            elif self.__content[self.__index] in CharType.OR:
                self.__index += 1
                if self.__content[self.__index] == '=':
                    self.__lexical.append((TKType.TK_BE, None))
                    self.__index += 1
                elif self.__content[self.__index] == '|':
                    self.__lexical.append((TKType.TK_OR, None))
                    self.__index += 1
            elif self.__content[self.__index] in CharType.BRACKET:
                self.__analyze_bracket()
            elif self.__content[self.__index] in CharType.SEMICOLON:
                self.__lexical.append((TKType.TK_SEMICOLON, None))
                self.__index += 1
            elif self.__content[self.__index] in CharType.POINT:
                if (self.__content[self.__index + 1] == '.' and
                        self.__content[self.__index + 2] == '.'):
                    self.__lexical.append((TKType.TK_ELLIPSIS, None))
                    self.__index += 3
                else:
                    self.__lexical.append((TKType.TK_DOT, None))
                    self.__index += 1
            elif self.__content[self.__index] in CharType.COMMA:
                self.__lexical.append((TKType.TK_COMMA, None))
                self.__index += 1
            elif self.__content[self.__index] in CharType.QUES:
                self.__lexical.append((TKType.TK_QUES, None))
                self.__index += 1
            elif self.__content[self.__index] in CharType.COLON:
                self.__lexical.append((TKType.TK_COLON, None))
                self.__index += 1
            elif self.__content[self.__index] in CharType.NL:
                self.__index += 1
            elif self.__content[self.__index] in CharType.NOLINE:
                idx = self.__content.find('\n', self.__index)
                if idx > 0:
                    self.__index = idx + 1
                else:
                    self.__index += 1
            else:
                self.__index += 1
        self.__lexical.append((TKType.TK_EOF, None))
