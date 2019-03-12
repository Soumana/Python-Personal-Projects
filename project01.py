from pathlib import Path
import os
import shutil




def get_files_from_directory(directory_path):
    result = []
    for item in Path(directory_path).iterdir():
        if item.is_file():
            result.append(item)
    return result




def get_files_recursive(directory_path):
    result = []
    for item in Path(directory_path).iterdir():
        if item.is_file():
            result.append(item)

        elif item.is_dir():
            result.extend(get_files_recursive(item))
    return result



def get_all_files():
    file_is_good = False
    all_the_files = []

    while not file_is_good:
        path_to_directory = input().split()

        try:
            if len(path_to_directory) == 2 and path_to_directory[0].lower() == 'd':
                user_path = path_to_directory[1:]
                formated_path = ' '.join(user_path)
                list_of_file_paths = get_files_from_directory(formated_path)
                for p in list_of_file_paths:
                    all_the_files.append(p)
                    print(p)
                file_is_good = True


            elif len(path_to_directory) == 2 and path_to_directory[0].lower() == 'r':
                p = path_to_directory[1:]
                f_p = ' '.join(p)
                list_of_file_paths = get_files_recursive(f_p)
                for p in list_of_file_paths:
                    all_the_files.append(p)
                    print(p)
                file_is_good = True


            else:
                print('ERROR')


        except FileNotFoundError:
            print('ERROR - File Not Found (get all files function')


    return all_the_files




def get_narrowed_files(all_the_files):
    narrowed_search = []
    response_is_good = False
    while not response_is_good:
        response = input().split()

        try:
            if len(response) == 1 and response[0].lower() == 'a':
                for file in all_the_files:
                    print(file)
                    narrowed_search.append(file)
                response_is_good = True

            elif len(response) > 1 and response[0].lower() == 'n':
                for file in all_the_files:
                    incomplete_search = response[1:]
                    complete_search = ' '.join(incomplete_search)
                    if complete_search.lower() in str(file).lower():
                        print(file)
                        narrowed_search.append(file)
                response_is_good = True

            elif len(response) == 2 and response[0].lower() == 'e':
                for file in all_the_files:
                    file_extension = os.path.splitext(str(file))
                    if file_extension[1] == response[1].lower() or file_extension[1][1:] == response[1].lower():
                        print(file)
                        narrowed_search.append(file)
                response_is_good = True

            elif len(response) > 1 and response[0].lower() == 't':
                textchars = bytearray({7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7f})
                is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))
                i_search = response[1:]
                c_search = ' '.join(i_search)
                for file in all_the_files:
                    if not is_binary_string(open(str(file), 'rb').read(1024)):
                        f = file.open('r')
                        for line in f.readlines():
                            if c_search.lower() in line.lower():
                                print(file)
                                narrowed_search.append(file)
                                break
                        f.close()
                response_is_good = True

            elif len(response) == 2 and response[0] == '<' and int(response[1]) >= 0:
                for file in all_the_files:
                    file_size_in_bytes = os.path.getsize(str(file))
                    if file_size_in_bytes < int(response[1]):
                        print(file)
                        narrowed_search.append(file)
                response_is_good = True



            elif len(response) == 2 and response[0] == '>' and int(response[1]) >= 0:
                for file in all_the_files:
                    file_size_in_bytes = os.path.getsize(str(file))
                    if file_size_in_bytes > int(response[1]):
                        print(file)
                        narrowed_search.append(file)
                response_is_good = True


            else:
                print('ERROR')

        except FileNotFoundError:
            print('ERROR get narrow files function')

    return narrowed_search





def show_final_files(narrowed_search):
    user_is_good = False
    while not user_is_good:
        user_response = input().split()

        try:
            if len(user_response) == 1 and user_response[0].lower() == 'f':
                textchars = bytearray({7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7f})
                is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))
                for file in narrowed_search:
                    if not is_binary_string(open(str(file), 'rb').read(1024)):
                        f = file.open('r')
                        print(f.readline().strip())
                    else:
                        print('NOT TEXT')
                user_is_good = True


            elif len(user_response) == 1 and user_response[0].lower() == 'd':
                for file in narrowed_search:
                    copy = str(file) + '.dup'
                    shutil.copy(str(file), copy)
                user_is_good = True


            elif len(user_response) == 1 and user_response[0].lower() == 't':
                for file in narrowed_search:
                    os.utime(str(file), None)
                user_is_good = True


            else:
                print('ERROR')

        except FileNotFoundError:
            print('ERROR in show_final_files function')






def main():
    all_the_files = get_all_files()
    narrowed_search = get_narrowed_files(all_the_files)
    show_final_files(narrowed_search)


if __name__ == '__main__':
    main()