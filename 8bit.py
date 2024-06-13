import tkinter as tk

def perform_not_gate_operation():
    input_bits = input_entry.get()
    output_bits = ""
    
    for bit in input_bits:
        if bit == '0':
            output_bits += '1'
        elif bit == '1':
            output_bits += '0'
        else:
            output_label.config(text="Invalid input. Please enter an 8-bit binary number.")
            return
    
    output_label.config(text=output_bits)
    
    canvas1.delete("all")
    canvas2.delete("all")
    
    for i, bit in enumerate(input_bits[:4]):
        x = 50 + i * 50
        y = 50
        canvas1.create_text(x, y - 20, text=bit)
    
        canvas1.create_rectangle(30, 70, 230, 130, outline="black", width=2)
    
   
    for i, bit in enumerate(output_bits[:4]):
        x = 50 + i * 50
        y = 150
        canvas1.create_text(x, y + 20, text=bit)
    
    for i in range(4):
        x1 = 50 + i * 50
        y1 = 70
        x2 = 50 + i * 50
        y2 = 130
        canvas1.create_line(x1, y1, x2, y1 - 20, arrow=tk.LAST)
        canvas1.create_line(x1, y2 + 20, x2, y2, arrow=tk.LAST)
    
    for i, bit in enumerate(input_bits[4:]):
        x = 50 + i * 50
        y = 50
        canvas2.create_text(x, y - 20, text=bit)
    
    
    canvas2.create_rectangle(30, 70, 230, 130, outline="black", width=2)
    
    for i, bit in enumerate(output_bits[4:]):
        x = 50 + i * 50
        y = 150
        canvas2.create_text(x, y + 20, text=bit)
    
    for i in range(4):
        x1 = 50 + i * 50
        y1 = 70
        x2 = 50 + i * 50
        y2 = 130
        canvas2.create_line(x1, y1, x2, y1 - 20, arrow=tk.LAST)
        canvas2.create_line(x1, y2 + 20, x2, y2, arrow=tk.LAST)

window = tk.Tk()
window.title("Binary Visualization with NOT Gate")

input_label = tk.Label(window, text="Enter an 8-bit binary number:")
input_label.pack()
input_entry = tk.Entry(window)
input_entry.pack()

calculate_button = tk.Button(window, text="Perform NOT Gate", command=perform_not_gate_operation)
calculate_button.pack()

canvas1 = tk.Canvas(window, width=300, height=200)
canvas1.pack()

canvas2 = tk.Canvas(window, width=300, height=200)
canvas2.pack()

output_label = tk.Label(window, text="", font=("Helvetica", 16))
output_label.pack()

window.mainloop()
