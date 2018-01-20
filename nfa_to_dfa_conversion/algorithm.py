print('Enter state names with space between two states (first state entered to be considered the start state): -')
state_list = list(set(input().split()))

print('Any repeated state has been discarded.')

print('Select start state: -')

while 1:

    start = input()

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

print(trans)

created_states = []
created_states.append([start])

dfa_trans = []
dfa_states = []
dfa_states.append([start])

while len(created_states) != 0:

    for i in alpha_list:

        break_flag = 0

        dest_states = []

        for j in created_states[0]:

            for k in trans[j]:

                if k[0] == i:

                    for l in k[1]:
                        dest_states.append(l)

        dest_states = list(set(dest_states))
        count = len(dest_states)

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
        dfa_states.append(dest_states)
        created_states.append(dest_states)

    created_states.pop(0)

for dfa_transitions in dfa_trans:
    print('State: ' + str(dfa_transitions[0]) + ' X ' + str(dfa_transitions[1]) + ' -> ' + str(dfa_transitions[2]))
    print()








