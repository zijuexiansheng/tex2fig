# tex2fig

Convert .tex to figures in pdf format. The purpose is to keep all the figures as vector pictures.

# Dependencies

* python
* LaTeX (with luatex85)

# Install

* `brew install zijuexiansheng/filbat/tex2fig`
* or, `./install.sh`

# Usage

See `tex2fig -h`

# More words

The following packages have been loaded. For more packages, you can add them into your .tex file:

* `graphicx`
* `subcaption`
* `tikz`
    * `\usetikzlibrary{graphdrawing, graphs, arrows, decorations.pathreplacing}`
    * `\usegdlibrary{layered, trees}`

Don't use any suffix if you are inserting a picture. It is recommended to convert the picture into pdf.
