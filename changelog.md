# QoLaTeX Changelog and ToDo

## QoColours

### ToDo:

- [ ] Maybe move some stuff to a "core" package that can load the absolute minimum for other packages which use the basic colour names
    - [ ] Alternatively, add a new package option which will only load the bare minimum commands and default scheme.
- [ ] `rgb` to `hsl` conversion (and reverse) can definitely be done better.
    - [ ] Avoiding using `pgfmath` would be ideal, possibly doable by treating everything as lengths to avoid floating point arithmetic.
    - [ ] Using the [alternative method](https://en.wikipedia.org/wiki/HSL_and_HSV#HSL_to_RGB_alternative) for converting hsl to rgb would be much nicer

## QoListings

### ToDo:

- [ ] Styles don't actually work properly
- [ ] Listings should be able to take a language directly instead of via `lstoptions` - This is really annoying!

## QoBeamer

## QoMath

### ToDo:

#### Commands to add

- [ ] Derivative, <img src="https://render.githubusercontent.com/render/math?math=\frac{\text{d} x}{\text{d} y}"> should have a single command taking two arguments, and an optional argument for an order, e.g. `\deriv[2]{x}{y}` <img src="https://render.githubusercontent.com/render/math?math=\frac{\text{d}^2 x}{\text{d} y^2}">
<!-- the img above is a hacky way to get latex rendered in markdown on github. Some things would support MathJax, but it's a bit insecure so instead I'm sending the latex to a github api which returns the rendered equation as an svg image, which is then inserted  -->
- [ ] An equivalent command should exist for partial derivatives
- [ ] There should be an alternative for the second order with the ability to specify two different denominators, `\pdivp{x}{y}{z}` <img src="https://render.githubusercontent.com/render/math?math=\frac{\partial^2 x}{\partial y \partial z}">
