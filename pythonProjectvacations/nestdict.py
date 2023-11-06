course={
    'php': {'duration': '3 months','fees': 15000},
    'java': {'duration': '2 months','fees': 10000},
    'python': {'duration': '3 months', 'fees': 11000},
}

print(course)
course['java']['fees']=20000
print(course['php'])
print(course['php']['fees'])
for k,v in course.items():
    print(k,v)