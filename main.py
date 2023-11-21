import re
import math
from collections import defaultdict
import traceback
import sys
import os
import locale
import hashlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from collections import defaultdict
import datetime
import re

INTEGER = 'INTEGER'
IDENTIFIER = 'IDENTIFIER'
PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MULTIPLY'
DIVIDE = 'DIVIDE'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'
IF = 'IF'
UNLESS = 'UNLESS'
PRINT = 'PRINT'
TRY = 'TRY'
ERROR = 'ERROR'
FOR = 'FOR'
WHILE = 'WHILE'
ABS = 'ABS'
ACOS = 'ACOS'
ASIN = 'ASIN'
CEIL = 'CEIL'
EXP = 'EXP'
FLOOR = 'FLOOR'
LOG = 'LOG'
MAX = 'MAX'
MIN = 'MIN'
PI = 'PI'
POW = 'POW'
SQRT = 'SQRT'
TAN = 'TAN'
ADDCSLASHES = 'ADDCSLASHES'
ADDSLASHES = 'ADDSLASHES'
BIN2HEX = 'BIN2HEX'
CHOP = 'CHOP'
CHR = 'CHR'
CHUNK_SPLIT = 'CHUNK_SPLIT'
CONVERT_CYR_STRING = 'CONVERT_CYR_STRING'
CONVERT_UUDECODE = 'CONVERT_UUDECODE'
CONVERT_UUENCODE = 'CONVERT_UUENCODE'
COUNT_CHARS = 'COUNT_CHARS'
CRC32 = 'CRC32'
CRYPT = 'CRYPT'
ECHO = 'ECHO'
EXPLODE = 'EXPLODE'
FPRINTF = 'FPRINTF'
GET_HTML_TRANSLATION_TABLE = 'GET_HTML_TRANSLATION_TABLE'
HEBREV = 'HEBREV'
HEBREV_UNICODE = 'HEBREV_UNICODE'
HEBREVC = 'HEBREVC'
HEBREVC_UNICODE = 'HEBREVC_UNICODE'
HEX2BIN = 'HEX2BIN'
HTML_ENTITY_DECODE = 'HTML_ENTITY_DECODE'
HTMLENTITIES = 'HTMLENTITIES'
HTML_SPECIALCHARS_DECODE = 'HTML_SPECIALCHARS_DECODE'
HTML_SPECIALCHARS = 'HTML_SPECIALCHARS'
IMPLD = 'IMPLD'  # Alias for implode
JOIN = 'JOIN'  # Alias for implode
LCFIRST = 'LCFIRST'
LEVENSHTEIN = 'LEVENSHTEIN'
LOCALECONV = 'LOCALECONV'
LTRIM = 'LTRIM'
MD5 = 'MD5'
MD5_FILE = 'MD5_FILE'
METAPHONE = 'METAPHONE'
MONEY_FORMAT = 'MONEY_FORMAT'
NL_LANGINFO = 'NL_LANGINFO'
NL2BR = 'NL2BR'
NUMBER_FORMAT = 'NUMBER_FORMAT'
ORD = 'ORD'
PARSE_STR = 'PARSE_STR'
PRINT = 'PRINT'
PRINTF = 'PRINTF'
QUOTED_PRINTABLE_DECODE = 'QUOTED_PRINTABLE_DECODE'
QUOTED_PRINTABLE_ENCODE = 'QUOTED_PRINTABLE_ENCODE'
QUOTEMETA = 'QUOTEMETA'
RTRIM = 'RTRIM'
SETLOCALE = 'SETLOCALE'
SHA1 = 'SHA1'
SHA1_FILE = 'SHA1_FILE'
SIMILAR_TEXT = 'SIMILAR_TEXT'
SOUNDEX = 'SOUNDEX'
SPRINTF = 'SPRINTF'
SSCANF = 'SSCANF'
STR_GETCSV = 'STR_GETCSV'
STR_IREPLACE = 'STR_IREPLACE'
STR_PAD = 'STR_PAD'
STR_REPEAT = 'STR_REPEAT'
STR_REPLACE = 'STR_REPLACE'
STR_ROT13 = 'STR_ROT13'
STR_SHUFFLE = 'STR_SHUFFLE'
STR_SPLIT = 'STR_SPLIT'
STR_WORD_COUNT = 'STR_WORD_COUNT'
STRCASECMP = 'STRCASECMP'
STRCHR = 'STRCHR'
STRCMP = 'STRCMP'
STRCOLL = 'STRCOLL'
STRCSPN = 'STRCSPN'
STRIP_TAGS = 'STRIP_TAGS'
STRIPCSLASHES = 'STRIPCSLASHES'
STRIPS = 'STRIPS'
STRIPOS = 'STRIPOS'
STRISTR = 'STRISTR'
STRLEN = 'STRLEN'
STRNATCASECMP = 'STRNATCASECMP'
STRNATCMP = 'STRNATCMP'
STRNCASECMP = 'STRNCASECMP'
STRNCMP = 'STRNCMP'
STRPBRK = 'STRPBRK'
STRPOS = 'STRPOS'
STRRCHR = 'STRRCHR'
STRREV = 'STRREV'
STRRIPOS = 'STRRIPOS'
STRRPOS = 'STRRPOS'
STRSPN = 'STRSPN'
STRSTR = 'STRSTR'
STRTOK = 'STRTOK'
STRTOLOWER = 'STRTOLOWER'
STRTOUPPER = 'STRTOUPPER'
STRTR = 'STRTR'
SUBSTR = 'SUBSTR'
SUBSTR_COMPARE = 'SUBSTR_COMPARE'
SUBSTR_COUNT = 'SUBSTR_COUNT'
SUBSTR_REPLACE = 'SUBSTR_REPLACE'
TRIM = 'TRIM'
UCFIRST = 'UCFIRST'
UCWORDS = 'UCWORDS'
VFPRINTF = 'VFPRINTF'
VPRINTF = 'VPRINTF'
VSPRINTF = 'VSPRINTF'
WORDWRAP = 'WORDWRAP'










EOF = 'EOF'







# Token class
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

# Lexer
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.keywords = {
            'if': IF,
            'unless': UNLESS,
            'print': PRINT,
            'try': TRY,
            'error': ERROR,
            'for': FOR,
            'while': WHILE,
            'sin': SIN,
            'cos': COS
        }

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def identifier(self):
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()
        return self.keywords.get(result, IDENTIFIER)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char.isalpha():
                return Token(self.identifier(), self.identifier())

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(MULTIPLY, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIVIDE, '/')

            if self.current_char == '(':
                self.advance()
                return Token(LPAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(RPAREN, ')')

            self.error()

        return Token(EOF, None)

# Parser
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def for_loop(self):
    	self.eat(FOR)
    	self.eat(LPAREN)
    	var_name = self.current_token.value
    	self.eat(IDENTIFIER)
    	self.eat(IN)
    	start = self.expr()
    	self.eat(TO)
    	end = self.expr()
    	self.eat(RPAREN)
    	self.eat(COLON)
    	self.eat(EOF)
    	for i in range(start, end + 1):
        	variables[var_name] = i
        	self.block()


    # New: Parse a 'while' loop
    def while_loop(self):
        self.eat(WHILE)
        condition = self.expr()
        self.eat(COLON)
        self.eat(EOF)
        while condition:
            self.block()
            condition = self.expr()

    def statement(self):
        if self.current_token.type == IF:
    # (Previous code remains the same)
	elif self.current_token.type == UNLESS:
    		self.eat(UNLESS)
    		condition = self.expr()
    		self.eat(COLON)
    		self.eat(EOF)
    		if not condition:
        		self.block()

        elif self.current_token.type == FOR:
            self.for_loop()
        elif self.current_token.type == WHILE:
            self.while_loop()
        elif self.current_token.type == SIN:
            self.eat(SIN)
            self.eat(LPAREN)
            angle = self.expr()
            self.eat(RPAREN)
            return math.sin(angle)
        elif self.current_token.type == COS:
            self.eat(COS)
            self.eat(LPAREN)
            angle = self.expr()
            self.eat(RPAREN)
            return math.cos(angle)

    def factor(self):
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return token.value
        elif token.type == IDENTIFIER:
            variable_name = token.value
            self.eat(IDENTIFIER)
            return variables[variable_name]

        elif token.type == LPAREN:
            self.eat(LPAREN)
            result = self.expr()
            self.eat(RPAREN)
            return result

    def term(self):
        result = self.factor()
        while self.current_token.type in (MULTIPLY, DIVIDE):
            token = self.current_token
            if token.type == MULTIPLY:
                self.eat(MULTIPLY)
                result *= self.factor()
            elif token.type == DIVIDE:
                self.eat(DIVIDE)
                result /= self.factor()
        return result

    def expr(self):
        result = self.term()
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result += self.term()
            elif token.type == MINUS:
                self.eat(MINUS)
                result -= self.term()
        return result

    def statement(self):
        if self.current_token.type == IF:
            self.eat(IF)
            condition = self.expr()
            if condition:
                self.eat(':')
                self.eat(EOF)
                return self.block()
            else:
                self.eat(ELSE)
                self.eat(':')
                self.eat(EOF)
                return self.block()
        elif self.current_token.type == PRINT:
            self.eat(PRINT)
            value = self.expr()
            return value

    def block(self):
        result = None
        while self.current_token.type != EOF:
            result = self.statement()
        return result

    def parse(self):
        return self.block()


 def abs_function(self):
        self.eat(ABS)
        self.eat(LPAREN)
        value = self.expr()
        self.eat(RPAREN)
        return abs(value)

    # New: Parse acos function
    def acos_function(self):
        self.eat(ACOS)
        self.eat(LPAREN)
        value = self.expr()
        self.eat(RPAREN)
        return math.acos(value)

    # New: Parse asin function
    def asin_function(self):
        self.eat(ASIN)
        self.eat(LPAREN)
        value = self.expr()
        self.eat(RPAREN)
        return math.asin(value)

    # New: Parse ceil function
    def ceil_function(self):
        self.eat(CEIL)
        self.eat(LPAREN)
        value = self.expr()
        self.eat(RPAREN)
        return math.ceil(value)

    # New: Parse exp function
    def exp_function(self):
        self.eat(EXP)
        self.eat(LPAREN)
        value = self.expr()
        self.eat(RPAREN)
        return math.exp(value)

    # New: Parse floor function
    def floor_function(self):
        self.eat(FLOOR)
        self.eat(LPAREN)
        value = self.expr()
        self.eat(RPAREN)
        return math.floor(value)

    # New: Parse log function
    def log_function(self):
        self.eat(LOG)
        self.eat(LPAREN)
        value = self.expr()
        self.eat(RPAREN)
        return math.log(value)

    # New: Parse max function
    def max_function(self):
        self.eat(MAX)
        self.eat(LPAREN)
        values = []
        while self.current_token.type != RPAREN:
            values.append(self.expr())
            if self.current_token.type == ',':
                self.eat(',')
        self.eat(RPAREN)
        return max(values)

    # New: Parse min function
    def min_function(self):
        self.eat(MIN)
        self.eat(LPAREN)
        values = []
        while self.current_token.type != RPAREN:
            values.append(self.expr())
            if self.current_token.type == ',':
                self.eat(',')
        self.eat(RPAREN)
        return min(values)

    # New: Parse pi constant
    def pi_constant(self):
        self.eat(PI)
        return math.pi

    # New: Parse pow function
    def pow_function(self):
        self.eat(POW)
        self.eat(LPAREN)
        base = self.expr()
        self.eat(',')
        exponent = self.expr()
        self.eat(RPAREN)
        return math.pow(base, exponent)

    # New: Parse sqrt function
    def sqrt_function(self):
        self.eat(SQRT)
        self.eat(LPAREN)
        value = self.expr()
        self.eat(RPAREN)
        return math.sqrt(value)

    # New: Parse tan function
    def tan_function(self):
        self.eat(TAN)
        self.eat(LPAREN)
        value = self.expr()
        self.eat(RPAREN)
        return math.tan(value)





      def addcslashes_function(self):
        self.eat(ADDCSLASHES)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(COMMA)
        chars = self.expr()
        self.eat(RPAREN)
        return text.encode('unicode_escape').decode()  # Add backslashes in front of specified characters

    # New: Parse addslashes function
    def addslashes_function(self):
        self.eat(ADDSLASHES)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return text.replace('\\', r'\\').replace('\'', r'\'').replace('\"', r'\"')  # Add backslashes in front of predefined characters

    # New: Parse bin2hex function
    def bin2hex_function(self):
        self.eat(BIN2HEX)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return text.encode('utf-8').hex()  # Convert ASCII characters to hexadecimal values

    # New: Parse chop function
    def chop_function(self):
        self.eat(CHOP)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return text.rstrip()  # Remove whitespace or other characters from the right end of a string

    # New: Parse chr function
    def chr_function(self):
        self.eat(CHR)
        self.eat(LPAREN)
        value = self.expr()
        self.eat(RPAREN)
        return chr(value)  # Convert an ASCII code to a character






      def chunk_split_function(self):
        self.eat(CHUNK_SPLIT)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(COMMA)
        chunk_len = self.expr()
        self.eat(COMMA)
        end = self.expr()
        self.eat(RPAREN)
        parts = [text[i:i + chunk_len] for i in range(0, len(text), chunk_len)]
        return '\n'.join(parts)

    # New: Parse convert_cyr_string function
    def convert_cyr_string_function(self):
        self.eat(CONVERT_CYR_STRING)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(COMMA)
        from_charset = self.expr()
        self.eat(COMMA)
        to_charset = self.expr()
        self.eat(RPAREN)
        return text.encode(from_charset).decode(to_charset, 'ignore')

    # New: Parse convert_uudecode function
    def convert_uudecode_function(self):
        self.eat(CONVERT_UUDECODE)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return text.encode('utf-8').decode('uu')

    # New: Parse convert_uuencode function
    def convert_uuencode_function(self):
        self.eat(CONVERT_UUENCODE)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return text.encode('utf-8').decode('uu')

    # New: Parse count_chars function
    def count_chars_function(self):
        self.eat(COUNT_CHARS)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        char_set = set(text)
        char_info = {}
        for char in char_set:
            char_info[char] = text.count(char)
        return char_info

    # New: Parse crc32 function
    def crc32_function(self):
        self.eat(CRC32)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return str(binascii.crc32(text.encode()))

    # New: Parse crypt function
    def crypt_function(self):
        self.eat(CRYPT)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        salt = os.urandom(16)
        hashed = crypt.crypt(text, salt)
        return hashed

    # New: Parse echo function
    def echo_function(self):
        self.eat(ECHO)
        self.eat(LPAREN)
        args = []
        while self.current_token.type != RPAREN:
            args.append(self.expr())
            if self.current_token.type == ',':
                self.eat(',')
        self.eat(RPAREN)
        for arg in args:
            sys.stdout.write(str(arg))
        sys.stdout.write('\n')

    # New: Parse explode function
    def explode_function(self):
        self.eat(EXPLODE)
        self.eat(LPAREN)
        delimiter = self.expr()
        self.eat(COMMA)
        text = self.expr()
        self.eat(RPAREN)
        return text.split(delimiter)

    # New: Parse fprintf function
    def fprintf_function(self):
        self.eat(FPRINTF)
        self.eat(LPAREN)
        format_str = self.expr()
        self.eat(COMMA)
        args = []
        while self.current_token.type != RPAREN:
            args.append(self.expr())
            if self.current_token.type == ',':
                self.eat(',')
        self.eat(RPAREN)
        sys.stdout.write(format_str % tuple(args))




     def get_html_translation_table_function(self):
        self.eat(GET_HTML_TRANSLATION_TABLE)
        self.eat(LPAREN)
        table_type = self.expr()
        self.eat(RPAREN)
        if table_type == 1:
            return html.entities.codepoint2name
        elif table_type == 2:
            return html.entities.name2codepoint

    # New: Parse hebrev function
    def hebrev_function(self):
        self.eat(HEBREV)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return hebrev(text)

    # New: Parse hebrevc function
    def hebrevc_function(self):
        self.eat(HEBREVC)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return hebrevc(text)

    # New: Parse hex2bin function
    def hex2bin_function(self):
        self.eat(HEX2BIN)
        self.eat(LPAREN)
        hex_string = self.expr()
        self.eat(RPAREN)
        return bytes.fromhex(hex_string).decode('utf-8')

    # New: Parse html_entity_decode function
    def html_entity_decode_function(self):
        self.eat(HTML_ENTITY_DECODE)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return html.unescape(text)

    # New: Parse htmlentities function
    def htmlentities_function(self):
        self.eat(HTMLENTITIES)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return html.escape(text, quote=True)

    # New: Parse htmlspecialchars_decode function
    def htmlspecialchars_decode_function(self):
        self.eat(HTML_SPECIALCHARS_DECODE)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return html.unescape(text)

    # New: Parse htmlspecialchars function
    def htmlspecialchars_function(self):
        self.eat(HTML_SPECIALCHARS)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return html.escape(text, quote=True)

    # New: Parse implode/join function
    def implode_function(self):
        self.eat(IMPLD)
        self.eat(LPAREN)
        separator = self.expr()
        self.eat(COMMA)
        elements = self.expr()
        self.eat(RPAREN)
        if isinstance(elements, list):
            return separator.join(str(e) for e in elements)
        else:
            return separator.join(elements)

    # New: Parse lcfirst function
    def lcfirst_function(self):
        self.eat(LCFIRST)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return text[0].lower() + text[1:]

    





      def levenshtein_function(self):
        self.eat(LEVENSHTEIN)
        self.eat(LPAREN)
        str1 = self.expr()
        self.eat(COMMA)
        str2 = self.expr()
        self.eat(RPAREN)
        return levenshtein(str1, str2)

    # New: Parse localeconv function
    def localeconv_function(self):
        self.eat(LOCALECONV)
        self.eat(LPAREN)
        self.eat(RPAREN)
        return locale.localeconv()

    # New: Parse ltrim function
    def ltrim_function(self):
        self.eat(LTRIM)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return text.lstrip()

    # New: Parse md5 function
    def md5_function(self):
        self.eat(MD5)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return hashlib.md5(text.encode()).hexdigest()

    # New: Parse md5_file function
    def md5_file_function(self):
        self.eat(MD5_FILE)
        self.eat(LPAREN)
        filename = self.expr()
        self.eat(RPAREN)
        with open(filename, 'rb') as file:
            return hashlib.md5(file.read()).hexdigest()

    # New: Parse metaphone function
    def metaphone_function(self):
        self.eat(METAPHONE)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return metaphone(text)

    # New: Parse money_format function
    def money_format_function(self):
        self.eat(MONEY_FORMAT)
        self.eat(LPAREN)
        format_str = self.expr()
        self.eat(COMMA)
        value = self.expr()
        self.eat(RPAREN)
        return locale.currency(value, grouping=True)

    # New: Parse nl_langinfo function
    def nl_langinfo_function(self):
        self.eat(NL_LANGINFO)
        self.eat(LPAREN)
        item = self.expr()
        self.eat(RPAREN)
        return locale.nl_langinfo(item)

    # New: Parse nl2br function
    def nl2br_function(self):
        self.eat(NL2BR)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return text.replace('\n', '<br>\n')

    # New: Parse number_format function
    def number_format_function(self):
        self.eat(NUMBER_FORMAT)
        self.eat(LPAREN)
        number = self.expr()
        self.eat(COMMA)
        decimals = self.expr()
        self.eat(COMMA)
        dec_point = self.expr()
        self.eat(COMMA)
        thousands_sep = self.expr()
        self.eat(RPAREN)
        return locale.format_string(f'%.{decimals}f', number, grouping=True)

    # New: Parse ord function
    def ord_function(self):
        self.eat(ORD)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return ord(text[0]) if text else None

    # New: Parse parse_str function
    def parse_str_function(self):
        self.eat(PARSE_STR)
        self.eat(LPAREN)
        query = self.expr()
        self.eat(RPAREN)
        variables = {}
        exec('variables = ' + query)
        return variables

    # New: Parse print function
    def print_function(self):
        self.eat(PRINT)
        self.eat(LPAREN)
        args = []
        while self.current_token.type != RPAREN:
            args.append(self.expr())
            if self.current_token.type == ',':
                self.eat(',')
        self.eat(RPAREN)
        for arg in args:
            print(arg, end='')
        print()

    # New: Parse printf function
    def printf_function(self):
        self.eat(PRINTF)
        self.eat(LPAREN)
        format_str = self.expr()
        self.eat(COMMA)
        args = []
        while self.current_token.type != RPAREN:
            args.append(self.expr())
            if self.current_token.type == ',':
                self.eat(',')
        self.eat(RPAREN)
        print(format_str % tuple(args))





      def quoted_printable_decode_function(self):
        self.eat(QUOTED_PRINTABLE_DECODE)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return quopri.decodestring(text.encode()).decode()

    # New: Parse quoted_printable_encode function
    def quoted_printable_encode_function(self):
        self.eat(QUOTED_PRINTABLE_ENCODE)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return quopri.encodestring(text.encode()).decode()

    # New: Parse quotemeta function
    def quotemeta_function(self):
        self.eat(QUOTEMETA)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return re.escape(text)

    # New: Parse rtrim function
    def rtrim_function(self):
        self.eat(RTRIM)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return text.rstrip()

    # New: Parse setlocale function
    def setlocale_function(self):
        self.eat(SETLOCALE)
        self.eat(LPAREN)
        category = self.expr()
        self.eat(COMMA)
        locale_str = self.expr()
        self.eat(RPAREN)
        return locale.setlocale(category, locale_str)

    # New: Parse sha1 function
    def sha1_function(self):
        self.eat(SHA1)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return hashlib.sha1(text.encode()).hexdigest()

    # New: Parse sha1_file function
    def sha1_file_function(self):
        self.eat(SHA1_FILE)
        self.eat(LPAREN)
        filename = self.expr()
        self.eat(RPAREN)
        with open(filename, 'rb') as file:
            return hashlib.sha1(file.read()).hexdigest()

    # New: Parse similar_text function
    def similar_text_function(self):
        self.eat(SIMILAR_TEXT)
        self.eat(LPAREN)
        str1 = self.expr()
        self.eat(COMMA)
        str2 = self.expr()
        self.eat(RPAREN)
        return similar_text(str1, str2)

    # New: Parse soundex function
    def soundex_function(self):
        self.eat(SOUNDEX)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return soundex(text)

    # New: Parse sprintf function
    def sprintf_function(self):
        self.eat(SPRINTF)
        self.eat(LPAREN)
        format_str = self.expr()
        self.eat(COMMA)
        args = []
        while self.current_token.type != RPAREN:
            args.append(self.expr())
            if self.current_token.type == ',':
                self.eat(',')
        self.eat(RPAREN)
        return format_str % tuple(args)

    # New: Parse sscanf function
    def sscanf_function(self):
        self.eat(SSCANF)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(COMMA)
        format_str = self.expr()
        self.eat(RPAREN)
        matches = re.match(format_str, text)
        if matches:
            return matches.groups()
        return ()

    # New: Parse str_getcsv function
    def str_getcsv_function(self):
        self.eat(STR_GETCSV)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        reader = csv.reader([text])
        return list(reader)[0]

    # New: Parse str_ireplace function
    def str_ireplace_function(self):
        self.eat(STR_IREPLACE)
        self.eat(LPAREN)
        search = self.expr()
        self.eat(COMMA)
        replace = self.expr()
        self.eat(COMMA)
        subject = self.expr()
        self.eat(RPAREN)
        return subject.lower().replace(search.lower(), replace)

    # New: Parse str_pad function
    def str_pad_function(self):
        self.eat(STR_PAD)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(COMMA)
        length = self.expr()
        self.eat(COMMA)
        pad_string = self.expr()
        self.eat(COMMA)
        pad_type = self.expr()
        self.eat(RPAREN)
        if pad_type == 1:
            return text.ljust(length, pad_string)
        elif pad_type == 2:
            return text.rjust(length, pad_string)
        else:
            return text.center(length, pad_string)

    # New: Parse str_repeat function
    def str_repeat_function(self):
        self.eat(STR_REPEAT)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(COMMA)
        count = self.expr()
        self.eat(RPAREN)
        return text * count

    # New: Parse str_replace function
    def str_replace_function(self):
        self.eat(STR_REPLACE)
        self.eat(LPAREN)
        search = self.expr()
        self.eat(COMMA)
        replace = self.expr()
        self.eat(COMMA)
        subject = self.expr()
        self.eat(RPAREN)
        return subject.replace(search, replace)

    # New: Parse str_rot13 function
    def str_rot13_function(self):
        self.eat(STR_ROT13)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return codecs.encode(text, 'rot_13')






     def str_shuffle_function(self):
        self.eat(STR_SHUFFLE)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        text_list = list(text)
        random.shuffle(text_list)
        return ''.join(text_list)

    # New: Parse str_split function
    def str_split_function(self):
        self.eat(STR_SPLIT)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(COMMA)
        delimiter = self.expr()
        self.eat(RPAREN)
        return text.split(delimiter)

    # New: Parse str_word_count function
    def str_word_count_function(self):
        self.eat(STR_WORD_COUNT)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        words = re.findall(r'\b\w+\b', text)
        return len(words)

    # New: Parse strcasecmp function
    def strcasecmp_function(self):
        self.eat(STRCASECMP)
        self.eat(LPAREN)
        str1 = self.expr()
        self.eat(COMMA)
        str2 = self.expr()
        self.eat(RPAREN)
        return str1.lower() == str2.lower()

    # New: Parse strchr function
    def strchr_function(self):
        self.eat(STRCHR)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(COMMA)
        search = self.expr()
        self.eat(RPAREN)
        return text.find(search)

    # New: Parse strcmp function
    def strcmp_function(self):
        self.eat(STRCMP)
        self.eat(LPAREN)
        str1 = self.expr()
        self.eat(COMMA)
        str2 = self.expr()
        self.eat(RPAREN)
        return str1 == str2

    # New: Parse strcoll function
    def strcoll_function(self):
        self.eat(STRCOLL)
        self.eat(LPAREN)
        str1 = self.expr()
        self.eat(COMMA)
        str2 = self.expr()
        self.eat(RPAREN)
        return locale.strcoll(str1, str2)

    # New: Parse strcspn function
    def strcspn_function(self):
        self.eat(STRCSPN)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(COMMA)
        charlist = self.expr()
        self.eat(RPAREN)
        return strcspn(text, charlist)

    # New: Parse strip_tags function
    def strip_tags_function(self):
        self.eat(STRIP_TAGS)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return re.sub(r'<[^>]+>', '', text)

    # New: Parse stripcslashes function
    def stripcslashes_function(self):
        self.eat(STRIPCSLASHES)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return text.encode().decode('unicode_escape')

    # New: Parse stripslashes function
    def stripslashes_function(self):
        self.eat(STRIPS)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return text.replace("\\", "")




	
    def stripos_function(self):
        self.eat(STRIPOS)
        self.eat(LPAREN)
        haystack = self.expr()
        self.eat(COMMA)
        needle = self.expr()
        self.eat(RPAREN)
        return haystack.lower().find(needle.lower())

    # New: Parse stristr function
    def stristr_function(self):
        self.eat(STRISTR)
        self.eat(LPAREN)
        haystack = self.expr()
        self.eat(COMMA)
        needle = self.expr()
        self.eat(RPAREN)
        return haystack.lower().replace(needle.lower(), '', 1)

    # New: Parse strlen function
    def strlen_function(self):
        self.eat(STRLEN)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return len(text)

    # New: Parse strnatcasecmp function
    def strnatcasecmp_function(self):
        self.eat(STRNATCASECMP)
        self.eat(LPAREN)
        str1 = self.expr()
        self.eat(COMMA)
        str2 = self.expr()
        self.eat(RPAREN)
        return strnatcasecmp(str1, str2)

    # New: Parse strnatcmp function
    def strnatcmp_function(self):
        self.eat(STRNATCMP)
        self.eat(LPAREN)
        str1 = self.expr()
        self.eat(COMMA)
        str2 = self.expr()
        self.eat(RPAREN)
        return strnatcmp(str1, str2)

    # New: Parse strncasecmp function
    def strncasecmp_function(self):
        self.eat(STRNCASECMP)
        self.eat(LPAREN)
        str1 = self.expr()
        self.eat(COMMA)
        str2 = self.expr()
        self.eat(COMMA)
        n = self.expr()
        self.eat(RPAREN)
        return str1.lower()[:n] == str2.lower()[:n]

    # New: Parse strncmp function
    def strncmp_function(self):
        self.eat(STRNCMP)
        self.eat(LPAREN)
        str1 = self.expr()
        self.eat(COMMA)
        str2 = self.expr()
        self.eat(COMMA)
        n = self.expr()
        self.eat(RPAREN)
        return str1[:n] == str2[:n]

    # New: Parse strpbrk function
    def strpbrk_function(self):
        self.eat(STRPBRK)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(COMMA)
        charlist = self.expr()
        self.eat(RPAREN)
        intersection = ''.join(set(text) & set(charlist))
        if intersection:
            return text.index(intersection)
        return False

    # New: Parse strpos function
    def strpos_function(self):
        self.eat(STRPOS)
        self.eat(LPAREN)
        haystack = self.expr()
        self.eat(COMMA)
        needle = self.expr()
        self.eat(RPAREN)
        return haystack.find(needle)

    # New: Parse strrchr function
    def strrchr_function(self):
        self.eat(STRRCHR)
        self.eat(LPAREN)
        haystack = self.expr()
        self.eat(COMMA)
        needle = self.expr()
        self.eat(RPAREN)
        return haystack.rfind(needle)

    # New: Parse strrev function
    def strrev_function(self):
        self.eat(STRREV)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return text[::-1]




    def strripos_function(self):
        self.eat(STRRIPOS)
        self.eat(LPAREN)
        haystack = self.expr()
        self.eat(COMMA)
        needle = self.expr()
        self.eat(RPAREN)
        return haystack.lower().rfind(needle.lower())

    # New: Parse strrpos function
    def strrpos_function(self):
        self.eat(STRRPOS)
        self.eat(LPAREN)
        haystack = self.expr()
        self.eat(COMMA)
        needle = self.expr()
        self.eat(RPAREN)
        return haystack.rfind(needle)

    # New: Parse strspn function
    def strspn_function(self):
        self.eat(STRSPN)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(COMMA)
        charlist = self.expr()
        self.eat(RPAREN)
        return len(re.match(f"[{charlist}]*", text).group(0))

    # New: Parse strstr function
    def strstr_function(self):
        self.eat(STRSTR)
        self.eat(LPAREN)
        haystack = self.expr()
        self.eat(COMMA)
        needle = self.expr()
        self.eat(RPAREN)
        index = haystack.find(needle)
        return haystack[index:] if index != -1 else False

    # New: Parse strtok function
    def strtok_function(self):
        self.eat(STRTOK)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(COMMA)
        delimiter = self.expr()
        self.eat(RPAREN)
        parts = text.split(delimiter)
        return parts.pop(0)

    # New: Parse strtolower function
    def strtolower_function(self):
        self.eat(STRTOLOWER)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return text.lower()

    # New: Parse strtoupper function
    def strtoupper_function(self):
        self.eat(STRTOUPPER)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return text.upper()

    # New: Parse strtr function
    def strtr_function(self):
        self.eat(STRTR)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(COMMA)
        from_chars = self.expr()
        self.eat(COMMA)
        to_chars = self.expr()
        self.eat(RPAREN)
        translation = str.maketrans(from_chars, to_chars)
        return text.translate(translation)

    # New: Parse substr function
    def substr_function(self):
        self.eat(SUBSTR)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(COMMA)
        start = self.expr()
        self.eat(COMMA)
        length = self.expr()
        self.eat(RPAREN)
        return text[start:start + length]

    # New: Parse substr_compare function
    def substr_compare_function(self):
        self.eat(SUBSTR_COMPARE)
        self.eat(LPAREN)
        main_str = self.expr()
        self.eat(COMMA)
        str = self.expr()
        self.eat(COMMA)
        start = self.expr()
        self.eat(COMMA)
        length = self.expr()
        self.eat(COMMA)
        case_insensitive = self.expr()
        self.eat(RPAREN)
        return main_str[start:start + length] == str[start:start + length] if not case_insensitive else main_str[start:start + length].lower() == str[start:start + length].lower()

    # New: Parse substr_count function
    def substr_count_function(self):
        self.eat(SUBSTR_COUNT)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(COMMA)
        substr = self.expr()
        self.eat(RPAREN)
        return text.count(substr)

    # New: Parse substr_replace function
    def substr_replace_function(self):
        self.eat(SUBSTR_REPLACE)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(COMMA)
        replacement = self.expr()
        self.eat(COMMA)
        start = self.expr()
        self.eat(COMMA)
        length = self.expr()
        self.eat(RPAREN)
        return text[:start] + replacement + text[start + length:]

    # New: Parse trim function
    def trim_function(self):
        self.eat(TRIM)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return text.strip()

    # New: Parse ucfirst function
    def ucfirst_function(self):
        self.eat(UCFIRST)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return text[0].upper() + text[1:]

    # New: Parse ucwords function
    def ucwords_function(self):
        self.eat(UCWORDS)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(RPAREN)
        return ' '.join(word.capitalize() for word in text.split())

    # New: Parse vfprintf function
    def vfprintf_function(self):
        self.eat(VFPRINTF)
        self.eat(LPAREN)
        stream = self.expr()
        self.eat(COMMA)
        format_string = self.expr()
        self.eat(COMMA)
        args = self.expr()
        self.eat(RPAREN)
        return vfprintf(stream, format_string, args)

    # New: Parse vprintf function
    def vprintf_function(self):
        self.eat(VPRINTF)
        self.eat(LPAREN)
        format_string = self.expr()
        self.eat(COMMA)
        args = self.expr()
        self.eat(RPAREN)
        return vprintf(format_string, args)

    # New: Parse vsprintf function
    def vsprintf_function(self):
        self.eat(VSPRINTF)
        self.eat(LPAREN)
        format_string = self.expr()
        self.eat(COMMA)
        args = self.expr()
        self.eat(RPAREN)
        return vsprintf(format_string, args)

    # New: Parse wordwrap function
    def wordwrap_function(self):
        self.eat(WORDWRAP)
        self.eat(LPAREN)
        text = self.expr()
        self.eat(COMMA)
        width = self.expr()
        self.eat(COMMA)
        break_long_words = self.expr()
        self.eat(RPAREN)
        return wordwrap(text, width, break_long_words)







    




    

















      

# Semantic Analyzer
variables = defaultdict(int)

# Interpreter
class Interpreter:
    def __init__(self, text):
        self.lexer = Lexer(text)
        self.parser = Parser(self.lexer)

    def eval(self):
        return self.parser.parse()

    def is_prime(self, n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True



     def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)






class ErrorDebug:
    # Error-related functions
    def error_clear_last(self):
        return None

    def error_get_last(self):
        return None

    def error_log(self, message, message_type=0, destination=0, extra_headers=None):
        return None

    def error_reporting(self, level=None):
        return None

    def restore_error_handler(self):
        return None

    def set_error_handler(self, error_handler):
        return None

    # Debug-related functions
    def debug_backtrace(self, options=None, limit=None):
        return None

    def debug_print_backtrace(self, options=None, limit=None):
        return None

    def restore_exception_handler(self):
        return None

    def set_exception_handler(self, exception_handler):
        return None

    def trigger_error(self, error_msg, error_type=E_USER_NOTICE):
        raise Exception(f"User-defined error: {error_msg}")

    def user_error(self, error_msg, error_type=E_USER_NOTICE):
        raise Exception(f"User-defined error: {error_msg}")






class Mailing:
    def send_mail(self, subject, message, to_email, from_email, smtp_server, smtp_port, smtp_username, smtp_password, cc=None, bcc=None, html=False):
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        if cc:
            msg['Cc'] = cc

        if bcc:
            msg['Bcc'] = bcc

        if html:
            message = MIMEText(message, 'html')
        else:
            message = MIMEText(message, 'plain')

        msg.attach(message)

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(from_email, to_email, msg.as_string())
            server.quit()
        except Exception as e:
            trigger_error(f"Email sending failed: {str(e)}", E_USER_ERROR)



class Function:
    def __init__(self, parameters, body, context):
        self.parameters = parameters
        self.body = body
        self.context = context

    def call(self, arguments):
        if len(arguments) != len(self.parameters):
            trigger_error(f"Function expects {len(self.parameters)} arguments, but {len(arguments)} were provided.", E_USER_ERROR)
            return None

        local_context = Context(parent=self.context)

        for i in range(len(self.parameters)):
            local_context.symbol_table[self.parameters[i]] = arguments[i]

        try:
            result = self.body.interpret(local_context)
            if result is not None:
                return result
        except ReturnValue as rv:
            return rv.value

    def __str__(self):
        return f"<Function: {self.parameters}>"

# New: Function definition node in the abstract syntax tree
class FunctionDefinitionNode:
    def __init__(self, name, parameters, body):
        self.name = name
        self.parameters = parameters
        self.body = body

    def interpret(self, context):
        function = Function(self.parameters, self.body, context)
        context.symbol_table[self.name] = function

# New: Function call node in the abstract syntax tree
class FunctionCallNode:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

    def interpret(self, context):
        function = context.get_symbol(self.name)

        if not isinstance(function, Function):
            trigger_error(f"'{self.name}' is not a function.", E_USER_ERROR)
            return None

        argument_values = [arg.interpret(context) for arg in self.arguments]
        return function.call(argument_values)






class ClassDefinitionNode:
    def __init__(self, name, attributes, methods):
        self.name = name
        self.attributes = attributes
        self.methods = methods

    def interpret(self, context):
        # Create a new class in the context
        new_class = HounaarClass(self.name)

        # Add attributes to the class
        for attribute in self.attributes:
            new_class.add_attribute(attribute)

        # Add methods to the class
        for method in self.methods:
            new_class.add_method(method)

        # Store the class in the context
        context.symbol_table[self.name] = new_class

class ObjectCreationNode:
    def __init__(self, class_name):
        self.class_name = class_name

    def interpret(self, context):
        # Create a new instance of the class
        hounaar_class = context.get_symbol(self.class_name)
        if isinstance(hounaar_class, HounaarClass):
            return hounaar_class.create_instance()
        else:
            raise Exception(f"Class '{self.class_name}' not found.")

class HounaarClass:
    def __init__(self, name):
        self.name = name
        self.attributes = {}
        self.methods = {}

    def add_attribute(self, attribute):
        self.attributes[attribute] = None

    def add_method(self, method):
        self.methods[method] = None

    def create_instance(self):
        return HounaarObject(self)

class HounaarObject:
    def __init__(self, hounaar_class):
        self.hounaar_class = hounaar_class
        self.attributes = hounaar_class.attributes.copy()

# Add these classes to your existing parser and interpreter logic






class CurrentDateTimeNode:
    def interpret(self, context):
        current_datetime = datetime.datetime.now()
        return current_datetime

class FormatDateTimeNode:
    def __init__(self, format_string, date_node):
        self.format_string = format_string
        self.date_node = date_node

    def interpret(self, context):
        date = self.date_node.interpret(context)
        formatted_date = date.strftime(self.format_string)
        return formatted_date




class ImportNode:
    def __init__(self, filename):
        self.filename = filename

    def interpret(self, context):
        # Check if the file exists
        if os.path.isfile(self.filename):
            # Read the contents of the imported file
            with open(self.filename, 'r') as file:
                imported_code = file.read()
                # Execute the imported code in the current context
                exec(imported_code, context.symbol_table)
        else:
            raise Exception(f"File not found: {self.filename}")







class RegexMatchNode:
    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text

    def interpret(self, context):
        # Perform a regex match
        match = re.match(self.pattern, self.text)
        return match

class RegexSearchNode:
    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text

    def interpret(self, context):
        # Perform a regex search
        search = re.search(self.pattern, self.text)
        return search

class RegexSubNode:
    def __init__(self, pattern, replacement, text):
        self.pattern = pattern
        self.replacement = replacement
        self.text = text

    def interpret(self, context):
        # Perform a regex substitution
        replaced_text = re.sub(self.pattern, self.replacement, self.text)
        return replaced_text


class ArrayDefinitionNode:
    def __init__(self, elements):
        self.elements = elements

    def interpret(self, context):
        # Create an array and initialize it with the provided elements
        array = HounaarArray(self.elements)
        return array

class ArrayAccessNode:
    def __init__(self, array, index):
        self.array = array
        self.index = index

    def interpret(self, context):
        # Access the specified element in the array
        if isinstance(self.array, HounaarArray):
            return self.array.get(self.index)
        else:
            raise Exception("Not an array.")

class ArrayAssignmentNode:
    def __init__(self, array, index, value):
        self.array = array
        self.index = index
        self.value = value

    def interpret(self, context):
        # Assign a value to the specified element in the array
        if isinstance(self.array, HounaarArray):
            self.array.set(self.index, self.value)
        else:
            raise Exception("Not an array.")

class HounaarArray:
    def __init__(self, elements=None):
        self.elements = elements if elements is not None else []

    def get(self, index):
        if 0 <= index < len(self.elements):
            return self.elements[index]
        else:
            raise Exception("Array index out of bounds.")

    def set(self, index, value):
        if 0 <= index < len(self.elements):
            self.elements[index] = value
        else:
            raise Exception("Array index out of bounds.")



class SwitchNode:
    def __init__(self, expression):
        self.expression = expression
        self.cases = []

    def add_case(self, value, code):
        self.cases.append((value, code))

    def set_default(self, code):
        self.default = code

    def interpret(self, context):
        switch_value = self.expression.interpret(context)
        matched = False

        for case_value, case_code in self.cases:
            if switch_value == case_value:
                matched = True
                context.enter_block()
                case_code.interpret(context)
                context.exit_block()
                break

        if not matched and hasattr(self, 'default'):
            context.enter_block()
            self.default.interpret(context)
            context.exit_block()

class BreakNode:
    def interpret(self, context):
        context.set_break()

class ContinueNode:
    def interpret(self, context):
        context.set_continue()



class IfNode:
    def __init__(self, condition, code_block):
        self.condition = condition
        self.code_block = code_block

    def interpret(self, context):
        if self.condition.interpret(context):
            context.enter_block()
            self.code_block.interpret(context)
            context.exit_block()

class IfElseNode:
    def __init__(self, condition, if_block, else_block):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block

    def interpret(self, context):
        if self.condition.interpret(context):
            context.enter_block()
            self.if_block.interpret(context)
            context.exit_block()
        else:
            context.enter_block()
            self.else_block.interpret(context)
            context.exit_block()

class IfElifElseNode:
    def __init__(self, conditions, code_blocks, else_block=None):
        self.conditions = conditions
        self.code_blocks = code_blocks
        self.else_block = else_block

    def interpret(self, context):
        for condition, code_block in zip(self.conditions, self.code_blocks):
            if condition.interpret(context):
                context.enter_block()
                code_block.interpret(context)
                context.exit_block()
                return
        if self.else_block is not None:
            context.enter_block()
            self.else_block.interpret(context)
            context.exit_block()











if __name__ == '__main__':
    while True:
        try:
            text = input('>>> ')
        except EOFError:
            break

        if not text:
            continue

        interpreter = Interpreter(text)
        result = interpreter.eval()
        print(result)

