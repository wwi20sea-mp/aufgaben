from functools import reduce

def maximum(liste):
    ''' Bestimmt mittels `reduce` das größte Element der gegebenen Liste. '''
    # [TODO]
    return 0

def test_maximum():
    assert(maximum([1,3,6,2,4]) == 6)
    assert(maximum([1,4]) == 4)
    assert(maximum([8]) == 8)
    assert(maximum([]) == None)
    print("Tests für maximum() ok.")

def length(liste):
    ''' Liefert die Länge der Liste. '''
    # [TODO]
    return 0

def test_length():
    assert(length([1,3,6,2,4]) == 5)
    assert(length([1,4]) == 2)
    assert(length([8]) == 1)
    assert(length([]) == 0)
    print("Tests für length() ok.")

def without(liste, i):
    ''' Liefert eine Liste, die alle Elemente außer dem an Stelle `i` enthält.'''
    # [TODO]
    return []

def test_without():
    assert(without([1,3,6,2,4],2) == [1,3,2,4])
    assert(without([1,3,6,2,4],4) == [1,3,6,2])
    assert(without([1,3,6,2,4],5) == [1,3,6,2,4])
    print("Tests für without() ok.")

def partition(liste, n):
    '''Liefert zwei Listen: Eine mit allen Elemente aus liste, die kleiner sind als n
       und eine mit den größeren Elementen.'''
    # [TODO]
    return [], []

def test_partition():
    assert(partition([4,18,25,2,1,42,38], 20) == ([4,18,2,1],[25,42,38]))
    print("Tests für partition() ok.")



if __name__ == "__main__":
    test_maximum()
    test_length()
    test_without()
    test_partition()