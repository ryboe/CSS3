# FUNCTIONS

attr         = ("attr()", "attr(${1:name})")
calc         = ("calc()", "calc(${1})")
content      = ("content()", "content(${1})")
counter      = ("counter()", "counter(${1:<ident>}${2:, ${3:<list-style-type>}})")
counters     = ("counters()", "counters(${1:<ident>}, \"${2:<string>}\"${3:, ${4:<list-style-type>}})")
cross_fade   = ("cross-fade()", "cross-fade(${1})")
cubic_bezier = ("cubic-bezier()", "cubic-bezier(${1:0}, ${2:0}, ${3:0}, ${4:0})")
element      = ("element()", "element(#${1})")
filter_func  = ("filter()", "filter(${1})")
hsl          = ("hsl()", "hsl(${1:0}, ${2:0}%, ${3:0}%)")
hsla         = ("hsla()", "hsla(${1:0}, ${2:0}%, ${3:0}%, ${4:0.0})")
image_func   = ("image()", "image(${1})")
image_set    = ("image-set()", "image-set(${1})")
matrix       = ("matrix()", "matrix(${1:0}, ${2:0}, ${3:0}, ${4:0}, ${5:0}, ${6:0})")
matrix3d     = ("matrix3d()", "matrix3d(${1:0}, ${2:0}, ${3:0}, ${4:0}, ${5:0}, ${6:0}, ${7:0}, ${8:0}, ${9:0}, ${10:0}, ${11:0}, ${12:0}, ${13:0}, ${14:0}, ${15:0}, ${16:0})")
minmax       = ("minmax()", "minmax(${1:<track-breadth>}, ${2:<track-breadth>})")
perspective  = ("perspective()", "perspective(${1:<length>})")
repeat       = ("repeat()", "repeat(${1})")
rgb          = ("rgb()", "rgb(${1:0}, ${2:0}, ${3:0})")
rgba         = ("rgba()", "rgba(${1:0}, ${2:0}, ${3:0}, ${4:0.0})")
rotate       = ("rotate()", "rotate(${1:<angle>})")
rotate3d     = ("rotate3d()", "rotate3d(${1:0}, ${2:0}, ${3:0}, ${4:<angle>})")
rotateX      = ("rotateX()", "rotateX(${1:<angle>})")
rotateY      = ("rotateY()", "rotateY(${1:<angle>})")
rotateZ      = ("rotateZ()", "rotateZ(${1:<angle>})")
scale        = ("scale()", "scale(${1:0}${2:, ${3:0}})")
scale3d      = ("scale3d()", "scale3d(${1:0}, ${2:0}, ${3:0})")
scaleX       = ("scaleX()", "scaleX(${1:0})")
scaleY       = ("scaleY()", "scaleY(${1:0})")
scaleZ       = ("scaleZ()", "scaleZ(${1:0})")
skew         = ("skew()", "skew(${1:<angle>}${2:, ${3:<angle>}})")
skewX        = ("skewX()", "skewX(${1:<angle>})")
skewY        = ("skewY()", "skewY(${1:<angle>})")
steps        = ("steps()", "steps(${1})")
subgrid      = ("subgrid", "subgrid ${1:<line-name-list>}")
toggle       = ("toggle()", "toggle(${1})")
translate    = ("translate()", "translate(${1:<length>}${2:, ${3:<length>}})")
translate3d  = ("translate3d()", "translate3d(${1:<length>}, ${2:<length>}, ${3:<length>})")
translateX   = ("translateX()", "translateX(${1:<length>})")
translateY   = ("translateY()", "translateY(${1:<length>})")
translateZ   = ("translateZ()", "translateX(${1:<length>})")
url          = ("url()", "url(${1})")
var          = ("var()", "var(--${1:name}, ${2:value})")
conic_gradient  = ("conic-gradient()", "conic-gradient(${1})")
linear_gradient = ("linear-gradient()", "linear-gradient(${1})")
radial_gradient = ("radial-gradient()", "radial-gradient(${1})")
repeating_conic_gradient  = ("repeating-conic-gradient()", "repeating-conic-gradient(${1})")
repeating_linear_gradient = ("repeating-linear-gradient()", "repeating-linear-gradient(${1})")
repeating_radial_gradient = ("repeating-radial-gradient()", "repeating-radial-gradient(${1})")


# TYPES

decibel    = ("<decibel>", "${1:0}dB")
flex       = ("<flex>", "${1:0}fr")
ident      = ("<ident>", "${1:<ident>}")
image      = [conic_gradient, cross_fade, element, filter_func, image_func, image_set, linear_gradient, radial_gradient, repeating_conic_gradient, repeating_linear_gradient, repeating_radial_gradient, url]
integer    = ("<integer>", "${1:<integer>}")
length     = ("<length>", "${1:<length>}")
number     = ("<number>", "${1:<number>}")
percentage = ("<percentage>", "${1:0}%")
position   = [("bottom",), ("center",), ("left",), ("right",), ("top",), calc, length, percentage]
string     = ("<string>", "\"${1}\"")
time       = ("<time>", "${1:<time>}")
transform  = [matrix, matrix3d, perspective, rotate, rotate3d, rotateX, rotateY, rotateZ, scale, scale3d, scaleX, scaleY, scaleZ, skew, skewX, skewY, translate, translate3d, translateX, translateY, translateZ]
single_transition_timing_function = [("ease",), ("ease-in",), ("ease-in-out",), ("ease-out",), ("linear",), ("step-end",), ("step-start",), cubic_bezier, steps]


# COMMON VALUES

all_values = [("inherit",), ("initial",), ("unset",), attr, toggle, var]
