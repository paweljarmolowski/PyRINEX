def test_count_nav_dict_elements(epochDict):
    r = epochDict 
    q = sum(len(v)for v in r.values())
    if q == 30:
        pass
    else:
        raise Exception("Epoch data frame has: {} elements".format(q))