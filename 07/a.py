def solve(lines):
    current_path = ""
    paths_size = {}
    dir_size = { "/": 0 }

    for line in lines:
        is_command = line[0] == "$"

        if is_command:
            cmd = line.split(" ")

            command = cmd[1]

            if command == "cd":
                ls_mode = False

                path = cmd[2]

                if path == "..":
                    current_path = current_path[:current_path.rfind("/")]
                elif path == "/":
                    current_path = "/"
                elif current_path == "/":
                    current_path += path
                else:
                    current_path += "/" + path

            if command == "ls":
                ls_mode = True
        else:
            if ls_mode:
                result = line.split(" ")

                if result[0] == "dir":
                    dir_name = result[1]
                    if current_path == "/":
                        dir_size[current_path+ dir_name] = 0
                    else:
                        dir_size[current_path + "/" + dir_name] = 0
                else:
                    file_name = result[1]
                    file_size = int(result[0])

                    paths_size[current_path + "/" + file_name] = file_size

                    # Add size to folders
                    if current_path not in dir_size:
                        dir_size[current_path] = 0

                    dir_size[current_path] += file_size

                    # Also add size to parent paths
                    parent_path = current_path
                    while parent_path != "/":
                        parent_path = parent_path[:parent_path.rfind("/")]

                        if parent_path == "":
                            parent_path = "/"

                        if parent_path not in dir_size:
                            dir_size[parent_path] = 0
                        dir_size[parent_path] += file_size


    print(dir_size)
    print([size for size in dir_size.values() if size <= 100000])
    print(sum([size for size in dir_size.values() if size <= 100000]))

