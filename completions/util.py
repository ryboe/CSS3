
def get_scopes(view, location):
    """Return the scopes at the given location.

    >>> get_scopes(123)
    ['source.css', 'foo.bar.baz.css']
    """
    return view.scope_name(location).split()


def scope_name(scopes, prefix):
    """Extract the "foo" name from a list of scopes.

    >>> scopes = ['source.css', 'meta.function.foo.css']
    >>> scope_name(scopes, prefix='meta.function')
    'foo'
    >>> scopes = ['source.css', 'meta.descriptor.color-profile.bar.css']
    >>> scope_name(scopes, prefix='meta.descriptor.color-profile')
    'bar'
    >>> scopes = ['source.css', 'meta.function.baz.css']
    >>> scope_name(scopes, prefix='meta.descriptor.color-profile')
    ''
    """
    if prefix[-1] != ".":
        prefix += "."

    name_index = 0
    for scope in reversed(scopes):
        if scope.startswith(prefix):
            # 'meta.function.foo.css' -> 'foo.css'
            scope = scope[len(prefix):]

            # ['foo', 'css'] -> 'foo'
            return scope.split(".")[name_index]

    return ""
