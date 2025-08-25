-def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    try:
        print("=== BMI Calculator ===")
        
        weight = float(input("Enter your weight (in kilograms): "))
        
        height_input = input("Enter your height (in meters or centimeters): ")
        height = float(height_input)
        
        # If height is likely in centimeters (greater than 3), convert to meters
        if height > 3:
            height = height / 100
            print(f"Converting height from {height_input} cm to {height} meters")
        
        if weight <= 0 or height <= 0:
            print("Please enter valid, positive numbers for weight and height.")
            return

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        
        print(f"\nResults:")
        print(f"Weight: {weight} kg")
        print(f"Height: {height} m")
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")

    except ValueError:
        print("Invalid input. Please enter numbers only for weight and height.")
if __name__ == "__main__": main()