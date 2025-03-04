#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Mar. 4, 2025
"""
This program asks the user for the diameter of the pizza.
It then calculates and displays the total cost of the pizza with tax.
"""
import constants


# Main function to hold all of the pizza cost processing.
def main():
    # Set constants.
    HST = constants.HST
    LABOUR_COST = constants.LABOUR_COST
    RENTAL_COST = constants.RENTAL_COST
    INGREDIENT_COST = constants.INGREDIENT_COST

    # Get the diameter from the user.
    diameter = int(input("Enter the diameter of the pizza (inches): "))

    # Calculate the subtotal.
    subtotal = LABOUR_COST + RENTAL_COST + (diameter * INGREDIENT_COST)

    # Calculate the tax.
    tax = subtotal * HST

    # Calculate the total amount the pizza costs.
    total = subtotal + tax

    # Display the total cost.
    print(f"\nThe total cost of the pizza is ${total:.2f}.")


if __name__ == "__main__":
    main()
