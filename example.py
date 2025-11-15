# example.py

from auto_rename_ai import rename_images

if __name__ == "__main__":
    input_folder = input("Enter the path to the folder containing images: ").strip()
    output_folder = input("Enter the path to the output folder: ").strip()

    rename_images(input_folder, output_folder)
    print("all the images processed and renamed successfully")
