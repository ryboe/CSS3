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
        t.string,
        t.url,
    ] + t.angle + t.color + t.length + t.number + t.percentage + t.time,
    "blenda": [("hsl",), ("hwb",), ("rgb",)] + t.color + t.percentage,
    "blur": t.length,
    "calc": t.angle + t.frequency + t.length + t.number + t.percentage + t.time,
    "child": t.integer,
    "cielab": t.number,
    "cielchab": t.number,
    "color": t.angle + t.color + t.number,
    "color-adjuster-rgb": [t.hex_color] + t.number + t.percentage,
    "conic-gradient": [
        ("at",),
        ("from",),
    ] + t.color_stop + t.position,
    "content": [
        ("after",),
        ("before",),
        ("first-letter",),
        ("marker",),
        ("text",),
    ],
    "counter": [("none",), t.identifier, t.symbols] + t.image,
    "counters": [("none",), t.identifier, t.string, t.symbols] + t.image,
    "cross-fade": t.color + t.image + t.percentage,
    "cubic-bezier": t.number,
    "device-cmyk": t.color + t.number + t.percentage,
    "device-gray": t.number,
    "device-nchannel": t.number,
    "device-rgb": t.number,
    "dir": [("ltr",), ("rtl",)],
    "drop": [("active",), ("invalid",), ("valid",)],
    "drop-shadow": t.color + t.length,
    "element": [
        ("first",),
        ("first-except",),
        ("last",),
        ("start",),
        t.identifier,
    ],
    "ellipse-circle": [("at",)] + t.shape_radius + t.position,
    "filter": t.number + t.percentage,
    "fit-content": t.length + t.percentage,
    "format": [t.string],
    "gray": t.number + t.percentage,
    # "has": [],           # TODO: has takes a selector list as an arg. should it have completions?
    # "host": [],          # TODO: host takes a selector list as an arg. should it have completions?
    # "host-context": [],  # TODO: host-context takes a selector list as an arg. should it have completions?
    "hsla": t.angle + t.number + t.percentage,
    "hue-rotate": t.angle,
    "hwb": t.angle + t.number + t.percentage,
    "icc-color": [t.identifier] + t.icc_color + t.number,
    "image": [t.string] + t.image + t.color,
    "image-set": [t.string] + t.image + t.resolution,
    "inset": [("round",)] + t.shape_arg,
    "leader": [("dotted",), ("solid",), ("space",), t.string],
    "linear-gradient": [("to",)] + t.angle + t.color_stop + t.side_or_corner,
    "local": [t.identifier, t.string],
    # "matches": [],  # TODO: matches takes a selector list as an arg. should it have completions?
    "matrix": t.number,
    "minmax": [("auto",), ("min-content",), ("max-content",)] + t.flex + t.length + t.percentage,
    # "not": [],      # TODO: not takes a selector list as an arg. should it have completions?
    "nth-child": [("of",)],
    "nth-last-child": [("of",)],
    "path": [t.string] + t.fill_rule,
    "perspective": t.length,
    "polygon": t.fill_rule + t.shape_arg,
    "radial-gradient": [
        ("at",),
        ("circle",),
        ("ellipse",),
    ] + t.color_stop + t.position + t.size,
    "red-green-blue-alpha-a": t.number + t.percentage,
    "repeat": [
        ("auto-fill",),
        ("auto-fit",),
        t.identifier,
    ] + t.integer + t.track_size,
    "rgba": t.rgb_component,
    "rotate": t.angle,
    "running": [t.identifier],
    # "select": [],   # TODO: select takes a selector list as an arg. should it have completions?
    "scale": t.number,
    "skew": t.angle,
    # "slotted": [],  # TODO: slotted takes a selector list as an arg. should it have completions?
    "snap-block": [("end",), ("near",), ("start",)] + t.length,
    "snap-inline": [("left",), ("near",), ("right",)] + t.length,
    "steps": [("start",), ("end",)] + t.integer,
    "string": [("first",), ("first-except",), ("last",), ("start",), t.identifier],
    "swash-styleset-stylistic-ornaments-character-variant-annotation": [t.identifier] + t.integer,
    "symbols": [
        ("alphabetic",),
        ("cyclic",),
        ("fixed",),
        ("numeric",),
        ("symbolic",),
        t.string,
    ] + t.image,
    "target-counters": [t.string, t.url] + t.counter_style,
    "target-text": [
        ("after",),
        ("before",),
        ("content",),
        ("first-letter",),
        t.string,
        t.url,
    ],
    "tint-shade-contrast": t.percentage,
    "translate": t.length + t.percentage,
    "translate-z": t.length,
    "whiteness-saturation-lightness-hue-blackness": t.percentage,
}

# Some functions take identifiers, or other symbols that are likely to be in
# the local symbol list, as arguments. Their completions should be returned
# without inhibiting word completions.
allow_word_completions = frozenset((
    "additive-symbols",
    "attr",
    "attr-pseudo-element",
    "counter",
    "counters",
    "element",
    "fallback",
    "font-family",
    "host",
    "host-context",
    "icc-color",
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
