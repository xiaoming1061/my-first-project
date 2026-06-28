a = {"a": "1", "b": "2", "c": "3"}
print(list(a.keys()))
print(a.get("a"))
print(a["a"])
print(a.get("a")== a["a"])
print(max(a,key = a.get))