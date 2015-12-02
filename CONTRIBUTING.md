# Contributing

Thank you for your interest in making it easier to write good CSS3! Here's how
you can help!

## Open an issue

If you think something's missing, make sure you're not asking for something on
[this list of bad CSS
properties](https://gist.github.com/y0ssar1an/bb95223148e486acbe7a#file-
bad_css). If it's not on that list, open an issue and we'll investigate. We'll
be monitoring the specs as they're updated on [the W3C
feed](http://www.w3.org/Style/CSS/current-work.en.html), but we still need your
help. Let's keep bad code out of the Web!

## Submit a pull request

It would be awesome to have more people dive into these regular expressions with
us! You should probably open an issue first before writing any code though.

## Set up a dev environment

1. Fork CSS3

Create a fork of CSS3 on GitHub.

2. Check Sublime Text's build number

To work with the new Sublime Syntax, you'll need to have Sublime Text 3 Build
3084 or greater. To check, click on Help > About Sublime Text, or Sublime Text >
About Sublime Text on OS X, to see the build number you currently have
installed. In addition, make sure [Package Control]((https://packagecontrol.io/installation))
is installed.

3. Uninstall CSS3

If you have CSS3 installed, uninstall it to prevent conflicts.

If you installed it through Package Control, then press `ctrl+shift+p`, or
`cmd+shift+p` on OS X, and then type "Package Control: Remove Package". Finally,
select CSS3 from the menu.

If you manually cloned it to your Packages directory, then delete the folder.

4. Disable built-in CSS Package

Disable the built-in CSS package to prevent any conflicts with CSS3.

Press `ctrl+shift+p`, or `cmd+shift+p` on OS X. Type "Package Control: Disable
Package", and press enter. Finally, select CSS to disable it.

5. Download source

```
cd "$HOME/Library/Application Support/Sublime Text 3/Packages"
git clone git@github.com:<your_username>/CSS3.git
```

6. Install AAAPackageDev

You’ll want this for opening the `CSS3.YAML-tmLanguage` file. It gives you a
highlighting option.

Press `ctrl+shift+p`, or `cmd+shift+p` on OS X, type "Package Control: Install
Package", and press enter. Next, type "AAAPackageDev" and press enter to install
it.

7. Restart Sublime Text

It's probably a good idea to restart now.

8. Sanity check

Press `` ctrl+` `` to open the console. Make sure there aren't any errors there.

Open any file ending with `.css`. Make sure Sublime Text says "CSS3" in the
bottom right-hand corner of the editor. You can also check View > Syntax and
make sure you see "✓ CSS3".

## Tips

* The `match` field uses [Oniguruma regular expressions](https://gist.github.com/alphabetum/4228696).
* If CSS files are opening as Plain Text, make sure your Sublime Text build is
3084 or greater.
* You might want to set `ignore_vcs_packages: true` in Package Settings >
Package Control > Settings - User, if Package Control reports git errors.

## Reading list

* [Sublime Syntax Spec](http://www.sublimetext.com/docs/3/syntax.html)
* [Sublime Syntax Examples](https://github.com/sublimehq/Packages)
* [SublimeLPC](https://github.com/abathur/SublimeLPC) (See syntax and test files)
* [CSS3 Spec](http://www.w3.org/Style/CSS/current-work.en.html)
