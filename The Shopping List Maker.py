#Task 1: Write a function that lets the user add items to a list.
 

pizza_toppings =["olives" , "peppers" ]
print(pizza_toppings)
pizza_toppings.append("onions")
pizza_toppings.append("tomatos")
print(pizza_toppings)
pizza_toppings.remove("onions")
print(pizza_toppings)

x = "peppers"
while x in pizza_toppings:
    print("I want a supreme pizza")
    break
print("I want cheese pizza")

