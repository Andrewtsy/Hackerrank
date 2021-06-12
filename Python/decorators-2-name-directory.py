
from operator import itemgetter

def person_lister(f):
    def inner(people):
        # people.sort(key=itemgetter(2))
        # return [f(person) for person in people]
        return map(f, sorted(people, key = lambda x: int(x[2])))
    return inner

