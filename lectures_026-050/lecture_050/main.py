print(' EXERCISE 13 '.center(50, '='))

shopping_list = []
prompt = '''
[1] - Insert
[2] - Delete
[3] - List
[4] - Exit
Choice: '''

choice = ''
while choice != '4':
    choice = input(prompt)

    if choice == '1':
        item = input('Item: ')
        shopping_list.append(item)
        print(f'Item: {item!r}, added')
    elif choice == '2':
        try:
            index = int(input('Enter the index of the item: '))
            if -len(shopping_list) <= index < len(shopping_list):
                del_item = shopping_list.pop(index)
                print(f'Item: {del_item!r}, removed')
            else:
                print('Invalid index')
        except ValueError:
            print('Index must be an integer ')

    elif choice == '3':
        print('🛒 SHOPPING LIST 🛒')
        if not shopping_list:
            print('EMPTY')
        else:
            for i, item in enumerate(shopping_list):
                print(f'{i} - {item!r}')
    elif choice == '4':
        print('Closing up!')
    else:
        print('Invalid option')
