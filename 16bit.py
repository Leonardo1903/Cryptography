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
    
    x_offset = 50
    for input_group, output_group in zip(input_groups, output_groups):
        
        for j, bit in enumerate(input_group):
            x = x_offset + j * 50
            y = 50
            canvas.create_text(x, y - 20, text=bit)
        
        
        canvas.create_rectangle(x_offset - 20, 70, x_offset + 180, 130, outline="black", width=2)
        
        
        for j, bit in enumerate(output_group):
            x = x_offset + j * 50
            y = 150
            canvas.create_text(x, y + 20, text=bit)
        
        
        for j in range(4):
            x1 = x_offset + j * 50
            y1 = 70
            x2 = x_offset + j * 50
            y2 = 130
            canvas.create_line(x1, y1, x2, y1 - 20, arrow=tk.LAST)
            canvas.create_line(x1, y2 + 20, x2, y2, arrow=tk.LAST)
        
        x_offset += 250  


window = tk.Tk()
window.title("Binary Visualization with NOT Gate")


input_label = tk.Label(window, text="Enter a binary number (16 bits):")
input_label.pack()
input_entry = tk.Entry(window)
input_entry.pack()


calculate_button = tk.Button(window, text="Perform NOT Gate", command=perform_not_gate_operation)
calculate_button.pack()


canvas = tk.Canvas(window, width=1550, height=400)  # Adjust the canvas width to fit all diagrams side by side
canvas.pack()


output_label = tk.Label(window, text="", font=("Helvetica", 16))
output_label.pack()


window.mainloop()
