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
            output_label.config(text="Invalid input. Please enter a valid binary number.")
            return
    
    output_label.config(text=output_bits)
    canvas.delete("all")
    input_groups = [input_bits[i:i+4] for i in range(0, len(input_bits), 4)]
    output_groups = [output_bits[i:i+4] for i in range(0, len(output_bits), 4)]
    num_diagrams = len(input_groups)
    canvas_width = max(1000, num_diagrams * 100)
    canvas_height = 400
    canvas.config(width=canvas_width, height=canvas_height)
    x_offset = (canvas_width - (num_diagrams * 100)) // 2
    y_offset = 30
    
    for input_group, output_group in zip(input_groups, output_groups):
        
        for j, bit in enumerate(input_group):
            x = x_offset + j * 25
            y = y_offset
            canvas.create_text(x, y - 20, text=bit)
        
        
        canvas.create_rectangle(x_offset - 10, y_offset + 20, x_offset + 90, y_offset + 80, outline="black", width=2)
        
        for j, bit in enumerate(output_group):
            x = x_offset + j * 25
            y = y_offset + 100
            canvas.create_text(x, y + 20, text=bit)
        
        for j in range(4):
            x1 = x_offset + j * 25
            y1 = y_offset + 20
            x2 = x_offset + j * 25
            y2 = y_offset + 80
            canvas.create_line(x1, y1, x2, y1 - 20, arrow=tk.LAST)
            canvas.create_line(x1, y2 + 20, x2, y2, arrow=tk.LAST)
        x_offset += 100  
        if x_offset + 100 > canvas_width:
            x_offset = (canvas_width - (num_diagrams * 1000)) // 2
            y_offset += 200  
window = tk.Tk()
window.title("Binary Visualization with NOT Gate")

input_label = tk.Label(window, text="Enter a binary number (32 bits):")
input_label.pack()
input_entry = tk.Entry(window)
input_entry.pack()

calculate_button = tk.Button(window, text="Perform NOT Gate", command=perform_not_gate_operation)
calculate_button.pack()

canvas = tk.Canvas(window, width=1000, height=600)  
canvas.pack()

output_label = tk.Label(window, text="", font=("Helvetica", 16))
output_label.pack()

window.mainloop()
