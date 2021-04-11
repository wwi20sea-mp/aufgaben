def ggT(a,b):
    ''' Berechnet den größten gemeinsamen Teiler von `a` und `b`.'''

    # Hinweise:
    # - Schreiben Sie eine rekursive Funktion.
    # - Für natürliche Zahlen a und b gilt immer:
    #   - ggT(a,a) = a
    #   - ggT(a,b) = ggT(b,a-b)
    
    # [TODO]
    return 0

def test_ggT():
    assert(ggT(3,3) == 3)
    assert(ggT(2,5) == 1)
    assert(ggT(60,24) == 12)
    print("Alle ggT-Tests ok.")

if __name__ == "__main__":
    test_ggT()