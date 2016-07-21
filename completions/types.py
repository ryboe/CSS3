# FUNCTIONS
# These completions are here instead of functions.py to avoid a circular import.
a            = ("a()", "a($1)")
alpha        = ("alpha()", "alpha($1)")
annotation   = ("annotation()", "annotation($1)")
attr         = ("attr()", "attr(${1:name})")
b            = ("b()", "b($1${2:0}%)")
blackness    = ("blackness()", "blackness($1${2:0}%)")
blend        = ("blend()", "blend(${1:<color>} ${2:0}%${3})")
blenda       = ("blenda()", "blenda(${1:<color>} ${2:0}%${3})")
blue         = ("blue()", "blue(${1:0})")
blur         = ("blur()", "blur(${1:<length>})")
brightness   = ("brightness()", "brightness($1)")
calc         = ("calc()", "calc($1)")
character_variant = ("character-variant()", "character-variant($1)")
child        = ("child()", "child(${1:0})")
cielab       = ("cielab()", "cielab(${1:<lightness>}, ${2:a}, ${3:b})")
cielchab     = ("cielchab()", "cielchab(${1:<lightness>}, ${2:<chroma>}, ${3:<hue>})")
circle       = ("circle()", "circle($1)")
color_func   = ("color()", "color(${1:<color-or-hue>} ${2:color-adjuster})")
conic_gradient = ("conic-gradient()", "conic-gradient(${1:from ${2:<angle>}}${3: at ${4:<position>}}${5})")
contrast     = ("contrast()", "contrast($1)")
counter      = ("counter()", "counter(${1:<identifier>})")
counters     = ("counters()", "counters(${1:<identifier>}, '${2:<string>}'$3)")
cross_fade   = ("cross-fade()", "cross-fade(${1:<mixing-image>}${2:, ${3:<final-image>}})")
cubic_bezier = ("cubic-bezier()", "cubic-bezier($1)")
device_cmyk  = ("device-cmyk()", "device-cmyk(${1:0}, ${2:0}, ${3:0}, ${4:0}${5:, ${6:1.0}}${7:, ${8:<color>}})")
device_gray  = ("device-gray()", "device-gray(${1:0})")
device_nchannel = ("device-nchannel()", "device-nchannel(${1:0})")
device_rgb   = ("device-rgb()", "device-rgb(${1:0}, ${2:0}, ${3:0})")
drop_shadow  = ("drop-shadow()", "drop-shadow(${1:<length>} ${2:<length>})")
element      = ("element()", "element(#${1:id})")
ellipse      = ("ellipse()", "ellipse($1)")
filter_func  = ("filter()", "filter($1)")
fit_content  = ("fit-content()", "fit-content($1)")
format_func  = ("format()", 'format("$1")')
gray         = ("gray()", "gray($1${2:, ${3:1.0}}})")
grayscale    = ("grayscale()", "grayscale($1)")
green        = ("green()", "green(${1:0})")
h            = ("h()", "h($1${2:<angle>})")
hsl          = ("hsl()", "hsl(${1:<hue>}, ${2:0}%, ${3:0}%)")
hsla         = ("hsla()", "hsla(${1:<hue>}, ${2:0}%, ${3:0}%, ${4:1.0})")
hue          = ("hue()", "hue($1{2:<angle>})")
hue_rotate   = ("hue-rotate()", "hue-rotate(${1:<angle>})")
hwb          = ("hwb()", "hwb(${1:<hue>}, ${2:0}%, ${3:0}%${4:, ${5:1.0}})")
icc_color_func = ("icc-color()", "icc-color(${1:name}, ${2:0})")
icc_named_color = ("icc-named-color()", "icc-named-color(${1:name}, ${2:<named-colo>r})")
image_func   = ("image()", "image($1)")
image_set    = ("image-set()", "image-set($1)")
inset        = ("inset()", "inset($1)")
invert       = ("invert()", "invert($1)")
l            = ("l()", "l($1${2:0}%)")
leader       = ("leader()", "leader($1)")
lightness    = ("lightness()", "lightness($1${2:0}%)")
linear_gradient = ("linear-gradient()", "linear-gradient($1)")
local        = ("local()", "local($1)")
minmax       = ("minmax()", "minmax(${1:<min>}, ${2:<max>})")
opacity      = ("opacity()", "opacity($1)")
ornaments    = ("ornaments()", "ornaments($1)")
polygon      = ("polygon()", "polygon($1)")
radial_gradient = ("radial-gradient()", "radial-gradient($1)")
red          = ("red()", "red(${1:0})")
repeat       = ("repeat()", "repeat($1)")
repeating_conic_gradient = ("repeating-conic-gradient()", "repeating-conic-gradient($1)")
repeating_linear_gradient = ("repeating-linear-gradient()", "repeating-linear-gradient($1)")
repeating_radial_gradient = ("repeating-radial-gradient()", "repeating-radial-gradient($1)")
rgb          = ("rgb()", "rgb(${1:0}, ${2:0}, ${3:0})")
rgba         = ("rgba()", "rgba(${1:0}, ${2:0}, ${3:0}, ${4:1.0})")
s            = ("s()", "s($1${2:0}%)")
saturate     = ("saturate()", "saturate($1)")
saturation   = ("saturation()", "saturation($1${2:0}%)")
sepia        = ("sepia()", "sepia($1)")
shade        = ("shade()", "shade(${1:0}%)")
snap_block   = ("snap-block()", "snap-block(${1:<length>})")
snap_inline  = ("snap-inline()", "snap-inline(${1:<length>})")
steps        = ("steps()", "steps($1)")
styleset     = ("styleset()", "styleset($1)")
stylistic    = ("stylistic()", "stylistic($1)")
swash        = ("swash()", "swash($1)")
symbols      = ("symbols()", "symbols($1)")
target_counter  = ("target-counter()", "target-counter($1)")
target_counters = ("target-counters()", "target-counters($1)")
target_text  = ("target-text()", "target-text($1)")
tint         = ("tint()", "tint(${1:0}%)")
url          = ("url()", "url('${1}')")
var          = ("var()", "var(--${1:name})")
w            = ("w()", "w($1${2:0}%)")
whiteness    = ("whiteness()", "whiteness($1${2:0}%)")

all_values = [("inherit",), ("initial",), ("revert",), ("unset",), var]


# OLD FUNCTIONS
# content      = ("content()", "content($1)")
# path         = ("path()", "path(${1:string})")
# matrix       = ("matrix()", "matrix(${1:0}, ${2:0}, ${3:0}, ${4:0}, ${5:0}, ${6:0})")
# matrix3d     = ("matrix3d()", "matrix3d(${1:0}, ${2:0}, ${3:0}, ${4:0}, ${5:0}, ${6:0}, ${7:0}, ${8:0}, ${9:0}, ${10:0}, ${11:0}, ${12:0}, ${13:0}, ${14:0}, ${15:0}, ${16:0})")
# perspective  = ("perspective()", "perspective(${1:length})")
# rotate       = ("rotate()", "rotate(${1:angle})")
# rotate3d     = ("rotate3d()", "rotate3d(${1:0}, ${2:0}, ${3:0}, ${4:angle})")
# rotateX      = ("rotateX()", "rotateX(${1:angle})")
# rotateY      = ("rotateY()", "rotateY(${1:angle})")
# rotateZ      = ("rotateZ()", "rotateZ(${1:angle})")
# scale        = ("scale()", "scale(${1:0}${2:, ${3:0}})")
# scale3d      = ("scale3d()", "scale3d(${1:0}, ${2:0}, ${3:0})")
# scaleX       = ("scaleX()", "scaleX(${1:0})")
# scaleY       = ("scaleY()", "scaleY(${1:0})")
# scaleZ       = ("scaleZ()", "scaleZ(${1:0})")
# skew         = ("skew()", "skew(${1:angle}${2:, ${3:angle}})")
# skewX        = ("skewX()", "skewX(${1:angle})")
# skewY        = ("skewY()", "skewY(${1:angle})")
# toggle       = ("toggle()", "toggle($1)")
# translate    = ("translate()", "translate(${1:length}${2:, ${3:length}})")
# translate3d  = ("translate3d()", "translate3d(${1:length}, ${2:length}, ${3:length})")
# translateX   = ("translateX()", "translateX(${1:length})")
# translateY   = ("translateY()", "translateY(${1:length})")
# translateZ   = ("translateZ()", "translateZ(${1:length})")

# TYPES
counter_style_name = ("<counter-style-name>", "${1:<counter-style-name>}")
hex_color = ("<hex-color>", "#$1")
family_name = ("<family-name>", "${1:<family-name>}")
font_face_name = ("<font-face-name>", "local($1)")
identifier = ("<identifier>", "${1:<identifier>}")
line_names = ("<line-names>", "[${1:<identifier>}]")
string = ("<string>", "'$1'")
urange = ("<urange>", "U+$1")

# COMPOSITE TYPES
angle = [("<angle>", "${1:<angle>}"), calc]
attachment = [("fixed",), ("local",), ("scroll",)]
auto_repeat = [repeat]
baseline_position = [
    ("baseline",),
    ("last-baseline",),
]
basic_shape = [circle, ellipse, inset, polygon]
blend_mode = [
    ("color",),
    ("color-burn",),
    ("color-dodge",),
    ("darken",),
    ("difference",),
    ("exclusion",),
    ("hard-light",),
    ("hue",),
    ("lighten",),
    ("luminosity",),
    ("multiply",),
    ("normal",),
    ("overlay",),
    ("saturation ",),
    ("screen",),
    ("soft-light",),
]
border_style = [
    ("dashed",),
    ("dotted",),
    ("double",),
    ("groove",),
    ("hidden",),
    ("inset",),
    ("none",),
    ("outset",),
    ("ridge",),
    ("solid",),
]
box = [("border-box",), ("content-box",), ("padding-box",)]
# caret_color = []  # TODO: write this when <caret-color> is defined in the spec
caret_shape = [
    ("auto",),
    ("bar",),
    ("block",),
    ("underscore",),
]
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
content_distribution = [
    ("space-around",),
    ("space-between",),
    ("space-evenly",),
    ("stretch",),
]
content_position = [
    ("center",),
    ("end",),
    ("flex-end",),
    ("flex-start",),
    ("left",),
    ("right",),
    ("start",),
]
contextual_alt_values = [("contextual",), ("no-contextual",)]
counter_style = [
    counter_style_name,
    symbols,
]
decibel = [("<decibel>", "${1:0}dB"), calc]
discretionary_lig_values = [
    ("discretionary-ligatures",),
    ("no-discretionary-ligatures",),
]
display_box = [("contents",), ("none",)]
display_inside = [
    ("flex",),
    ("flow",),
    ("flow-root",),
    ("grid",),
    ("ruby",),
    ("table",),
]
display_internal = [
    ("ruby-base",),
    ("ruby-base-container",),
    ("ruby-text",),
    ("ruby-text-container",),
    ("table-caption",),
    ("table-cell",),
    ("table-column",),
    ("table-column-group",),
    ("table-footer-group",),
    ("table-header-group",),
    ("table-row",),
    ("table-row-group",),
]
display_legacy = [
    ("inline-block",),
    ("inline-flex",),
    ("inline-grid",),
    ("inline-list-item",),
    ("inline-table",),
]
display_listitem = [("flow",), ("flow-root",), ("list-item",)]
display_outside = [("block",), ("inline",), ("run-in",)]
east_asian_variant_values = [
    ("jis04",),
    ("jis78",),
    ("jis83",),
    ("jis90",),
    ("simplified",),
    ("traditional",),
]
east_asian_width_values = [("full-width",), ("proportional-width",)]
extent_keyword = [
    ("closest-corner",),
    ("closest-side",),
    ("farthest-corner",),
    ("farthest-side",),
]
fill_rule = [("evenodd",), ("nonzero",)]
fixed_repeat = [repeat]
flex = [("<flex>", "${1:0}fr"), calc]
flex_direction = [("column",), ("column-reverse",), ("row",), ("row-reverse",)]
flex_wrap = [("nowrap",), ("wrap",), ("wrap-reverse",)]
font_family_generic = [
    ("cursive",),
    ("fantasy",),
    ("monospace",),
    ("sans-serif",),
    ("serif",),
]
font_family_name = [identifier, string]
frequency = [("<frequency>", "${1:0}Hz"), calc]
gradient = [
    conic_gradient,
    repeating_conic_gradient,
    linear_gradient,
    repeating_linear_gradient,
    radial_gradient,
    repeating_radial_gradient,
]
historical_lig_values = [("no-historical-ligatures",), ("historical-ligatures",)]
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
integer = [("<integer>", "${1:0}"), calc]
length = [("<length>", "${1:<length>}"), calc]
line_style = [
    ("dashed",),
    ("dotted",),
    ("double",),
    ("groove",),
    ("hidden",),
    ("inset",),
    ("none",),
    ("outset",),
    ("ridge",),
    ("solid",),
]
line_width = [("medium",), ("thick",), ("thin",)] + length
overflow_position = [
    ("safe",),
    ("unsafe",),
]
media_types = [
    ("all", "all"),
    ("and", "and "),
    ("not", "not "),
    ("only", "only "),
    ("print", "print"),
    ("screen", "screen"),
    ("speech", "speech"),
]
number = [("<number>", "${1:0}"), calc]
numeric_figure_values = [("lining-nums",), ("oldstyle-nums",)]
numeric_fraction_values = [("diagonal-fractions",), ("stacked-fractions",)]
numeric_spacing_values = [("proportional-nums",), ("tabular-nums",)]
paint = [
    ("child",),
    ("context-fill",),
    ("context-stroke",),
    ("none",),
    child,
    url,
] + color
percentage = [("<percentage>", "${1:0}%"), calc]
position = [
    ("bottom",),
    ("center",),
    ("left",),
    ("right",),
    ("top",),
] + length + percentage
quote = [
    ("close-quote",),
    ("no-close-quote",),
    ("no-open-quote",),
    ("open-quote",),
]
repeat_style = [
    ("no-repeat",),
    ("repeat",),
    ("repeat-x",),
    ("repeat-y",),
    ("round",),
    ("space",),
]
resolution = [("<resolution>", "${1:<resolution>}"), calc]
rgb_component = number + percentage
self_position = [
    ("center",),
    ("end",),
    ("flex-end",),
    ("flex-start",),
    ("left",),
    ("right",),
    ("self-end",),
    ("self-start",),
    ("start",),
]
semitones = [("<semitones>", "${1:0}st"), calc]
shape_arg = length + percentage
shape_box = [("margin-box",)] + box
shape_radius = [("closest-side",), ("farthest-side",)] + length + percentage
side_or_corner = [("bottom",), ("left",), ("right",), ("top",)]
single_animation_composition = [("accumulate",), ("add",), ("replace",)]
single_animation_direction = [("alternate",), ("alternate-reverse",), ("normal",), ("reverse",)]
single_animation_fill_mode = [("backwards",), ("both",), ("forwards",), ("none",)]
single_animation_iteration_count = [("infinite",)] + number
single_animation_name = [("none",), identifier]
single_animation_play_state = [("paused",), ("running",)]
single_timing_function = [
    ("ease",),
    ("ease-in",),
    ("ease-in-out",),
    ("ease-out",),
    ("linear",),
    ("step-end",),
    ("step-start",),
    cubic_bezier,
    steps,
]
size = extent_keyword + length + percentage
symbol = [identifier, string] + image
target = [target_counter, target_counters, target_text]
time = [("<time>", "${1:0}s"), calc]
track_breadth = [
    ("auto",),
    ("max-content",),
    ("min-content",),
] + flex + length + percentage
track_repeat = [repeat]
track_size = [fit_content, minmax] + track_breadth
width = [
    ("fill",),
    ("fit-content",),
    ("max-content",),
    ("min-content",),
    fit_content,
]
baseline_shift = [
    ("baseline",),
    ("sub",),
    ("super",)
] + length + percentage
bg_image = [("none",)] + image
bg_size = [
    ("auto",),
    ("contain",),
    ("cover",),
] + length + percentage
border_width = [("medium",), ("thick",), ("thin",)] + length
color_stop = color + length + percentage
content_list = [
    ("contents",),
    ("document-url",),
    leader,
    url,
    string,
] + quote + target
feature_tag_value = [("off",), ("on",), string] + integer
fixed_breadth = length + percentage
fixed_size = [minmax] + fixed_breadth
font_variant = (
    common_lig_values + discretionary_lig_values + historical_lig_values +
    east_asian_variant_values + east_asian_width_values +
    numeric_figure_values + numeric_fraction_values + numeric_spacing_values
)
geometry_box = [("fill-box",), ("stroke-box",), ("view-box",)] + shape_box
grid_line = [("auto",), ("span",), identifier] + integer
track_list = [line_names] + track_repeat + track_size
auto_track_list = [line_names] + auto_repeat + fixed_repeat + fixed_size

# TODO: delete this
# OLD TYPES
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
# # hue         = [("blue",), ("bluish",), ("bluish()", "bluish($1%)"), ("green",), ("greenish",), ("greenish()", "greenish($1%)"), ("orange",), ("orangish",), ("orangish()", "orangish($1%)"), ("purple",), ("purplish",), ("purplish()", "purplish($1%)"), ("red",), ("reddish",), ("reddish()", "reddish($1%)"), ("yellow",), ("yellowish",), ("yellowish()", "yellowish($1%)"), angle, number]
# percentage  = ("<percentage>", "$1%")
# position    = [("bottom",), ("center",), ("left",), ("right",), ("top",), length, percentage, calc]
# resolution  = ("<resolution>", "${1:<resolution>}")
# semitones   = ("<semitones>", "${1:0}st")
# string      = ("<string>", "'$1'")
# svg_color   = color + [cielab, cielchab, device_gray, device_nchannel, device_rgb, icc_color, icc_named_color]
# timing_function = [("ease",), ("ease-in",), ("ease-in-out",), ("ease-out",), ("linear",), ("step-end",), ("step-start",), cubic_bezier, steps]
# time        = ("<time>", "${1:<time>}")
# transform   = [matrix, matrix3d, perspective, rotate, rotate3d, rotateX, rotateY, rotateZ, scale, scale3d, scaleX, scaleY, scaleZ, skew, skewX, skewY, translate, translate3d, translateX, translateY, translateZ]
# urange      = ("<urange>", "U+$1")
