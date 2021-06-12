def split(string):
    return [char for char in string]

def minion_game(string):
    length = int(len(string))
    vowels = split('AEIOU')
    s = split(string)
    scores = {'Stuart': 0, 'Kevin': 0}
    for n, i in enumerate(s):
        num = length-n
        if i in vowels:
            scores['Kevin'] += int(num)
        else:
            scores['Stuart'] += int(num)
    if scores['Kevin'] > scores['Stuart']:
        print('Kevin {score}'.format(score = scores['Kevin']))
    elif scores['Kevin'] < scores['Stuart']:
        print('Stuart {score}'.format(score = scores['Stuart']))
    else:
        print('Draw')

