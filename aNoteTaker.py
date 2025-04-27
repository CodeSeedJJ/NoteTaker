import os

def get_text_files(directory):
    """List all text files in the directory."""
    return [f for f in os.listdir(directory) if f.endswith('.txt')]

def choose_text_file(directory):
    """Prompt the user to choose an existing text file or create a new one."""
    text_files = get_text_files(directory)
    if text_files:
        print("Select a text file to append to:")
        for i, file in enumerate(text_files, 1):
            print(f"{i}. {file}")
        print(f"{len(text_files) + 1}. Create a new text file")
        
        choice = int(input("Enter the number of the text file (or create a new one): "))
        
        if choice == len(text_files) + 1:
            new_file = input("Enter the name of the new text file: ") + '.txt'
            return new_file
        elif 1 <= choice <= len(text_files):
            return text_files[choice - 1]
        else:
            print("Invalid choice. Try again.")
            return choose_text_file(directory)
    else:
        print("No existing text files found. Creating a new one.")
        new_file = input("Enter the name of the new text file: ") + '.txt'
        return new_file

def write_note_to_text_file(file_path):
    """Prompt the user for the contents of the note and save it."""
    note = input("Enter your note: ")
    
    with open(file_path, 'a') as text_file:
        text_file.write(f"{note}\n")
    print(f"Note saved to {file_path}")

def main():
    text_directory = "D:\\github\\notes"  
    text_file = choose_text_file(text_directory)  
    file_path = os.path.join(text_directory, text_file)  
    write_note_to_text_file(file_path)  

if __name__ == "__main__":
    main()
