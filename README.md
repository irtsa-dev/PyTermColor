![PyPI](https://img.shields.io/pypi/v/idev-pytermcolor) ![Python](https://img.shields.io/pypi/pyversions/idev-pytermcolor)
# **PyTermColor**
A [**python**](https://www.python.org) collection of functions to print of colored text to console / terminal.
<br />
<br />
​<br />
## Installation
With `git` [GitHub](https://github.com/IrtsaDevelopment/PyColor):
```
git clone https://github.com/irtsa-dev/PyTermColor.git
```
With `pip` [PyPi](https://pypi.org/project/idev-pytermcolor)
```
pip install idev-pytermcolor
```
<br />
<br />
<br />
<br />
<br />
<br />

## Usage
To import:
```py
from PyTermColor.Color import *
```
<br />

Then, later on you may utilize:
```py
printColor(text: str, textColor: str, backgroundColor: str = None, decorations: list | str = [], end: str = '\n')
# Prints off text and background in the given color with provided decorations.

printRGBColor(text: str, textRGB: tuple, backgroundRGB: tuple = (), decorations: list | str = [], end: str = '\n')
# Prints off text and background in the given rgb value with provided decorations.


showColorList()
# Prints off a list of valid arguments for color.

showDecorationList()
# Prints off a list of valid arguments for decoration.
```
​
<br />
<br />
### Code Examples
```py
from PyTermColor.Color import *

printColor('hello', 'red')
```
```py
from PyTermColor.Color import *

printColorRGB('hello', (100, 200, 50))
```
```py
from PyTermnColor.Color import *

printColor('hello', 'red', decorations = 'bold')
printColor('hello there', 'red', decorations = ['bold', 'underline'])
```
