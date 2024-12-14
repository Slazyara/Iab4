import time


start_time = time.perf_counter()
for i in range(100):
    import task1
end_time = time.perf_counter()
am=end_time- start_time
#print(f"Основа - {end_time - start_time}")


start_time = time.perf_counter()
for i in range(100):
    import dop2
end_time = time.perf_counter()
a1=end_time- start_time

#print(f"Доп 1  - {end_time - start_time}")

start_time = time.perf_counter()
for i in range(100):
    import dop3
end_time = time.perf_counter()
a2=end_time- start_time

#print(f"Доп 2  - {end_time - start_time}")

start_time = time.perf_counter()
for i in range(100):
    import dop3
end_time = time.perf_counter()
a3=end_time- start_time

#print(f"Доп 5  - {end_time - start_time}")


print(f"Основное задание- {am}")
print(f"Доп 1- {a1}")
print(f"Доп 2- {a2}")
print(f"Доп 3- {a3}")
#print(am,"  ",a1,"  ",a2,"   ",a5)