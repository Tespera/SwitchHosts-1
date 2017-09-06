# coding=utf-8

hosts_path = 'C:\Windows\System32\drivers\etc\hosts'


def show_all_hosts():
    """展示所有的hosts"""
    with open(hosts_path) as file_object:
        for line in file_object:
            print(line.rstrip())


def show_invalid_hosts():
    """展示#号的注释"""
    with open(hosts_path) as file_object:
        for line in file_object:
            if line[0] == '#':
                print(line.rstrip())


def check_hosts(new_hosts):
    """检查hosts是否存在"""
    check_hosts = []
    read_hosts = new_hosts[:]

    for read_host in read_hosts:
        check_hosts.append(read_host + '\n')

    with open(hosts_path, 'r') as file_object:  # 'a'续写，增量更新
        for check_host in check_hosts:
            for line in file_object:
                if line in check_host:
                    print(line, '以上hosts已存在，请重新输入')
                    return True


def add_hosts(new_hosts):
    """增加hosts[]"""
    with open(hosts_path, 'a') as file_object:  # 'a'续写，增量更新
        for new_host in new_hosts:
            file_object.write("\n" + new_host)

    return print('\n已添加完毕!')


# 撤销刚才增加的hosts
def cancel_new_hosts(new_hosts):
    """撤销刚才增加hosts"""
    current_file_data = ''
    with open(hosts_path, 'r') as file_object:
        for new_host in new_hosts:
            for line in file_object:
                if line == new_host:
                    print('这是你要撤回的数据:' + line)
                else:
                    current_file_data += line

    with open(hosts_path, 'w') as file_object:
        file_object.write(current_file_data)

    return print('\n撤销成功!')


# 控制台
def main():

    active = True

    while active:

        input_def = input('''
        ---SwitchHosts小工具---
        \n 请输入你想要实现的功能:
        \n r:展示你所有的hosts
        \n r#:展示你所有注释掉的hosts
        \n a:增加hosts(附带撤销功能) \n
        ''')

        if input_def == 'r':
            show_all_hosts()

            # question = input('\n 需要继续执行么？y or n')
            # if question == 'n':
            #     active = False
            # else:
            #     continue

        elif input_def == 'r#':
            show_invalid_hosts()

        elif input_def == 'a':
            new_hosts = input('\n请输入你要增加的hosts，以/号分割')
            # 转成list
            new_hosts = new_hosts.split('/')

            if check_hosts(new_hosts):
                pass
            else:
                add_hosts(new_hosts)
                add_question = input('是否需要展示最新的hosts? y or n')

                if add_question == 'y':
                    show_all_hosts()
                else:
                    continue

if __name__ == main():

    main()

