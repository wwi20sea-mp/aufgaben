def test_sortfunction(sortfunction):
    assert(list(sortfunction([3,1,5,2,17,22,42,38])) == [1,2,3,5,17,22,38,42])
    assert(list(sortfunction([1,2,3,4,5])) == [1,2,3,4,5])
    assert(list(sortfunction([])) == [])
    print("Alle Tests für {} ok".format(sortfunction.__name__))
