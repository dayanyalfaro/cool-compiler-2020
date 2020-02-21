class AST:
    def __init__(self):
        pass


# <program> ::= <classes>
class Program(AST):
    def __init__(self, classes):
        super(Program, self).__init__()
        self.classes = classes


# <class> ::= class TYPE <inheritance> { <features_list_opt> } ;
class Class(AST):
    def __init__(self, name, parent, features):
        super(Class, self).__init__()
        self.name = name
        self.parent = parent
        self.features = features


# <feature> ::= ID ( <formal_params_list_opt> ) : TYPE { <expression> }
class ClassMethod(AST):
    def __init__(self, name, params, return_type, expr):
        super(ClassMethod, self).__init__()
        self.name = name
        self.params = params
        self.return_type = return_type
        self.expr = expr


# <formal> ::= ID : TYPE <- <expression> | <formal_param>
class Formal(AST):
    def __init__(self, name, Type, expr):
        super(Formal, self).__init__()
        self.name = name
        self.type = Type
        self.expr = expr


# <formal_param> ::= ID : TYPE
class FormalParameter(AST):
    def __init__(self, name, param_type):
        super(FormalParameter, self).__init__()
        self.name = name
        self.param_type = param_type


# <formal_param> ::= ID : TYPE | ID : TYPE <- <expression> 
class Parameter(AST):
    def __init__(self, name, TYPE, expr):
        super(Parameter, self).__init__()
        self.name = name
        self.TYPE = TYPE
        self.expr = expr

# <expression>
class Expr(AST):
    def __init__(self):
        super(Expr, self).__init__()

# <expression> ::= ID <- <expr>
class AssingExpr(Expr):
    def __init__(self, instance, expr):
        super(AssingExpr, self).__init__()
        self.instance = instance
        self.expr = expr

# <expression> ::= <expression>.ID( <arguments_list_opt> )
class DynamicCall(Expr):
    def __init__(self, instance, method, args):
        super(DynamicCall, self).__init__()
        self.instance = instance
        self.method = method
        self.args = args

# <expression> ::= <expression><at-type>.ID( <arguments_list_opt> )
class StaticCall(Expr):
    def __init__(self, instance, static_type, method, args):
        super(StaticCall, self).__init__()
        self.instance = instance
        self.method = method
        self.static_type = static_type
        self.args = args

# <arguments_list>  ::= <arguments_list_opt> , <expression>
#                   |   <expression>

class Arg(Expr):
    def __init__(self, expr):
        super(Arg, self)
        self.expr = expr

# <expression> ::= <case>
# <case> ::= case <expression> of <actions> esac
class Case(Expr):
    def __init__(self, expr, actions):
        super(Case, self).__init__()
        self.expr = expr
        self.actions = actions

# <actions> ::= <action>
#            |   <action> <actions>
# <action> ::= ID : TYPE => <expr>
class Action(AST):
    def __init__(self, name, action_type, body):
        super(Action, self).__init__()
        self.name = name
        self.action_type = action_type
        self.body = body

# <expression> ::= <if_then_else>
# <if_then_else> ::= if <expression> then <expression> else <expression> fi
class If(Expr):
    def __init__(self, predicate, then_body, else_body):
        super(If, self).__init__()
        self.predicate = predicate
        self.then_body = then_body
        self.else_body = else_body

# <expression> ::= <while>
# <while> ::= while <expression> loop <expression> pool
class While(Expr):
    def __init__(self, predicate, body):
        super(While, self).__init__()
        self.predicate = predicate
        self.body = body

# <expression> ::= <block_expression>
# <block_expression> ::= { <block_list> }
# <block_list> ::= <block_list> <expression> ;
#               |   <expression> ;
class Block(Expr):
    def __init__(self, exprs):
        super(Block, self).__init__()
        self.exprs = exprs

# <expression> ::= <let_expression>
# <let_expression> ::= let <nested_formals> in <expression>
# <nested_formals> ::= <formal>
#                  |   <nested_formals> , <formal>
class Let(Expr):
    def __init__(self, formal_list, body):
        super(Let, self).__init__()
        self.formal_list = formal_list
        self.body = body

# <expression> ::= new TYPE
class NewType(Expr):
    def __init__(self, Type):
        super(NewType, self)
        self.type = Type

# <expression> ::= isvoid <expr>
class IsVoid(Expr):
    def __init__(self, expr):
        super(IsVoid, self).__init__()
        self.expr = expr

# <expression> ::= <expression> + <expression>
class Sum(Expr):
    def __init__(self, summand1, summand2):
        super(Sum, self).__init__()
        self.summand1 = summand1
        self.summand2 = summand2


# <expression> ::= <expression> - <expression>
class Sub(Expr):
    def __init__(self, minuend, subtrahend):
        super(Sub, self).__init__()
        self.minuend = minuend
        self.subtrahend = subtrahend


# <expression> ::= <expression> * <expression>
class Mult(Expr):
    def __init__(self, factor1, factor2):
        super(Mult, self).__init__()
        self.factor1 = factor1
        self.factor2 = factor2


# <expression> ::= <expression> / <expression>
class Div(Expr):
    def __init__(self, dividend , divisor):
        super(Div, self).__init__()
        self.dividend  = dividend 
        self.divisor = divisor


# <expression> ::= ~ <expression>
class LogicalNot(Expr):
    def __init__(self, expr):
        super(LogicalNot, self).__init__()
        self.expr = expr


# <expression> ::= <expression> < <expression>
class LessThan(Expr):
    def __init__(self, left, right):
        super(LessThan, self).__init__()
        self.left = left
        self.right = right


# <expression> ::= <expression> <= <expression>
class LessOrEqualThan(Expr):
    def __init__(self, left, right):
        super(LessOrEqualThan, self).__init__()
        self.left = left
        self.right = right

# <expression> ::= <expression> = <expression>
class Equals(Expr):
    def __init__(self, left, right):
        super(Equals, self).__init__()
        self.left = left
        self.right = right


# <expression> ::= not <expression>
class Not(Expr):
    def __init__(self, expr):
        super(Not, self).__init__()
        self.expr = expr


# <expression> ::= ID
class Object(Expr):
    def __init__(self, name):
        super(Object, self).__init__()
        self.name = name


# <expression> ::= SELF
class SELF(Object):
    def __init__(self):
        super(SELF, self).__init__("SELF")


# <expression> ::= INTEGER
class INTEGER(Expr):
    def __init__(self, value):
        super(INTEGER, self).__init__()
        self.value = value


# <expression> ::= INTEGER
class STRING(Expr):
    def __init__(self, value):
        super(STRING, self).__init__()
        self.value = value

# <expression> ::= TRUE | FALSE
class Boolean(Expr):
    def __init__(self, value):
        super(Boolean, self).__init__()
        self.value = value