
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BAND BANDEQU BOR BOREQU BREAK CASE CEQ CGE CGT CHAR CHARACTER CLE CLT CNEQ COLON COMMA COMMETBLOCK COMMETLINE CONTINUE DECIMAL DEFAULT DIVIDE DIVIDEQU DO DOUBLE ELSE EQUAL FALSE FLOAT FOR IDENTIFIER IF INCLUDE INT INV LBRACE LPAREN LSQUARE MINUS MINUSELF MINUSEQU MULTI MULTIEQU NOT NUMBER OR PLUS PLUSELF PLUSEQU RBRACE RETURN RPAREN RSQUARE SEMICOLON STRING SWITCH TRUE VOID WHILE\n    program : functions\n            | e\n    \n    e :\n    \n    functions : function\n              | function functions\n    \n    function : func_ret IDENTIFIER LPAREN params RPAREN block\n             | func_ret IDENTIFIER LPAREN RPAREN block\n    \n    func_ret : VOID\n             | var_type\n    \n    var_type : INT\n             | DOUBLE\n             | FLOAT\n             | CHAR\n    \n    params : param\n           | param COMMA params\n    \n    param : var_type IDENTIFIER\n          | var_type IDENTIFIER LSQUARE RSQUARE\n    \n    block : LBRACE e RBRACE\n          | LBRACE statements RBRACE\n    \n    statements : statement\n               | statement statements\n    \n    statement : declaration SEMICOLON\n              | expression SEMICOLON\n              | return SEMICOLON\n              | BREAK SEMICOLON\n              | CONTINUE SEMICOLON\n              | for_block\n              | while_block\n              | do_while_block\n              | if_block\n              | switch_block\n    \n    switch_block : SWITCH LPAREN expression RPAREN LBRACE case_blocks RBRACE\n    \n    case_blocks : e\n                | default_block\n                | case_block case_blocks\n    \n    case_block : CASE expression COLON block\n    \n    default_block : DEFAULT COLON block\n    \n    if_block : IF LPAREN expression RPAREN block elif_blocks\n    \n    elif_blocks : e\n                | else_block\n                | elif_block elif_blocks\n    \n    elif_block : ELSE IF LPAREN expression RPAREN block\n    \n    else_block : ELSE block\n    \n    for_block : FOR LPAREN for_init SEMICOLON for_cond SEMICOLON for_update RPAREN block\n    \n    for_init : e\n             | declaration\n             | expression\n    \n    for_cond : e\n             | expression\n    \n    for_update : e\n               | expression\n    \n    while_block : WHILE LPAREN expression RPAREN block\n    \n    do_while_block : DO block WHILE LPAREN expression RPAREN\n    \n    expression : LPAREN expression RPAREN\n                | expression operator expression\n                | unary expression\n                | expression unary\n                | operand\n    \n    operator : operator_calc\n             | operator_boolean\n             | operator_bit\n             | operator_cond\n    \n    operator_calc : PLUS\n                  | MINUS\n                  | MULTI\n                  | DIVIDE\n                  | EQUAL\n                  | PLUSEQU\n                  | MINUSEQU\n                  | MULTIEQU\n                  | DIVIDEQU\n    \n    operator_boolean : AND\n                     | OR\n                     | NOT\n    \n    operator_bit : BAND\n                 | BOR\n                 | BANDEQU\n                 | BOREQU\n                 | INV\n    \n    operator_cond : CEQ\n                  | CNEQ\n                  | CGT\n                  | CLT\n                  | CGE\n                  | CLE\n    \n    operand : IDENTIFIER\n            | variable\n            | IDENTIFIER LSQUARE expression RSQUARE\n    \n    return : RETURN expression\n           | RETURN\n    \n    declaration : var_type IDENTIFIER\n                | var_type IDENTIFIER EQUAL expression\n                | var_type IDENTIFIER LSQUARE NUMBER RSQUARE\n                | var_type IDENTIFIER LSQUARE NUMBER RSQUARE EQUAL expression\n    \n    unary : NOT\n          | INV\n          | PLUSELF\n          | MINUSELF\n    \n    variable : NUMBER\n             | MINUS NUMBER\n             | DECIMAL\n             | MINUS DECIMAL\n             | CHARACTER\n             | STRING\n             | TRUE\n             | FALSE\n             | func_call\n    \n    func_call : IDENTIFIER LPAREN args RPAREN\n              | IDENTIFIER LPAREN RPAREN\n    \n    args : expression\n         | expression COMMA args\n    '
    
_lr_action_items = {'$end':([0,1,2,3,4,12,20,24,64,65,],[-3,0,-1,-2,-4,-5,-7,-6,-18,-19,]),'VOID':([0,4,20,24,64,65,],[6,6,-7,-6,-18,-19,]),'INT':([0,4,14,20,21,22,24,27,33,34,35,36,37,64,65,67,68,98,99,100,107,146,148,152,153,154,155,156,168,169,171,179,183,],[8,8,8,-7,8,8,-6,8,-27,-28,-29,-30,-31,-18,-19,-22,-23,-24,-25,-26,8,-52,-3,-53,-38,-39,-40,-3,-41,-43,-32,-44,-42,]),'DOUBLE':([0,4,14,20,21,22,24,27,33,34,35,36,37,64,65,67,68,98,99,100,107,146,148,152,153,154,155,156,168,169,171,179,183,],[9,9,9,-7,9,9,-6,9,-27,-28,-29,-30,-31,-18,-19,-22,-23,-24,-25,-26,9,-52,-3,-53,-38,-39,-40,-3,-41,-43,-32,-44,-42,]),'FLOAT':([0,4,14,20,21,22,24,27,33,34,35,36,37,64,65,67,68,98,99,100,107,146,148,152,153,154,155,156,168,169,171,179,183,],[10,10,10,-7,10,10,-6,10,-27,-28,-29,-30,-31,-18,-19,-22,-23,-24,-25,-26,10,-52,-3,-53,-38,-39,-40,-3,-41,-43,-32,-44,-42,]),'CHAR':([0,4,14,20,21,22,24,27,33,34,35,36,37,64,65,67,68,98,99,100,107,146,148,152,153,154,155,156,168,169,171,179,183,],[11,11,11,-7,11,11,-6,11,-27,-28,-29,-30,-31,-18,-19,-22,-23,-24,-25,-26,11,-52,-3,-53,-38,-39,-40,-3,-41,-43,-32,-44,-42,]),'IDENTIFIER':([5,6,7,8,9,10,11,18,21,27,33,34,35,36,37,38,41,42,44,50,51,52,53,64,65,67,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,107,108,110,111,116,135,136,138,146,148,150,151,152,153,154,155,156,163,168,169,171,176,179,183,],[13,-8,-9,-10,-11,-12,-13,23,39,39,-27,-28,-29,-30,-31,101,39,39,39,-95,-96,-97,-98,-18,-19,-22,-23,39,-59,-60,-61,-62,-74,-79,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-75,-76,-77,-78,-80,-81,-82,-83,-84,-85,-24,-25,-26,39,39,39,39,39,39,39,39,39,39,-52,-3,39,39,-53,-38,-39,-40,-3,39,-41,-43,-32,39,-44,-42,]),'LPAREN':([13,21,27,33,34,35,36,37,39,41,42,44,45,46,48,49,50,51,52,53,64,65,67,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,107,108,110,111,116,128,135,136,138,146,148,150,151,152,153,154,155,156,163,168,169,170,171,176,179,183,],[14,41,41,-27,-28,-29,-30,-31,103,41,41,41,107,108,110,111,-95,-96,-97,-98,-18,-19,-22,-23,41,-59,-60,-61,-62,-74,-79,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-75,-76,-77,-78,-80,-81,-82,-83,-84,-85,-24,-25,-26,41,41,41,41,41,41,41,138,41,41,41,-52,-3,41,41,-53,-38,-39,-40,-3,41,-41,-43,176,-32,41,-44,-42,]),'RPAREN':([14,15,17,23,39,40,43,52,53,54,56,57,58,59,60,61,62,70,75,76,103,104,105,112,113,114,115,119,120,121,122,127,129,130,133,134,142,147,151,165,166,167,180,],[16,19,-14,-16,-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-15,-57,-95,-96,120,122,-56,-100,-102,-17,-55,134,-109,-110,-54,137,139,140,-88,-108,-111,152,-3,175,-50,-51,182,]),'LBRACE':([16,19,47,137,139,140,157,173,175,178,182,],[21,21,21,21,21,149,21,21,21,21,21,]),'COMMA':([17,23,39,40,43,52,53,54,56,57,58,59,60,61,70,75,76,105,112,113,114,115,120,121,122,133,134,],[22,-16,-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,-56,-100,-102,-17,-55,-109,135,-54,-88,-108,]),'RBRACE':([21,25,26,27,33,34,35,36,37,64,65,66,67,68,98,99,100,146,148,149,152,153,154,155,156,158,159,160,161,168,169,171,172,177,179,181,183,],[-3,64,65,-20,-27,-28,-29,-30,-31,-18,-19,-21,-22,-23,-24,-25,-26,-52,-3,-3,-53,-38,-39,-40,-3,171,-33,-34,-3,-41,-43,-32,-35,-37,-44,-36,-42,]),'BREAK':([21,27,33,34,35,36,37,64,65,67,68,98,99,100,146,148,152,153,154,155,156,168,169,171,179,183,],[31,31,-27,-28,-29,-30,-31,-18,-19,-22,-23,-24,-25,-26,-52,-3,-53,-38,-39,-40,-3,-41,-43,-32,-44,-42,]),'CONTINUE':([21,27,33,34,35,36,37,64,65,67,68,98,99,100,146,148,152,153,154,155,156,168,169,171,179,183,],[32,32,-27,-28,-29,-30,-31,-18,-19,-22,-23,-24,-25,-26,-52,-3,-53,-38,-39,-40,-3,-41,-43,-32,-44,-42,]),'RETURN':([21,27,33,34,35,36,37,64,65,67,68,98,99,100,146,148,152,153,154,155,156,168,169,171,179,183,],[44,44,-27,-28,-29,-30,-31,-18,-19,-22,-23,-24,-25,-26,-52,-3,-53,-38,-39,-40,-3,-41,-43,-32,-44,-42,]),'FOR':([21,27,33,34,35,36,37,64,65,67,68,98,99,100,146,148,152,153,154,155,156,168,169,171,179,183,],[45,45,-27,-28,-29,-30,-31,-18,-19,-22,-23,-24,-25,-26,-52,-3,-53,-38,-39,-40,-3,-41,-43,-32,-44,-42,]),'WHILE':([21,27,33,34,35,36,37,64,65,67,68,98,99,100,109,146,148,152,153,154,155,156,168,169,171,179,183,],[46,46,-27,-28,-29,-30,-31,-18,-19,-22,-23,-24,-25,-26,128,-52,-3,-53,-38,-39,-40,-3,-41,-43,-32,-44,-42,]),'DO':([21,27,33,34,35,36,37,64,65,67,68,98,99,100,146,148,152,153,154,155,156,168,169,171,179,183,],[47,47,-27,-28,-29,-30,-31,-18,-19,-22,-23,-24,-25,-26,-52,-3,-53,-38,-39,-40,-3,-41,-43,-32,-44,-42,]),'IF':([21,27,33,34,35,36,37,64,65,67,68,98,99,100,146,148,152,153,154,155,156,157,168,169,171,179,183,],[48,48,-27,-28,-29,-30,-31,-18,-19,-22,-23,-24,-25,-26,-52,-3,-53,-38,-39,-40,-3,170,-41,-43,-32,-44,-42,]),'SWITCH':([21,27,33,34,35,36,37,64,65,67,68,98,99,100,146,148,152,153,154,155,156,168,169,171,179,183,],[49,49,-27,-28,-29,-30,-31,-18,-19,-22,-23,-24,-25,-26,-52,-3,-53,-38,-39,-40,-3,-41,-43,-32,-44,-42,]),'NOT':([21,27,29,33,34,35,36,37,39,40,41,42,43,44,50,51,52,53,54,56,57,58,59,60,61,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,105,106,107,108,110,111,112,113,115,116,118,120,121,122,126,127,129,130,131,133,134,135,136,138,145,146,147,148,150,151,152,153,154,155,156,163,164,167,168,169,171,174,176,179,180,183,],[50,50,75,-27,-28,-29,-30,-31,-86,-99,50,50,-58,50,-95,-96,-97,-98,-87,-101,-103,-104,-105,-106,-107,-18,-19,-22,-23,50,-57,-59,-60,-61,-62,-74,-79,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-75,-76,-77,-78,-80,-81,-82,-83,-84,-85,-24,-25,-26,50,50,75,75,75,50,50,50,50,-100,-102,75,50,75,-109,75,-54,75,75,75,75,75,-88,-108,50,50,50,75,-52,75,-3,50,50,-53,-38,-39,-40,-3,50,75,75,-41,-43,-32,75,50,-44,75,-42,]),'INV':([21,27,29,33,34,35,36,37,39,40,41,42,43,44,50,51,52,53,54,56,57,58,59,60,61,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,105,106,107,108,110,111,112,113,115,116,118,120,121,122,126,127,129,130,131,133,134,135,136,138,145,146,147,148,150,151,152,153,154,155,156,163,164,167,168,169,171,174,176,179,180,183,],[51,51,76,-27,-28,-29,-30,-31,-86,-99,51,51,-58,51,-95,-96,-97,-98,-87,-101,-103,-104,-105,-106,-107,-18,-19,-22,-23,51,-57,-59,-60,-61,-62,-74,-79,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-75,-76,-77,-78,-80,-81,-82,-83,-84,-85,-24,-25,-26,51,51,76,76,76,51,51,51,51,-100,-102,76,51,76,-109,76,-54,76,76,76,76,76,-88,-108,51,51,51,76,-52,76,-3,51,51,-53,-38,-39,-40,-3,51,76,76,-41,-43,-32,76,51,-44,76,-42,]),'PLUSELF':([21,27,29,33,34,35,36,37,39,40,41,42,43,44,50,51,52,53,54,56,57,58,59,60,61,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,105,106,107,108,110,111,112,113,115,116,118,120,121,122,126,127,129,130,131,133,134,135,136,138,145,146,147,148,150,151,152,153,154,155,156,163,164,167,168,169,171,174,176,179,180,183,],[52,52,52,-27,-28,-29,-30,-31,-86,-99,52,52,-58,52,-95,-96,-97,-98,-87,-101,-103,-104,-105,-106,-107,-18,-19,-22,-23,52,-57,-59,-60,-61,-62,-74,-79,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-75,-76,-77,-78,-80,-81,-82,-83,-84,-85,-24,-25,-26,52,52,52,52,52,52,52,52,52,-100,-102,52,52,52,-109,52,-54,52,52,52,52,52,-88,-108,52,52,52,52,-52,52,-3,52,52,-53,-38,-39,-40,-3,52,52,52,-41,-43,-32,52,52,-44,52,-42,]),'MINUSELF':([21,27,29,33,34,35,36,37,39,40,41,42,43,44,50,51,52,53,54,56,57,58,59,60,61,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,105,106,107,108,110,111,112,113,115,116,118,120,121,122,126,127,129,130,131,133,134,135,136,138,145,146,147,148,150,151,152,153,154,155,156,163,164,167,168,169,171,174,176,179,180,183,],[53,53,53,-27,-28,-29,-30,-31,-86,-99,53,53,-58,53,-95,-96,-97,-98,-87,-101,-103,-104,-105,-106,-107,-18,-19,-22,-23,53,-57,-59,-60,-61,-62,-74,-79,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-75,-76,-77,-78,-80,-81,-82,-83,-84,-85,-24,-25,-26,53,53,53,53,53,53,53,53,53,-100,-102,53,53,53,-109,53,-54,53,53,53,53,53,-88,-108,53,53,53,53,-52,53,-3,53,53,-53,-38,-39,-40,-3,53,53,53,-41,-43,-32,53,53,-44,53,-42,]),'NUMBER':([21,27,33,34,35,36,37,41,42,44,50,51,52,53,55,64,65,67,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,107,108,110,111,116,117,135,136,138,146,148,150,151,152,153,154,155,156,163,168,169,171,176,179,183,],[40,40,-27,-28,-29,-30,-31,40,40,40,-95,-96,-97,-98,112,-18,-19,-22,-23,40,-59,-60,-61,-62,-74,-79,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-75,-76,-77,-78,-80,-81,-82,-83,-84,-85,-24,-25,-26,40,40,40,40,40,40,40,132,40,40,40,-52,-3,40,40,-53,-38,-39,-40,-3,40,-41,-43,-32,40,-44,-42,]),'MINUS':([21,27,29,33,34,35,36,37,39,40,41,42,43,44,50,51,52,53,54,56,57,58,59,60,61,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,105,106,107,108,110,111,112,113,115,116,118,120,121,122,126,127,129,130,131,133,134,135,136,138,145,146,147,148,150,151,152,153,154,155,156,163,164,167,168,169,171,174,176,179,180,183,],[55,55,78,-27,-28,-29,-30,-31,-86,-99,55,55,-58,55,-95,-96,-97,-98,-87,-101,-103,-104,-105,-106,-107,-18,-19,-22,-23,55,-57,-59,-60,-61,-62,-74,-79,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-75,-76,-77,-78,-80,-81,-82,-83,-84,-85,-24,-25,-26,55,55,78,78,78,55,55,55,55,-100,-102,78,55,78,-109,78,-54,78,78,78,78,78,-88,-108,55,55,55,78,-52,78,-3,55,55,-53,-38,-39,-40,-3,55,78,78,-41,-43,-32,78,55,-44,78,-42,]),'DECIMAL':([21,27,33,34,35,36,37,41,42,44,50,51,52,53,55,64,65,67,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,107,108,110,111,116,135,136,138,146,148,150,151,152,153,154,155,156,163,168,169,171,176,179,183,],[56,56,-27,-28,-29,-30,-31,56,56,56,-95,-96,-97,-98,113,-18,-19,-22,-23,56,-59,-60,-61,-62,-74,-79,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-75,-76,-77,-78,-80,-81,-82,-83,-84,-85,-24,-25,-26,56,56,56,56,56,56,56,56,56,56,-52,-3,56,56,-53,-38,-39,-40,-3,56,-41,-43,-32,56,-44,-42,]),'CHARACTER':([21,27,33,34,35,36,37,41,42,44,50,51,52,53,64,65,67,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,107,108,110,111,116,135,136,138,146,148,150,151,152,153,154,155,156,163,168,169,171,176,179,183,],[57,57,-27,-28,-29,-30,-31,57,57,57,-95,-96,-97,-98,-18,-19,-22,-23,57,-59,-60,-61,-62,-74,-79,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-75,-76,-77,-78,-80,-81,-82,-83,-84,-85,-24,-25,-26,57,57,57,57,57,57,57,57,57,57,-52,-3,57,57,-53,-38,-39,-40,-3,57,-41,-43,-32,57,-44,-42,]),'STRING':([21,27,33,34,35,36,37,41,42,44,50,51,52,53,64,65,67,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,107,108,110,111,116,135,136,138,146,148,150,151,152,153,154,155,156,163,168,169,171,176,179,183,],[58,58,-27,-28,-29,-30,-31,58,58,58,-95,-96,-97,-98,-18,-19,-22,-23,58,-59,-60,-61,-62,-74,-79,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-75,-76,-77,-78,-80,-81,-82,-83,-84,-85,-24,-25,-26,58,58,58,58,58,58,58,58,58,58,-52,-3,58,58,-53,-38,-39,-40,-3,58,-41,-43,-32,58,-44,-42,]),'TRUE':([21,27,33,34,35,36,37,41,42,44,50,51,52,53,64,65,67,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,107,108,110,111,116,135,136,138,146,148,150,151,152,153,154,155,156,163,168,169,171,176,179,183,],[59,59,-27,-28,-29,-30,-31,59,59,59,-95,-96,-97,-98,-18,-19,-22,-23,59,-59,-60,-61,-62,-74,-79,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-75,-76,-77,-78,-80,-81,-82,-83,-84,-85,-24,-25,-26,59,59,59,59,59,59,59,59,59,59,-52,-3,59,59,-53,-38,-39,-40,-3,59,-41,-43,-32,59,-44,-42,]),'FALSE':([21,27,33,34,35,36,37,41,42,44,50,51,52,53,64,65,67,68,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,107,108,110,111,116,135,136,138,146,148,150,151,152,153,154,155,156,163,168,169,171,176,179,183,],[60,60,-27,-28,-29,-30,-31,60,60,60,-95,-96,-97,-98,-18,-19,-22,-23,60,-59,-60,-61,-62,-74,-79,-63,-64,-65,-66,-67,-68,-69,-70,-71,-72,-73,-75,-76,-77,-78,-80,-81,-82,-83,-84,-85,-24,-25,-26,60,60,60,60,60,60,60,60,60,60,-52,-3,60,60,-53,-38,-39,-40,-3,60,-41,-43,-32,60,-44,-42,]),'LSQUARE':([23,39,101,],[63,102,117,]),'SEMICOLON':([28,29,30,31,32,39,40,43,44,52,53,54,56,57,58,59,60,61,70,75,76,101,105,106,107,112,113,115,120,122,123,124,125,126,131,133,134,136,141,143,144,145,164,],[67,68,98,99,100,-86,-99,-58,-90,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,-91,-56,-89,-3,-100,-102,-55,-109,-54,136,-45,-46,-47,-92,-88,-108,-3,-93,151,-48,-49,-94,]),'PLUS':([29,39,40,43,52,53,54,56,57,58,59,60,61,70,75,76,104,105,106,112,113,115,118,120,121,122,126,127,129,130,131,133,134,145,147,164,167,174,180,],[77,-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,77,77,77,-100,-102,77,77,-109,77,-54,77,77,77,77,77,-88,-108,77,77,77,77,77,77,]),'MULTI':([29,39,40,43,52,53,54,56,57,58,59,60,61,70,75,76,104,105,106,112,113,115,118,120,121,122,126,127,129,130,131,133,134,145,147,164,167,174,180,],[79,-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,79,79,79,-100,-102,79,79,-109,79,-54,79,79,79,79,79,-88,-108,79,79,79,79,79,79,]),'DIVIDE':([29,39,40,43,52,53,54,56,57,58,59,60,61,70,75,76,104,105,106,112,113,115,118,120,121,122,126,127,129,130,131,133,134,145,147,164,167,174,180,],[80,-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,80,80,80,-100,-102,80,80,-109,80,-54,80,80,80,80,80,-88,-108,80,80,80,80,80,80,]),'EQUAL':([29,39,40,43,52,53,54,56,57,58,59,60,61,70,75,76,101,104,105,106,112,113,115,118,120,121,122,126,127,129,130,131,133,134,141,145,147,164,167,174,180,],[81,-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,116,81,81,81,-100,-102,81,81,-109,81,-54,81,81,81,81,81,-88,-108,150,81,81,81,81,81,81,]),'PLUSEQU':([29,39,40,43,52,53,54,56,57,58,59,60,61,70,75,76,104,105,106,112,113,115,118,120,121,122,126,127,129,130,131,133,134,145,147,164,167,174,180,],[82,-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,82,82,82,-100,-102,82,82,-109,82,-54,82,82,82,82,82,-88,-108,82,82,82,82,82,82,]),'MINUSEQU':([29,39,40,43,52,53,54,56,57,58,59,60,61,70,75,76,104,105,106,112,113,115,118,120,121,122,126,127,129,130,131,133,134,145,147,164,167,174,180,],[83,-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,83,83,83,-100,-102,83,83,-109,83,-54,83,83,83,83,83,-88,-108,83,83,83,83,83,83,]),'MULTIEQU':([29,39,40,43,52,53,54,56,57,58,59,60,61,70,75,76,104,105,106,112,113,115,118,120,121,122,126,127,129,130,131,133,134,145,147,164,167,174,180,],[84,-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,84,84,84,-100,-102,84,84,-109,84,-54,84,84,84,84,84,-88,-108,84,84,84,84,84,84,]),'DIVIDEQU':([29,39,40,43,52,53,54,56,57,58,59,60,61,70,75,76,104,105,106,112,113,115,118,120,121,122,126,127,129,130,131,133,134,145,147,164,167,174,180,],[85,-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,85,85,85,-100,-102,85,85,-109,85,-54,85,85,85,85,85,-88,-108,85,85,85,85,85,85,]),'AND':([29,39,40,43,52,53,54,56,57,58,59,60,61,70,75,76,104,105,106,112,113,115,118,120,121,122,126,127,129,130,131,133,134,145,147,164,167,174,180,],[86,-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,86,86,86,-100,-102,86,86,-109,86,-54,86,86,86,86,86,-88,-108,86,86,86,86,86,86,]),'OR':([29,39,40,43,52,53,54,56,57,58,59,60,61,70,75,76,104,105,106,112,113,115,118,120,121,122,126,127,129,130,131,133,134,145,147,164,167,174,180,],[87,-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,87,87,87,-100,-102,87,87,-109,87,-54,87,87,87,87,87,-88,-108,87,87,87,87,87,87,]),'BAND':([29,39,40,43,52,53,54,56,57,58,59,60,61,70,75,76,104,105,106,112,113,115,118,120,121,122,126,127,129,130,131,133,134,145,147,164,167,174,180,],[88,-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,88,88,88,-100,-102,88,88,-109,88,-54,88,88,88,88,88,-88,-108,88,88,88,88,88,88,]),'BOR':([29,39,40,43,52,53,54,56,57,58,59,60,61,70,75,76,104,105,106,112,113,115,118,120,121,122,126,127,129,130,131,133,134,145,147,164,167,174,180,],[89,-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,89,89,89,-100,-102,89,89,-109,89,-54,89,89,89,89,89,-88,-108,89,89,89,89,89,89,]),'BANDEQU':([29,39,40,43,52,53,54,56,57,58,59,60,61,70,75,76,104,105,106,112,113,115,118,120,121,122,126,127,129,130,131,133,134,145,147,164,167,174,180,],[90,-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,90,90,90,-100,-102,90,90,-109,90,-54,90,90,90,90,90,-88,-108,90,90,90,90,90,90,]),'BOREQU':([29,39,40,43,52,53,54,56,57,58,59,60,61,70,75,76,104,105,106,112,113,115,118,120,121,122,126,127,129,130,131,133,134,145,147,164,167,174,180,],[91,-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,91,91,91,-100,-102,91,91,-109,91,-54,91,91,91,91,91,-88,-108,91,91,91,91,91,91,]),'CEQ':([29,39,40,43,52,53,54,56,57,58,59,60,61,70,75,76,104,105,106,112,113,115,118,120,121,122,126,127,129,130,131,133,134,145,147,164,167,174,180,],[92,-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,92,92,92,-100,-102,92,92,-109,92,-54,92,92,92,92,92,-88,-108,92,92,92,92,92,92,]),'CNEQ':([29,39,40,43,52,53,54,56,57,58,59,60,61,70,75,76,104,105,106,112,113,115,118,120,121,122,126,127,129,130,131,133,134,145,147,164,167,174,180,],[93,-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,93,93,93,-100,-102,93,93,-109,93,-54,93,93,93,93,93,-88,-108,93,93,93,93,93,93,]),'CGT':([29,39,40,43,52,53,54,56,57,58,59,60,61,70,75,76,104,105,106,112,113,115,118,120,121,122,126,127,129,130,131,133,134,145,147,164,167,174,180,],[94,-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,94,94,94,-100,-102,94,94,-109,94,-54,94,94,94,94,94,-88,-108,94,94,94,94,94,94,]),'CLT':([29,39,40,43,52,53,54,56,57,58,59,60,61,70,75,76,104,105,106,112,113,115,118,120,121,122,126,127,129,130,131,133,134,145,147,164,167,174,180,],[95,-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,95,95,95,-100,-102,95,95,-109,95,-54,95,95,95,95,95,-88,-108,95,95,95,95,95,95,]),'CGE':([29,39,40,43,52,53,54,56,57,58,59,60,61,70,75,76,104,105,106,112,113,115,118,120,121,122,126,127,129,130,131,133,134,145,147,164,167,174,180,],[96,-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,96,96,96,-100,-102,96,96,-109,96,-54,96,96,96,96,96,-88,-108,96,96,96,96,96,96,]),'CLE':([29,39,40,43,52,53,54,56,57,58,59,60,61,70,75,76,104,105,106,112,113,115,118,120,121,122,126,127,129,130,131,133,134,145,147,164,167,174,180,],[97,-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,97,97,97,-100,-102,97,97,-109,97,-54,97,97,97,97,97,-88,-108,97,97,97,97,97,97,]),'RSQUARE':([39,40,43,52,53,54,56,57,58,59,60,61,63,70,75,76,105,112,113,115,118,120,122,132,133,134,],[-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,114,-57,-95,-96,-56,-100,-102,-55,133,-109,-54,141,-88,-108,]),'COLON':([39,40,43,52,53,54,56,57,58,59,60,61,70,75,76,105,112,113,115,120,122,133,134,162,174,],[-86,-99,-58,-97,-98,-87,-101,-103,-104,-105,-106,-107,-57,-95,-96,-56,-100,-102,-55,-109,-54,-88,-108,173,178,]),'ELSE':([64,65,148,156,183,],[-18,-19,157,157,-42,]),'DEFAULT':([64,65,149,161,181,],[-18,-19,162,162,-36,]),'CASE':([64,65,149,161,181,],[-18,-19,163,163,-36,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'functions':([0,4,],[2,12,]),'e':([0,21,107,136,148,149,151,156,161,],[3,25,124,144,154,159,166,154,159,]),'function':([0,4,],[4,4,]),'func_ret':([0,4,],[5,5,]),'var_type':([0,4,14,21,22,27,107,],[7,7,18,38,18,38,38,]),'params':([14,22,],[15,62,]),'param':([14,22,],[17,17,]),'block':([16,19,47,137,139,157,173,175,178,182,],[20,24,109,146,148,169,177,179,181,183,]),'statements':([21,27,],[26,66,]),'statement':([21,27,],[27,27,]),'declaration':([21,27,107,],[28,28,125,]),'expression':([21,27,41,42,44,69,102,103,107,108,110,111,116,135,136,138,150,151,163,176,],[29,29,104,105,106,115,118,121,126,127,129,130,131,121,145,147,164,167,174,180,]),'return':([21,27,],[30,30,]),'for_block':([21,27,],[33,33,]),'while_block':([21,27,],[34,34,]),'do_while_block':([21,27,],[35,35,]),'if_block':([21,27,],[36,36,]),'switch_block':([21,27,],[37,37,]),'unary':([21,27,29,41,42,44,69,102,103,104,105,106,107,108,110,111,115,116,118,121,126,127,129,130,131,135,136,138,145,147,150,151,163,164,167,174,176,180,],[42,42,70,42,42,42,42,42,42,70,70,70,42,42,42,42,70,42,70,70,70,70,70,70,70,42,42,42,70,70,42,42,42,70,70,70,42,70,]),'operand':([21,27,41,42,44,69,102,103,107,108,110,111,116,135,136,138,150,151,163,176,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'variable':([21,27,41,42,44,69,102,103,107,108,110,111,116,135,136,138,150,151,163,176,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'func_call':([21,27,41,42,44,69,102,103,107,108,110,111,116,135,136,138,150,151,163,176,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'operator':([29,104,105,106,115,118,121,126,127,129,130,131,145,147,164,167,174,180,],[69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,]),'operator_calc':([29,104,105,106,115,118,121,126,127,129,130,131,145,147,164,167,174,180,],[71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,]),'operator_boolean':([29,104,105,106,115,118,121,126,127,129,130,131,145,147,164,167,174,180,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,]),'operator_bit':([29,104,105,106,115,118,121,126,127,129,130,131,145,147,164,167,174,180,],[73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,]),'operator_cond':([29,104,105,106,115,118,121,126,127,129,130,131,145,147,164,167,174,180,],[74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'args':([103,135,],[119,142,]),'for_init':([107,],[123,]),'for_cond':([136,],[143,]),'elif_blocks':([148,156,],[153,168,]),'else_block':([148,156,],[155,155,]),'elif_block':([148,156,],[156,156,]),'case_blocks':([149,161,],[158,172,]),'default_block':([149,161,],[160,160,]),'case_block':([149,161,],[161,161,]),'for_update':([151,],[165,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> functions','program',1,'p_program','yacc.py',21),
  ('program -> e','program',1,'p_program','yacc.py',22),
  ('e -> <empty>','e',0,'p_e','yacc.py',28),
  ('functions -> function','functions',1,'p_functions','yacc.py',34),
  ('functions -> function functions','functions',2,'p_functions','yacc.py',35),
  ('function -> func_ret IDENTIFIER LPAREN params RPAREN block','function',6,'p_function','yacc.py',41),
  ('function -> func_ret IDENTIFIER LPAREN RPAREN block','function',5,'p_function','yacc.py',42),
  ('func_ret -> VOID','func_ret',1,'p_func_ret','yacc.py',48),
  ('func_ret -> var_type','func_ret',1,'p_func_ret','yacc.py',49),
  ('var_type -> INT','var_type',1,'p_var_type','yacc.py',55),
  ('var_type -> DOUBLE','var_type',1,'p_var_type','yacc.py',56),
  ('var_type -> FLOAT','var_type',1,'p_var_type','yacc.py',57),
  ('var_type -> CHAR','var_type',1,'p_var_type','yacc.py',58),
  ('params -> param','params',1,'p_params','yacc.py',64),
  ('params -> param COMMA params','params',3,'p_params','yacc.py',65),
  ('param -> var_type IDENTIFIER','param',2,'p_param','yacc.py',71),
  ('param -> var_type IDENTIFIER LSQUARE RSQUARE','param',4,'p_param','yacc.py',72),
  ('block -> LBRACE e RBRACE','block',3,'p_block','yacc.py',78),
  ('block -> LBRACE statements RBRACE','block',3,'p_block','yacc.py',79),
  ('statements -> statement','statements',1,'p_statements','yacc.py',85),
  ('statements -> statement statements','statements',2,'p_statements','yacc.py',86),
  ('statement -> declaration SEMICOLON','statement',2,'p_statement','yacc.py',92),
  ('statement -> expression SEMICOLON','statement',2,'p_statement','yacc.py',93),
  ('statement -> return SEMICOLON','statement',2,'p_statement','yacc.py',94),
  ('statement -> BREAK SEMICOLON','statement',2,'p_statement','yacc.py',95),
  ('statement -> CONTINUE SEMICOLON','statement',2,'p_statement','yacc.py',96),
  ('statement -> for_block','statement',1,'p_statement','yacc.py',97),
  ('statement -> while_block','statement',1,'p_statement','yacc.py',98),
  ('statement -> do_while_block','statement',1,'p_statement','yacc.py',99),
  ('statement -> if_block','statement',1,'p_statement','yacc.py',100),
  ('statement -> switch_block','statement',1,'p_statement','yacc.py',101),
  ('switch_block -> SWITCH LPAREN expression RPAREN LBRACE case_blocks RBRACE','switch_block',7,'p_switch_block','yacc.py',107),
  ('case_blocks -> e','case_blocks',1,'p_case_blocks','yacc.py',113),
  ('case_blocks -> default_block','case_blocks',1,'p_case_blocks','yacc.py',114),
  ('case_blocks -> case_block case_blocks','case_blocks',2,'p_case_blocks','yacc.py',115),
  ('case_block -> CASE expression COLON block','case_block',4,'p_case_block','yacc.py',121),
  ('default_block -> DEFAULT COLON block','default_block',3,'p_default_block','yacc.py',127),
  ('if_block -> IF LPAREN expression RPAREN block elif_blocks','if_block',6,'p_if_block','yacc.py',133),
  ('elif_blocks -> e','elif_blocks',1,'p_elif_blocks','yacc.py',139),
  ('elif_blocks -> else_block','elif_blocks',1,'p_elif_blocks','yacc.py',140),
  ('elif_blocks -> elif_block elif_blocks','elif_blocks',2,'p_elif_blocks','yacc.py',141),
  ('elif_block -> ELSE IF LPAREN expression RPAREN block','elif_block',6,'p_elif_block','yacc.py',147),
  ('else_block -> ELSE block','else_block',2,'p_else_block','yacc.py',153),
  ('for_block -> FOR LPAREN for_init SEMICOLON for_cond SEMICOLON for_update RPAREN block','for_block',9,'p_for_block','yacc.py',159),
  ('for_init -> e','for_init',1,'p_for_init','yacc.py',165),
  ('for_init -> declaration','for_init',1,'p_for_init','yacc.py',166),
  ('for_init -> expression','for_init',1,'p_for_init','yacc.py',167),
  ('for_cond -> e','for_cond',1,'p_for_cond','yacc.py',173),
  ('for_cond -> expression','for_cond',1,'p_for_cond','yacc.py',174),
  ('for_update -> e','for_update',1,'p_for_update','yacc.py',180),
  ('for_update -> expression','for_update',1,'p_for_update','yacc.py',181),
  ('while_block -> WHILE LPAREN expression RPAREN block','while_block',5,'p_while_block','yacc.py',187),
  ('do_while_block -> DO block WHILE LPAREN expression RPAREN','do_while_block',6,'p_do_while_block','yacc.py',193),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','yacc.py',199),
  ('expression -> expression operator expression','expression',3,'p_expression','yacc.py',200),
  ('expression -> unary expression','expression',2,'p_expression','yacc.py',201),
  ('expression -> expression unary','expression',2,'p_expression','yacc.py',202),
  ('expression -> operand','expression',1,'p_expression','yacc.py',203),
  ('operator -> operator_calc','operator',1,'p_operator','yacc.py',209),
  ('operator -> operator_boolean','operator',1,'p_operator','yacc.py',210),
  ('operator -> operator_bit','operator',1,'p_operator','yacc.py',211),
  ('operator -> operator_cond','operator',1,'p_operator','yacc.py',212),
  ('operator_calc -> PLUS','operator_calc',1,'p_operator_calc','yacc.py',218),
  ('operator_calc -> MINUS','operator_calc',1,'p_operator_calc','yacc.py',219),
  ('operator_calc -> MULTI','operator_calc',1,'p_operator_calc','yacc.py',220),
  ('operator_calc -> DIVIDE','operator_calc',1,'p_operator_calc','yacc.py',221),
  ('operator_calc -> EQUAL','operator_calc',1,'p_operator_calc','yacc.py',222),
  ('operator_calc -> PLUSEQU','operator_calc',1,'p_operator_calc','yacc.py',223),
  ('operator_calc -> MINUSEQU','operator_calc',1,'p_operator_calc','yacc.py',224),
  ('operator_calc -> MULTIEQU','operator_calc',1,'p_operator_calc','yacc.py',225),
  ('operator_calc -> DIVIDEQU','operator_calc',1,'p_operator_calc','yacc.py',226),
  ('operator_boolean -> AND','operator_boolean',1,'p_operator_boolean','yacc.py',232),
  ('operator_boolean -> OR','operator_boolean',1,'p_operator_boolean','yacc.py',233),
  ('operator_boolean -> NOT','operator_boolean',1,'p_operator_boolean','yacc.py',234),
  ('operator_bit -> BAND','operator_bit',1,'p_operator_bit','yacc.py',240),
  ('operator_bit -> BOR','operator_bit',1,'p_operator_bit','yacc.py',241),
  ('operator_bit -> BANDEQU','operator_bit',1,'p_operator_bit','yacc.py',242),
  ('operator_bit -> BOREQU','operator_bit',1,'p_operator_bit','yacc.py',243),
  ('operator_bit -> INV','operator_bit',1,'p_operator_bit','yacc.py',244),
  ('operator_cond -> CEQ','operator_cond',1,'p_operator_cond','yacc.py',250),
  ('operator_cond -> CNEQ','operator_cond',1,'p_operator_cond','yacc.py',251),
  ('operator_cond -> CGT','operator_cond',1,'p_operator_cond','yacc.py',252),
  ('operator_cond -> CLT','operator_cond',1,'p_operator_cond','yacc.py',253),
  ('operator_cond -> CGE','operator_cond',1,'p_operator_cond','yacc.py',254),
  ('operator_cond -> CLE','operator_cond',1,'p_operator_cond','yacc.py',255),
  ('operand -> IDENTIFIER','operand',1,'p_operand','yacc.py',261),
  ('operand -> variable','operand',1,'p_operand','yacc.py',262),
  ('operand -> IDENTIFIER LSQUARE expression RSQUARE','operand',4,'p_operand','yacc.py',263),
  ('return -> RETURN expression','return',2,'p_return','yacc.py',269),
  ('return -> RETURN','return',1,'p_return','yacc.py',270),
  ('declaration -> var_type IDENTIFIER','declaration',2,'p_declaration','yacc.py',276),
  ('declaration -> var_type IDENTIFIER EQUAL expression','declaration',4,'p_declaration','yacc.py',277),
  ('declaration -> var_type IDENTIFIER LSQUARE NUMBER RSQUARE','declaration',5,'p_declaration','yacc.py',278),
  ('declaration -> var_type IDENTIFIER LSQUARE NUMBER RSQUARE EQUAL expression','declaration',7,'p_declaration','yacc.py',279),
  ('unary -> NOT','unary',1,'p_unary','yacc.py',285),
  ('unary -> INV','unary',1,'p_unary','yacc.py',286),
  ('unary -> PLUSELF','unary',1,'p_unary','yacc.py',287),
  ('unary -> MINUSELF','unary',1,'p_unary','yacc.py',288),
  ('variable -> NUMBER','variable',1,'p_variable','yacc.py',294),
  ('variable -> MINUS NUMBER','variable',2,'p_variable','yacc.py',295),
  ('variable -> DECIMAL','variable',1,'p_variable','yacc.py',296),
  ('variable -> MINUS DECIMAL','variable',2,'p_variable','yacc.py',297),
  ('variable -> CHARACTER','variable',1,'p_variable','yacc.py',298),
  ('variable -> STRING','variable',1,'p_variable','yacc.py',299),
  ('variable -> TRUE','variable',1,'p_variable','yacc.py',300),
  ('variable -> FALSE','variable',1,'p_variable','yacc.py',301),
  ('variable -> func_call','variable',1,'p_variable','yacc.py',302),
  ('func_call -> IDENTIFIER LPAREN args RPAREN','func_call',4,'p_func_call','yacc.py',308),
  ('func_call -> IDENTIFIER LPAREN RPAREN','func_call',3,'p_func_call','yacc.py',309),
  ('args -> expression','args',1,'p_args','yacc.py',315),
  ('args -> expression COMMA args','args',3,'p_args','yacc.py',316),
]