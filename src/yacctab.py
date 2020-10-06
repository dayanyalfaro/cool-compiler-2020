
# yacctab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASSIGNrightNOTnonassocLTEQLTEQleftPLUSMINUSleftMULTIPLYDIVIDErightISVOIDrightINT_COMPleftATleftDOTARROW ASSIGN AT BOOLEAN BOOL_TYPE CASE CLASS COLON COMMA DIVIDE DOT ELSE EQ ESAC FALSE FI ID IF IN INHERITS INTEGER INT_COMP INT_TYPE IO_TYPE ISVOID LBRACE LET LOOP LPAREN LT LTEQ LexicographicError MAIN_TYPE MINUS MULTIPLY NEW NOT OBJECT_TYPE OF PLUS POOL RBRACE RPAREN SELF SELF_TYPE SEMICOLON STRING STRING_TYPE THEN TRUE TYPE WHILE\n        program : class_list\n        \n        class_list : class_list class SEMICOLON\n                   | class SEMICOLON\n        \n        class : CLASS TYPE LBRACE features_list_opt RBRACE\n        \n        class : CLASS TYPE INHERITS TYPE LBRACE features_list_opt RBRACE\n        \n        features_list_opt : features_list\n                          | empty\n        \n        features_list : features_list feature SEMICOLON\n                      | feature SEMICOLON\n        \n        feature : ID LPAREN formal_params_list RPAREN COLON TYPE LBRACE expression RBRACE\n        \n        feature : ID LPAREN RPAREN COLON TYPE LBRACE expression RBRACE\n        \n        feature : attribute_init\n        \n        attribute_init : ID COLON TYPE ASSIGN expression \n                       | attribute_def\n        \n        attribute_def : ID COLON TYPE\n        \n        formal_params_list  : formal_params_list COMMA formal_param\n                            | formal_param\n        \n        formal_param : ID COLON TYPE\n        \n        expression : ID\n        \n        expression : INTEGER\n        \n        expression : TRUE \n                   | FALSE\n        \n        expression : STRING\n        \n        expression  : SELF\n        \n        expression : LBRACE block_list RBRACE\n        \n        block_list : block_list expression SEMICOLON\n                   | expression SEMICOLON\n        \n        expression : ID ASSIGN expression\n        \n        expression : expression DOT ID LPAREN arguments_list_opt RPAREN\n        \n        arguments_list_opt : arguments_list\n                           | empty\n        \n        arguments_list : arguments_list COMMA expression\n                       | expression\n        \n        expression : expression AT TYPE DOT ID LPAREN arguments_list_opt RPAREN\n        \n        expression : ID LPAREN arguments_list_opt RPAREN\n        \n        expression : expression PLUS expression\n                   | expression MINUS expression\n                   | expression MULTIPLY expression\n                   | expression DIVIDE expression\n        \n        expression : expression LT expression\n                   | expression LTEQ expression\n                   | expression EQ expression\n        \n        expression : LPAREN expression RPAREN\n        \n        expression : IF expression THEN expression ELSE expression FI\n        \n        expression : WHILE expression LOOP expression POOL\n        \n         expression : let_expression\n        \n        let_expression : LET nested_vars IN expression\n        \n        nested_vars  : let_var_init\n                        | nested_vars COMMA let_var_init\n        \n        let_var_init : ID COLON TYPE ASSIGN expression \n                       | let_var_def\n        \n        let_var_def : ID COLON TYPE\n        \n        expression : CASE expression OF actions_list ESAC\n        \n        actions_list : actions_list action\n                     | action\n        \n        action : ID COLON TYPE ARROW expression SEMICOLON\n        \n        expression : NEW TYPE\n        \n        expression : ISVOID expression\n        \n        expression : INT_COMP expression\n        \n        expression : NOT expression\n        \n        empty :\n        '
    
_lr_action_items = {'CLASS':([0,2,6,8,],[4,4,-3,-2,]),'$end':([1,2,6,8,],[0,-1,-3,-2,]),'SEMICOLON':([3,5,14,16,17,19,20,30,37,42,43,44,45,46,47,48,53,74,79,80,81,82,89,96,97,98,99,100,101,102,103,104,106,114,115,125,128,133,134,138,144,146,147,],[6,8,21,-12,-14,-4,25,-15,-5,-19,-13,-20,-21,-22,-23,-24,-46,105,-57,-58,-59,-60,-28,-36,-37,-38,-39,-40,-41,-42,-25,119,-43,-11,-35,-47,-10,-45,-53,-29,-44,-34,148,]),'TYPE':([4,10,23,32,35,39,55,65,112,136,],[7,18,30,38,41,60,79,95,127,141,]),'LBRACE':([7,18,36,41,49,50,51,52,54,56,57,58,60,61,62,63,66,67,68,69,70,71,72,73,87,105,107,108,110,116,117,119,132,137,139,145,],[9,24,49,61,49,49,49,49,49,49,49,49,87,49,49,49,49,49,49,49,49,49,49,49,49,-27,49,49,49,49,49,-26,49,49,49,49,]),'INHERITS':([7,],[10,]),'RBRACE':([9,11,12,13,21,24,25,31,42,44,45,46,47,48,53,73,79,80,81,82,88,89,96,97,98,99,100,101,102,103,105,106,113,115,119,125,133,134,138,144,146,],[-61,19,-6,-7,-9,-61,-8,37,-19,-20,-21,-22,-23,-24,-46,103,-57,-58,-59,-60,114,-28,-36,-37,-38,-39,-40,-41,-42,-25,-27,-43,128,-35,-26,-47,-45,-53,-29,-44,-34,]),'ID':([9,12,21,22,24,25,34,36,49,50,51,52,54,56,57,58,59,61,62,63,64,66,67,68,69,70,71,72,73,87,105,107,108,109,110,111,116,117,118,119,122,123,132,135,137,139,145,148,],[15,15,-9,26,15,-8,26,42,42,42,42,42,42,42,42,42,85,42,42,42,94,42,42,42,42,42,42,42,42,42,-27,42,42,124,42,85,42,42,131,-26,124,-55,42,-54,42,42,42,-56,]),'LPAREN':([15,36,42,49,50,51,52,54,56,57,58,61,62,63,66,67,68,69,70,71,72,73,87,94,105,107,108,110,116,117,119,131,132,137,139,145,],[22,50,63,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,117,-27,50,50,50,50,50,-26,139,50,50,50,50,]),'COLON':([15,26,28,33,85,124,],[23,32,35,39,112,136,]),'RPAREN':([22,27,29,38,40,42,44,45,46,47,48,53,63,75,79,80,81,82,89,90,91,92,93,96,97,98,99,100,101,102,103,106,115,117,125,129,130,133,134,138,139,143,144,146,],[28,33,-17,-18,-16,-19,-20,-21,-22,-23,-24,-46,-61,106,-57,-58,-59,-60,-28,115,-30,-31,-33,-36,-37,-38,-39,-40,-41,-42,-25,-43,-35,-61,-47,-32,138,-45,-53,-29,-61,146,-44,-34,]),'COMMA':([27,29,38,40,42,44,45,46,47,48,53,79,80,81,82,83,84,86,89,91,93,96,97,98,99,100,101,102,103,106,115,125,126,127,129,133,134,138,142,144,146,],[34,-17,-18,-16,-19,-20,-21,-22,-23,-24,-46,-57,-58,-59,-60,111,-48,-51,-28,116,-33,-36,-37,-38,-39,-40,-41,-42,-25,-43,-35,-47,-49,-52,-32,-45,-53,-29,-50,-44,-34,]),'ASSIGN':([30,42,127,],[36,62,137,]),'INTEGER':([36,49,50,51,52,54,56,57,58,61,62,63,66,67,68,69,70,71,72,73,87,105,107,108,110,116,117,119,132,137,139,145,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-27,44,44,44,44,44,-26,44,44,44,44,]),'TRUE':([36,49,50,51,52,54,56,57,58,61,62,63,66,67,68,69,70,71,72,73,87,105,107,108,110,116,117,119,132,137,139,145,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-27,45,45,45,45,45,-26,45,45,45,45,]),'FALSE':([36,49,50,51,52,54,56,57,58,61,62,63,66,67,68,69,70,71,72,73,87,105,107,108,110,116,117,119,132,137,139,145,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-27,46,46,46,46,46,-26,46,46,46,46,]),'STRING':([36,49,50,51,52,54,56,57,58,61,62,63,66,67,68,69,70,71,72,73,87,105,107,108,110,116,117,119,132,137,139,145,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-27,47,47,47,47,47,-26,47,47,47,47,]),'SELF':([36,49,50,51,52,54,56,57,58,61,62,63,66,67,68,69,70,71,72,73,87,105,107,108,110,116,117,119,132,137,139,145,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-27,48,48,48,48,48,-26,48,48,48,48,]),'IF':([36,49,50,51,52,54,56,57,58,61,62,63,66,67,68,69,70,71,72,73,87,105,107,108,110,116,117,119,132,137,139,145,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,-27,51,51,51,51,51,-26,51,51,51,51,]),'WHILE':([36,49,50,51,52,54,56,57,58,61,62,63,66,67,68,69,70,71,72,73,87,105,107,108,110,116,117,119,132,137,139,145,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-27,52,52,52,52,52,-26,52,52,52,52,]),'CASE':([36,49,50,51,52,54,56,57,58,61,62,63,66,67,68,69,70,71,72,73,87,105,107,108,110,116,117,119,132,137,139,145,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,-27,54,54,54,54,54,-26,54,54,54,54,]),'NEW':([36,49,50,51,52,54,56,57,58,61,62,63,66,67,68,69,70,71,72,73,87,105,107,108,110,116,117,119,132,137,139,145,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,-27,55,55,55,55,55,-26,55,55,55,55,]),'ISVOID':([36,49,50,51,52,54,56,57,58,61,62,63,66,67,68,69,70,71,72,73,87,105,107,108,110,116,117,119,132,137,139,145,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,-27,56,56,56,56,56,-26,56,56,56,56,]),'INT_COMP':([36,49,50,51,52,54,56,57,58,61,62,63,66,67,68,69,70,71,72,73,87,105,107,108,110,116,117,119,132,137,139,145,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,-27,57,57,57,57,57,-26,57,57,57,57,]),'NOT':([36,49,50,51,52,54,56,57,58,61,62,63,66,67,68,69,70,71,72,73,87,105,107,108,110,116,117,119,132,137,139,145,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,-27,58,58,58,58,58,-26,58,58,58,58,]),'LET':([36,49,50,51,52,54,56,57,58,61,62,63,66,67,68,69,70,71,72,73,87,105,107,108,110,116,117,119,132,137,139,145,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,-27,59,59,59,59,59,-26,59,59,59,59,]),'DOT':([42,43,44,45,46,47,48,53,74,75,76,77,78,79,80,81,82,88,89,93,95,96,97,98,99,100,101,102,103,104,106,113,115,120,121,125,129,133,134,138,140,142,144,146,147,],[-19,64,-20,-21,-22,-23,-24,-46,64,64,64,64,64,-57,64,64,64,64,64,64,118,64,64,64,64,64,64,64,-25,64,-43,64,-35,64,64,64,64,-45,-53,-29,64,64,-44,-34,64,]),'AT':([42,43,44,45,46,47,48,53,74,75,76,77,78,79,80,81,82,88,89,93,96,97,98,99,100,101,102,103,104,106,113,115,120,121,125,129,133,134,138,140,142,144,146,147,],[-19,65,-20,-21,-22,-23,-24,-46,65,65,65,65,65,-57,65,65,65,65,65,65,65,65,65,65,65,65,65,-25,65,-43,65,-35,65,65,65,65,-45,-53,-29,65,65,-44,-34,65,]),'PLUS':([42,43,44,45,46,47,48,53,74,75,76,77,78,79,80,81,82,88,89,93,96,97,98,99,100,101,102,103,104,106,113,115,120,121,125,129,133,134,138,140,142,144,146,147,],[-19,66,-20,-21,-22,-23,-24,-46,66,66,66,66,66,-57,-58,-59,66,66,66,66,-36,-37,-38,-39,66,66,66,-25,66,-43,66,-35,66,66,66,66,-45,-53,-29,66,66,-44,-34,66,]),'MINUS':([42,43,44,45,46,47,48,53,74,75,76,77,78,79,80,81,82,88,89,93,96,97,98,99,100,101,102,103,104,106,113,115,120,121,125,129,133,134,138,140,142,144,146,147,],[-19,67,-20,-21,-22,-23,-24,-46,67,67,67,67,67,-57,-58,-59,67,67,67,67,-36,-37,-38,-39,67,67,67,-25,67,-43,67,-35,67,67,67,67,-45,-53,-29,67,67,-44,-34,67,]),'MULTIPLY':([42,43,44,45,46,47,48,53,74,75,76,77,78,79,80,81,82,88,89,93,96,97,98,99,100,101,102,103,104,106,113,115,120,121,125,129,133,134,138,140,142,144,146,147,],[-19,68,-20,-21,-22,-23,-24,-46,68,68,68,68,68,-57,-58,-59,68,68,68,68,68,68,-38,-39,68,68,68,-25,68,-43,68,-35,68,68,68,68,-45,-53,-29,68,68,-44,-34,68,]),'DIVIDE':([42,43,44,45,46,47,48,53,74,75,76,77,78,79,80,81,82,88,89,93,96,97,98,99,100,101,102,103,104,106,113,115,120,121,125,129,133,134,138,140,142,144,146,147,],[-19,69,-20,-21,-22,-23,-24,-46,69,69,69,69,69,-57,-58,-59,69,69,69,69,69,69,-38,-39,69,69,69,-25,69,-43,69,-35,69,69,69,69,-45,-53,-29,69,69,-44,-34,69,]),'LT':([42,43,44,45,46,47,48,53,74,75,76,77,78,79,80,81,82,88,89,93,96,97,98,99,100,101,102,103,104,106,113,115,120,121,125,129,133,134,138,140,142,144,146,147,],[-19,70,-20,-21,-22,-23,-24,-46,70,70,70,70,70,-57,-58,-59,70,70,70,70,-36,-37,-38,-39,None,None,None,-25,70,-43,70,-35,70,70,70,70,-45,-53,-29,70,70,-44,-34,70,]),'LTEQ':([42,43,44,45,46,47,48,53,74,75,76,77,78,79,80,81,82,88,89,93,96,97,98,99,100,101,102,103,104,106,113,115,120,121,125,129,133,134,138,140,142,144,146,147,],[-19,71,-20,-21,-22,-23,-24,-46,71,71,71,71,71,-57,-58,-59,71,71,71,71,-36,-37,-38,-39,None,None,None,-25,71,-43,71,-35,71,71,71,71,-45,-53,-29,71,71,-44,-34,71,]),'EQ':([42,43,44,45,46,47,48,53,74,75,76,77,78,79,80,81,82,88,89,93,96,97,98,99,100,101,102,103,104,106,113,115,120,121,125,129,133,134,138,140,142,144,146,147,],[-19,72,-20,-21,-22,-23,-24,-46,72,72,72,72,72,-57,-58,-59,72,72,72,72,-36,-37,-38,-39,None,None,None,-25,72,-43,72,-35,72,72,72,72,-45,-53,-29,72,72,-44,-34,72,]),'THEN':([42,44,45,46,47,48,53,76,79,80,81,82,89,96,97,98,99,100,101,102,103,106,115,125,133,134,138,144,146,],[-19,-20,-21,-22,-23,-24,-46,107,-57,-58,-59,-60,-28,-36,-37,-38,-39,-40,-41,-42,-25,-43,-35,-47,-45,-53,-29,-44,-34,]),'LOOP':([42,44,45,46,47,48,53,77,79,80,81,82,89,96,97,98,99,100,101,102,103,106,115,125,133,134,138,144,146,],[-19,-20,-21,-22,-23,-24,-46,108,-57,-58,-59,-60,-28,-36,-37,-38,-39,-40,-41,-42,-25,-43,-35,-47,-45,-53,-29,-44,-34,]),'OF':([42,44,45,46,47,48,53,78,79,80,81,82,89,96,97,98,99,100,101,102,103,106,115,125,133,134,138,144,146,],[-19,-20,-21,-22,-23,-24,-46,109,-57,-58,-59,-60,-28,-36,-37,-38,-39,-40,-41,-42,-25,-43,-35,-47,-45,-53,-29,-44,-34,]),'ELSE':([42,44,45,46,47,48,53,79,80,81,82,89,96,97,98,99,100,101,102,103,106,115,120,125,133,134,138,144,146,],[-19,-20,-21,-22,-23,-24,-46,-57,-58,-59,-60,-28,-36,-37,-38,-39,-40,-41,-42,-25,-43,-35,132,-47,-45,-53,-29,-44,-34,]),'POOL':([42,44,45,46,47,48,53,79,80,81,82,89,96,97,98,99,100,101,102,103,106,115,121,125,133,134,138,144,146,],[-19,-20,-21,-22,-23,-24,-46,-57,-58,-59,-60,-28,-36,-37,-38,-39,-40,-41,-42,-25,-43,-35,133,-47,-45,-53,-29,-44,-34,]),'FI':([42,44,45,46,47,48,53,79,80,81,82,89,96,97,98,99,100,101,102,103,106,115,125,133,134,138,140,144,146,],[-19,-20,-21,-22,-23,-24,-46,-57,-58,-59,-60,-28,-36,-37,-38,-39,-40,-41,-42,-25,-43,-35,-47,-45,-53,-29,144,-44,-34,]),'IN':([42,44,45,46,47,48,53,79,80,81,82,83,84,86,89,96,97,98,99,100,101,102,103,106,115,125,126,127,133,134,138,142,144,146,],[-19,-20,-21,-22,-23,-24,-46,-57,-58,-59,-60,110,-48,-51,-28,-36,-37,-38,-39,-40,-41,-42,-25,-43,-35,-47,-49,-52,-45,-53,-29,-50,-44,-34,]),'ESAC':([122,123,135,148,],[134,-55,-54,-56,]),'ARROW':([141,],[145,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'class_list':([0,],[2,]),'class':([0,2,],[3,5,]),'features_list_opt':([9,24,],[11,31,]),'features_list':([9,24,],[12,12,]),'empty':([9,24,63,117,139,],[13,13,92,92,92,]),'feature':([9,12,24,],[14,20,14,]),'attribute_init':([9,12,24,],[16,16,16,]),'attribute_def':([9,12,24,],[17,17,17,]),'formal_params_list':([22,],[27,]),'formal_param':([22,34,],[29,40,]),'expression':([36,49,50,51,52,54,56,57,58,61,62,63,66,67,68,69,70,71,72,73,87,107,108,110,116,117,132,137,139,145,],[43,74,75,76,77,78,80,81,82,88,89,93,96,97,98,99,100,101,102,104,113,120,121,125,129,93,140,142,93,147,]),'let_expression':([36,49,50,51,52,54,56,57,58,61,62,63,66,67,68,69,70,71,72,73,87,107,108,110,116,117,132,137,139,145,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'block_list':([49,],[73,]),'nested_vars':([59,],[83,]),'let_var_init':([59,111,],[84,126,]),'let_var_def':([59,111,],[86,86,]),'arguments_list_opt':([63,117,139,],[90,130,143,]),'arguments_list':([63,117,139,],[91,91,91,]),'actions_list':([109,],[122,]),'action':([109,122,],[123,135,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> class_list','program',1,'p_program','parser.py',92),
  ('class_list -> class_list class SEMICOLON','class_list',3,'p_class_list','parser.py',98),
  ('class_list -> class SEMICOLON','class_list',2,'p_class_list','parser.py',99),
  ('class -> CLASS TYPE LBRACE features_list_opt RBRACE','class',5,'p_class','parser.py',108),
  ('class -> CLASS TYPE INHERITS TYPE LBRACE features_list_opt RBRACE','class',7,'p_class_inherits','parser.py',114),
  ('features_list_opt -> features_list','features_list_opt',1,'p_feature_list_opt','parser.py',120),
  ('features_list_opt -> empty','features_list_opt',1,'p_feature_list_opt','parser.py',121),
  ('features_list -> features_list feature SEMICOLON','features_list',3,'p_feature_list','parser.py',127),
  ('features_list -> feature SEMICOLON','features_list',2,'p_feature_list','parser.py',128),
  ('feature -> ID LPAREN formal_params_list RPAREN COLON TYPE LBRACE expression RBRACE','feature',9,'p_feature_method','parser.py',137),
  ('feature -> ID LPAREN RPAREN COLON TYPE LBRACE expression RBRACE','feature',8,'p_feature_method_no_formals','parser.py',144),
  ('feature -> attribute_init','feature',1,'p_feature_attr_initialized','parser.py',151),
  ('attribute_init -> ID COLON TYPE ASSIGN expression','attribute_init',5,'p_atrribute_init','parser.py',157),
  ('attribute_init -> attribute_def','attribute_init',1,'p_atrribute_init','parser.py',158),
  ('attribute_def -> ID COLON TYPE','attribute_def',3,'p_feature_attr','parser.py',168),
  ('formal_params_list -> formal_params_list COMMA formal_param','formal_params_list',3,'p_formal_list_many','parser.py',174),
  ('formal_params_list -> formal_param','formal_params_list',1,'p_formal_list_many','parser.py',175),
  ('formal_param -> ID COLON TYPE','formal_param',3,'p_formal_param','parser.py',184),
  ('expression -> ID','expression',1,'p_expression_object_identifier','parser.py',190),
  ('expression -> INTEGER','expression',1,'p_expression_integer_constant','parser.py',196),
  ('expression -> TRUE','expression',1,'p_expression_boolean_constant','parser.py',202),
  ('expression -> FALSE','expression',1,'p_expression_boolean_constant','parser.py',203),
  ('expression -> STRING','expression',1,'p_expression_string_constant','parser.py',209),
  ('expression -> SELF','expression',1,'p_expr_self','parser.py',215),
  ('expression -> LBRACE block_list RBRACE','expression',3,'p_expression_block','parser.py',221),
  ('block_list -> block_list expression SEMICOLON','block_list',3,'p_block_list','parser.py',227),
  ('block_list -> expression SEMICOLON','block_list',2,'p_block_list','parser.py',228),
  ('expression -> ID ASSIGN expression','expression',3,'p_expression_assignment','parser.py',237),
  ('expression -> expression DOT ID LPAREN arguments_list_opt RPAREN','expression',6,'p_expression_dispatch','parser.py',245),
  ('arguments_list_opt -> arguments_list','arguments_list_opt',1,'p_arguments_list_opt','parser.py',252),
  ('arguments_list_opt -> empty','arguments_list_opt',1,'p_arguments_list_opt','parser.py',253),
  ('arguments_list -> arguments_list COMMA expression','arguments_list',3,'p_arguments_list','parser.py',259),
  ('arguments_list -> expression','arguments_list',1,'p_arguments_list','parser.py',260),
  ('expression -> expression AT TYPE DOT ID LPAREN arguments_list_opt RPAREN','expression',8,'p_expression_static_dispatch','parser.py',269),
  ('expression -> ID LPAREN arguments_list_opt RPAREN','expression',4,'p_expression_self_dispatch','parser.py',276),
  ('expression -> expression PLUS expression','expression',3,'p_expression_math_operations','parser.py',285),
  ('expression -> expression MINUS expression','expression',3,'p_expression_math_operations','parser.py',286),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression_math_operations','parser.py',287),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_math_operations','parser.py',288),
  ('expression -> expression LT expression','expression',3,'p_expression_math_comparisons','parser.py',301),
  ('expression -> expression LTEQ expression','expression',3,'p_expression_math_comparisons','parser.py',302),
  ('expression -> expression EQ expression','expression',3,'p_expression_math_comparisons','parser.py',303),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_with_parenthesis','parser.py',314),
  ('expression -> IF expression THEN expression ELSE expression FI','expression',7,'p_expression_if_conditional','parser.py',322),
  ('expression -> WHILE expression LOOP expression POOL','expression',5,'p_expression_while_loop','parser.py',329),
  ('expression -> let_expression','expression',1,'p_expression_let','parser.py',337),
  ('let_expression -> LET nested_vars IN expression','let_expression',4,'p_expression_let_simple','parser.py',343),
  ('nested_vars -> let_var_init','nested_vars',1,'p_nested_let_vars','parser.py',349),
  ('nested_vars -> nested_vars COMMA let_var_init','nested_vars',3,'p_nested_let_vars','parser.py',350),
  ('let_var_init -> ID COLON TYPE ASSIGN expression','let_var_init',5,'p_let_var_initialized','parser.py',359),
  ('let_var_init -> let_var_def','let_var_init',1,'p_let_var_initialized','parser.py',360),
  ('let_var_def -> ID COLON TYPE','let_var_def',3,'p_let_var_def','parser.py',370),
  ('expression -> CASE expression OF actions_list ESAC','expression',5,'p_expression_case','parser.py',378),
  ('actions_list -> actions_list action','actions_list',2,'p_actions_list','parser.py',384),
  ('actions_list -> action','actions_list',1,'p_actions_list','parser.py',385),
  ('action -> ID COLON TYPE ARROW expression SEMICOLON','action',6,'p_action_expr','parser.py',394),
  ('expression -> NEW TYPE','expression',2,'p_expression_new','parser.py',403),
  ('expression -> ISVOID expression','expression',2,'p_expression_isvoid','parser.py',409),
  ('expression -> INT_COMP expression','expression',2,'p_expression_integer_complement','parser.py',415),
  ('expression -> NOT expression','expression',2,'p_expression_boolean_complement','parser.py',421),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',427),
]
