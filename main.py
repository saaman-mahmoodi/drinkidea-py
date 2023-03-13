# Import the required modules
import time


# Define a function to ask the user a question and return their answer
def ask_question(question):
    while True:
        answer = input(question).strip().lower()
        if answer:
            return answer


# Define the decision tree for recommending a drink
def recommend_drink():
    # Ask the user if they want an alcoholic drink
    alcohol = ask_question("Do you want an alcoholic drink? (yes/no): ")
    if alcohol == "yes":
        # Ask the user what type of alcohol they prefer
        liquor = ask_question("Do you prefer beer, wine, or spirits? ").split()[0]
        if liquor == "beer":
            # Ask the user what type of beer they prefer
            beer_type = ask_question("Do you want a light or dark beer? ").split()[0]
            if beer_type == "light":
                brand = ask_question("Do you want a Corona or a Heineken? ").split()[0]
                return f"You should have a {brand} beer."
            else:
                brand = ask_question("Do you want a Guinness or a Stout? ").split()[0]
                return f"You should have a {brand} beer."
        elif liquor == "wine":
            # Ask the user what type of wine they prefer
            wine_type = ask_question("Do you want a red or white wine? ").split()[0]
            if wine_type == "red":
                brand = ask_question("Do you want a Merlot or a Cabernet Sauvignon? ").split()[0]
                return f"You should have a {brand} wine."
            else:
                brand = ask_question("Do you want a Chardonnay or a Sauvignon Blanc? ").split()[0]
                return f"You should have a {brand} wine."
        else:
            spirit_type = ask_question("Do you prefer vodka, rum, whiskey, gin, or tequila? ").split()[0]
            if spirit_type == "vodka":
                mixer = ask_question("Do you want a mixer with your vodka? (yes/no): ")
                if mixer == "yes":
                    return "You should have a vodka and cranberry juice."
                else:
                    return "You should have a shot of vodka."
            elif spirit_type == "rum":
                mixer = ask_question("Do you want a mixer with your rum? (yes/no): ")
                if mixer == "yes":
                    return "You should have a rum and coke."
                else:
                    return "You should have a shot of rum."
            elif spirit_type == "whiskey":
                mixer = ask_question("Do you want a mixer with your whiskey? (yes/no): ")
                if mixer == "yes":
                    return "You should have a whiskey and ginger ale."
                else:
                    return "You should have a shot of whiskey."
            elif spirit_type == "gin":
                mixer = ask_question("Do you want a mixer with your gin? (yes/no): ")
                if mixer == "yes":
                    return "You should have a gin and tonic."
                else:
                    return "You should have a shot of gin."
            else:
                mixer = ask_question("Do you want a mixer with your tequila? (yes/no): ")
                if mixer == "yes":
                    return "You should have a margarita."
                else:
                    return "You should have a shot of tequila."
    else:
        # Ask the user if they want a hot or cold drink
        temperature = ask_question("Do you want a hot or cold drink? ").split()[0]
        if temperature == "hot":
            # Ask the user what type of hot drink they prefer
            hot_drink = ask_question("Do you want coffee, tea, or hot chocolate? ").split()[0]
            if hot_drink == "coffee":
                # Ask the user what type of coffee they prefer
                coffee_type = ask_question("Do you want a latte, cappuccino, or americano? ").split()[0]
                if coffee_type == "latte":
                    return "You should have a latte."
                elif coffee_type == "cappuccino":
                    return "You should have a cappuccino."
                else:
                    return "You should have an americano."
            elif hot_drink == "tea":
                # Ask the user what type of tea they prefer
                tea_type = ask_question("Do you want black, green, or herbal tea? ").split()[0]
                if tea_type == "black":
                    return "You should have black tea."
                elif tea_type == "green":
                    return "You should have green tea."
                else:
                    return "You should have herbal tea."
            else:
                return "You should have hot chocolate."
        else:
            # Ask the user what type of cold drink they prefer
            cold_drink = ask_question("Do you want soda, juice, or iced tea? ").split()[0]
            if cold_drink == "soda":
                # Ask the user what type of soda they prefer
                soda_type = ask_question("Do you want a cola or a lemon-lime soda? ").split()[0]
                if soda_type == "cola":
                    return "You should have a cola."
                else:
                    return "You should have a lemon-lime soda."
            elif cold_drink == "juice":
                # Ask the user what type of juice they prefer
                juice_type = ask_question("Do you want orange, apple, or grape juice? ").split()[0]
                if juice_type == "orange":
                    return "You should have orange juice."
                elif juice_type == "apple":
                    return "You should have apple juice."
                else:
                    return "You should have grape juice."
            else:
                return "You should have iced tea."


# Call the recommend_drink() function and print the result
print("Welcome to the drink recommendation AI!")
time.sleep(1)
print("I will ask you a few questions to find out what drink you should have.")
time.sleep(1)
print(recommend_drink())
