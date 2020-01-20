def get_scopes(view, location):
    """Return the scopes at the given location.

    >>> get_scopes(123)
    ['source.css', 'foo.bar.baz.css']
    """
    return view.scope_name(location).split()


def get_scope_that_starts_with(scopes, starts_with):
    for scope in reversed(scopes):
        if scope.startswith(starts_with):
            return scope

    raise ValueError(
        "No scope starts with {} in scope list:\n\t{}".format(starts_with, scopes)
    )
