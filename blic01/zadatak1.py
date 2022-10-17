def fun(predmeti):
    assert isinstance(predmeti, list) and all([isinstance(i, str) for i in predmeti])
    return {k:v[::-1] for k, v  in enumerate(predmeti) }


predmeti = ["Stol", "Stolica", "Krevet", "Fotelja"]
print(fun(predmeti))