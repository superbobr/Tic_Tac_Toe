user_input = '         '
moves = 1
print('---------')
print(f'| {user_input[0]} {user_input[1]} {user_input[2]} |')
print(f'| {user_input[3]} {user_input[4]} {user_input[5]} |')
print(f'| {user_input[6]} {user_input[7]} {user_input[8]} |')
print('---------')

while True:

    new_list = [[user_input[6], user_input[3], user_input[0]], [user_input[7], user_input[4], user_input[1]],
                [user_input[8], user_input[5], user_input[2]]]
    move_input = input().split()

    while not (move_input[0].isnumeric() and move_input[1].isnumeric()):
        print('You should enter numbers!')
        move_input = input().split()
    move_input = list(map(int, move_input))

    while (move_input[0] < 1 or move_input[1] < 1) or (move_input[0] > 3 or move_input[1] > 3):
        print('Coordinates should be from 1 to 3!')
        move_input = input().split()
        move_input = list(map(int, move_input))
    while new_list[move_input[0] - 1][move_input[1] - 1] == 'X' or new_list[move_input[0] - 1][
        move_input[1] - 1] == 'O':
        print('This cell is occupied! Choose another one!')
        move_input = input().split()
        move_input = list(map(int, move_input))
    else:
        if moves % 2 != 0:
            new_list[move_input[0] - 1][move_input[1] - 1] = 'X'
        else:
            new_list[move_input[0] - 1][move_input[1] - 1] = 'O'

    new_list = [[new_list[0][2], new_list[1][2], new_list[2][2]], [new_list[0][1], new_list[1][1], new_list[2][1]],
                [new_list[0][0], new_list[1][0], new_list[2][0]]]
    user_input = ''.join(new_list[0]) + ''.join(new_list[1]) + ''.join(new_list[2])
    print('---------')
    print(f'| {user_input[0]} {user_input[1]} {user_input[2]} |')
    print(f'| {user_input[3]} {user_input[4]} {user_input[5]} |')
    print(f'| {user_input[6]} {user_input[7]} {user_input[8]} |')
    print('---------')
    moves += 1

    if user_input[0] == 'X' and user_input[1] == 'X' and user_input[2] == 'X':
        print('X wins')
        break
    if user_input[3] == 'X' and user_input[4] == 'X' and user_input[5] == 'X':
        print('X wins')
        break
    if user_input[6] == 'X' and user_input[7] == 'X' and user_input[8] == 'X':
        print('X wins')
        break
    if user_input[2] == 'X' and user_input[4] == 'X' and user_input[6] == 'X':
        print('X wins')
        break
    if user_input[2] == 'X' and user_input[5] == 'X' and user_input[8] == 'X':
        print('X wins')
        break
    if user_input[1] == 'X' and user_input[4] == 'X' and user_input[7] == 'X':
        print('X wins')
        break
    if user_input[0] == 'X' and user_input[3] == 'X' and user_input[6] == 'X':
        print('X wins')
        break
    if user_input[0] == 'X' and user_input[4] == 'X' and user_input[8] == 'X':
        print('X wins')
        break

    if user_input[0] == 'O' and user_input[1] == 'O' and user_input[2] == 'O':
        print('O wins')
        break
    if user_input[3] == 'O' and user_input[4] == 'O' and user_input[5] == 'O':
        print('O wins')
        break
    if user_input[6] == 'O' and user_input[7] == 'O' and user_input[8] == 'O':
        print('O wins')
        break
    if user_input[2] == 'O' and user_input[4] == 'O' and user_input[6] == 'O':
        print('O wins')
        break
    if user_input[2] == 'O' and user_input[5] == 'O' and user_input[8] == 'O':
        print('O wins')
        break
    if user_input[1] == 'O' and user_input[4] == 'O' and user_input[7] == 'O':
        print('O wins')
        break
    if user_input[0] == 'O' and user_input[3] == 'O' and user_input[6] == 'O':
        print('O wins')
        break
    if user_input[0] == 'O' and user_input[4] == 'O' and user_input[8] == 'O':
        print('O wins')
        break
    if moves == 10:
        print('Draw')
        break
