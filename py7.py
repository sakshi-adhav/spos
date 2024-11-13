import ply.lex as lex
import ply.yacc as yacc

# LEX Part (Lexical Analysis)

# List of token names
tokens = (
    'NUMBER',   # Token for numbers
    'PLUS',     # Token for +
    'MINUS',    # Token for -
    'TIMES',    # Token for *
    'DIVIDE',   # Token for /
    'LPAREN',   # Token for (
    'RPAREN'    # Token for )
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# Regular expression rule for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Convert the token to an integer
    return t

# Ignoring spaces and tabs
t_ignore = ' \t'

# Error handling for illegal characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# YACC Part (Syntax Analysis)

# Precedence rules to handle the order of operations
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Parsing rules

# Rule for expressions involving binary operations
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

# Rule for grouped expressions in parentheses
def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

# Rule for numbers
def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error!")

# Build the parser
parser = yacc.yacc()

# Main loop to test the calculator
if __name__ == "__main__":
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print("Result:", result)
