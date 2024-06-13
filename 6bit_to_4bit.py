import tkinter as tk

def custom_compression(input_bits):
    output_bits = input_bits[:4] 
    return output_bits

def custom_decompression(input_bits):   
    output_bits = input_bits + "00" 
    return output_bits

def perform_custom_operation():
    input_bits = input_entry.get()
    
    if len(input_bits) != 6 or not input_bits.isdigit():
        output_label.config(text="Invalid input. Please enter a 6-bit binary number.")
        return
    
    output_bits = custom_compression(input_bits)
    
    output_label.config(text=output_bits)
    
    canvas.delete("all")
    
    for i, bit in enumerate(input_bits):
        x = 50 + i * 30
        y = 50
        canvas.create_text(x, y - 20, text=bit)
    
    canvas.create_rectangle(30, 70, 250, 130, outline="black", width=2)
    
    for i, bit in enumerate(output_bits):
        x = 50 + i * 30
        y = 150
        canvas.create_text(x, y + 20, text=bit)

def perform_custom_reverse_operation():
    input_bits = input_entry.get()
    
    if len(input_bits) != 4 or not input_bits.isdigit():
        output_label.config(text="Invalid input. Please enter a 4-bit binary number.")
        return
    
    output_bits = custom_decompression(input_bits)
    
    output_label.config(text=output_bits)
    
    canvas.delete("all")
    
    for i, bit in enumerate(input_bits):
        x = 50 + i * 30
        y = 50
        canvas.create_text(x, y - 20, text=bit)
    
    canvas.create_rectangle(30, 70, 190, 130, outline="black", width=2)
    
    for i, bit in enumerate(output_bits):
        x = 50 + i * 30
        y = 150
        canvas.create_text(x, y + 20, text=bit)

window = tk.Tk()
window.title("Binary Compression and Decompression")

input_label = tk.Label(window, text="Enter a 6 or 4 bit binary number:")
input_label.pack()
input_entry = tk.Entry(window)
input_entry.pack()

compress_button = tk.Button(window, text="Compress", command=perform_custom_operation)
compress_button.pack()

decompress_button = tk.Button(window, text="Expand", command=perform_custom_reverse_operation)
decompress_button.pack()

canvas = tk.Canvas(window, width=300, height=200)
canvas.pack()

output_label = tk.Label(window, text="", font=("Helvetica", 16))
output_label.pack()

window.mainloop()
