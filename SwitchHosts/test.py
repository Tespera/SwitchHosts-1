hosts_path = 'C:\Windows\System32\drivers\etc\hosts'

# current_hosts = ['4/n', '7/n']
# file_object = ['#0', '1', '2', '4', '7']
# current_file_data = ''

# for current_host in current_hosts:
#     print(current_host, '1')
#     for line in file_object:
#         print(line, '2')
#         if line == current_host:
#             print('这是你要撤回的数据:' + line)
#         else:
#             current_file_data += line
#
# if '\n' not in line:
#     line += '\n'
#     if line == current_host:
#         print('这是你要撤回的数据:' + line)
#     else:
#         print(line, current_host)
#         current_file_data += line
# else:
#     if line == current_host:
#         print('这是你要撤回的数据:' + line)
#     else:
#         current_file_data += line

# index_hosts = []
# with open(hosts_path, 'r') as file_object:
#     for line in file_object:
#         index_hosts.append(line)
# print(index_hosts)

with open(hosts_path) as file_object:
    contents = file_object.read()

    index_numbers = ['4', '7']

    for i in index_numbers:
        print(contents.replace(i, ''))

    contents.replace(i, '')
def cancel_new_hosts(new_hosts):
    """撤销刚才增加hosts"""
    if len(new_hosts) >= 2:

        current_hosts = []
        read_hosts = new_hosts[:]

        for read_host in read_hosts:
            current_hosts.append(read_host + '\n')

        current_hosts[-1].replace('\n', '')

        with open(hosts_path, 'r') as file_object:
            current_file_data = ''

            for current_host in current_hosts:
                for line in file_object:
                    if line == current_host:
                        print('这是你要撤回的数据:' + line)
                    else:
                        current_file_data += line

        with open(hosts_path, 'w') as file_object:
            file_object.write(current_file_data)

    else:

        with open(hosts_path, 'r') as file_object:
            current_file_data = ''

            for new_host in new_hosts:
                for line in file_object:
                    if line == new_host:
                        print('这是你要撤回的数据:' + line)
                    else:
                        current_file_data += line

        with open(hosts_path, 'w') as file_object:
            file_object.write(current_file_data)

    return print('\n撤销成功!')