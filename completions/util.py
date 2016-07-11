
def get_current_scopes(view, location):
    return view.scope_name(location).split()


def get_name_from_scopes_with_prefix(scopes, prefix):
    """
    Scans a list of scopes and returns the name of the function or descriptor
    with the given prefix. If there are multiple matches, only the name from the
    highest-precedence (rightmost) scope will be returned. If there are no
    scopes with the given prefix, an empty string is returned.

    Args:
        scopes (list: str): e.g. ['source.css', 'foo.bar.baz.css']
        prefix (str): e.g. 'foo.bar'

    Returns:
        The

    >>> scopes = ['source.css', 'meta.function.foo.css']
    >>> get_name(scopes, prefix='meta.function')
    'foo'
    >>> scopes = ['source.css', 'meta.descriptor.color-profile.bar.css']
    >>> get_name(scopes, prefix='meta.descriptor.color-profile')
    'bar'
    >>> scopes = ['source.css', 'meta.function.baz.css']
    >>> get_name(scopes, prefix='meta.descriptor.color-profile')
    ''
    """
    name_index = -2
    for scope in reversed(scopes):
        if scope.startswith(prefix):
            # ['meta', 'function', 'foo', 'css'] -> 'foo'
            return scope.split(".")[name_index]

    return ""
