package generator.python
import predef._

object strategy extends gen.PythonGenerator
{
    import base.{Def, Prop, Setter}

    case class Parameter(p : Typed.Parameter) extends base.Parameter

    trait Suspended extends base.Printer
    {
        def suspended =
            Prop("suspended", "return self.inner.suspended") |
            Setter("suspended", "self.inner.suspended = value")

        override def body = super.body | suspended
    }

    case class Import(args : List[String], f : Typed.Function)
            extends base.Printer
            with    base.DocString
            with    base.Alias
            with    base.DecoratedName
            with    base.Bind
            with    base.HasImpl
            with    Suspended
    {
        def mkParam(p : Typed.Parameter) = strategy.Parameter(p)
        type Parameter = strategy.Parameter

        override def init_body = super.init_body |
                ImportFrom("Event", "marketsim.gen._out.event._event") |
                "self.on_order_created = Event()" |
                "event.subscribe(self.impl.on_order_created, _(self)._send, self)" |||
                ImportFrom("event", "marketsim") |||
                ImportFrom("_", "marketsim")

        def className =
            parameters.head.p.ty.unOptionalize match {
                case t : TypesBound.Interface => t.decl.name
                case a : TypesBound.Alias => a.decl.name
                case _ => throw new Exception(s"First argument for a strategy $name must be a user defined type")
            }

        override def alias = super.alias match {
            case "Strategy" => className
            case "TwoSides" => className
            case "OneSide" => className + "Side"
            case "OneSideStrategy" => className + "Side"
            case x => x
        }

        def myBase = Typed.topLevel.ISingleAssetStrategy

        override def base_class_list = myBase :: Nil

        def send = Def("_send", "order, source", "self.on_order_created.fire(order, self)")

        override def body = super.body | send
    }

    def generatePython(/** arguments of the annotation */ args  : List[String])
                      (/** function to process         */ f     : Typed.Function) =
    {
        new Import(args, f)
    }

    val name = "python.strategy"
}
