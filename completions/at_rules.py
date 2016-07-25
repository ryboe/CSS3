from CSS3.completions import types as t

font_feature_types = [
    ("@annotation", "@annotation {\n\t$1\n}\n"),
    ("@character-variant", "@character-variant {\n\t$1\n}\n"),
    ("@ornaments", "@ornaments {\n\t$1\n}\n"),
    ("@styleset", "@styleset {\n\t$1\n}\n"),
    ("@stylistic", "@stylistic {\n\t$1\n}\n"),
    ("@swash", "@swash {\n\t$1\n}\n"),
]
namespace_values = [t.identifier, t.string, t.url]
nestable = [
    # @-rules that can appear inside other @-rules.
    ("@counter-style", "@counter-style ${1:name} {\n\t$2\n}\n"),
    ("@font-face", "@font-face {\n\t$1\n}\n"),
    ("@font-feature-values", "@font-feature-values ${1:font-family} {\n\t$2\n}\n"),
    ("@keyframes", "@keyframes ${1:name} {\n\t$2\n}\n"),
    ("@media", "@media ${1:media-query-list} {\n\t$2\n}\n"),
    ("@page", "@page $1{\n\t$2\n}\n"),
    ("@viewport", "@viewport {\n\t$1\n}\n"),
    ("@supports", "@supports $1 {\n\t$2\n}\n"),
]
page_margin_boxes = [
    ("@bottom-center", "@bottom-center {\n\t$1\n}\n"),
    ("@bottom-left", "@bottom-left {\n\t$1\n}\n"),
    ("@bottom-left-corner", "@bottom-left-corner {\n\t$1\n}\n"),
    ("@bottom-right", "@bottom-right {\n\t$1\n}\n"),
    ("@bottom-right-corner", "@bottom-right-corner {\n\t$1\n}\n"),
    ("@left-bottom", "@left-bottom {\n\t$1\n}\n"),
    ("@left-middle", "@left-middle {\n\t$1\n}\n"),
    ("@left-top", "@left-top {\n\t$1\n}\n"),
    ("@right-bottom", "@right-bottom {\n\t$1\n}\n"),
    ("@right-middle", "@right-middle {\n\t$1\n}\n"),
    ("@right-top", "@right-top {\n\t$1\n}\n"),
    ("@top-center", "@top-center {\n\t$1\n}\n"),
    ("@top-left", "@top-left {\n\t$1\n}\n"),
    ("@top-left-corner", "@top-left-corner {\n\t$1\n}\n"),
    ("@top-right", "@top-right {\n\t$1\n}\n"),
    ("@top-right-corner", "@top-right-corner {\n\t$1\n}\n"),
]
all_rules = [
    # @-rules that can appear at the top level only.
    ("@charset", "@charset 'UTF-8';\n"),
    ("@color-profile", "@color-profile {\n\t$2\n}\n"),
    ("@custom-media", "@custom-media --${1:name} ${2:media-query-list};\n"),
    ("@import", "@import ${1:path} ${2:media-query-list};\n"),
    ("@namespace", "@namespace $1;\n"),
] + nestable

all_rules.sort()

scopes_that_forbid_nested_at_rules = (
    "meta.property-list.css, "
    "meta.at-rule.font-face.block.css, "
    "meta.at-rule.keyframes.block.css, "
    "meta.at-rule.font-feature-values.block.css, "
    "meta.at-rule.viewport.block.css, "
    "meta.at-rule.color-profile.block.css, "
    "meta.at-rule.counter-style.block.css, "
    "meta.at-rule.page.block.css"
)


def supports_nested(view, location):
    """Returns True if location is in @media or @supports, but NOT any other
    scope.

    @media and @supports can have @-rules nested inside.
    """
    if not view.match_selector(location, "meta.at-rule.media.block.css, meta.at-rule.supports.block.css"):
        return False

    return not view.match_selector(location, scopes_that_forbid_nested_at_rules)
