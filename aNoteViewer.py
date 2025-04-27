import os

def get_txt_files(directory):
    """List all .txt files in the directory."""
    return [f for f in os.listdir(directory) if f.endswith('.txt')]

def choose_txt_file(directory):
    """Prompt the user to choose an existing .txt file."""
    txt_files = get_txt_files(directory)
    if txt_files:
        print("Select a note file to open:")
        for i, file in enumerate(txt_files, 1):
            print(f"{i}. {file}")
        
        choice = int(input("Enter the number of the note file: "))
        
        if 1 <= choice <= len(txt_files):
            return txt_files[choice - 1]
        else:
            print("Invalid choice. Try again.")
            return choose_txt_file(directory)
    else:
        print("No .txt files found.")
        return None

def open_note_file(file_path):
    """Open and display the contents of the selected note file."""
    with open(file_path, 'r') as note_file:
        print(f"\nOpening note: {file_path}\n")
        print(note_file.read())

def main():
    notes_directory = "D:\\github\\notes"  # Replace with your notes directory
    note_file = choose_txt_file(notes_directory)  # Choose note file
    if note_file:
        file_path = os.path.join(notes_directory, note_file)  # Get full file path
        open_note_file(file_path)  # Open and display the note

if __name__ == "__main__":
    main()
