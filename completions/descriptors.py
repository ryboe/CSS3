from CSS3.completions import types as t
import sublime

# DESCRIPTOR NAMES
color_profile = [
    ("rendering-intent", "rendering-intent: ${1};"),
    ("src", "src: ${1};"),
]
counter_style = [
    ("additive-symbols", "additive-symbols: ${1};"),
    ("fallback", "fallback: ${1:<counter-style-name>};"),
    ("negative", "negative: ${1};"),
    ("pad", "pad: ${1};"),
    ("prefix", "prefix: ${1:<symbol>};"),
    ("range", "range: ${1};"),
    ("speak-as", "speak-as: ${1};"),
    ("suffix", "suffix: ${1:<symbol>};"),
    ("symbols", "symbols: ${1};"),
    ("system", "system: ${1};"),
]
font_face = [
    ("font-display", "font-display: ${1};"),
    ("font-family", "font-family: ${1:<family-name>};"),
    ("font-feature-settings", "font-feature-settings: ${1};"),
    ("font-stretch", "font-stretch: ${1};"),
    ("font-style", "font-style: ${1};"),
    ("font-variant", "font-variant: ${1};"),
    ("font-weight", "font-weight: ${1};"),
    ("src", "src: ${1};"),
]
font_palette_values = [
    ("font-family", "font-family: ${1};"),
    ("base-palette", "base-palette: ${1};"),
    ("color-0", "color-0: ${1};"),
    ("color-1", "color-1: ${1};"),
    ("color-2", "color-2: ${1};"),
    ("color-3", "color-3: ${1};"),
    ("color-4", "color-4: ${1};"),
    ("color-5", "color-5: ${1};"),
    ("color-6", "color-6: ${1};"),
    ("color-7", "color-7: ${1};"),
    ("color-8", "color-8: ${1};"),
    ("color-9", "color-9: ${1};"),
]
viewport = [
    ("height", "height: ${1:<viewport-length>} ${2:<viewport-length>};"),
    ("max-height", "max-height: ${1:<viewport-length>};"),
    ("max-width", "max-width: ${1:<viewport-length>};"),
    ("max-zoom", "max-zoom: ${1};"),
    ("min-height", "min-height: ${1:<viewport-length>};"),
    ("min-width", "min-width: ${1:<viewport-length>};"),
    ("min-zoom", "min-zoom: ${1};"),
    ("orientation", "orientation: ${1};"),
    ("user-zoom", "user-zoom: ${1};"),
    ("width", "width: ${1:<viewport-length>} ${2:<viewport-length>};"),
    ("zoom", "zoom: ${1};"),
]

# DESCRIPTOR VALUES
color_profile_values = {
    "rendering-intent": [
        ("absolute-colorimetric",),
        ("perceptual",),
        ("relative-colorimetric",),
        ("saturation",),
    ],
    "src": [t.local, t.format_func, t.url],
}
counter_style_values = {
    "additive-symbols": t.integer + t.symbol,
    "negative": t.symbol,
    "pad": t.integer + t.symbol,
    "range": [("auto",), ("infinite",)] + t.integer,
    "speak-as": [
        ("<counter-style-name>", "${1}"),
        ("auto",),
        ("bullets",),
        ("numbers",),
        ("spell-out",),
        ("words",),
    ],
    "suffix-prefix": t.symbol,
    "symbols": t.symbol,
    "system": [
        ("additive",),
        ("alphabetic",),
        ("cyclic",),
        ("extends",),
        ("fixed",),
        ("numeric",),
        ("symbolic",),
        t.counter_style_name,
    ]
    + t.integer,
}
font_face_values = {
    "font-display": [("auto",), ("block",), ("fallback",), ("optional",), ("swap",),],
    "font-family": [t.family_name],
    "font-feature-settings": [("normal",)] + t.feature_tag_value,
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
    ]
    + t.percentage,
    "font-style": [("italic",), ("normal",), ("oblique",)] + t.angle,
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
        t.annotation,
        t.character_variant,
        t.ornaments,
        t.styleset,
        t.stylistic,
        t.swash,
    ]
    + (
        t.common_lig_values
        + t.discretionary_lig_values
        + t.historical_lig_values
        + t.contextual_alt_values
        + t.numeric_figure_values
        + t.numeric_spacing_values
        + t.numeric_fraction_values
        + t.east_asian_variant_values
        + t.east_asian_width_values
    ),
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
    "src": [t.format_func, t.font_face_name, t.local, t.url,],
    "unicode-range": [t.urange],
}
viewport_values = {
    "orientation": [("auto",), ("landscape",), ("portrait",)],
    "user-zoom": [("fixed",), ("zoom",)],
    "width-height": [("auto",), ("extend-to-zoom",)] + t.length + t.percentage,
    "zoom": [("auto",)] + t.number + t.percentage,
}

allow_word_completions = frozenset(
    (
        "additive-symbols",
        "fallback",
        "font-family",
        "name",
        "negative",
        "pad",
        "prefix",
        "speak-as",
        "suffix",
        "symbols",
        "system",
    )
)

# descriptor_to_values maps @-rules to the completions for their descriptors'
# values.
descriptor_to_values = {
    "color-profile": color_profile_values,
    "counter-style": counter_style_values,
    "font-face": font_face_values,
    "viewport": viewport_values,
}


def get_values(descriptor_type, descriptor_name):
    # There is a separate completions dictionary for every @-rule.
    completions_dict = descriptor_to_values.get(descriptor_type, {})
    completions = completions_dict.get(descriptor_name, []) + [t.var]

    if descriptor_name in allow_word_completions:
        return completions

    return completions, sublime.INHIBIT_WORD_COMPLETIONS


def sort_and_uniq_completions():
    completions_dicts = (
        color_profile_values,
        counter_style_values,
        font_face_values,
        viewport_values,
    )

    for completions_dict in completions_dicts:
        for name in completions_dict:
            completions_dict[name] = list(set(completions_dict[name]))
            completions_dict[name].sort()


sort_and_uniq_completions()
