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
tolerance_values = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10
}
def resistor_label(colors):
    if len(colors) == 1:
        return f"{color_values[colors[0]]} ohms"
    if len(colors) == 4:
        first_two = colors[:2]
        digits = [str(color_values[color])for color in first_two]
        value = int("".join(digits))
        multiplier_color = colors[2]
        multiplier = 10**color_values[multiplier_color]
        tolerance_color = colors[3]
        tolerance = tolerance_values[tolerance_color]
    elif len(colors) == 5:
        first_three = colors[:3]
        digits = [str(color_values[color])for color in first_three]
        value = int("".join(digits))
        multiplier = 10 ** color_values[colors[3]]
        tolerance = tolerance_values[colors[4]]
    resistance = value * multiplier
        
    if resistance >= 1000000000:
        return f"{resistance/1000000000:g} gigaohms ±{tolerance}%"
    elif resistance >= 1000000:
        return f"{resistance/1000000:g} megaohms ±{tolerance}%"
    elif resistance >= 1000:
        return f"{resistance/1000:g} kiloohms ±{tolerance}%"
    else:
        return f"{resistance} ohms ±{tolerance}%"
        
