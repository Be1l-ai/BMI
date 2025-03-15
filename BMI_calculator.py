def calculate_bmi(weight, height):
    """Calculate the Body Mass Index (BMI) given weight and height."""
    return weight / (height ** 2)

def get_bmi_category(bmi):
    """Determine the BMI category based on BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Healthy"
    else:
        return "Overweight"

def main():
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        print(f"Your BMI is {bmi:.2f} ({category})")
    except ValueError:
        print("Please enter valid numerical values for weight and height.")

main()
