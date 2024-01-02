# PythonTermColor | Color






#Global Variables
Colors = {
    'red' : (200, 0, 0),
    'green' : (0, 200, 0),
    'blue': (0, 0, 200),
    'purple': (200, 0, 200),
    'yellow' : (200, 200, 0),
    'orange' : (200, 100, 0),

    'brightred' : (255, 0, 0),
    'brightgreen' : (0, 255, 0),
    'brightblue': (0, 0, 255),
    'brightpurple': (255, 0, 255),
    'brightyellow' : (255, 255, 0),
    'brightorange' : (255, 175, 0),

    'lightred' : (200, 100, 100),
    'lightgreen' : (100, 200, 100),
    'lightblue': (100, 100, 200),
    'lightpurple': (200, 100, 200),
    'lightyellow' : (200, 200, 100),
    'lightorange' : (200, 150, 100),

    'darkred' : (100, 0, 0),
    'darkgreen' : (0, 100, 0),
    'darkblue': (0, 0, 100),
    'darkpurple': (100, 0, 100),
    'darkyellow' : (100, 100, 0),
    'darkorange' : (100, 50, 0),
}

Decorations = {
    'bold' : '\x1b[1m',
    'underline' : '\x1b[4m',
    'inverted' : '\x1b[7m'
}






#Private Functions
def __isValidRGB(rgb: tuple) -> bool:
    if type(rgb) != tuple: raise ValueError('Argument rgb must be a tuple.')
    if len(rgb) < 3: raise ValueError('Argument rgb must contain all rgb values.')
    if len(rgb) > 3: raise ValueError('Argument rgb contains too many values to be a valid rgb value.')
    if any([True for i in rgb if not type(i) is int]): return False
    if any([True for i in rgb if i < 0 or i > 255]): return False
    return True



def __createColor(rgb: tuple) -> str:
    red = str(rgb[0])
    green = str(rgb[1])
    blue = str(rgb[2])

    return red + ';' + green + ';' + blue + 'm'






#Public Functions
def showColorList() -> None:
    '''
    Prints off list of valid arguments for color.
    '''
    global Colors
    for color in Colors: print(color)



def showDecorationList() -> None:
    '''
    Prints off list of valid arguments for decoration.
    '''
    global Decorations
    for decoration in Decorations: print(decoration)



def printRGBColor(text: str, rgb: tuple, decorations: list | str = [], end: str = '\n') -> None:
    '''
    Prints text in color from a given rgb format.\n
    text: str
     Text to print off.
    rgb: tuple
     Tuple of rgb values to make text.
    decorations: list | str
     List or string of decoration values to add to the text.
    end: str
     How the printed text should end.
    '''
    
    global Decorations

    if type(decorations) == str: decorations = [decorations]
    if not __isValidRGB(rgb): raise ValueError('Argument rgb contains an illegal value, all values must be between 0-255.')
    if any([True for i in decorations if i not in Decorations]): raise ValueError('Argument decorations must contain valid decoration types from given list of Decorations.')
    
    color = __createColor(rgb)
    decorations = ''.join([Decorations[decoration] for decoration in decorations])

    print(decorations + '\x1b[38;2;' + color, end = '')
    print(text, end = '')
    print('\x1b[0m', end = end)



def printColor(text: str, color: str, decorations: list | str = [], end: str = '\n') -> None:
    '''
    Prints text in color from a given color.\n
    text: str
     Text to print off.
    color: str
     String of the color to make text.
    decorations: list | str
     List or string of decoration values to add to the text.
    end: str
     How the printed text should end.
    '''
    global Colors
    global Decorations

    if type(decorations) == str: decorations = [decorations]
    if color not in Colors: raise ValueError('Argument color must be a valid color from given list of Colors.')
    if any([True for i in decorations if i not in Decorations]): raise ValueError('Argument decorations must contain valid decoration types from given list of Decorations.')

    color = Colors[color]

    printRGBColor(text, color, decorations, end)