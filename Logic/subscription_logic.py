import csv
#This file implements the user story "As a gym member I want more 
#flexible subscription plans, such as one month or a single class, so that I can easily find the best subscription that suits me"

FILE_PATH = "Data/db/subscription_data.csv"


# Load subscription plans from the CSV file
def load_subscription_plans():
    plans = []
    with open(FILE_PATH, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            plans.append(row)
    return plans


# Get all available subscription plans
def get_subscription_plans():
    plans = load_subscription_plans()
    return plans


# Get plan information
def get_plan_details(plan_name):
    plans = load_subscription_plans()
    plan = next((p for p in plans if p["PlanName"] == plan_name), None)

    if not plan:
        return "Invalid plan name."

    details = f"\n{plan_name}\n"
    details += f"Description: {plan['Description']}\n"
    details += f"Target Audience: {plan['TargetAudience']}\n"

    # Special handling for Class Bundle
    if plan_name == "Class Bundle":
        details += "Details:\n"
        bundle_details = plan["Details"].replace("\\n", "\n")
        details += f"{bundle_details}\n"
    else:
        details += f"Price: £{plan['Price']}\n"
        details += "Details:\n"
        formatted_details = plan["Details"].replace("\\n", "\n").replace("\\•", "•")
        details += formatted_details

    return details
