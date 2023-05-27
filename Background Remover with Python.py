from rembg import remove
from PIL import Image 
input_path = "Seyi.jpg"
output_path = "Seyi1.png"
input = Image.open(input_path)
output = remove(input)
output.save(output_path)