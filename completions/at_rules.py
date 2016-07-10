from CSS3.completions import descriptors
from CSS3.completions import util
import sublime

# @-rules that can appear inside other @-rules.
nestable_at_rules = [
    ("@counter-style", "@counter-style ${1:name} {\n\t${2}\n}"),
    ("@font-face", "@font-face {\n\t${1}\n}"),
    ("@font-feature-values", "@font-feature-values ${1:font-family} {\n\t${2}\n}"),
    ("@keyframes", "@keyframes ${1:name} {\n\t${2}\n}"),
    ("@media", "@media ${1:media-query-list} {\n\t${2}\n}"),
    ("@page", "@page ${1} {\n\t${2}\n}"),
    ("@viewport", "@viewport ${1} {\n\t${2}\n}"),
    ("@supports", "@supports ${1} {\n\t${2}\n}"),
]

# @-rules that can appear at the top-level.
at_rules = [
    ("@charset", '@charset "UTF-8";'),
    ("@color-profile", "@color-profile {\n\t${2}\n}"),
    ("@custom-media", "@custom-media --${1:name} ${2:media-query-list};"),
    ("@import", "@import ${1:path} ${2:media-query-list};"),
    ("@namespace", "@namespace ${1};"),
] + nestable_at_rules

at_rules.sort()

at_page_selectors = [
    (":blank",),
    (":first",),
    (":left",),
    (":recto",),
    (":right",),
    (":verso",),
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


def get_completions(view, location):
    current_scopes = util.get_current_scopes(view, location)

    if should_offer_at_rule_completions(view, location):
        return nestable_at_rules, sublime.INHIBIT_WORD_COMPLETIONS

    if view.match_selector(location, "meta.at-rule.keyframes.block.css -meta.keyframes-declaration-list.css"):
        # @keyframes selector
        return keyframes_selector, sublime.INHIBIT_WORD_COMPLETIONS

    if view.match_selector(location, "meta.at-rule.font-face.block.css"):
        # @font-face
        if view.match_selector(location, "source.css -meta.descriptor.font-face"):
            return descriptors.font_face_descriptors, sublime.INHIBIT_WORD_COMPLETIONS
        return descriptors.get_values(current_scopes, descriptors_for="font-face")

    if view.match_selector(location, "meta.at-rule.font-feature-values.block.css"):
        # @font-feature-values
        if view.match_selector(location, "-meta.font-feature-type-block.css"):
            return font_feature_types, sublime.INHIBIT_WORD_COMPLETIONS
        return []

    if view.match_selector(location, "meta.at-rule.viewport.block.css"):
        # @viewport
        if view.match_selector(location, "source.css -meta.descriptor.viewport"):
            return descriptors.viewport_descriptors, sublime.INHIBIT_WORD_COMPLETIONS
        return descriptors.get_values(current_scopes, descriptors_for="viewport")

    if view.match_selector(location, "meta.at-rule.page.block.css -meta.page-margin-box.css"):
        # @top-right, etc.
        return page_margin_boxes, sublime.INHIBIT_WORD_COMPLETIONS

    if view.match_selector(location, "meta.at-rule.page.css -meta.at-rule.page.block.css"):
        # @page :left, etc.
        return at_page_selectors

    if view.match_selector(location, "meta.at-rule.charset.css"):
        # @charset
        return [('"UTF-8";',)], sublime.INHIBIT_WORD_COMPLETIONS

    if view.match_selector(location, "meta.at-rule.counter-style.block.css"):
        # @counter-style
        if view.match_selector(location, "-meta.descriptor.counter-style"):
            return descriptors.counter_style_descriptors, sublime.INHIBIT_WORD_COMPLETIONS
        return descriptors.get_values(current_scopes, descriptors_for="counter-style")

    if view.match_selector(location, "meta.at-rule.color-profile.block.css"):
        if view.match_selector(location, "-meta.descriptor.color-profile"):
            return descriptors.color_profile_descriptors, sublime.INHIBIT_WORD_COMPLETIONS

        return descriptors.get_values(current_scopes, descriptors_for="color-profile")


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


def should_offer_at_rule_completions(view, location):
    """Return True if the given location should offer @-rules as completions.

    @media and @supports can have @-rules nested inside them.

    Example:
        @media screen {
            @media (min-width: 480px) {
                ...
            }
        }

    For the other @-rules, however, nested @-rules don't make sense.

    Example:
        @media screen {
            @keyframes {
                @media???
            }
        }

    Args:
        view (sublime.View):
        location (int): the integer position of the

    This function returns True if we're in an @media or @supports scope, but NOT
    in any other scope.
    """
    if not view.match_selector(location, "meta.at-rule.media.block.css, meta.at-rule.supports.block.css"):
        return False

    return not view.match_selector(location, scopes_that_forbid_nested_at_rules)
