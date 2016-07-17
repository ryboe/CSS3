
font_feature_types = [
    ("@annotation", "@annotation {\n\t${1}\n}"),
    ("@character-variant", "@character-variant {\n\t${1}\n}"),
    ("@ornaments", "@ornaments {\n\t${1}\n}"),
    ("@styleset", "@styleset {\n\t${1}\n}"),
    ("@stylistic", "@stylistic {\n\t${1}\n}"),
    ("@swash", "@swash {\n\t${1}\n}"),
]
nestable = [
    # @-rules that can appear inside other @-rules.
    ("@counter-style", "@counter-style ${1:name} {\n\t${2}\n}"),
    ("@font-face", "@font-face {\n\t${1}\n}"),
    ("@font-feature-values", "@font-feature-values ${1:font-family} {\n\t${2}\n}"),
    ("@keyframes", "@keyframes ${1:name} {\n\t${2}\n}"),
    ("@media", "@media ${1:media-query-list} {\n\t${2}\n}"),
    ("@page", "@page ${1} {\n\t${2}\n}"),
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
    ("@color-profile", "@color-profile {\n\t${2}\n}"),
    ("@custom-media", "@custom-media --${1:name} ${2:media-query-list};"),
    ("@import", "@import ${1:path} ${2:media-query-list};"),
    ("@namespace", "@namespace ${1};"),
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


# TODO: delete this
# def get_completions(view, location):
#     current_scopes = util.get_scopes(location)

#     # @keyframes selector
#     if view.match_selector(location, "meta.at-rule.keyframes.block.css -meta.keyframes-declaration-list.css"):
#         return selectors.keyframes, sublime.INHIBIT_WORD_COMPLETIONS

#     # @keyframes properties and values
#     if view.match_selector(location, "meta.keyframes-declaration-list.css"):
#         if view.match_selector(location, "source.css -meta.property-value."):
#             return properties.names, sublime.INHIBIT_WORD_COMPLETIONS
#         return properties.get_values(current_scopes)

#     # @font-face
#     if view.match_selector(location, "meta.at-rule.font-face.block.css"):
#         if view.match_selector(location, "source.css -meta.descriptor.font-face."):
#             return descriptors.font_face, sublime.INHIBIT_WORD_COMPLETIONS
#         return descriptors.get_values(current_scopes, descriptors_for="font-face")

#     # @font-feature-values
#     if view.match_selector(location, "meta.at-rule.font-feature-values.block.css"):
#         if view.match_selector(location, "-meta.font-feature-type-block.css"):
#             return font_feature_types, sublime.INHIBIT_WORD_COMPLETIONS
#         return []

#     # @viewport
#     if view.match_selector(location, "meta.at-rule.viewport.block.css"):
#         if view.match_selector(location, "source.css -meta.descriptor.viewport"):
#             return descriptors.viewport, sublime.INHIBIT_WORD_COMPLETIONS
#         return descriptors.get_values(current_scopes, descriptors_for="viewport")

#     # @top-right, etc.
#     if view.match_selector(location, "meta.at-rule.page.block.css -meta.page-margin-box.css"):
#         return page_margin_boxes, sublime.INHIBIT_WORD_COMPLETIONS

#     # @page :left, etc.
#     if view.match_selector(location, "meta.at-rule.page.css -meta.at-rule.page.block.css"):
#         return selectors.at_page

#     # @charset
#     if view.match_selector(location, "meta.at-rule.charset.css"):
#         return [('"UTF-8";',)], sublime.INHIBIT_WORD_COMPLETIONS

#     # @counter-style
#     if view.match_selector(location, "meta.at-rule.counter-style.block.css"):
#         if view.match_selector(location, "-meta.descriptor.counter-style"):
#             return descriptors.counter_style, sublime.INHIBIT_WORD_COMPLETIONS
#         return descriptors.get_values(current_scopes, descriptors_for="counter-style")

#     # @color-profile
#     if view.match_selector(location, "meta.at-rule.color-profile.block.css"):
#         if view.match_selector(location, "-meta.descriptor.color-profile"):
#             return descriptors.color_profile, sublime.INHIBIT_WORD_COMPLETIONS
#         return descriptors.get_values(current_scopes, descriptors_for="color-profile")
