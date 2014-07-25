CSS3
====

The most complete CSS support for Sublime Text 3.

## Features

* __Absurdly Complete__: I basically mined the entire set of draft CSS specs
  and supported everything. Some of this stuff won't be implemented in browsers
  for *years*. With a few exceptions, if it's in the spec, it's in here.
* __Productive__: A full set of completions is offered for every property,
  including many prefixed properties.
* __Modern__: Bad, old CSS is flagged. Unnecessarily prefixed properties aren't
  highlighted. Catches lots of mistakes.
* __Faithful__: Follows the spec extremely closely, with minor deviations that
  encourage a few best practices from the Google HTML/CSS style guide.


## Installation

This package replaces my previous CSS3_Syntax plugin. It's a billion times better :)

1. [Install Package Control](https://sublime.wbond.net/installation)
2. (Recommended) Disable the default CSS package

    * __Mac__: `cmd+shift+p` → Package Control: Disable Package → CSS
    * __Linux/Windows__: `ctrl+shift+p` → Package Control: Disable Package → CSS

    ![disabling the default CSS package](https://github.com/y0ssar1an/CSS3/raw/master/screenshots/disable_default.gif)

    *Warning: may break other CSS plugins*
3. Install CSS3

    * __Mac__:           `cmd+shift+p` → Package Control: Install Package → CSS3
    * __Linux/Windows__: `ctrl+shift+p` → Package Control: Install Package → CSS3
4. (Optional) Set CSS3 as the default language for .css files.

    * Open a .css file.
    * View → Syntax → Open all with current extension as... → CSS3

    ![setting CSS3 as default](https://github.com/y0ssar1an/CSS3/raw/master/screenshots/set_default.gif)

    *Warning: may break other CSS plugins*

## Best Practices

* End every property with a semicolon.
* Don't put a space between the property name and the colon (:)

    `width : 100px;  /* BAD */`

    `width: 100px;   /* GOOD */`

* Put a space between the selector and the opening curly brace.

## Known Issues

1. __Within nested code blocks, like in a @media query, if the first
selector starts with a letter, it will not be highlighted.__
This is an annoying limitation of the Sublime Text syntax highlighting
system. It can't recursively match curly braces across multiple lines. In
this case, the first nested selector is mistaken for a property, which
doesn't match. I went through three or four rewrites trying to cope with
this problem before I arrived at the current design, which is the least
fragile and most predictable. Other CSS highlighters, including my previous
CSS3_Syntax and the Default CSS bundle, all suffer from the same problem,
but are way easier to break. It's hardly a showstopper, but if this bugs
you like it bugs me, two simple workarounds are shown below.

![nested selector bug and two workarounds](https://github.com/y0ssar1an/CSS3/raw/master/screenshots/nested_selector_bug.png)

## Help Me Out!

* There are no authoritative lists of browser prefixed CSS extensions.
* MDN is riddled with errors. I fixed several. It's still better than
W3Schools.
* The specs contain errors.
* The specs are changing all the time!

If you think something is missing, like a prefixed property *that's on the
standards track*, open an issue and I'll investigate. I will monitor the specs
as they are updated on [the W3C feed](http://www.w3.org/Style/CSS/current-work.en.html),
but I still need your help to make the best CSS package for Sublime Text even
better!
