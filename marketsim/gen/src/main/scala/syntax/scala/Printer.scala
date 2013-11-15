package syntax.scala

class Printer() extends PrettyPrinter.Base {

    val crlf = "\r\n"
    val tab = "\t"

    // TODO: introduce for AST and Typed classes common traits and implement pretty printers through them

    def pars(s : Any, condition : Boolean = true) =
        if (condition) "(" + s + ")" else s.toString

    def apply(e : Typed.BooleanExpr) = e match {
        case Typed.Or(x, y) => x + " or " + y
        case Typed.And(x, y) =>
            def wrap(z : Typed.BooleanExpr) = pars(z, z.isInstanceOf[Typed.Or])
            wrap(x) + " and " + wrap(y)
        case Typed.Not(x) =>
            def wrap(z : Typed.BooleanExpr) = pars(z, !z.isInstanceOf[Typed.Condition])
            "not " + wrap(x)
        case Typed.Condition(c, x, y) => x.toString + c + y
    }

    def priority(e : Typed.Expr) = e match {
        case _ : Typed.FloatConst => 0
        case _ : Typed.ParamRef => 0
        case _ : Typed.Neg => 0
        case _ : Typed.FunctionCall => 0
        case Typed.BinOp(_,AST.Mul, _, _) => 1
        case Typed.BinOp(_,AST.Div, _, _) => 1
        case Typed.BinOp(_,AST.Add, _, _) => 2
        case Typed.BinOp(_,AST.Sub, _, _) => 2
        case _ : Typed.IfThenElse => 3
    }

    def need_brackets(x : Typed.Expr, e : Typed.Expr, rhs : Boolean) =
        priority(x) > priority(e) || priority(x) == priority(e) && rhs

    def wrap(x : Typed.Expr, e : Typed.Expr, rhs : Boolean) =
        pars(x, need_brackets(x, e, rhs))

    def wrap(x : Typed.Expr, e : Typed.Expr) : String = wrap(x, e, rhs = false)


    def apply(e : Typed.Expr) = e match {
        case Typed.BinOp(_, symbol, x, y) => wrap(x, e) + symbol + wrap(y, e, rhs = true)
        case Typed.Neg(_, x) => "-" + wrap(x, e)
        case Typed.IfThenElse(_, cond, x, y) => s"if $cond then ${wrap(x,e)} else ${wrap(y,e)}"
        case Typed.FunctionCall(f, args) => f.name + args.map({ _._2 }).mkString("(",",",")")
        case Typed.FloatConst(x) => x.toString
        case Typed.ParamRef(s) => s.name
    }


    def prefixedIfSome[A](p : Option[A], prefix : String = "") =
        if (p.nonEmpty) prefix + p.get else ""

    def apply(p : Typed.Parameter) =
    {
        import p._
        (name
         + " : " + ty
         + prefixedIfSome(initializer, " = "))
    }

    def apply(p : Typed.Annotation) =
        "@" + p.target.name + "(" + p.parameters.map({ "\"" + _ + "\""}).mkString(", ") + ")"

    def apply(p : Typed.Function) = {
        import p._
        (crlf + prefixedIfSome(docstring)
                + annotations.map({_ + crlf}).mkString("")
                + "def " + name
                + parameters.mkString("(", ", ", ")")
                + " : " + ret_type
                + prefixedIfSome(body, crlf + tab + " = ")
                )
    }

    def apply(p : AST.Definitions) = p.definitions.map({_ + crlf + crlf}).mkString("")
}

package object PP
{
    val crlf = "\r\n"
    val tab = "\t"
    
    trait Printable {
        def toScala : String
    }

    def pars(s : Any, condition : Boolean = true) =
        if (condition) "(" + s + ")" else s.toString

    def prefixedIfSome[A](p : Option[A], prefix : String = "") =
        if (p.nonEmpty) prefix + p.get else ""

    object ast {

        trait Definitions extends Printable {
            self: AST.Definitions =>
            def toScala = definitions.map({_ + crlf + crlf}).mkString("")
        }
        trait Function extends Printable {
            self: AST.FunDef =>
            def toScala =
                (prefixedIfSome(docstring)
                        + annotations.map({_ + crlf}).mkString("")
                        + "def " + name
                        + "(" + parameters.mkString(", ") + ")"
                        + prefixedIfSome(ret_type, " : ")
                        + prefixedIfSome(body, " = "))
        }

        trait DocString extends Printable {
            self: AST.DocString =>
            def toScala =
                ("/** " + brief
                        + detailed.lines.map({ crlf + " *" + _ }).mkString("") + crlf
                        + " */" + crlf)

        }

        trait Annotation extends Printable {
            self: AST.Annotation =>
            def toScala =
                "@" + name + "(" + parameters.map({ "\"" + _ + "\""}).mkString(", ") + ")"
        }

        trait QualifiedName extends Printable {
            self: AST.QualifiedName =>
            def toScala = names.mkString(".")
        }

        trait Parameter extends Printable {
            self: AST.Parameter =>
            def toScala =
                (annotations.map({ _ + " "}).mkString("")
                        + name
                        + prefixedIfSome(ty, " : ")
                        + prefixedIfSome(initializer, " = "))
        }

        trait BinOpSymbol extends Printable {
            val priority : Int
        }

        trait Add extends BinOpSymbol {
            def toScala = "+"
            val priority = 2
        }
        trait Sub extends BinOpSymbol {
            def toScala = "-"
            val priority = 2
        }
        trait Mul extends BinOpSymbol {
            def toScala = "*"
            val priority = 1
        }
        trait Div extends BinOpSymbol {
            def toScala = "/"
            val priority = 1
        }

        trait Expr extends Printable {
            val priority : Int

            def wrap(x : Expr, rhs : Boolean = false) =
                pars(x, need_brackets(x, rhs))

            def need_brackets(x : Expr, rhs : Boolean) =
                x.priority > priority || x.priority == priority && rhs
        }

        trait Const extends Expr {
            self: AST.Const =>
            def toScala = value.toString
            val priority = 0
        }

        trait Var extends Expr {
            self: AST.Var =>
            def toScala = s
            val priority = 0
        }

        trait FunCall extends Expr {
            self: AST.FunCall =>
            def toScala = name + pars(args.mkString(","))
            val priority = 0
        }

        trait BinOp extends Expr {
            self: AST.BinOp =>
            def toScala = wrap(x) + symbol + wrap(y, rhs = true)
            val priority = symbol.priority
        }

        trait Neg extends Expr {
            self: AST.Neg =>
            def toScala = "-" + wrap(x)
            val priority = 0
        }

        trait IfThenElse extends Expr {
            self: AST.IfThenElse =>
            def toScala = s"if $cond then ${wrap(x)} else ${wrap(y)}"
            val priority = 3
        }

        trait Or extends Printable {
            self: AST.Or =>
            def toScala = x + " or " + y
        }

        trait And extends Printable {
            self: AST.And =>
            def wrap(z : AST.BooleanExpr) = pars(z, z.isInstanceOf[AST.Or])
            def toScala = wrap(x) + " and " + wrap(y)
        }

        trait Not extends Printable {
            self: AST.Not =>
            def wrap(z : AST.BooleanExpr) = pars(z, !z.isInstanceOf[AST.Condition])
            def toScala = "not " + wrap(x)
        }

        trait Condition extends Printable {
            self: AST.Condition =>
            def toScala = x.toString + symbol + y
        }

        trait Less extends Printable {
            def toScala = "<"
        }
        trait LessEqual extends Printable {
            def toScala = "<="
        }
        trait Greater extends Printable {
            def toScala = ">"
        }
        trait GreaterEqual extends Printable {
            def toScala = ">="
        }
        trait Equal extends Printable {
            def toScala = "="
        }
        trait NotEqual extends Printable {
            def toScala = "<>"
        }

        trait SimpleType extends Printable {
            self: AST.SimpleType =>
            def toScala = name
        }

        trait UnitType extends Printable {
            def toScala = "()"
        }

        trait TupleType extends Printable {
            self: AST.TupleType =>
            def toScala = pars(types.mkString(","))
        }

        trait FunctionType extends Printable {
            self: AST.FunctionType =>
            def toScala = s"$arg_type => $ret_type"
        }
    }

    object types {

        trait Unit extends ast.UnitType

        trait `Float` extends Printable {
            def toScala = "Float"
        }

        trait `Boolean` extends Printable {
            def toScala = "Boolean"
        }

        trait Tuple extends Printable {
            self: Types.Tuple =>
            def toScala = pars(elems.mkString(","))
        }

        trait Function extends Printable {
            self: Types.Function =>
            def toScala = (if (args.length == 1) args(0) else args.mkString("(", ",", ")")) + s" => $ret"
        }
    }
}
