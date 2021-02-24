from CSS3.completions import types as t
import sublime

# This dict maps function names to their completions. It includes pseudo-class
# and pseudo-element functions like :nth-child() and ::attr().
func_name_to_completions = {
    "
    "clamp": t.angle + t.frequency + t.length + t.number + t.percentage + t.time,
    "attr": [
        ("angle",),  # A tuple with only one string means the label is the same
        ("ch",),  # as the completion, i.e. ("foo",) is equivalent to
        ("cm",),  # ("foo", "foo").
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
    ]
    + t.angle
    + t.color
    + t.length
    + t.number
    + t.percentage
    + t.time,
    "auto": [t.identifier, t.string],
    "blenda": [("hsl",), ("hwb",), ("rgb",)] + t.color + t.percentage,
    "blur": t.length,
    "calc": t.angle + t.frequency + t.length + t.number + t.percentage + t.time,
    "child": t.integer,
    "cielab": t.number,
    "cielchab": t.number,
    "color": [("dgi-p3",), ("rec2020",), ("srgb",), t.identifier, t.string]
    + t.color
    + t.number
    + t.percentage,
    "color-adjuster-rgb": [t.hex_color] + t.number + t.percentage,
    "color-adjust": t.color,
    "color-contrast": t.color,
    "color-mix": t.color + t.number + t.percentage,
    "conic-gradient": [("at", "at "), ("from", "from "),] + t.color_stop + t.position,
    "content": [("after",), ("before",), ("first-letter",), ("marker",), ("text",),],
    "contrast": t.number + t.percentage,
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
    "element": [("first",), ("first-except",), ("last",), ("start",), t.identifier,],
    "ellipse-circle": [("at", "at ")] + t.shape_radius + t.position,
    "fade": t.length + t.percentage,
    "filter": t.number + t.percentage,
    "fit-content": t.length + t.percentage,
    "format": [t.string],
    "frames": t.integer,
    "gray": t.number + t.percentage,
    # "has": [],           # TODO: has takes a selector list as an arg. should it have completions?
    # "host": [],          # TODO: host takes a selector list as an arg. should it have completions?
    # "host-context": [],  # TODO: host-context takes a selector list as an arg. should it have completions?
    "hsla": [("from",)] + t.color + t.angle + t.number + t.percentage,
    "hue": t.angle,
    "hue-rotate": t.angle,
    "hwb": [("from",)] + t.color + t.angle + t.number + t.percentage,
    "icc-color": [t.identifier] + t.icc_color + t.number,
    "image": [t.string] + t.image + t.color,
    "image-set": [t.string] + t.image + t.resolution,
    "inset": [("round",)] + t.shape_arg,
    "lab": [("from",)] + t.color + t.number + t.percentage,
    "lch": [("from",)] + t.color + t.number + t.percentage,
    "leader": [("dotted",), ("solid",), ("space",), t.string],
    "linear-gradient": [("to", "to ")] + t.angle + t.color_stop + t.side_or_corner,
    "local": [t.identifier, t.string],
    # "matches": [],  # TODO: matches takes a selector list as an arg. should it have completions?
    "matrix": t.number,
    "max": t.angle + t.frequency + t.length + t.number + t.percentage + t.time,
    "min": t.angle + t.frequency + t.length + t.number + t.percentage + t.time,
    "minmax": [("auto",), ("min-content",), ("max-content",)]
    + t.flex
    + t.length
    + t.percentage,
    # "not": [],      # TODO: not takes a selector list as an arg. should it have completions?
    "nth-child": [("of", "of ")],
    "nth-last-child": [("of", "of ")],
    "path": [t.string] + t.fill_rule,
    "perspective": t.length,
    "polygon": t.fill_rule + t.shape_arg,
    "radial-gradient": [("at", "at "), ("circle",), ("ellipse",),]
    + t.color_stop
    + t.position
    + t.size,
    "ray": [("contain",)] + t.angle + t.size,
    "red-green-blue-alpha-a": t.number + t.percentage,
    "repeat": [("auto-fill",), t.identifier, t.line_names,]
    + t.integer
    + t.track_size,
    "rgba": [("from",)] + t.color + t.rgb_component,
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
    "swash-styleset-stylistic-ornaments-character-variant-annotation": [t.identifier]
    + t.integer,
    "symbols": [
        ("alphabetic",),
        ("cyclic",),
        ("fixed",),
        ("numeric",),
        ("symbolic",),
        t.string,
    ]
    + t.image,
    "target-counters": [t.string, t.url] + t.counter_style,
    "target-text": [
        ("after",),
        ("before",),
        ("content",),
        ("first-letter",),
        t.string,
        t.url,
    ],
    "tint-shade": t.percentage,
    "translate": t.length + t.percentage,
    "translate-z": t.length,
    "whiteness-saturation-lightness-blackness": t.percentage,
}

# Some functions take identifiers, or other symbols that are likely to be in
# the local symbol list, as arguments. Their completions should be returned
# without inhibiting word completions.
allow_word_completions = frozenset(
    (
        "attr",
        "attr-pseudo-element",
        "auto",
        "color",
        "counter",
        "counters",
        "element",
        "host",
        "host-context",
        "icc-color",
        "local",
        "repeat",
        "running",
        "select",
        "string",
        "swash-styleset-stylistic-ornaments-character-variant-annotation",
        "symbols",
        "target-counters",
        "var",
    )
)


def get_completions(func_name):
    # Append the var() completion to every set of completions.
    completions = func_name_to_completions.get(func_name, []) + [t.var]

    if func_name in allow_word_completions:
        return completions

    return completions, sublime.INHIBIT_WORD_COMPLETIONS


def sort_and_uniq_completions():
    for name in func_name_to_completions:
        func_name_to_completions[name] = list(set(func_name_to_completions[name]))
        func_name_to_completions[name].sort()


sort_and_uniq_completions()
