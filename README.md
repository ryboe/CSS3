CSS3
====

The most complete CSS support for Sublime Text 3.

## Features

* __Absurdly Complete__: I basically mined the entire set of draft specs
  and supported everything. Some of this stuff won't be implemented in browsers
  for *years*. With very few exceptions, if it's in the spec, it's supported.
* __Productive__: Offers a full set of completions for every property. The
  completions are highly specific to what you're writing.
* __Modern__: Bad, old CSS is flagged. Unnecessarily prefixed properties aren't
  highlighted. Catches lots of mistakes. Encourages best practices.
* __Faithful__: Follows the W3C specs extremely closely.

## Before & After

![before and after](http://i.imgur.com/JUTJPZJ.gif)

## Installation

1. [Install Package Control](https://sublime.wbond.net/installation)
2. Install CSS3

    | Platform | Install Command                                                      |
    | -------- | -------------------------------------------------------------------- |
    | Mac      | `cmd+shift+p`&nbsp;&nbsp; → Package Control: Install Package → CSS3  |
    | Linux    | `ctrl+shift+p` → Package Control: Install Package → CSS3             |
    | Windows  | `ctrl+shift+p` → Package Control: Install Package → CSS3             |

3. (Recommended) Disable the default CSS package

    | Platform | Disable Command                                                      |
    | -------- | -------------------------------------------------------------------- |
    | Mac      | `cmd+shift+p`&nbsp;&nbsp; → Package Control: Disable Package → CSS   |
    | Linux    | `ctrl+shift+p` → Package Control: Disable Package → CSS              |
    | Windows  | `ctrl+shift+p` → Package Control: Disable Package → CSS              |

    ![disabling the default CSS package](http://i.imgur.com/PVoavnb.gif)

    Make sure you don't have any open files set to the default CSS syntax (bottom-right)
    or you may get an error message.

    *Warning: may break other CSS plugins*

4. (Recommended) Disable CSS completions in Emmet

    If you have Emmet installed, its completions will drown out the
    carefully researched, standards-based completions offered by this package.
    You can disable Emmet completions by adding these two lines to your Emmet
    Package settings.

    ```
    "show_css_completions": false,
    "disable_tab_abbreviations_for_scopes": "source.css"
    ```

5. (Recommended) Set CSS3 as the default language for `.css` files
    * Open a `.css` file.
    * View → Syntax → Open all with current extension as... → CSS3

    ![setting CSS3 as default](https://github.com/y0ssar1an/CSS3/raw/develop/screenshots/set_default.gif)

    *Warning: may break other CSS plugins*

## Best Practices

* [Always use quotes inside `url()`](https://drafts.csswg.org/css-values/#urls).
  Unquoted URLs are intentionally not highlighted.

## Help Me Out!

If you think something's missing, make sure you're not asking for something
on [this list of bad CSS properties](https://gist.github.com/y0ssar1an/bb95223148e486acbe7a#file-bad_css).
If it's not on that list, open an issue and I'll investigate. I'll be monitoring
the specs as they're updated on [the W3C feed](https://www.w3.org/Style/CSS/current-work.en.html),
but I still need your help. Let's keep bad code out of the Web!
