import numpy as np
import pandas as pd
import pickle
from tkinter import *
from tkinter import messagebox

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Function to predict breast cancer
def predict():
    try:
        # Get input values from the GUI
        input_features = [int(clump_thickness.get()),
                          int(uniform_cell_size.get()),
                          int(uniform_cell_shape.get()),
                          int(marginal_adhesion.get()),
                          int(single_epithelial_size.get()),
                          int(bare_nuclei.get()),
                          int(bland_chromatin.get()),
                          int(normal_nucleoli.get()),
                          int(mitoses.get())]

        # Convert input to a DataFrame
        features_value = [np.array(input_features)]
        features_name = ['clump_thickness', 'uniform_cell_size', 'uniform_cell_shape',
                         'marginal_adhesion', 'single_epithelial_size', 'bare_nuclei',
                         'bland_chromatin', 'normal_nucleoli', 'mitoses']
        df = pd.DataFrame(features_value, columns=features_name)

        # Make prediction
        output = model.predict(df)

        # Show result
        if output == 4:
            messagebox.showinfo("Result", "You have chances of Breast Cancer 😔")
        else:
            messagebox.showinfo("Result", "You Don't Have Breast Cancer")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = Tk()
root.title("Breast Cancer Detection")
root.geometry("400x400")

# Add input fields
Label(root, text="Clump Thickness").grid(row=0, column=0)
clump_thickness = Entry(root)
clump_thickness.grid(row=0, column=1)

Label(root, text="Uniform Cell Size").grid(row=1, column=0)
uniform_cell_size = Entry(root)
uniform_cell_size.grid(row=1, column=1)

Label(root, text="Uniform Cell Shape").grid(row=2, column=0)
uniform_cell_shape = Entry(root)
uniform_cell_shape.grid(row=2, column=1)

Label(root, text="Marginal Adhesion").grid(row=3, column=0)
marginal_adhesion = Entry(root)
marginal_adhesion.grid(row=3, column=1)

Label(root, text="Single Epithelial Size").grid(row=4, column=0)
single_epithelial_size = Entry(root)
single_epithelial_size.grid(row=4, column=1)

Label(root, text="Bare Nuclei").grid(row=5, column=0)
bare_nuclei = Entry(root)
bare_nuclei.grid(row=5, column=1)

Label(root, text="Bland Chromatin").grid(row=6, column=0)
bland_chromatin = Entry(root)
bland_chromatin.grid(row=6, column=1)

Label(root, text="Normal Nucleoli").grid(row=7, column=0)
normal_nucleoli = Entry(root)
normal_nucleoli.grid(row=7, column=1)

Label(root, text="Mitoses").grid(row=8, column=0)
mitoses = Entry(root)
mitoses.grid(row=8, column=1)

# Add predict button
Button(root, text="Predict", command=predict).grid(row=9, column=0, columnspan=2)

# Run the application
root.mainloop()