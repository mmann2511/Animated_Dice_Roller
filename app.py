from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/roll")
def roll_api():
    expr = request.args.get("expr")
    print("EXPR RECEIVED:", repr(expr))

    if expr is None:
        return {"error": "Missing dice expression"}
    
    try:
        return roll_expression(expr)
    except (ValueError, IndexError):
        return {"error": "Invalid dice expression"}


def roll_die(sides):
    return random.randint(1, sides)

def roll_dice(n, sides):
    rolls = []
    for _ in range(n):
        roll = roll_die(sides)
        rolls.append(roll)
    return rolls  

def sum_rolls(rolls):
    total = 0
    for num in rolls:
        total += num

    return total  

def parse_simple(expr):
    parts = expr.lower().split('d')

    count = parts[0]
    if count == '':
        count = 1

    sides  = parts[1]

    return int(count), int(sides)    

def parse_with_modifier(expr):
    parts = expr.lower().split('d')

    count = parts[0]
    if count == '':
        count = 1

    sides = parts[1]

    if '+' not in sides and '-' not in sides:
        modifier = 0
    elif '+' in sides:
        sides_modifier = sides.split("+")
        sides = sides_modifier[0] 
        modifier = sides_modifier[1]
    elif '-' in sides:
        sides_modifier = sides.split("-")
        sides = sides_modifier[0]
        modifier = sides_modifier[1]
        modifier = int(modifier) * -1    
        

    return int(count), int(sides), int(modifier)  


def roll_expression(expr):
    count, sides, modifier = parse_with_modifier(expr)

    dice_roll = roll_dice(count, sides)
    total = sum_rolls(dice_roll) + modifier 

    roll_dict = {'rolls': dice_roll, 'modifier': modifier, 'total': total}

    return roll_dict








if __name__ == "__main__":
    # Test Code
    for _ in range(5):
        print(roll_die(20))

    for _ in range(3):
        print(roll_dice(4, 10))

    print(sum_rolls([2, 5, 1]))  

    print(parse_simple('d20'))  
    print(parse_simple('2d6'))  
    print(parse_simple('10d100'))     
    print(parse_with_modifier("d20+1"))
    print(parse_with_modifier("5d10-1"))
    print(parse_with_modifier("2d6"))

    result = roll_expression("1d1+5")
    print(result)



        


    app.run(debug=True)


