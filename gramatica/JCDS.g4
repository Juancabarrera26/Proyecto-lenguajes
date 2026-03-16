grammar JCDS;

program
    : statement+ EOF
    ;

statement
    : assignment
    | expression
    ;

assignment
    : ID '=' expression
    ;

expression
    : expression '^' expression
    | expression '*' expression
    | expression '/' expression
    | expression '+' expression
    | expression '-' expression
    | NUMBER
    | ID
    | '(' expression ')'
    ;

ID
    : [a-zA-Z]+
    ;

NUMBER
    : [0-9]+
    ;

WS
    : [ \t\r\n]+ -> skip
    ;
