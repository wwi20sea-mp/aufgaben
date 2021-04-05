from functools import reduce

def get_smallest_pos(mylist):
    '''Liefert die Position des kleinsten Elements in der List `mylist`.
       wirft einen ValueError, falls die Liste leer ist.'''
    if len(mylist) == 0:
        raise ValueError("Fehler: Kleinstes Element einer leeren Liste gesucht.")
    head, *tail = mylist
    if len(tail) == 0:
        return 0
    mintail = get_smallest_pos(tail)
    return 0 if head <= tail[mintail] else mintail + 1

def get_and_remove_smallest(mylist):
    '''Sucht das kleinste Element aus der Liste `mylist`.
       Liefert dieses Element und eine Liste, in der es nicht mehr vorkommt.'''
    minpos = get_smallest_pos(mylist)
    return mylist[minpos], mylist[:minpos] + mylist[minpos+1:]

def selectionsort(mylist):
    '''Sortiert die Liste `mylist`mit dem Verfahren SelectionSort.
       Liefert die sortierte Liste zurück'''
    if len(mylist) == 0:
        return []
    m, list_without_m = get_and_remove_smallest(mylist)
    return [m] + selectionsort(list_without_m)

# [TODO]: Tests hinzufügen

l1 = [12,5,2,3,1,17,42]
m,l = get_and_remove_smallest(l1)
print(l1)
print(m, l)
print(selectionsort(l1))