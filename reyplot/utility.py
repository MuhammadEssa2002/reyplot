def __hex_to_rgb_rey__(color):
    """Convert a hex string or color name to an (r, g, b) tuple normalized to 0-1."""

    # ---- Color name dictionary ----
    COLOR_NAMES = {
        "red": "#ff0000",
        "green": "#00ff00",
        "blue": "#0000ff",
        "white": "#ffffff",
        "black": "#000000",
        "gray": "#808080",
        "grey": "#808080",
        "orange": "#ffa500",
        "yellow": "#ffff00",
        "purple": "#800080",
        "cyan": "#00ffff",
        "magenta": "#ff00ff",

        # Extra beautiful colors (ReyPlot style)
        "sky": "#87ceeb",
        "skyblue": "#87ceeb",
        "teal": "#008080",
        "maroon": "#800000",
        "navy": "#000080",
    }

    # If user gave a color name
    if isinstance(color, str):
        lower = color.lower().strip()

        if lower in COLOR_NAMES:
            color = COLOR_NAMES[lower]

    # Now convert from hex to RGB
    try:
        hex_code = color.lstrip('#')
        length = len(hex_code)

        # Support 3-digit hex (e.g., #f00)
        if length == 3:
            hex_code = ''.join([c * 2 for c in hex_code])
            length = 6

        return tuple(
            int(hex_code[i:i + 2], 16) / 255.0
            for i in range(0, length, 2)
        )

    except Exception:
        # Default to black if invalid
        return (0, 0, 0)

class scatter_color_select:
    def __init__(self):
        self.COLOR_NAMES = {
    1: "#800000", # maroon
    2: "#ffa500",  # orange
    3: "#0000ff",  # blue
    4: "#000000",  # black
    5: "#808080",  # gray
    6: "#00ff00",  # green
    7: "#00ffff", # cyan
    8: "#008080", # teal
    9: "#ffff00",  # yellow
    10: "#800080", # purple
    }
        self.count = 0
    
    def give_color(self):
        if (self.count > 9):
            self.count = 0
        self.count = self.count + 1
        return self.COLOR_NAMES[self.count]
