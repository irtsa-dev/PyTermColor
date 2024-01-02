A [**python**](https://www.python.org) collection of functions to print of colored text to console / terminal.
<br />
<br />
​<br />
## Installation
With `git` [GitHub](https://github.com/IrtsaDevelopment/PyColor):
```
git clone https://github.com/IrtsaDevelopment/PyTermColor.git
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
from PyTermColor import *
```
<br />

Then, later on you may utilize:
```py
printColor(text: str, color: str, decorations: list | str = [], end: str = '\n')
# Prints off text in the given color with provided decorations.

printRGBColor(text: str, rgb: tuple, decorations: list | str = [], end: str = '\n')
# Prints off text in the given rgb value with provided decorations.


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
from PyTermColor import *

printColor('hello', 'red')
```
```py
from PyTermColor import *

printColorRGB('hello', (100, 200, 50))
```
```py
from PyTermnColor import *

printColor('hello', 'red', 'bold')
printColor('hello there', 'red', ['bold', 'underline'])
```
