
import os
import shutil

folder_path = input("Enter folder path: ")

if not os.path.isdir(folder_path):
    print("Folder not found!")

else:
    folders = {
        "Images": [".jpg", ".png", ".jpeg"],
        "Documents": [".pdf", ".txt", ".docx"],
        "Videos": [".mp4", ".mkv"],
        "Music": [".mp3", ".wav"],
        "Others": []
    }

    for folder in folders:
        os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

    for file in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):

            extension = os.path.splitext(file)[1].lower()
            category = "Others"

            for folder, extensions in folders.items():
                if extension in extensions:
                    category = folder
                    break

            new_path = os.path.join(folder_path, category, file)

            if os.path.exists(new_path):
                print("Skipped:", file)
            else:
                shutil.move(file_path, new_path)
                print("Moved:", file, "->", category)

    print("\nFile organization completed!")
