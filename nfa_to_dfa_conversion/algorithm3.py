print('Enter state names with space between two states (first state entered to be considered the start state): -')
state_list = list(set(input().split()))

print('Any repeated state has been discarded.')

print('Select start state: -')

while 1:

    start = list(input().split())

    if len(start) > 1:
        print('Mention only a single state. Try again: -')
        continue

    try:
        start = start[0]
    except:
        print('Empty string not allowed. Try again: -')
        continue

    if start not in state_list:
        print('No such state found. Try again.')
        continue

    break

print('Select final states: -')

while 1:

    final = list(set(input().split()))

    try_flag = 0

    for i in final:

        if i not in state_list:
            print('A (few) state(s) was/were not identified. Try again')
            try_flag = 1
            break

    if try_flag == 1:
        continue

    break

print('Any state repeatedly marked final has been discarded.')


print('Enter alphabet set with space between two alphabets: -')
temp_aplha_list = list(set(input().split()))
alpha_list = []
alpha_list.append('/')

rep_flag = 0

for i in temp_aplha_list:

    if i in state_list:
        rep_flag = 1
        continue

    alpha_list.append(i)

if rep_flag == 1:
    print('There is/are alphabet(s) recognised by same string as that of some states and are hence discarded.')

trans = {}

for i in state_list:
    trans[i] = []

for i in state_list:

    print('\n' + 'Defining TRANSITIONS for state \'' + i + '\'' + ' : -' + '\n')

    for j in alpha_list:

        print('State transition(s) of \'' + i + '\'' + ' on input \'' + j + '\'' + " (Type 'none' for no transition): -")

        while 1:

            try_flag = 0
            trans_in = input()

            if trans_in == 'none':
                break

            to_states = list(set(trans_in.split()))

            for k in to_states:

                if k not in state_list:
                    print('A (few) state(s) was/were not identified. Try again')
                    try_flag = 1
                    break

            if try_flag == 1:
                continue

            trans[i].append([j, to_states])

            break

print('\nFollowing is/are the state transitions for the equivalent DFA: -')

created_states = [] # queue of new generated states
created_states.append([start])

dfa_trans = []
dfa_states = []
dfa_states.append([start])

while len(created_states) != 0: # Looping till no new state is encountered

    # print(created_states)

    dfa_states_temp = [] # All new states generated for the currently analysed state set (say q(a))

    for i in alpha_list: # Defining all transitions for the state q(a)

        if i == '/':
            continue

        dest_states = [] # All states transitions from q(a) to input 'i'

        for j in created_states[0]: # Collecting all transitions of state set q(a) for input i

            for k in trans[j]:

                if k[0] == i:

                    for l in k[1]:
                        dest_states.append(l)

        if len(dest_states) == 0:
            continue

        dest_states = list(set(dest_states))

        add_states = []

        for j in dest_states: # Check for lambda transitions ('\')

            for k in trans[j]:

                if k[0] == '/':

                    for l in k[1]:
                        add_states.append(l)

        for j in add_states:
            if j not in dest_states:
                dest_states.append(j)

        count = len(dest_states)

        break_flag = 0 # Indicates if the resultant state of the transition is found in the already created set of states

        for j in dfa_states:

            cnt = 0

            for k in dest_states:

                if k in j:
                    cnt += 1

            if cnt == count:
                dfa_trans.append([created_states[0], i, j])
                break_flag = 1
                break

        if break_flag == 1:
            continue

        dfa_trans.append([created_states[0], i, dest_states])
        dfa_states_temp.append(dest_states)

        if dest_states not in created_states:
            created_states.append(dest_states)

    for i in dfa_states_temp:

        if i not in dfa_states:
            dfa_states.append(i)

    created_states.pop(0)

for dfa_transitions in dfa_trans:
    print('State: ' + str(dfa_transitions[0]) + ' X ' + str(dfa_transitions[1]) + ' -> ' + str(dfa_transitions[2]))
    print()

dfa_final = []

for i in dfa_states:
    for j in i:
        if j in final:
            dfa_final.append(i)

print('The final states is/are: -')

for i in dfa_final:
    print(i)











