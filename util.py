#! -*- coding:utf-8 -*-
class CharType:
    SPACE = [' ', '\t', '\r']
    MACRO = ['#']
    CNT = ['\\']
    NL = ['\n']
    ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    DIGIT = ['0','1','2','3','4','5','6','7','8','9']
    DEXDIGIT = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','A','B','C','D','E','F']
    DEXFLAG = ['x', 'X']
    UNDERLINE = ['_']
    STR = ['"']
    CHAR = ["'"]
    DIVIDE = ['/']
    STAR = ['*']
    EQUAL = ['=']
    PLUS = ['+']
    EXCLA = ['!']
    MINUS = ['-']
    MT = ['>']
    LT = ['<']
    MOD = ['%']
    BTBT = ['^']
    AND = ['&']
    OR = ['|']
    BRACKET = ['(',')','[',']','{','}']
    SEMICOLON = [';']
    POINT = ['.']
    COMMA = [',']
    QUES = ['?']
    COLON = [':']
    NOLINE = ['\\']

class KeyWord:
    WD = ['double','int','struct','break','else','long','switch','case','enum','typedef','char','return','union','float','short','continue','for','void','default','goto','sizeof','do','if','while']
    SKIP_WD = ['auto','register','extern','signed','unsigned','volatile','const','static', '__attribute__']

class TKType:
    TK_PLUS = 1  # +
    TK_MINUS = 2 # -
    TK_STAR = 3 # *
    TK_DIVIDE = 4 # /
    TK_MOD = 5 # %
    TK_ADDR = 6 # &
    TK_AND = 7 # &&
    TK_NOT = 8 # !
    TK_BOR = 9 # |
    TK_OR = 10 # ||
    TK_PE = 11 # +=
    TK_ME = 12 # -=
    TK_SE = 13 # *=
    TK_DE = 14 # /=
    TK_ANDE = 15 # &=
    TK_BT = 16 # ^
    TK_BTE = 17 # ^=
    TK_MDE = 18 # %=
    TK_BE = 19 # |=
    TK_EQ = 20 # ==
    TK_NEQ = 21 # !=
    TK_LT = 22 # <
    TK_MT = 23 # >
    TK_LET = 24 # <=
    TK_MET = 25 # >=
    TK_MOVL = 26 # <<
    TK_MOVR = 27 # >>
    TK_ASSIGN = 28 # =
    TK_PP = 29 # ++
    TK_MM = 30 # --
    TK_POINTO = 31 # ->
    TK_DOT = 32 # .
    TK_PTHSL = 33 # (
    TK_PTHSR= 34 # )
    TK_BRCTL= 35 # [
    TK_BRCTR= 36 # ]
    TK_BEGIN = 37 # {
    TK_END = 38 # }
    TK_SEMICOLON = 39 # ;
    TK_COMMA = 40 # ,
    TK_ELLIPSIS = 41 # ...
    TK_QUES = 42 # ?
    TK_COLON = 43 # :
    TK_MACRO = 44 # #
    TK_NEWLINE = 45 # \n

    TK_EOF = 70 # endfile




    KW_DOUBLE = 150
    KW_INT = 151 # int
    KW_STRUCT = 152 # struct
    KW_BREAK = 153 # break
    KW_ELSE = 154 # else
    KW_LONG = 155
    KW_SWITCH = 156
    KW_CASE = 157
    KW_ENUM = 158
    KW_TYPEDEF = 159
    KW_CHAR = 160 # char
    KW_RETURN = 161 # return
    KW_UNION = 162
    KW_FLOAT = 163
    KW_SHORT = 164 # short
    KW_CONTINUE = 165 # continue
    KW_FOR = 166 # for
    KW_VOID = 167 # void
    KW_DEFAULT = 168
    KW_GOTO = 169
    KW_SIZEOF = 170 # sizeof
    KW_DO = 171
    KW_IF = 172 # if
    KW_WHILE = 173

    TK_IDENT = 200

# const
    TK_CINT = 220 # const int
    TK_CFLOAT = 221 # const float
    TK_CCHAR = 222 # const char
    TK_CSTR = 223 # const string


    WDMAP = {'double':KW_DOUBLE,'int':KW_INT,'struct':KW_STRUCT,'break':KW_BREAK,'else':KW_ELSE,'long':KW_LONG,'switch':KW_SWITCH,'case':KW_CASE,'enum':KW_ENUM,'typedef':KW_TYPEDEF,'char':KW_CHAR,'return':KW_RETURN,'union':KW_UNION,'float':KW_FLOAT,'short':KW_SHORT,'continue':KW_CONTINUE,'for':KW_FOR,'void':KW_VOID,'default':KW_DEFAULT,'goto':KW_GOTO,'sizeof':KW_SIZEOF,'do':KW_DO,'if':KW_IF,'while':KW_WHILE}
    TSTWDMAP = {TK_PLUS:'+', TK_MINUS:'-', TK_STAR:'*', TK_DIVIDE:'/', TK_MOD:'%',
        TK_ADDR:'&', TK_AND:'&&', TK_NOT:'!', TK_BOR:'|', TK_OR:'||', TK_PE:'+=',
        TK_ME:'-=', TK_SE:'*=', TK_DE:'/=', TK_ANDE:'&=', TK_BT:'^', TK_BTE:'^=', TK_PP:'++', TK_MM:'--',
        TK_MDE:'%=', TK_BE:'|=', TK_EQ:'==', TK_NEQ:'!=', TK_LT:'<',
        TK_MT:'>', TK_LET:'<=', TK_MET:'>=', TK_MOVL:'<<', TK_MOVR:'>>',
        TK_ASSIGN:'=', TK_POINTO:'->', TK_DOT:'.', TK_PTHSL:'(', TK_PTHSR:')',
        TK_BRCTL:'[', TK_BRCTR:']', TK_BEGIN:'{', TK_END:'}', TK_SEMICOLON:';',
        TK_COMMA:',', TK_ELLIPSIS:'...', TK_QUES:'?', TK_COLON:':', TK_EOF:'EOF',
        KW_DOUBLE:'double', KW_INT:'int', KW_STRUCT:'struct', KW_BREAK:'break', KW_ELSE:'else',
        KW_LONG:'long', KW_SWITCH:'switch', KW_CASE:'case', KW_ENUM:'enum', KW_TYPEDEF:'typedef',
        KW_CHAR:'char', KW_RETURN:'return', KW_UNION:'union', KW_FLOAT:'float',
        KW_SHORT:'short', KW_CONTINUE:'continue', KW_FOR:'for', KW_VOID:'void', KW_DEFAULT:'default',
        KW_GOTO:'goto', KW_SIZEOF:'sizeof', KW_DO:'do', KW_IF:'if', KW_WHILE:'while'}
