# Contributing

## Create an issue

Your pull request is more likely to be accepted if you open an issue first. This
gives me a chance to provide early feedback so you don't waste your time. For
example, you might think it's weird that some property isn't highlighted, when
it's actually a [known bad property](https://gist.github.com/y0ssar1an/bb95223148e486acbe7a).

Check the list of open issues to see if your issue already exists.

## Make your changes

Clone the repo into your `Packages/` folder so you can make changes and see the
effect immediately. Sometimes you need to restart first.

## Add a missing property

1) **Add the property to the syntax highlighter:** Copy the provided snippet
from `tool/newprop_css3.sublime-snippet` to your Packages/User folder. Now open
the CSS3.sublime-syntax file, navigate to the correct place in the text (the
property-* contexts are in alphabetical order), and type `newprop`. The snippet
will ensure that you don't mistype anything, and don't forget to include the
appropriate `meta_content_scope`. `meta_content_scope` should follow the format
`meta.property-value.my-awesome-property.css`. You must follow the format
exactly, otherwise completions will not work.

If the property has keyword values, your `match` regex should look like this:

```
'\b(?:foo|baz|bar){{b}}'
```

To prevent highlighting mistakes, you want your regexes to be as specific as
possible. The `\b` (leading) and `{{b}}` (trailing) word boundaries prevent the
`foo` text from inadvertently matching something like `myfoo`, `maxfoo`, or
`foo-max`. If you want the full explanation for why these are necessary, open
an issue with the question label. The short answer is that without these
boundaries, you might partially highlight invalid user text.

Do not use look-behind expressions in your regexes. Look-behind expressions look
like this:

```
(?<=subexp)  # positive look-behind
(?<!subexp)  # negative look-behind
```

If there is even a single look-behind regex in `CSS3.sublime-syntax`, Sublime
will fallback to its old regex engine and performance will drop like a rock.

The next thing to understand is the `(?:)` pattern. This is an optimization that
prevents the `foo|baz|bar` text from being "captured". Capture groups are useful
for applying scopes to part of a match. When you're matching property value
keywords (e.g. `auto`, `none`, `yellow`, `dashed`), you almost never want
to do that. We can save a little performance by using a non-capturing group.

Finally, note that `foo|baz|bar` are in reverse-alphabetical order. This is an
easy way to guarantee that longer potential matches are tried first. The short
explanation is that this prevents another class of mismatches.

2) **Add completions for the new property:** Open `completions/properties.py`.
Add this line to the `names` list:

```py
names = [
    ("my-awesome-property", "my-awesome-property: ${1};"),
]
```

Each completion is a `(<label>, <snippet>)` tuple. The `<label>` is the text
that shows up in the completions menu when you're typing. The `<snippet>` is the
text that will be inserted. The cursor will jump to the `${1}` position.
Pressing TAB again will jump over the semicolon to the end of the snippet. If
`<snippet>` is omitted (e.g. `("my-awesome-property",)`), the inserted snippet
will be the same text as the label.

Now add the property values completions to the `name_to_completions` dictionary.

```py
name_to_completions = {
    "my-awesome-property": [("some-value",), t.string] + t.color + t.integer,
}
```

Aside from the keyword values (`"some-value"`), you probably don't need to make
any new completions yourself. There's a huge library available in
`completions/types.py`. Make sure to understand which types are tuples
(`t.string`), and which are lists of tuples (`t.color`, `t.integer`).

You do not need to add separate completions for each vendor prefix to the
`name_to_completions` dictionary. Notice that there are no keys in that
dictionary with vendor prefixes.

You will need to restart for the changes to take effect.

## Add a new function

Read the instructions for adding a new property for context. This time you will
be using `tool/newfunc_css3.sublime-snippet`. You will add the function
completion to the top of `completions/types.py`:

```py
my_awesome_func = ("my-awesome-func()", "my-awesome-func(${1})")
```

For the function values (when the cursor is between the parentheses), you will
add those to the `func_name_to_completions` dictionary in
`completions/functions.py`. Again, you do not need separate keys for each
vendor prefix.

## Don't worry if you don't get all this!

If you get stuck, just open a work-in-progress PR and apply the blue **wip**
label to it. I'll review it and get you unstuck. Even a **wip** PR is greatly
appreciated.

## Submit your PR

Thanks for helping out! It's a lot of work to keep CSS3 up to date with the
latest browser/spec changes. Stuff gets by me. Any update is appreciated, no
matter how small.
