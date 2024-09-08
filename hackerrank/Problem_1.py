n = int(input())
list_ = []
for i in range(n):
    command, *list_temp = input().split()
    if command == 'insert':
        list_.insert(*list(map(int,list_temp)))
    elif command == 'print':
        print(list_)
    elif command == 'remove':
        list_.remove(*list(map(int,list_temp)))
    elif command == 'append':
        list_.append(*list(map(int,list_temp)))
    elif command == 'sort':
        list_.sort()
    elif command == 'pop':
        list_.pop()
    elif command == 'reverse':
        list_.reverse()