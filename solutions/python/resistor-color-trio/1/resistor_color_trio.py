color_values = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}
def label(colors):
    first_two = colors[:2]
    digits = [str(color_values[color]) for color in first_two]
    value = int("".join(digits))
    multiplier_color = colors[2]
    multiplier = 10**color_values[multiplier_color]
    resistance = value*multiplier
    if resistance >= 1000000000:
        return f"{resistance // 1000000000} gigaohms"
    elif resistance >= 1000000:
        return f"{resistance // 1000000} megaohms"
    elif resistance >= 1000:
        return f"{resistance // 1000} kiloohms"
    else:
        return f"{resistance} ohms"
