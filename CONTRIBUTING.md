# Contributing

Thank you for your interest in making it easier to write good CSS3! Here's how
you can help!

## Open an issue

If you think something's missing, make sure you're not asking for something on
[this list of bad CSS
properties](https://gist.github.com/y0ssar1an/bb95223148e486acbe7a#file-
bad_css). If it's not on that list, open an issue and I'll investigate. I'll be
monitoring the specs as they're updated on [the W3C
feed](http://www.w3.org/Style/CSS/current-work.en.html), but I still need your
help. Let's keep bad code out of the Web!

## Submit a pull request

It would be awesome to have more people dive into these regular expressions with
me! You should probably open an issue first before writing any code though.

## Setup a dev environment

If you're ready to dive into the code, then this is how. The following
instructions are for hackers only.

### Fork CSS3

Create a fork of CSS3 on GitHub.

### Install Sublime Text 3dev

If your version of Sublime Text 3 is build 3083 or lower, then you'll need to
install Sublime Text 3dev, which is a build ahead of regular Sublime Text 3.
Click [here](http://www.sublimetext.com/3dev) to download it. You need to be a
registered user to install it. Make sure your version of Sublime Text 3 is build
3084 or greater. Otherwise, the new syntax definitions will not work.

You should probably uninstall the old version before installing the new version
to prevent possible conflicts. If you want to keep your User preferences, make
sure you save them somewhere before uninstalling the old version of Sublime Text
3 so that you can reimport them after installing the new version. In addition,
make sure [Package Control]((https://packagecontrol.io/installation)) is
installed in the new version of Sublime Text 3.

### Uninstall CSS3

If you have CSS3 installed, you should probably uninstall it to prevent any
conflicts.

If you installed it through Package Control, then press `cmd+shift+p` and then
type "Package Control: Remove Package". Finally, select CSS3 from the menu.

If you manually cloned it to your Packages directory, then delete the folder.

### Disable built-in CSS Package

You'll probably want to disable the built-in CSS package to prevent any
conflicts with CSS3.

Press `cmd+shift+p`, type "Package Control: Disable Package", and press enter.
Finally, select CSS to disable it.

### Download source

```
cd "$HOME/Library/Application Support/Sublime Text 3/Packages"
git clone git@github.com:<your_username>/CSS3.git
```

### Install AAAPackageDev

You’ll want this for opening the `CSS3.YAML-tmLanguage` file. It gives you a
highlighting option.

Press `cmd+shift+p`, type "Package Control: Install Package", and press enter.
Next, type "AAAPackageDev" and press enter to install that package.

### Restart Sublime Text

Probably a good idea to restart now.

### Sanity check

Press `` ctrl+` `` to open the console. Make sure there aren't any errors there.

Open any file ending with `.css`. Make sure Sublime Text says "CSS3" in the
bottom right-hand corner of the editor. You can also check View > Syntax and
make sure you see "✓ CSS3".

## Tips

* `match` field uses Ruby regex syntax.
* If CSS files are opening as Plain Text, make sure your Sublime Text build is
3084 or greater.

## Reading list

* [Sublime Syntax Spec](http://www.sublimetext.com/docs/3/syntax.html)
* [Sublime Syntax Examples](https://github.com/sublimehq/Packages)
* [SublimeLPC](https://github.com/abathur/SublimeLPC) (Syntax and tests)
* [CSS3 Spec](http://www.w3.org/Style/CSS/current-work.en.html)
