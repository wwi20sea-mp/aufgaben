from functools import reduce

def maximum(liste):
    ''' Bestimmt mittels `reduce` das größte Element der gegebenen Liste. '''
    if len(liste) == 0:
        return None
    return reduce(lambda x,y : x if x>y else y, liste)

def test_maximum():
    assert(maximum([1,3,6,2,4]) == 6)
    assert(maximum([1,4]) == 4)
    assert(maximum([8]) == 8)
    assert(maximum([]) == None)
    print("Tests für maximum() ok.")

def length(liste):
    ''' Liefert die Länge der Liste. '''
    if liste == []:
        return 0
    head, *tail = liste
    return 1 + length(tail)

def test_length():
    assert(length([1,3,6,2,4]) == 5)
    assert(length([1,4]) == 2)
    assert(length([8]) == 1)
    assert(length([]) == 0)
    print("Tests für length() ok.")

def without(liste, i):
    ''' Liefert eine Liste, die alle Elemente außer dem an Stelle `i` enthält.'''
    if not i in range(0,length(liste)):
        return liste
    return liste[:i] + liste[i+1:]

def test_without():
    assert(without([1,3,6,2,4],2) == [1,3,2,4])
    assert(without([1,3,6,2,4],4) == [1,3,6,2])
    assert(without([1,3,6,2,4],5) == [1,3,6,2,4])
    print("Tests für without() ok.")


if __name__ == "__main__":
    test_maximum()
    test_length()
    test_without()