from PIL import Image

def open_image(file_path):
    try:
        image = Image.open(file_path)
        return image
    except IOError:
        print("Error: Unable to open image file.")
        return None

def show_image(image):
    image.show()

def close_image(Image):
    Image.close()

def print_rgb_from_pixel(image, x, y):
    r, g, b = image.getpixel((x, y))
    print(f"Value at pixel : ({x},{y}) =({r}, {g}, {b}")

def text_to_binary(text):
    # Append a null character as a delimiter
    text += '\x00'
    binary_array = []
    for letter in text:
        if (ord(letter)>127):
            raise IOError("Invalid character in string")
        binary_array += list(bin(ord(letter))[2:].zfill(8))
    return binary_array


def pair_image(image):
    pixels = list(image.getdata())
    for pixels_index in range(image.width * image.height):
        pixels[pixels_index] = (pixels[pixels_index][0]-pixels[pixels_index][0]%2,
                                pixels[pixels_index][1]-pixels[pixels_index][1]%2,
                                pixels[pixels_index][2]-pixels[pixels_index][2]%2)
    image.putdata(pixels)
    return image

def encode_image(binarry_array, pair_image):
    if (len(binarry_array) > pair_image.width * pair_image.height):
        raise Exception("Message too long to be encoded in this image")
    pair_image_matrice = list(pair_image.getdata())
    encoded_image_matrice = [(pair_image_matrice[bit_index//3][0]+int(binarry_array[bit_index]),
                              pair_image_matrice[bit_index//3][1]+int(binarry_array[bit_index+1]),
                              pair_image_matrice[bit_index//3][2]+int(binarry_array[bit_index+2])) 
                             for bit_index in range(0,len(binarry_array)-2,3)]
    encoded_image_matrice+=pair_image_matrice[len(encoded_image_matrice):]
    pair_image.putdata(encoded_image_matrice)
    return pair_image

def decode_image(image):
    pixels = list(image.getdata())
    lsb_array =[color %2 for pixel in pixels for color in pixel]
    message = []
    for char_index in range(0, len(lsb_array), 8):
        letter = chr(int("".join(str(bit) for bit in lsb_array[char_index:char_index+8]), 2))
        if letter == '\x00':
            break
        message.append(letter)
    
    return "".join(message)