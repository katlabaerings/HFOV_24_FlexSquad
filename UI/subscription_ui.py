from Logic.subscription_logic import get_subscription_plans, get_plan_details

def display_subscription_options():
    plans = get_subscription_plans()
    for idx, plan in enumerate(plans, 1):
        print(f"{idx}. {plan['PlanName']}")

def show_plan_details():
    print("\nCity Gym Hub Subscription Plans:\n")
    display_subscription_options()
    choice = int(input("\nEnter the number of the plan you'd like to know more about: "))
    plans = get_subscription_plans()
    selected_plan = plans[choice - 1]["PlanName"]
    
    print(get_plan_details(selected_plan))

    if selected_plan == "Class Bundle":
        display_class_bundle_options()
    else:
        display_post_plan_options(selected_plan)

def display_post_plan_options(selected_plan):
    while True:
        print("\nSelect:")
        print(f"1. Buy a {selected_plan}")
        print("2. Back to Subscription Plans")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print(f"\nThank you for choosing to buy the {selected_plan}!")
            # Add logic for purchasing the plan here...
            break
        elif choice == 2:
            show_plan_details()
            break
        elif choice == 3:
            print("\nExiting...")
            break
        else:
            print("Invalid choice. Please select 1, 2 or 3.")

def display_class_bundle_options():
    while True:
        print("\nSelect:")
        print("1. Buy 5-Class Bundle (£45, valid for 3 months)")
        print("2. Buy 10-Class Bundle (£80, valid for 6 months)")
        print("3. Buy 20-Class Bundle (£150, valid for 6 months)")
        print("4. Back to Subscription Plans")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print("\nThank you for purchasing the 5-Class Bundle!")
            break
        elif choice == 2:
            print("\nThank you for purchasing the 10-Class Bundle!")
            break
        elif choice == 3:
            print("\nThank you for purchasing the 20-Class Bundle!")
            break
        elif choice == 4:
            show_plan_details()
            break
        elif choice == 5:
            print("\nExiting...")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

def main_menu():
    show_plan_details()

if __name__ == "__main__":
    main_menu()

