# interested in being able to execute in terminal like
# bpytop, neofetch, or asciiquarium instead of python marco_calc.py
# could be something to look into 
import json
from json.decoder import JSONDecodeError


def calc():
    print( "X/" * 11, "CALCULATION", "\\X" * 11 )
    
    print("CHOOSE MEAL FROM LIST BELOW")
    try:
        with open("meals.json", "r") as infile:
            json_object = json.load(infile)
            for i in json_object:
                print(i)
    except FileNotFoundError:
        print(">>No meals returning to menu<<")
        return
    except JSONDecodeError:
        print(">>No meals return to menu")

    print("ENTER to return to menu")
    user_input = input("Enter meal name: ")
    if user_input == "": return

    # get measured serving size weight
    serving_size = float(input("Enter serving size: "))
    
    # multipler
    mult = serving_size / json_object[user_input]["serving size"]
    
    # printing output
    print("#"*5, "AMOUNT IN SERVING", "#"*5)
    # multiplies the the value by the multiplier to know how much of each
    # nutrition is the meal being consumed
    for index, item in enumerate(json_object[user_input]):
        # skips serving size of meal
        if index == 0: continue
        x = json_object[user_input][item] * mult
        print( "{:15s} {:10s} {:10s}".format( f"## {item}", f"{round(x, 1)}", "##" ) )
    
    print("#"*29)
    print("X\\"*14, "/X"*14, "\n")


def add_meal():
    print( "++" * 10, "NEW MEAL", "++" * 10 )
    meal = {}
    
    print("ENTER to return to menu")

    # was thinking of putting the inputs in the dictionary but thought
    # that would look really messy to look at 
    meal_name = input("Enter name of meal: ")
    if meal_name == "": return

    serving = float(input("Enter serving size: "))

    calories = float(input("Calories: "))
    fats = float(input("Fats: "))
    carbs = float(input("Carbs: "))
    protein = float(input("Protein: "))
    
    # adds nutrition to dictionary
    meal[meal_name.lower()] = {
        "serving size": serving,
        "calories": calories,
        "fats": fats,
        "carbs": carbs,
        "protein": protein
    }
    
    # loops again if there is an error such as no file or empty file
    # breaks after writing into json file
    while True:
        try:
            with open("meals.json", "r") as infile: 
                json_object = json.load(infile)
                json_object.update(meal)
            
            with open("meals.json", "w") as outfile:
                json.dump(json_object, outfile, indent=4)
                outfile.close()
                infile.close()
            break

        except FileNotFoundError:
            # print("file no existo, creato filo")
            with open("meals.json", "x") as file:
                # print(f"created file: {file.name}")
                file.close()
        except JSONDecodeError:
            # print("File empty, baka :)")
            with open("meals.json", "w+") as outfile:
                json.dump({}, outfile, indent=4)
                outfile.close()

    #print(json.dumps(meal, indent=4))
    print("+"*50, "\n")

# remove meals from json file
# if there isnt anything return back to menu
def remove_meal():
    print( "--" * 10, "MEAL REMOVAL", "--" * 10 )
    try:
        with open("meals.json", "r") as infile:
            json_object = json.load(infile)
            if len(json_object) != 0:
                for i in json_object:
                    print(i)
            else:
                print(">>Nothing to remove returning to menu<<")
                return
    except FileNotFoundError:
        print(">>No Meals returning to menu<<")
        return
    
    # loops if meal doesnt exist 
    print("ENTER to return to menu")
    while True:
        try:
            user_input = input("Enter meal name here: ")
            if user_input == "": return
            
            json_object.pop(user_input.lower())

            break
        except KeyError:
            print(f"No meal called {user_input}")


    with open("meals.json", "w") as outfile:
        json.dump(json_object, outfile, indent=4)
    infile.close()
    outfile.close()

    print("-"*54)

def main():
    user_input = 0
    #this might be remove as selection can be done in calc()
    current_meal = "nada"
    while user_input != 4:
        print("=+" * 10, "MENU", "=+" * 10)
        print("1) calculate")
        print("2) add meal")
        print("3) remove meal")
        print("4) quit")
        print("=+"*23)

        user_input = int(input("Enter Choice here: "))
        if user_input == 1:
            calc()
        if user_input == 2:
            add_meal()
        if user_input == 3:
            remove_meal()

main()
