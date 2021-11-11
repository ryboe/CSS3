CSS3
====

![GitHub Actions Status Badge](https://github.com/ryboe/CSS3/actions/workflows/test-syntax.yaml/badge.svg?branch=master)

The most complete CSS and PostCSS-cssnext support for Sublime Text.

## Features

* __Absurdly Complete__: I mined the entire set of draft specs and supported
  everything. Some of this stuff won't be implemented in browsers for *years*.
  If it's in the spec, it's supported.
* __Future Proof__: [PostCSS-cssnext](http://cssnext.io) is fully supported. If
  you use [cssnext](http://cssnext.io), you can use futuristic CSS like...
  - nesting
  - custom selectors
  - custom properties
  - custom media queries
  - [CSS Modules](https://github.com/css-modules/css-modules)
  - lots more
* __Productive__: Offers a full set of completions for properties, descriptors,
  @-rules, functions, and selectors. The completions are highly specific to what
  you're writing.
* __Modern__: Bad, old CSS is flagged. Unnecessarily prefixed properties aren't
  highlighted. Catches lots of mistakes. Encourages best practices.
* __Faithful__: Follows the W3C specs extremely closely.
* __Fast__: CSS3 has been designed for Sublime's new custom regex engine,
  which is crazy fast. The syntax highlighting typically takes less than 100ms,
  even for very large CSS files.


## Before & After

![before and after](http://i.imgur.com/H4yUEC6.jpg)

## Installation

1. [Install Package Control](https://sublime.wbond.net/installation)
2. Install CSS3

    | Platform      | Install Command                                                      |
    | --------------| -------------------------------------------------------------------- |
    | Mac           | `cmd+shift+p`&nbsp;&nbsp; → Package Control: Install Package → CSS3  |
    | Linux/Windows | `ctrl+shift+p` → Package Control: Install Package → CSS3             |

3. (Required) Disable the default CSS package

    | Platform      | Disable Command                                                      |
    | ------------- | -------------------------------------------------------------------- |
    | Mac           | `cmd+shift+p`&nbsp;&nbsp; → Package Control: Disable Package → CSS   |
    | Linux/Windows | `ctrl+shift+p` → Package Control: Disable Package → CSS              |

    ![disabling the default CSS package](http://i.imgur.com/JUTJPZJ.gif)

    Make sure you don't have any open files set to the default CSS syntax (bottom-right)
    or you may get an error message.

4. (Strongly Recommended) Enable completions inside completions

    By default, Sublime will not offer completions inside completions. In other
    words, the completions menu is suppressed when you're tabbing through a
    snippet. This prevents a lot of CSS3 completions from appearing. Add these
    keys to your User Settings to fix this:

    ```json
    "auto_complete_commit_on_tab": true,
    "auto_complete_with_fields": true,
    ```

5. (Recommended) Hide CSS completions from Emmet

    If you have Emmet installed, its completions will drown out the
    carefully researched, standards-based completions offered by this package.
    You can hide Emmet completions for CSS only by adding this line to
    your Emmet package settings.
    ```json
    "abbreviation_preview": "markup"
    ```

6. (Recommended) Set CSS3 as the default language for `.css` files
    * Open a `.css` file.
    * View → Syntax → Open all with current extension as... → CSS3

    ![setting CSS3 as default](http://i.imgur.com/0xRQRFp.gif)

## Best Practices

* [Always use quotes inside `url()`](https://drafts.csswg.org/css-values/#urls).
  Unquoted URLs are intentionally not highlighted.

## Help Me Out!

If you think something's missing, make sure you're not asking for something
on [this list of bad CSS properties](https://gist.github.com/ryboe/bb95223148e486acbe7a#file-bad_css).
If it's not on that list, open an issue and I'll investigate. *Definitely* check
out the [CONTRIBUTING](https://github.com/ryboe/CSS3/blob/master/CONTRIBUTING.md)
guidelines before submitting your PR. It could save you a lot of time. I'll be
monitoring the specs as they're updated on [this W3C feed](https://www.w3.org/Style/CSS/current-work.en.html),
but I still need your help. Let's keep bad code out of the Web!
