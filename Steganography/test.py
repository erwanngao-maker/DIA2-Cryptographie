from PIL import Image
import os
import steganographie as stgp

Image_directory = "Jojo_Images/"

# Une methode simple est d'essayer de cacher le nom du fichier de chaque image dans l'image elle meme


for filename in os.listdir(Image_directory):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        path = os.path.join(Image_directory, filename)
    else:
        raise Exception("Invalid File detected")
    image = stgp.open_image(path)
    binary_message = stgp.text_to_binary(filename)
    pair_image = stgp.pair_image(image)
    encoded_image = stgp.encode_image(binary_message,pair_image)
    decoded_message = stgp.decode_image(encoded_image)
    if (decoded_message != filename):
        print(f"Decoded message :{decoded_message}\nMessage was :{filename}")
    else:
        print("Encode and decode successful")

