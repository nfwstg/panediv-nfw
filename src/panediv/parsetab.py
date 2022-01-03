
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "COMMAND_DQ COMMAND_SIMPLE COMMAND_SQ NUMBER PERCENTcommand : COMMAND_SIMPLE\n               | COMMAND_SQ\n               | COMMAND_DQpane : command\n            | '(' command ')'\n            | '(' command ',' ')'pane : NUMBER\n            | '(' ',' NUMBER ')'pane : PERCENT\n            | '(' ',' PERCENT ')'pane : '(' command ',' NUMBER ')'pane : '(' command ',' PERCENT ')'pane : columnpane : rowpanes : ','panes : pane ','panes : panes ',' panepanes : panes ','column : '{' panes '}'row : '[' panes ']'"
    
_lr_action_items = {'COMMAND_SIMPLE':([0,],[2,]),'COMMAND_SQ':([0,],[3,]),'COMMAND_DQ':([0,],[4,]),'$end':([1,2,3,4,],[0,-1,-2,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'command':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> command","S'",1,None,None,None),
  ('command -> COMMAND_SIMPLE','command',1,'p_command','parse.py',11),
  ('command -> COMMAND_SQ','command',1,'p_command','parse.py',12),
  ('command -> COMMAND_DQ','command',1,'p_command','parse.py',13),
  ('pane -> command','pane',1,'p_pane_command','parse.py',17),
  ('pane -> ( command )','pane',3,'p_pane_command','parse.py',18),
  ('pane -> ( command , )','pane',4,'p_pane_command','parse.py',19),
  ('pane -> NUMBER','pane',1,'p_pane_number','parse.py',23),
  ('pane -> ( , NUMBER )','pane',4,'p_pane_number','parse.py',24),
  ('pane -> PERCENT','pane',1,'p_pane_percent','parse.py',28),
  ('pane -> ( , PERCENT )','pane',4,'p_pane_percent','parse.py',29),
  ('pane -> ( command , NUMBER )','pane',5,'p_pane_command_and_number','parse.py',33),
  ('pane -> ( command , PERCENT )','pane',5,'p_pane_command_and_percent','parse.py',37),
  ('pane -> column','pane',1,'p_pane_column','parse.py',41),
  ('pane -> row','pane',1,'p_pane_row','parse.py',45),
  ('panes -> ,','panes',1,'p_panes_start_with_conmma','parse.py',49),
  ('panes -> pane ,','panes',2,'p_panes_start_with_pane','parse.py',53),
  ('panes -> panes , pane','panes',3,'p_panes_mid','parse.py',57),
  ('panes -> panes ,','panes',2,'p_panes_last','parse.py',61),
  ('column -> { panes }','column',3,'p_column','parse.py',65),
  ('row -> [ panes ]','row',3,'p_row','parse.py',69),
]