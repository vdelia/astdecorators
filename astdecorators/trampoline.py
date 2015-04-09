import decorator
import ast, meta

def trampoline(f, *args, **kwargs):
    g = f(*args, **kwargs)
    while callable(g):
        g = g()
    return g

class RewriteReturn(ast.NodeTransformer):

    def visit_Return(self, node):
        newnode = ast.Return(
                value=ast.Lambda(
                    args=ast.arguments(
                        args=[],
                        vararg=None,
                        kwarg=None, defaults=[]),
                    body=node.value),
                    )
        return ast.copy_location(newnode, node)

@decorator.decorator
def trampolined(f, *args, **kwargs):

    tree = meta.decompiler.decompile_func(f)
    transformed_tree = RewriteReturn().visit(tree)
    ast.fix_missing_locations(transformed_tree)

    scope = dict(globals())
    f = meta.decompiler.compile_func(transformed_tree, '', scope)
    scope[f.func_name] = f
    
    return trampoline(f, *args, **kwargs)

