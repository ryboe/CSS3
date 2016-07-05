# @-rules that can appear inside other @-rules.
nestable_at_rules = [
    ("@counter-style", "@counter-style ${1:name} {\n\t${2}\n}"),
    ("@font-face", "@font-face {\n\t${1}\n}"),
    ("@font-feature-values", "@font-feature-values ${1:font-family} {\n\t${2}\n}"),
    ("@keyframes", "@keyframes ${1:name} {\n\t${2}\n}"),
    ("@media", "@media ${1:media-query-list} {\n\t${2}\n}"),
    ("@page", "@page ${1} {\n\t${2}\n}"),
    ("@viewport", "@viewport ${1} {\n\t${2}\n}"),
]

at_rules = [
    ("@charset", '@charset "UTF-8";'),
    ("@color-profile", "@color-profile {\n\t${2}\n}"),
    ("@custom-media", "@custom-media --${1:name} ${2:media-query-list};"),
    ("@import", "@import ${1:path} ${2:media-query-list};"),
    ("@namespace", "@namespace ${1};"),
    ("@supports", "@supports ${1} {\n\t${2}\n}"),
] + nestable_at_rules

at_page_selectors = [
    (":blank",),
    (":first",),
    (":left",),
    (":recto",),
    (":right",),
    (":verso",),
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

font_feature_types = [
    ("@annotation", "@annotation {\n\t${1}\n}"),
    ("@character-variant", "@character-variant {\n\t${1}\n}"),
    ("@ornaments", "@ornaments {\n\t${1}\n}"),
    ("@styleset", "@styleset {\n\t${1}\n}"),
    ("@stylistic", "@stylistic {\n\t${1}\n}"),
    ("@swash", "@swash {\n\t${1}\n}"),
]

keyframes_selector = [
    ("from", "from {\n\t${1}\n}"),
    ("to", "to {\n\t${1}\n}"),
]

at_rules.sort()
