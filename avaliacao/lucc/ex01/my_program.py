from local_lib.path import Path

def create_file(folder_name,file_name,text):
    new_folder = Path(f"./{folder_name}").mkdir_p()
    new_file = Path(f"./{folder_name}/{file_name}.txt")
    new_file.touch().write_text(text)
    print(new_file.read_text())

def main():
    create_file("folder1","hello","Hello World!")
    pass

if __name__ == '__main__':
    main()