# Contributing

## Create an issue

Your pull request is more likely to be accepted if you open an issue

## Make your changes

Branch off the `dev` branch, not `master`. Master is the release branch that
gets scanned every hour by the Package Control bot. To keep the package size
small, development-specific files (e.g. tests, helper scripts) are kept out of
the master branch.

If you want to make a change to the syntax highlighter, **do not** edit
`CSS3.tmLanguage` directly. Instead, edit `CSS3.YAML-tmLanguage` and compile
it into `CSS3.tmLanguage` with [PackageDev](https://packagecontrol.io/packages/PackageDev).

If you're thinking about adding a property, make sure it's not on [this list of
bad CSS properties](https://gist.github.com/y0ssar1an/bb95223148e486acbe7a).

## Submit your PR

First of all, thanks for helping out! It's a lot of work to keep CSS3 up to date
with the latest browser/spec changes. Stuff gets by me. Any update is
appreciated, no matter how small.

Please reference the Issue # in your PR notes.
