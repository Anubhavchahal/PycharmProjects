d={
    'name':'python',
    'fees':8000,
    'duration':'2months',
}
n= d.get('name')
print(n)

for a in d.keys():
    print(a)
for b in d.values():
    print(b)

for a,b in d.items():
    print(a,'-',b)

del d['fees']
print(d)
m= d.pop('duration')
print(m)
d = dict(name='python',fees=8000)
print(d)
d['review']="good"
print(d)