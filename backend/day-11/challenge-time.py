#--------------------------------------------------------------------
def read_file(file_path):
    names = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                names.append(line.strip())
        return names
    except FileNotFoundError as e:
        print(f"Sorry, the file cannot be found: {e}")
    except Exception as e:
        print(f"Error: {e}")
#--------------------------------------------------------------------
def write_file(file_path, alphabetical_names):
    try:
        with open(file_path, 'w') as file:
            for name in alphabetical_names:
                file.write(name + '\n')
    except Exception as e:
        print(f"Error: {e}")
#--------------------------------------------------------------------
def write_back():
    try:
        file_path = 'backend\\day-11\\names.txt'
        names = read_file(file_path)
        alphabetical_names = sorted(names)
        write_file(file_path, alphabetical_names)
        print(f"Names have been sorted alphabetically and written back to {file_path}.")
    except TypeError as e:
        print(f"Something went wrong: {e}")

write_back()