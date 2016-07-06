from CSS3.completions import types as t

# This dict maps function names to their completions. It includes pseudo-class
# and pseudo-element functions like :nth-child() and ::attr().
func_name_to_completions = {
    "attr": [
        ("angle",),  # A tuple with only one string means the label is the same
        ("ch",),     # as the completion, i.e. ("foo",) is equivalent to
        ("cm",),     # ("foo", "foo").
        ("color",),
        ("dB",),
        ("deg",),
        ("em",),
        ("ex",),
        ("frequency",),
        ("grad",),
        ("Hz",),
        ("in",),
        ("integer",),
        ("kHz",),
        ("length",),
        ("mm",),
        ("ms",),
        ("number",),
        ("pc",),
        ("pt",),
        ("px",),
        ("rad",),
        ("rem",),
        ("string",),
        ("time",),
        ("turn",),
        ("url",),
        ("vh",),
        ("vmax",),
        ("vmin",),
        ("vw",),
    ],
    "blenda": [("hsl",), ("hwb",), ("rgb",)] + t.color,
    "color": t.color,
    "conic-gradient": [("at",), ("from",)] + t.position,
    "content": [
        ("after",),
        ("before",),
        ("first-letter",),
        ("marker",),
        ("text",),
    ],
    "counter": [("none",), t.symbols] + t.image,
    "counters": [("none",), t.symbols] + t.image,
    "cross-fade": t.color + t.image,
    "device-cmyk": t.color,
    "dir": [("ltr",), ("rtl",)],
    "drop": [("active",), ("invalid",), ("valid",)],
    "drop-shadow": t.color,
    "element": [("first",), ("first-except",), ("last",), ("start",)],
    "ellipse-circle": [("at",), ("closest-side",), ("farthest-side",)] + t.position,
    # "has": [],           # TODO: has takes a selector list as an arg. should it have completions?
    # "host": [],          # TODO: host takes a selector list as an arg. should it have completions?
    # "host-context": [],  # TODO: host-context takes a selector list as an arg. should it have completions?
    "icc-color": t.icc_color,
    "image": t.image + t.color,
    "image-set": t.image,
    "inset": [("round",)],
    "leader": [("dotted",), ("solid",), ("space",)],
    "linear-gradient": [
        ("bottom",),
        ("left",),
        ("right",),
        ("to",),
        ("top",),
    ] + t.color,
    # "matches": [],  # TODO: matches takes a selector list as an arg. should it have completions?
    "minmax": [("auto",), ("min-content",), ("max-content",)],
    # "not": [],      # TODO: not takes a selector list as an arg. should it have completions?
    "nth-child": [("of",)],
    "nth-last-child": [("of",)],
    "path": [("evenodd",), ("nonzero",)],
    "polygon": [("evenodd",), ("nonzero",)],
    "radial-gradient": [
        ("at",),
        ("circle",),
        ("closest-corner",),
        ("closest-side",),
        ("ellipse",),
        ("farthest-corner",),
        ("farthest-side",),
    ] + t.color + t.position,
    "repeat": [
        ("auto",),
        ("auto-fill",),
        ("auto-fit",),
        ("max-content",),
        ("min-content",),
        t.minmax,
        t.fit_content,
    ],
    # "select": [],   # TODO: select takes a selector list as an arg. should it have completions?
    # "slotted": [],  # TODO: slotted takes a selector list as an arg. should it have completions?
    "snap-block": [("end",), ("near",), ("start",)],
    "snap-inline": [("left",), ("near",), ("right",)],
    "steps": [("start",), ("end",)],
    "string": [("first",), ("first-except",), ("last",), ("start",)],
    "symbols": [
        ("alphabetic",),
        ("cyclic",),
        ("fixed",),
        ("numeric",),
        ("symbolic",)
    ] + t.image,
    "target-counters": [t.symbols, t.url],
    "target-text": [
        ("after",),
        ("before",),
        ("content",),
        ("first-letter",),
        t.url,
    ],
}

# Some functions take identifiers, or other symbols that are likely to be in
# the local symbol list, as arguments. Their completions should be returned
# without inhibiting word completions.
allow_word_completions = frozenset((
    "::attr",
    "additive-symbols",
    "attr",
    "counter",
    "counters",
    "element",
    "fallback",
    "font-family",
    "host",
    "host-context",
    "local",
    "name",
    "negative",
    "pad",
    "prefix",
    "repeat",
    "running",
    "select",
    "speak-as",
    "string",
    "suffix",
    "swash-styleset-stylistic-ornaments-character-variant-annotation",
    "symbols",
    "system",
    "target-counters",
    "var",
))


def sort_and_uniq_completions():
    for name in func_name_to_completions:
        func_name_to_completions[name] = list(set(func_name_to_completions[name]))
        func_name_to_completions[name].sort()


sort_and_uniq_completions()
