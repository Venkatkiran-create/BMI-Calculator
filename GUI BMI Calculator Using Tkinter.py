import tkinter as tk
from tkinter import messagebox
import csv
import matplotlib.pyplot as plt

def calculate_bmi(weight, height):
    """Calculate the BMI value."""
    return weight / (height ** 2)

def categorize_bmi(bmi):
    """Categorize the BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def save_bmi_data(weight, height, bmi, category):
    """Save BMI data to a CSV file."""
    with open("bmi_data.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([weight, height, bmi, category])

def plot_bmi_trends():
    """Plot historical BMI data."""
    weights, heights, bmis = [], [], []
    try:
        with open("bmi_data.csv", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                weights.append(float(row[0]))
                heights.append(float(row[1]))
                bmis.append(float(row[2]))

        plt.plot(bmis, marker='o')
        plt.title("BMI Trends")
        plt.xlabel("Entry Number")
        plt.ylabel("BMI")
        plt.grid()
        plt.show()
    except FileNotFoundError:
        messagebox.showerror("File Not Found", "No BMI data found. Please calculate at least one BMI.")
    except ValueError:
        messagebox.showerror("Data Error", "There was an error reading the BMI data.")

def calculate_and_display_bmi():
    """Calculate BMI and display the result."""
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive.")
        
        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)
        
        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")
        
        save_bmi_data(weight, height, bmi, category)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create and place labels and entry fields
tk.Label(root, text="Enter Weight (kg):").grid(row=0, column=0)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1)

tk.Label(root, text="Enter Height (m):").grid(row=1, column=0)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

# Create a button to calculate BMI
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_and_display_bmi)
calculate_button.grid(row=2, column=1)

# Create a button to show BMI trends
trend_button = tk.Button(root, text="Show Trends", command=plot_bmi_trends)
trend_button.grid(row=3, column=1)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2)

# Start the GUI event loop
root.mainloop()
