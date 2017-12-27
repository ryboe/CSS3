
at_page = [
    (":blank", ":blank "),
    (":first", ":first "),
    (":left", ":left "),
    (":recto", ":recto "),
    (":right", ":right "),
    (":verso", ":verso "),
]

html_tags = [
    ("a",),
    ("abbr",),
    ("address",),
    ("area",),
    ("article",),
    ("aside",),
    ("audio",),
    ("b",),
    ("base",),
    ("bdi",),
    ("bdo",),
    ("blockquote",),
    ("body",),
    ("br",),
    ("button",),
    ("canvas",),
    ("caption",),
    ("cite",),
    ("code",),
    ("col",),
    ("colgroup",),
    ("data",),
    ("datalist",),
    ("dd",),
    ("del",),
    ("details",),
    ("dfn",),
    ("dialog",),
    ("div",),
    ("dl",),
    ("dt",),
    ("em",),
    ("embed",),
    ("fieldset",),
    ("figcaption",),
    ("figure",),
    ("footer",),
    ("form",),
    ("h1",),
    ("h2",),
    ("h3",),
    ("h4",),
    ("h5",),
    ("h6",),
    ("head",),
    ("header",),
    ("hr",),
    ("html",),
    ("i",),
    ("iframe",),
    ("img",),
    ("input",),
    ("ins",),
    ("kbd",),
    ("label",),
    ("legend",),
    ("li",),
    ("link",),
    ("main",),
    ("map",),
    ("mark",),
    ("meta",),
    ("meter",),
    ("nav",),
    ("noscript",),
    ("object",),
    ("ol",),
    ("optgroup",),
    ("option",),
    ("output",),
    ("p",),
    ("param",),
    ("picture",),
    ("pre",),
    ("progress",),
    ("q",),
    ("rb",),
    ("rp",),
    ("rt",),
    ("rtc",),
    ("ruby",),
    ("s",),
    ("samp",),
    ("script",),
    ("section",),
    ("select",),
    ("small",),
    ("source",),
    ("span",),
    ("strong",),
    ("style",),
    ("sub",),
    ("summary",),
    ("sup",),
    ("table",),
    ("tbody",),
    ("td",),
    ("template",),
    ("textarea",),
    ("tfoot",),
    ("th",),
    ("thead",),
    ("time",),
    ("title",),
    ("tr",),
    ("track",),
    ("u",),
    ("ul",),
    ("var",),
    ("video",),
    ("wbr",),
]

keyframes = [
    ("from", "from {\n\t${1}\n}"),
    ("to", "to {\n\t${1}\n}"),
    ("<percentage>", "${1:0}% {\n\t${2}\n}"),
]

pseudo_classes = [
    ("active",),
    ("any-link",),
    ("blank",),
    ("checked",),
    ("current",),
    ("default",),
    ("dir()", "dir(${1})"),
    ("disabled",),
    ("drop",),
    ("drop()", "drop(${1})"),
    ("empty",),
    ("enabled",),
    ("first-child",),
    ("first-of-type",),
    ("focus",),
    ("focus-within",),
    ("future",),
    ("has()", "has(${1})"),
    ("host",),
    ("host()", "host(${1})"),
    ("host-context()", "host-context(${1})"),
    ("hover",),
    ("in-range",),
    ("indeterminate",),
    ("invalid",),
    ("lang()", "lang(${1})"),
    ("last-child",),
    ("last-of-type",),
    ("link",),
    ("matches()", "matches(${1})"),
    ("not()", "not(${1})"),
    ("nth-child()", "nth-child(${1})"),
    ("nth-column()", "nth-column(${1})"),
    ("nth-last-child()", "nth-last-child(${1})"),
    ("nth-last-column()", "nth-last-column(${1})"),
    ("nth-last-of-type()", "nth-last-of-type(${1})"),
    ("nth-of-type()", "nth-of-type(${1})"),
    ("only-child",),
    ("only-of-type",),
    ("optional",),
    ("out-of-range",),
    ("past",),
    ("paused",),
    ("placeholder-shown",),
    ("playing",),
    ("read-only",),
    ("read-write",),
    ("required",),
    ("root",),
    ("scope",),
    ("scope-context()", "scope-context(${1})"),
    ("target",),
    ("user-invalid",),
    ("valid",),
    ("visited",),
]

pseudo_elements = [
    ("after",),
    ("attr()", "attr(${1})"),
    ("before",),
    ("content",),
    ("first-letter",),
    ("first-line",),
    ("grammar-error",),
    ("inactive-selection",),
    ("input-placeholder",),
    ("marker",),
    ("placeholder",),
    ("region",),
    ("selection",),
    ("shadow",),
    ("slotted()", "slotted(${1})"),
    ("spelling-error",),
]
