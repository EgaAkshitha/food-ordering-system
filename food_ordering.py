# Food Ordering System #


menu = {
    1: {"name": "Pizza", "price": 250},
    2: {"name": "Burger", "price": 120},
    3: {"name": "Biryani", "price": 200},
    4: {"name": "Egg Fried Rice", "price": 150},
    5: {"name": "Noodles", "price": 130},
    6: {"name": "French Fries", "price": 100},
    7: {"name": "Ice Cream", "price": 80},
    8: {"name": "Soft Drink", "price": 50}
}

cart = {}

def display_menu():
    print("\n========== FOOD MENU ==========")

    for item_id, item in menu.items():
        print(
            f"{item_id}. {item['name']:<15} ₹{item['price']}"
        )

    print("===============================")


def add_to_cart():
    display_menu()

    try:
        item_id = int(input("Enter food item number: "))

        if item_id not in menu:
            print("Invalid food item!")
            return

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        if item_id in cart:
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

        print(
            f"{menu[item_id]['name']} added to cart successfully!"
        )

    except ValueError:
        print("Please enter a valid number.")


def view_cart():
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\n========== YOUR CART ==========")

    total = 0

    for item_id, quantity in cart.items():
        item = menu[item_id]

        item_total = item["price"] * quantity
        total += item_total

        print(
            f"{item['name']:<15} "
            f"x {quantity:<3} "
            f"₹{item_total}"
        )

    print("-------------------------------")
    print(f"Total Amount: ₹{total}")
    print("===============================")


def remove_from_cart():
    if not cart:
        print("\nYour cart is empty.")
        return

    view_cart()

    try:
        item_id = int(input("Enter item number to remove: "))

        if item_id in cart:
            del cart[item_id]
            print("Item removed successfully!")
        else:
            print("Item is not available in your cart.")

    except ValueError:
        print("Please enter a valid number.")


def update_quantity():
    if not cart:
        print("\nYour cart is empty.")
        return

    view_cart()

    try:
        item_id = int(input("Enter item number: "))

        if item_id not in cart:
            print("Item is not available in your cart.")
            return

        quantity = int(input("Enter new quantity: "))

        if quantity <= 0:
            del cart[item_id]
            print("Item removed from cart.")
        else:
            cart[item_id] = quantity
            print("Quantity updated successfully!")

    except ValueError:
        print("Please enter a valid number.")


def calculate_bill():
    subtotal = 0

    for item_id, quantity in cart.items():
        subtotal += menu[item_id]["price"] * quantity

    # Discount
    if subtotal >= 1000:
        discount = subtotal * 0.10
    elif subtotal >= 500:
        discount = subtotal * 0.05
    else:
        discount = 0

    delivery_charge = 40 if subtotal > 0 else 0

    final_amount = subtotal - discount + delivery_charge

    return subtotal, discount, delivery_charge, final_amount


def place_order():
    if not cart:
        print("\nYour cart is empty. Add some food first.")
        return

    print("\n========== ORDER BILL ==========")

    subtotal, discount, delivery, final_amount = calculate_bill()

    view_cart()

    print(f"Subtotal       : ₹{subtotal}")
    print(f"Discount       : ₹{discount:.2f}")
    print(f"Delivery Charge: ₹{delivery}")
    print("-------------------------------")
    print(f"Final Amount   : ₹{final_amount:.2f}")

    print("\nSelect Payment Method")
    print("1. Cash on Delivery")
    print("2. UPI")
    print("3. Card")

    try:
        payment = int(input("Enter your choice: "))

        if payment == 1:
            payment_method = "Cash on Delivery"
        elif payment == 2:
            payment_method = "UPI"
        elif payment == 3:
            payment_method = "Card"
        else:
            print("Invalid payment option.")
            return

        print("\n========== ORDER CONFIRMED ==========")
        print("Thank you for ordering!")
        print(f"Payment Method: {payment_method}")
        print(f"Amount Paid   : ₹{final_amount:.2f}")
        print("Your food will be delivered soon.")
        print("======================================")

        # Clear cart after order
        cart.clear()

    except ValueError:
        print("Please enter a valid option.")

def main():
    while True:

        print("\n========== FOOD ORDERING SYSTEM ==========")
        print("1. Display Food Menu")
        print("2. Add Food to Cart")
        print("3. View Cart")
        print("4. Update Quantity")
        print("5. Remove Food from Cart")
        print("6. Place Order")
        print("7. Exit")
        print("==========================================")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                display_menu()

            elif choice == 2:
                add_to_cart()

            elif choice == 3:
                view_cart()

            elif choice == 4:
                update_quantity()

            elif choice == 5:
                remove_from_cart()

            elif choice == 6:
                place_order()

            elif choice == 7:
                print("Thank you for using Food Ordering System!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Please enter a valid number.")

main()