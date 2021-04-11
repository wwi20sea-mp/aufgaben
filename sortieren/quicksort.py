def qsort(myList):
    '''Sortiert die Liste `myList` mit dem Verfahren QuickSort.
       Liefert die sortierte Liste.
    '''
    if len(myList) == 0:
        return []
    head, *tail = myList
    left = [i for i in tail if i <= head]
    right = [i for i in tail if i > head]
    return qsort(left) + [head] + qsort(right)
    
def test_qsort():
    from test import test_sortfunction
    test_sortfunction(qsort)




# Bonus: Eine QuickSort-Variante, die Iteratoren nutzt, um unnötige Kopieroperationen
#        einzusparen. Etwas schneller, aber dafür schwerer lesbar.
import itertools

def qsort_iter(myList):
    '''Sortiert die Liste `myList` mit dem Verfahren QuickSort.
       Liefert einen Iterator auf die sortierte Liste.

       Hinweis: Diese Variante verwendet Iteratoren und Hilfsfunktionen aus dem
       Package `itertools`, um unnötige Kopieropertaionen zu vermeiden.
    '''
    myListIter = iter(myList)
    head = next(myListIter, None)
    if head is None:
        return []
    ileft, iright = itertools.tee(myListIter)
    return itertools.chain(
        qsort_iter(filter(lambda x : x <= head, ileft)),
        [head],
        qsort_iter(filter(lambda x : x > head, iright))
    )

def test_qsort_iter():
    from test import test_sortfunction
    test_sortfunction(qsort_iter)

if __name__ == "__main__":
    test_qsort()
    test_qsort_iter()
