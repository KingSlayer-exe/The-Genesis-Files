import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        # Get input values
        weight_lbs = float(entry_weight.get())
        feet = float(entry_feet.get())
        inches = float(entry_inches.get())

        # Validate input
        if weight_lbs <= 0 or feet < 0 or inches < 0:
            messagebox.showerror("Invalid Input", "Please enter positive numbers only.")
            return

        # Convert weight (lbs to kg) and height (ft + in to meters)
        weight_kg = weight_lbs * 0.453592
        total_inches = (feet * 12) + inches
        height_m = total_inches * 0.0254

        if height_m == 0:
            messagebox.showerror("Invalid Input", "Height cannot be zero.")
            return

        # Calculate BMI
        bmi = weight_kg / (height_m ** 2)
        result = f"Your BMI is: {bmi:.2f}\n"

        # BMI category
        if bmi < 18.5:
            result += "You are underweight."
        elif 18.5 <= bmi < 25:
            result += "You have a normal weight."
        elif 25 <= bmi < 30:
            result += "You are overweight."
        else:
            result += "You are obese."

        label_result.config(text=result)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter numeric values.")

# GUI Setup
window = tk.Tk()
window.title("BMI Calculator (US Units)")
window.geometry("320x300")

# Weight input (lbs)
tk.Label(window, text="Enter weight (lbs):").pack(pady=5)
entry_weight = tk.Entry(window)
entry_weight.pack()

# Height input (feet and inches)
tk.Label(window, text="Enter height:").pack(pady=5)
frame_height = tk.Frame(window)
frame_height.pack()

tk.Label(frame_height, text="Feet:").pack(side=tk.LEFT)
entry_feet = tk.Entry(frame_height, width=5)
entry_feet.pack(side=tk.LEFT, padx=5)

tk.Label(frame_height, text="Inches:").pack(side=tk.LEFT)
entry_inches = tk.Entry(frame_height, width=5)
entry_inches.pack(side=tk.LEFT)

# Calculate button
tk.Button(window, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

# Result label
label_result = tk.Label(window, text="", font=("Arial", 10))
label_result.pack(pady=10)

# Run the GUI
window.mainloop()

