# Contributing

## Create an issue

Your pull request is more likely to be accepted if you open an issue. This gives
me a chance to provide early feedback so you don't waste your time. For example,
you might think it's weird that some property isn't highlighted, when in fact
it's a [known bad property](https://gist.github.com/y0ssar1an/bb95223148e486acbe7a).

Check the list of open issues to see if your issue already exists.

## Make your changes

Branch off `dev`, not `master`. Master is the release branch that gets scanned
every hour by the Package Control bot. To keep the package size small,
development-specific files (e.g. tests, helper scripts) are kept out of the
`master` branch.

If you want to make a change to the syntax highlighter, **do not** edit
`CSS3.tmLanguage` directly. Instead, edit `CSS3.YAML-tmLanguage` and compile
it into `CSS3.tmLanguage` with [PackageDev](https://packagecontrol.io/packages/PackageDev).

![PackageDev Convert Command](https://github.com/y0ssar1an/CSS3/raw/dev/screenshots/packagedev_convert.png)

When you're editing `CSS3.YAML-tmLanguage`, make sure the syntax is set to
`Sublime Text Syntax Def (YAML)`. It will give you good completions and catch
mistakes.

## Submit your PR

Thanks for helping out! It's a lot of work to keep CSS3 up to date with the
latest browser/spec changes. Stuff gets by me. Any update is appreciated, no
matter how small.
