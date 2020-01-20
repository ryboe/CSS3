from CSS3.completions import types as t

font_feature_types = [
    ("@annotation", "@annotation {\n\t${1}\n}"),
    ("@character-variant", "@character-variant {\n\t${1}\n}"),
    ("@ornaments", "@ornaments {\n\t${1}\n}"),
    ("@styleset", "@styleset {\n\t${1}\n}"),
    ("@stylistic", "@stylistic {\n\t${1}\n}"),
    ("@swash", "@swash {\n\t${1}\n}"),
]
namespace_values = [t.identifier, t.string, t.url]
nestable = [
    # @-rules that can appear inside other @-rules.
    ("@counter-style", "@counter-style ${1:name} {\n\t${2}\n}"),
    ("@font-face", "@font-face {\n\t${1}\n}"),
    ("@font-feature-values", "@font-feature-values ${1:font-family} {\n\t${2}\n}"),
    ("@font-palette-values", "@font-palette-values ${1} {\n\t${2}\n}"),
    ("@keyframes", "@keyframes ${1:name} {\n\t${2}\n}"),
    ("@media", "@media ${1:media-query-list} {\n\t${2}\n}"),
    ("@page", "@page ${1}{\n\t${2}\n}"),
    ("@viewport", "@viewport {\n\t${1}\n}"),
    ("@supports", "@supports ${1} {\n\t${2}\n}"),
]
page_margin_boxes = [
    ("@bottom-center", "@bottom-center {\n\t${1}\n}"),
    ("@bottom-left", "@bottom-left {\n\t${1}\n}"),
    ("@bottom-left-corner", "@bottom-left-corner {\n\t${1}\n}"),
    ("@bottom-right", "@bottom-right {\n\t${1}\n}"),
    ("@bottom-right-corner", "@bottom-right-corner {\n\t${1}\n}"),
    ("@left-bottom", "@left-bottom {\n\t${1}\n}"),
    ("@left-middle", "@left-middle {\n\t${1}\n}"),
    ("@left-top", "@left-top {\n\t${1}\n}"),
    ("@right-bottom", "@right-bottom {\n\t${1}\n}"),
    ("@right-middle", "@right-middle {\n\t${1}\n}"),
    ("@right-top", "@right-top {\n\t${1}\n}"),
    ("@top-center", "@top-center {\n\t${1}\n}"),
    ("@top-left", "@top-left {\n\t${1}\n}"),
    ("@top-left-corner", "@top-left-corner {\n\t${1}\n}"),
    ("@top-right", "@top-right {\n\t${1}\n}"),
    ("@top-right-corner", "@top-right-corner {\n\t${1}\n}"),
]
all_rules = [
    # @-rules that can appear at the top level only.
    ("@charset", "@charset 'UTF-8';"),
    ("@color-profile", "@color-profile ${1} {\n\t${2}\n}"),
    ("@custom-media", "@custom-media --${1:name} ${2:media-query-list};"),
    ("@import", "@import ${1:path} ${2:media-query-list};"),
    ("@namespace", "@namespace ${1};"),
] + nestable

all_rules.sort()

scopes_that_forbid_nested_at_rules = (
    "meta.declaration-list.css, "
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
    if not view.match_selector(
        location, "meta.at-rule.media.block.css, meta.at-rule.supports.block.css"
    ):
        return False

    return not view.match_selector(location, scopes_that_forbid_nested_at_rules)
