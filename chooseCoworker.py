import tkinter as tk

# Logan Gillis

# Define what a co-worker will mean in this scenario. We want to determine who will pay for coffee fairly, keeping varying prices in mind. 
# This means we only care about the name of the coworker, and the price of their drink. 
class Coworker:
    def __init__(self, name, drink_price):
        self.name = name
        self.drink_price = drink_price


# This function takes a list of coworkers and their respective drink prices. if their are none, or the program has reached the end of the 
# list, it will return nothing. If the list is populated, the most expensive drink will be extracted. Every other drink price will be 
# compared, and the person with the most expensive drink will be returned. After they are returned, they are removed from the list 
# to avoid the same person paying twice.
def decide_who_pays(coworkers):
    if not coworkers:
        return None
    most_expensive_drink = max([coworker.drink_price for coworker in coworkers])
    for coworker in coworkers:
        if coworker.drink_price == most_expensive_drink:
            coworkers.remove(coworker)
            return coworker

# Initialize GUI using tkinter
def run_gui():
    root = tk.Tk()
    root.title("Coffee Payment Decider")


    # List of coworkers to be compared
    list_of_coworkers = [Coworker("Bob", 2.50),
                    Coworker("Jeremy", 4.50),
                    Coworker("Craig", 2.00),
                    Coworker("Alex", 2.75),
                    Coworker("Linda", 3.50),
                    Coworker("Katie", 3.50),
                    Coworker("Greg", 1.00)]

    # Finds the fairest person to pay based off of the most expensive drink. Once everyone has payed, the list needs to be reloaded.
    def calc_and_display_payer(result_label):
        chosen_coworker = decide_who_pays(list_of_coworkers)
        if chosen_coworker:
            result_label.config(text=f"{chosen_coworker.name} is paying!")
        else:
             result_label.config(text="Reload list!")

    # Button used to calculate who should pay.
    calculate_button = tk.Button(root, text="calculate", command=lambda:calc_and_display_payer(result_label))
    calculate_button.pack(pady=10)

    # Result
    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    run_gui()
    