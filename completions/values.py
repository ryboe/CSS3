
a            = ("a()", "a(${1})")
alpha        = ("alpha()", "alpha(${1})")
annotation   = ("annotation()", "annotation(${1})")
attr         = ("attr()", "attr(${1:name})")
b            = ("b()", "b(${1}${2:100}%)")
blackness    = ("blackness()", "blackness(${1}${2:100}%)")
blend        = ("blend()", "blend(${1:color} ${2:100}%${3})")
blenda       = ("blenda()", "blenda(${1:color} ${2:100}%${3})")
blue         = ("blue()", "blue(${1:0})")
character_variant = ("character-variant()", "character-variant(${1})")
cielab       = ("cielab()", "cielab(${1:lightness}, ${2:a}, ${3:b})")
cielchab     = ("cielchab()", "cielchab(${1:lightness}, ${2:chroma}, ${3:hue})")
color_func   = ("color()", "color(${1:color-or-hue} ${2:color-adjuster})")
conic_gradient = ("conic-gradient()", "conic-gradient(${1:from ${2:angle}}${3: at ${4:position}}${5})")
contrast     = ("contrast()", "contrast(${1:100}%)")
cross_fade   = ("cross-fade()", "cross-fade(${1:mixing-image}${2:, ${3:final-image}})")
device_cmyk  = ("device-cmyk()", "device-cmyk(${1:0}, ${2:0}, ${3:0}, ${4:0}${5:, ${6:1.0}}${7:, ${8:color}})")
device_gray  = ("device-gray()", "device-gray(${1:0})")
device_nchannel = ("device-nchannel()", "device-nchannel(${1:0})")
device_rgb   = ("device-rgb()", "device-rgb(${1:0}, ${2:0}, ${3:0})")
element      = ("element()", "element(#${1:id})")
fit_content  = ("fit-content()", "fit-content(${1})")
format_func  = ("format()", 'format("${1}")')
gray         = ("gray()", "gray(${1}${2:, ${3:1.0}}})")
green        = ("green()", "green(${1:0})")
h            = ("h()", "h(${1}${2:angle})")
hsl          = ("hsl()", "hsl(${1:hue}, ${2:100}%, ${3:100}%)")
hsla         = ("hsla()", "hsla(${1:hue}, ${2:100}%, ${3:100}%, ${4:1.0})")
hue          = ("hue()", "hue(${1}{2:angle})")
hwb          = ("hwb()", "hwb(${1:hue}, ${2:100}%, ${3:100}%${4:, ${5:1.0}})")
icc_color_func = ("icc-color()", "icc-color(${1:name}, ${2:0})")
icc_named_color = ("icc-named-color()", "icc-named-color(${1:name}, ${2:named-color})")
image_func   = ("image()", "image(${1})")
image_set    = ("image-set()", "image-set(${1})")
l            = ("l()", "l(${1}${2:100}%)")
lightness    = ("lightness()", "lightness(${1}${2:100}%)")
linear_gradient = ("linear-gradient()", "linear-gradient(${1})")
local        = ("local()", "local(${1})")
minmax       = ("minmax()", "minmax(${1:min}, ${2:max})")
ornaments    = ("ornaments()", "ornaments(${1})")
radial_gradient = ("radial-gradient()", "radial-gradient(${1})")
red          = ("red()", "red(${1:0})")
repeating_conic_gradient = ("repeating-conic-gradient()", "repeating-conic-gradient(${1})")
repeating_linear_gradient = ("repeating-linear-gradient()", "repeating-linear-gradient(${1})")
repeating_radial_gradient = ("repeating-radial-gradient()", "repeating-radial-gradient(${1})")
rgb          = ("rgb()", "rgb(${1:0}, ${2:0}, ${3:0})")
rgba         = ("rgba()", "rgba(${1:0}, ${2:0}, ${3:0}, ${4:1.0})")
s            = ("s()", "s(${1}${2:100}%)")
saturation   = ("saturation()", "saturation(${1}${2:100}%)")
shade        = ("shade()", "shade(${1:100}%)")
styleset     = ("styleset()", "styleset(${1})")
stylistic    = ("stylistic()", "stylistic(${1})")
swash        = ("swash()", "swash(${1})")
symbols      = ("symbols()", "symbols(${1})")
tint         = ("tint()", "tint(${1:100}%)")
url          = ("url()", "url(${1:quoted-string})")
var          = ("var()", "var(--${1:name})")
w            = ("w()", "w(${1}${2:100}%)")
whiteness    = ("whiteness()", "whiteness(${1}${2:100}%)")







# annotation   = ("annotation()", "annotation(${1})")
# blur         = ("blur()", "blur(${1:length})")
# brightness   = ("brightness()", "brightness(${1})")
# calc         = ("calc()", "calc(${1})")
# character_variant = ("character-variant()", "character-variant(${1})")
# child        = ("child()", "child(${1:integer})")
# circle       = ("circle()", "circle(${1})")
# content      = ("content()", "content(${1})")
# counter      = ("counter()", "counter(${1:ident}${2:, ${3:list-style-type}})")
# counters     = ("counters()", "counters(${1:ident}, \"${2:string}\"${3:, ${4:list-style-type}})")
# cubic_bezier = ("cubic-bezier()", "cubic-bezier(${1:0}, ${2:0}, ${3:0}, ${4:0})")
# d_path       = ("path()", "path(${1:string})")
# drop_shadow  = ("drop-shadow()", "drop-shadow(${1:length} ${2:length})")
# ellipse      = ("ellipse()", "ellipse(${1})")
# filter_func  = ("filter()", "filter(${1})")
# grayscale    = ("grayscale()", "grayscale(${1})")
# hue_rotate   = ("hue-rotate()", "hue-rotate(${1:angle})")
# inset        = ("inset()", "inset(${1})")
# invert       = ("invert()", "invert(${1})")
# matrix       = ("matrix()", "matrix(${1:0}, ${2:0}, ${3:0}, ${4:0}, ${5:0}, ${6:0})")
# matrix3d     = ("matrix3d()", "matrix3d(${1:0}, ${2:0}, ${3:0}, ${4:0}, ${5:0}, ${6:0}, ${7:0}, ${8:0}, ${9:0}, ${10:0}, ${11:0}, ${12:0}, ${13:0}, ${14:0}, ${15:0}, ${16:0})")
# opacity      = ("opacity()", "opacity(${1})")
# ornaments    = ("ornaments()", "ornaments(${1})")
# path         = ("path()", "path(${1})")
# perspective  = ("perspective()", "perspective(${1:length})")
# polygon      = ("polygon()", "polygon(${1})")
# repeat       = ("repeat()", "repeat(${1})")
# rotate       = ("rotate()", "rotate(${1:angle})")
# rotate3d     = ("rotate3d()", "rotate3d(${1:0}, ${2:0}, ${3:0}, ${4:angle})")
# rotateX      = ("rotateX()", "rotateX(${1:angle})")
# rotateY      = ("rotateY()", "rotateY(${1:angle})")
# rotateZ      = ("rotateZ()", "rotateZ(${1:angle})")
# saturate     = ("saturate()", "saturate(${1})")
# scale        = ("scale()", "scale(${1:0}${2:, ${3:0}})")
# scale3d      = ("scale3d()", "scale3d(${1:0}, ${2:0}, ${3:0})")
# scaleX       = ("scaleX()", "scaleX(${1:0})")
# scaleY       = ("scaleY()", "scaleY(${1:0})")
# scaleZ       = ("scaleZ()", "scaleZ(${1:0})")
# sepia        = ("sepia()", "sepia(${1})")
# skew         = ("skew()", "skew(${1:angle}${2:, ${3:angle}})")
# skewX        = ("skewX()", "skewX(${1:angle})")
# skewY        = ("skewY()", "skewY(${1:angle})")
# snap_block   = ("snap-block()", "snap-block(${1})")
# snap_inline  = ("snap-inline()", "snap-inline(${1})")
# steps        = ("steps()", "steps(${1})")
# styleset     = ("styleset()", "styleset(${1})")
# stylistic    = ("stylistic()", "stylistic(${1})")
# swash        = ("swash()", "swash(${1})")
# toggle       = ("toggle()", "toggle(${1})")
# translate    = ("translate()", "translate(${1:length}${2:, ${3:length}})")
# translate3d  = ("translate3d()", "translate3d(${1:length}, ${2:length}, ${3:length})")
# translateX   = ("translateX()", "translateX(${1:length})")
# translateY   = ("translateY()", "translateY(${1:length})")
# translateZ   = ("translateZ()", "translateZ(${1:length})")

# TYPES
color = [
    ("aliceblue",),
    ("antiquewhite",),
    ("aqua",),
    ("aquamarine",),
    ("azure",),
    ("beige",),
    ("bisque",),
    ("black",),
    ("blanchedalmond",),
    ("blue",),
    ("blueviolet",),
    ("brown",),
    ("burlywood",),
    ("cadetblue",),
    ("chartreuse",),
    ("chocolate",),
    ("coral",),
    ("cornflowerblue",),
    ("cornsilk",),
    ("crimson",),
    ("currentcolor",),
    ("cyan",),
    ("darkblue",),
    ("darkcyan",),
    ("darkgoldenrod",),
    ("darkgray",),
    ("darkgreen",),
    ("darkgrey",),
    ("darkkhaki",),
    ("darkmagenta",),
    ("darkolivegreen",),
    ("darkorange",),
    ("darkorchid",),
    ("darkred",),
    ("darksalmon",),
    ("darkseagreen",),
    ("darkslateblue",),
    ("darkslategray",),
    ("darkslategrey",),
    ("darkturquoise",),
    ("darkviolet",),
    ("deeppink",),
    ("deepskyblue",),
    ("dimgray",),
    ("dimgrey",),
    ("dodgerblue",),
    ("firebrick",),
    ("floralwhite",),
    ("forestgreen",),
    ("fuchsia",),
    ("gainsboro",),
    ("ghostwhite",),
    ("gold",),
    ("goldenrod",),
    ("gray",),
    ("green",),
    ("greenyellow",),
    ("grey",),
    ("honeydew",),
    ("hotpink",),
    ("indianred",),
    ("indigo",),
    ("ivory",),
    ("khaki",),
    ("lavender",),
    ("lavenderblush",),
    ("lawngreen",),
    ("lemonchiffon",),
    ("lightblue",),
    ("lightcoral",),
    ("lightcyan",),
    ("lightgoldenrodyellow",),
    ("lightgray",),
    ("lightgreen",),
    ("lightgrey",),
    ("lightpink",),
    ("lightsalmon",),
    ("lightseagreen",),
    ("lightskyblue",),
    ("lightslategray",),
    ("lightslategrey",),
    ("lightsteelblue",),
    ("lightyellow",),
    ("lime",),
    ("limegreen",),
    ("linen",),
    ("magenta",),
    ("maroon",),
    ("mediumaquamarine",),
    ("mediumblue",),
    ("mediumorchid",),
    ("mediumpurple",),
    ("mediumseagreen",),
    ("mediumslateblue",),
    ("mediumspringgreen",),
    ("mediumturquoise",),
    ("mediumvioletred",),
    ("midnightblue",),
    ("mintcream",),
    ("mistyrose",),
    ("moccasin",),
    ("navajowhite",),
    ("navy",),
    ("oldlace",),
    ("olive",),
    ("olivedrab",),
    ("orange",),
    ("orangered",),
    ("orchid",),
    ("palegoldenrod",),
    ("palegreen",),
    ("paleturquoise",),
    ("palevioletred",),
    ("papayawhip",),
    ("peachpuff",),
    ("peru",),
    ("pink",),
    ("plum",),
    ("powderblue",),
    ("purple",),
    ("rebeccapurple",),
    ("red",),
    ("rosybrown",),
    ("royalblue",),
    ("saddlebrown",),
    ("salmon",),
    ("sandybrown",),
    ("seagreen",),
    ("seashell",),
    ("sienna",),
    ("silver",),
    ("skyblue",),
    ("slateblue",),
    ("slategray",),
    ("slategrey",),
    ("snow",),
    ("springgreen",),
    ("steelblue",),
    ("tan",),
    ("teal",),
    ("thistle",),
    ("tomato",),
    ("transparent",),
    ("turquoise",),
    ("violet",),
    ("wheat",),
    ("white",),
    ("whitesmoke",),
    ("yellow",),
    ("yellowgreen",),
    a,
    alpha,
    b,
    blackness,
    blend,
    blenda,
    blue,
    cielab,
    cielchab,
    color_func,
    contrast,
    device_cmyk,
    device_gray,
    device_nchannel,
    device_rgb,
    gray,
    green,
    h,
    hsl,
    hsla,
    hue,
    hwb,
    icc_color_func,
    icc_named_color,
    l,
    lightness,
    red,
    rgb,
    rgba,
    s,
    saturation,
    shade,
    tint,
    w,
    whiteness,
]

common_lig_values = [("common-ligatures",), ("no-common-ligatures",)]

contextual_alt_values = [("contextual",), ("no-contextual",)]

discretionary_lig_values = [
    ("discretionary-ligatures",),
    ("no-discretionary-ligatures",),
]


east_asian_variant_values = [
    ("jis04",),
    ("jis78",),
    ("jis83",),
    ("jis90",),
    ("simplified",),
    ("traditional",),
]

east_asian_width_values = [("full-width",), ("proportional-width",)]

historical_lig_values = [("no-historical-ligatures",), ("historical-ligatures",)]

numeric_figure_values = [("lining-nums",), ("oldstyle-nums",)]

numeric_fraction_values = [("diagonal-fractions",), ("stacked-fractions",)]

numeric_spacing_values = [("proportional-nums",), ("tabular-nums",)]

font_variant = (
    common_lig_values + discretionary_lig_values + historical_lig_values +
    east_asian_variant_values + east_asian_width_values +
    numeric_figure_values + numeric_fraction_values + numeric_spacing_values
)

gradient = [
    conic_gradient,
    repeating_conic_gradient,
    linear_gradient,
    repeating_linear_gradient,
    radial_gradient,
    repeating_radial_gradient,
]

icc_color = [
    cielab,
    cielchab,
    device_gray,
    device_rgb,
    device_nchannel,
    icc_color_func,
]

image = [
    cross_fade,
    element,
    image_func,
    image_set,
    url,
] + gradient

position = [
    ("bottom",),
    ("center",),
    ("left",),
    ("right",),
    ("top",),
]

# Some functions take identifiers, or other symbols that are likely to be in
# the local symbol list, as arguments. Their completions should be returned
# without inhibiting word completions.
allow_word_completions = frozenset((
    "additive-symbols",
    "attr",
    "::attr",
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

# VALUES

color_profile_descriptor_to_completions = {
    "rendering-intent": [
        ("absolute-colorimetric",),
        ("auto",),
        ("perceptual",),
        ("relative-colorimetric",),
        ("saturation",),
    ],
    "src": [
        ("sRGB",),
        local,
        url,
    ],
}

counter_style_descriptor_to_completions = {
    "additive-symbols": image,
    "negative": image,
    "pad": [("auto",), ("infinite",)] + image,
    "prefix": image,
    "range": [("auto",), ("infinite",)],
    "speak-as": [
        ("auto",),
        ("bullets",),
        ("numbers",),
        ("spell-out",),
        ("words",),
    ],
    "suffix": image,
    "symbols": image,
    "system": [
        ("additive",),
        ("alphabetic",),
        ("cyclic",),
        ("extends",),
        ("fixed",),
        ("numeric",),
        ("symbolic",),
    ],
}

font_face_descriptor_to_completions = {
    "font-family": [
        ("cursive",),
        ("fantasy",),
        ("monospace",),
        ("sans-serif",),
        ("serif",),
    ],
    "font-feature-settings": [("off",), ("on",), ("normal",)],
    "font-stretch": [
        ("condensed",),
        ("expanded",),
        ("extra-condensed",),
        ("extra-expanded",),
        ("normal",),
        ("semi-condensed",),
        ("semi-expanded",),
        ("ultra-condensed",),
        ("ultra-expanded",),
    ],
    "font-style": [
        ("italic",),
        ("normal",),
        ("oblique",),
    ],
    "font-variant": [
        ("all-petite-caps",),
        ("all-small-caps",),
        ("historical-forms",),
        ("none",),
        ("normal",),
        ("ordinal",),
        ("petite-caps",),
        ("ruby",),
        ("slashed-zero",),
        ("small-caps",),
        ("sub",),
        ("super",),
        ("titling-caps",),
        ("unicase",),

        annotation,
        character_variant,
        ornaments,
        styleset,
        stylistic,
        swash,
    ] + font_variant,
    "font-weight": [
        ("100",),
        ("200",),
        ("300",),
        ("400",),
        ("500",),
        ("600",),
        ("700",),
        ("800",),
        ("900",),
        ("bold",),
        ("normal",),
    ],
    "src": [
        format_func,
        local,
        url,
    ],
}

viewport_descriptor_to_completions = {
    "orientation": [
        ("auto",),
        ("landscape",),
        ("portrait",),
    ],
    "user-zoom": [
        ("fixed",),
        ("zoom",),
    ],
    "zoom": [
        ("auto",),
    ],
}

at_rule_to_completions_dict = {
    "color-profile": color_profile_descriptor_to_completions,
    "counter-style": counter_style_descriptor_to_completions,
    "font-face": font_face_descriptor_to_completions,
    "viewport": viewport_descriptor_to_completions,
}

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
    "blenda": [("hsl",), ("hwb",), ("rgb",)] + color,
    "color": color,
    "conic-gradient": [("at",), ("from",)] + position,
    "content": [
        ("after",),
        ("before",),
        ("first-letter",),
        ("marker",),
        ("text",),
    ],
    "counter": [("none",), symbols] + image,
    "counters": [("none",), symbols] + image,
    "cross-fade": color + image,
    "device-cmyk": color,
    "dir": [("ltr",), ("rtl",)],
    "drop": [("active",), ("invalid",), ("valid",)],
    "drop-shadow": color,
    "element": [("first",), ("first-except",), ("last",), ("start",)],
    "ellipse-circle": [("at",), ("closest-side",), ("farthest-side",)] + position,
    # "has": [],           # TODO: has takes a selector list as an arg. should it have completions?
    # "host": [],          # TODO: host takes a selector list as an arg. should it have completions?
    # "host-context": [],  # TODO: host-context takes a selector list as an arg. should it have completions?
    "icc-color": icc_color,
    "image": image + color,
    "image-set": image,
    "inset": [("round",)],
    "leader": [("dotted",), ("solid",), ("space",)],
    "linear-gradient": [
        ("bottom",),
        ("left",),
        ("right",),
        ("to",),
        ("top",),
    ] + color,
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
    ] + color + position,
    "repeat": [
        ("auto",),
        ("auto-fill",),
        ("auto-fit",),
        ("max-content",),
        ("min-content",),
        minmax,
        fit_content,
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
    ] + image,
    "target-counters": [symbols, url],
    "target-text": [
        ("after",),
        ("before",),
        ("content",),
        ("first-letter",),
        url,
    ],
}


def sort_completions():
    """Sort the completions in the func_name_to_completions dictionary.

    They will appear in alphabetical order in the completions menu.
    """
    completions_maps = (
        func_name_to_completions,
        color_profile_descriptor_to_completions,
        counter_style_descriptor_to_completions,
        font_face_descriptor_to_completions,
    )

    for m in completions_maps:
        for name in m:
            m[name].sort()

sort_completions()





























# TYPES
# angle       = ("<angle>", "${1:<angle>}")
# basic_shape = [inset, circle, ellipse, polygon]
# color       = [("aliceblue",), ("antiquewhite",), ("aqua",), ("aquamarine",), ("azure",), ("beige",), ("bisque",), ("black",), ("blanchedalmond",), ("blue",), ("blueviolet",), ("brown",), ("burlywood",), ("cadetblue",), ("chartreuse",), ("chocolate",), ("coral",), ("cornflowerblue",), ("cornsilk",), ("crimson",), ("currentColor",), ("currentcolor",), ("cyan",), ("darkblue",), ("darkcyan",), ("darkgoldenrod",), ("darkgray",), ("darkgreen",), ("darkgrey",), ("darkkhaki",), ("darkmagenta",), ("darkolivegreen",), ("darkorange",), ("darkorchid",), ("darkred",), ("darksalmon",), ("darkseagreen",), ("darkslateblue",), ("darkslategray",), ("darkslategrey",), ("darkturquoise",), ("darkviolet",), ("deeppink",), ("deepskyblue",), ("dimgray",), ("dimgrey",), ("dodgerblue",), ("firebrick",), ("floralwhite",), ("forestgreen",), ("fuchsia",), ("gainsboro",), ("ghostwhite",), ("gold",), ("goldenrod",), ("gray",), ("green",), ("greenyellow",), ("grey",), ("honeydew",), ("hotpink",), ("indianred",), ("indigo",), ("ivory",), ("khaki",), ("lavender",), ("lavenderblush",), ("lawngreen",), ("lemonchiffon",), ("lightblue",), ("lightcoral",), ("lightcyan",), ("lightgoldenrodyellow",), ("lightgray",), ("lightgreen",), ("lightgrey",), ("lightpink",), ("lightsalmon",), ("lightseagreen",), ("lightskyblue",), ("lightslategray",), ("lightslategrey",), ("lightsteelblue",), ("lightyellow",), ("lime",), ("limegreen",), ("linen",), ("magenta",), ("maroon",), ("mediumaquamarine",), ("mediumblue",), ("mediumorchid",), ("mediumpurple",), ("mediumseagreen",), ("mediumslateblue",), ("mediumspringgreen",), ("mediumturquoise",), ("mediumvioletred",), ("midnightblue",), ("mintcream",), ("mistyrose",), ("moccasin",), ("navajowhite",), ("navy",), ("oldlace",), ("olive",), ("olivedrab",), ("orange",), ("orangered",), ("orchid",), ("palegoldenrod",), ("palegreen",), ("paleturquoise",), ("palevioletred",), ("papayawhip",), ("peachpuff",), ("peru",), ("pink",), ("plum",), ("powderblue",), ("purple",), ("rebeccapurple",), ("red",), ("rosybrown",), ("royalblue",), ("saddlebrown",), ("salmon",), ("sandybrown",), ("seagreen",), ("seashell",), ("sienna",), ("silver",), ("skyblue",), ("slateblue",), ("slategray",), ("slategrey",), ("snow",), ("springgreen",), ("steelblue",), ("tan",), ("teal",), ("thistle",), ("tomato",), ("transparent",), ("turquoise",), ("violet",), ("wheat",), ("white",), ("whitesmoke",), ("yellow",), ("yellowgreen",), color_func, device_cmyk, gray, hsl, hsla, hwb, rgb, rgba]
# counter_style = [("afar",), ("agaw",), ("ancient-tamil",), ("arabic-indic",), ("ari",), ("armenian",), ("bengali",), ("binary",), ("blin",), ("cambodian",), ("cambodian-consonant",), ("circle",), ("circled-decimal",), ("circled-ideograph",), ("circled-katakana",), ("circled-korean-consonant",), ("circled-korean-syllable",), ("circled-lower-latin",), ("circled-upper-latin",), ("cjk-decimal",), ("cjk-earthly-branch",), ("cjk-heavenly-stem",), ("cjk-ideographic",), ("decimal",), ("decimal-leading-zero",), ("devanagari",), ("disc",), ("disclosure-closed",), ("disclosure-open",), ("dizi",), ("dotted-decimal",), ("double-circled-decimal",), ("ethiopic-numeric",), ("filled-circled-decimal",), ("fullwidth-decimal",), ("fullwidth-lower-alpha",), ("fullwidth-lower-roman",), ("fullwidth-upper-alpha",), ("fullwidth-upper-roman",), ("gedeo",), ("georgian",), ("greek",), ("gujarati",), ("gumuz",), ("gurmukhi",), ("hadiyya",), ("harari",), ("hebrew",), ("hebrew-extended",), ("hindi",), ("hiragana",), ("hiragana-iroha",), ("japanese-formal",), ("japanese-informal",), ("kaffa",), ("kannada",), ("katakana",), ("katakana-iroha",), ("kebena",), ("kembata",), ("khmer",), ("khmer-consonant",), ("konso",), ("korean-consonant",), ("korean-hangul-formal",), ("korean-hanja-formal",), ("korean-hanja-informal",), ("korean-syllable",), ("kunama",), ("lao",), ("lepcha",), ("lower-alpha",), ("lower-alpha-symbolic",), ("lower-armenian",), ("lower-belorussian",), ("lower-bulgarian",), ("lower-greek",), ("lower-hexadecimal",), ("lower-latin",), ("lower-macedonian",), ("lower-oromo-qubee",), ("lower-roman",), ("lower-russian",), ("lower-russian-full",), ("lower-serbo-croatian",), ("lower-ukrainian",), ("lower-ukrainian-full",), ("malayalam",), ("meen",), ("mongolian",), ("myanmar",), ("new-base-60",), ("none",), ("octal",), ("oriya",), ("oromo",), ("parenthesized-decimal",), ("parenthesized-hangul-consonant",), ("parenthesized-hangul-syllable",), ("parenthesized-ideograph",), ("parenthesized-lower-latin",), ("persian",), ("persian-abjad",), ("persian-alphabetic",), ("saho",), ("shan",), ("sidama",), ("silti",), ("simp-chinese-formal",), ("simp-chinese-informal",), ("simple-lower-roman",), ("simple-upper-roman",), ("square",), ("super-decimal",), ("tamil",), ("telugu",), ("thai",), ("thai-alphabetic",), ("tibetan",), ("tigre",), ("trad-chinese-formal",), ("trad-chinese-informal",), ("upper-alpha",), ("upper-alpha-symbolic",), ("upper-armenian",), ("upper-belorussian",), ("upper-bulgarian",), ("upper-hexadecimal",), ("upper-latin",), ("upper-macedonian",), ("upper-oromo-qubee",), ("upper-roman",), ("upper-russian",), ("upper-russian-full",), ("upper-serbo-croatian",), ("upper-ukrainian",), ("upper-ukrainian-full",), ("wolaita",), ("yemsa",)]
# decibel     = ("<decibel>", "${1:0}dB")
# filters     = [blur, brightness, contrast, drop_shadow, grayscale, hue_rotate, invert, opacity, saturate, sepia]
# flex        = ("<flex>", "${1:0}fr")
# frequency   = ("<frequency>", "${1:<frequency>}")
# ident       = ("<ident>", "${1:<ident>}")
# image       = [conic_gradient, cross_fade, element, filter_func, image_func, image_set, linear_gradient, radial_gradient, repeating_conic_gradient, repeating_linear_gradient, repeating_radial_gradient, url]
# integer     = ("<integer>", "${1:<integer>}")
# length      = ("<length>", "${1:<length>}")
# number      = ("<number>", "${1:<number>}")
# # TODO: this should be enabled only inside the color(), hsl(), hsla(), and hwb() functions
# # hue         = [("blue",), ("bluish",), ("bluish()", "bluish(${1}%)"), ("green",), ("greenish",), ("greenish()", "greenish(${1}%)"), ("orange",), ("orangish",), ("orangish()", "orangish(${1}%)"), ("purple",), ("purplish",), ("purplish()", "purplish(${1}%)"), ("red",), ("reddish",), ("reddish()", "reddish(${1}%)"), ("yellow",), ("yellowish",), ("yellowish()", "yellowish(${1}%)"), angle, number]
# percentage  = ("<percentage>", "${1}%")
# position    = [("bottom",), ("center",), ("left",), ("right",), ("top",), length, percentage, calc]
# resolution  = ("<resolution>", "${1:<resolution>}")
# semitones   = ("<semitones>", "${1:0}st")
# string      = ("<string>", "'${1}'")
# svg_color   = color + [cielab, cielchab, device_gray, device_nchannel, device_rgb, icc_color, icc_named_color]
# timing_function = [("ease",), ("ease-in",), ("ease-in-out",), ("ease-out",), ("linear",), ("step-end",), ("step-start",), cubic_bezier, steps]
# time        = ("<time>", "${1:<time>}")
# transform   = [matrix, matrix3d, perspective, rotate, rotate3d, rotateX, rotateY, rotateZ, scale, scale3d, scaleX, scaleY, scaleZ, skew, skewX, skewY, translate, translate3d, translateX, translateY, translateZ]
# urange      = ("<urange>", "U+${1}")


# # COMMON VALUES
# all_values = [("inherit",), ("initial",), ("revert",), ("unset",), var]


# TODO
# add completions to the scopes inside functions.
#   missing lots of completion opportunities, e.g. all the <hue> and color() funcs
#     e.g. reddish, purplish, lightness, l, whiteness, w
#     <hue> should only be available inside color(), hsl(), hsla(), and hwb()
#   need to go through every #type-function-* rule and add completions for all the contents of those rules
