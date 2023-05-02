import math
import random
warehouse = ['...',
            '...',
            '...']

rows = len(warehouse)
cols = len(warehouse[0])

grid = [[' ' for j in range(cols)] for i in range(rows)]
value = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]

print(warehouse)
print(rows)
print(cols)
print(grid)
print(value)
print(policy)

#user_input = (2,2) # btw 1-9, update
#user_key = "X" # or "O"

#if user_input:
#    grid[user_input[0]-1][user_input[1]-1] = "X"

print(warehouse)
print(rows)
print(cols)
#print('grid:',grid)
print(value)
print(policy)

# AI agent

blanks = True
turn_counter = 0
winner = False

#while blanks:
while not winner:
    turn_counter += 1
    num_blanks = 0

    # check for open spaces
    available_spaces = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == ' ':
                #blanks = True
                num_blanks += 1
                available_spaces.append((i,j))
    if num_blanks == 0:
        print(num_blanks)
        blanks = False
        break
        # no spaces left (eventually will mean no winner)
    print(available_spaces)

    # check winner
    
    r1 = grid[0]
    r2 = grid[1]
    r3 = grid[2]
    
    all_rows = [r1,r2,r3]

    c1 = r1[0] + r2[0] + r3[0]
    c2 = r1[1] + r2[1] + r3[1]
    c3 = r1[2] + r2[2] + r3[2]

    print('r1:',r1)
    print('r2:',r2)
    print('r3:',r3)

    all_cols = [c1,c2,c3]

    for r in all_rows:
        print('r index',r)
        if r[0] == r[1] and r[0] == r[2]:
            #if '.' not in r[0]:
            if r[0] == 'O' or r[0] == 'X':
                f = open("logs.txt", "a")
                f.write("\n")
                f.write('we have a winner?')
                f.write("\n")
                f.close()
                winner = True
                break

    if winner:
        break
    ''''    for c in all_cols:
        if c[0] == c[1] and c[0] == c[2]:
            #if '.' not in c[0]:
            if r[0] == 'O' or r[0] == 'X':
                f = open("logs.txt", "a")
                f.write("\n")
                f.write('we have a winner?')
                f.write("\n")
                f.close()
                winner = True
                break
    
    if winner:
        break
    '''
    '''
    for r in range(len(grid)):
        current_row = grid[r]
        for c in range(len(grid)):
            current_col = current_row[c]
            if 
    '''


    # user
    if turn_counter % 2 != 0: # odd
        # make from user input
        #my_set = (random.randint(0,2),random.randint(0,2))

        rand_num = random.randint(0,(len(available_spaces)-1))
        my_set = available_spaces[rand_num]

        if grid[my_set[0]][my_set[1]] == ' ':
            grid[my_set[0]][my_set[1]] = 'X'
            # TODO: need this to be balanced, currently one player can have
            # more turns than the other, although could be resolved by
            # adding winning conditions
            # need to make comparison based on available spaces
            # / make random selection from pool of avail spaces
            # should loop over grid here, make list of avail spaces, 
            # then determine best move / add in user move
        else:
            print('cant go here')


    # AI
    elif turn_counter % 2 == 0: # even
        #my_set = (random.randint(0,2),random.randint(0,2))
        rand_num = random.randint(0,(len(available_spaces)-1))
        my_set = available_spaces[rand_num]

        if grid[my_set[0]][my_set[1]] == ' ':
            grid[my_set[0]][my_set[1]] = 'O'

    f = open("logs.txt", "a")
    f.write(str(turn_counter))
    f.write("\n")
    f.write(str(grid[0]))
    f.write("\n")
    f.write(str(grid[1]))
    f.write("\n")
    f.write(str(grid[2]))
    f.write("\n")
    f.close()

print(warehouse)
print('rows:',rows)
print(cols)
print(value)
print(policy)
print('grid:')
print(grid[0])
print(grid[1])
print(grid[2])