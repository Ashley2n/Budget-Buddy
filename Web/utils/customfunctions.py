
def format_price(value):
    return f"${value:+,.2f}"

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False