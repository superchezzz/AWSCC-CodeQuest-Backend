
def read_file(file_path):
    try:
        with open(file_path) as file:
            lines=file.readlines()
            for line in lines:
                print(line.strip())

    except FileNotFoundError as e:
        print(f"Sorry the file cannot be found :< {e}")
    except Exception as e:
        print(f"Error: {e}")

file_path='backend\\day-11\\names.txt'
read_file(file_path)
