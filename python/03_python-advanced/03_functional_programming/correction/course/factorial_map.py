factorials = []
def f(x):
    if x == 0:
        factorials.append(1)
        return
    factorials.append(factorials[-1]*x)
li = list(range(10))
my_map(li, f)
print(factorials)