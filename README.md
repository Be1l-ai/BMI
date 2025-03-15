# BMI Calculator
Here's a simple script to calculate your Body mass index (BMI) based on your input. Created for fun and practices. 

## Project Description
This Python script calculates the Body Mass Index (BMI) based on user-provided weight (in kilograms) and height (in meters). It demonstrates basic input handling, arithmetic operations, and conditional logic, serving as an introductory project for beginners.

## Installation
1. **Ensure Python 3.x is installed:**  
   Download and install from [python.org/downloads](https://www.python.org/downloads/)

2. **Download the project repository:**  
   Open your terminal or command prompt and clone the repository:
   ```bash
   git clone https://github.com/Be1l-ai/BMI.git
   ```

## Usage
1. **Navigate to the project directory:**
   ```bash
   cd bmi-calculator
   ```

2. **Run the script:**
   ```bash
   python BMI_calculator.py
   ```

3. **Follow the prompts:**  
   When you run the script, enter your weight and height as requested.

## Example Output
```
Enter your weight in kg: 70
Enter your height in meters: 1.75
Your BMI is 22.86 (Healthy)
```

## Project Structure
```
bmi-calculator/
├── README.md               # This file
└── BMI_calculator.py       # Python script for BMI calculation
```


```

---

### Python Script (BMI_calculator.py)

```python
# BMI_calculator.py

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
```

---

This guide and project provide a solid foundation for Python beginners to practice basic programming concepts. The code is organized into functions for modularity and clarity, and error handling has been added to manage invalid user inputs.

Happy coding!
