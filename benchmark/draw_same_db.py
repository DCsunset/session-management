import matplotlib.pyplot as plt

metadata_basic_1_login_0 = []
result_str_basic_1_login_0 = []
result_basic_1_login_0 = []

with open('./mariadb_basic/basic/1/login/data0.txt', 'r') as f:
    for line in f:
        metadata_basic_1_login_0 = list(line.strip(' ').split(','))

result_str_basic_1_login_0 = metadata_basic_1_login_0[0].split()
index = list(range(1, len(result_str_basic_1_login_0) + 1))

for latency in result_str_basic_1_login_0:
    if latency[-2] == 'm':
        result_basic_1_login_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_basic_1_login_0.append(float(latency[0: -2]) * 1000)
    else:
        result_basic_1_login_0.append(float(latency[0: -2]) * 0.001)


metadata_basic_4_login_0 = []
result_str_basic_4_login_0 = []
result_basic_4_login_0 = []

with open('./mariadb_basic/basic/4/login/data0.txt', 'r') as f:
    for line in f:
        metadata_basic_4_login_0 = list(line.strip(' ').split(','))

result_str_basic_4_login_0 = metadata_basic_4_login_0[0].split()
index = list(range(1, len(result_str_basic_4_login_0) + 1))

for latency in result_str_basic_4_login_0:
    if latency[-2] == 'm':
        result_basic_4_login_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_basic_4_login_0.append(float(latency[0: -2]) * 1000)
    else:
        result_basic_4_login_0.append(float(latency[0: -2]) * 0.001)


metadata_basic_4_login_1 = []
result_str_basic_4_login_1 = []
result_basic_4_login_1 = []

with open('./mariadb_basic/basic/4/login/data1.txt', 'r') as f:
    for line in f:
        metadata_basic_4_login_1 = list(line.strip(' ').split(','))

result_str_basic_4_login_1 = metadata_basic_4_login_1[0].split()
index = list(range(1, len(result_str_basic_4_login_1) + 1))

for latency in result_str_basic_4_login_1:
    if latency[-2] == 'm':
        result_basic_4_login_1.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_basic_4_login_1.append(float(latency[0: -2]) * 1000)
    else:
        result_basic_4_login_1.append(float(latency[0: -2]) * 0.001)


metadata_basic_4_login_2 = []
result_str_basic_4_login_2 = []
result_basic_4_login_2 = []

with open('./mariadb_basic/basic/4/login/data2.txt', 'r') as f:
    for line in f:
        metadata_basic_4_login_2 = list(line.strip(' ').split(','))

result_str_basic_4_login_2 = metadata_basic_4_login_2[0].split()
index = list(range(1, len(result_str_basic_4_login_2) + 1))

for latency in result_str_basic_4_login_2:
    if latency[-2] == 'm':
        result_basic_4_login_2.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_basic_4_login_2.append(float(latency[0: -2]) * 1000)
    else:
        result_basic_4_login_2.append(float(latency[0: -2]) * 0.001)


metadata_basic_4_login_3 = []
result_str_basic_4_login_3 = []
result_basic_4_login_3 = []

with open('./mariadb_basic/basic/4/login/data3.txt', 'r') as f:
    for line in f:
        metadata_basic_4_login_3 = list(line.strip(' ').split(','))

result_str_basic_4_login_3 = metadata_basic_4_login_3[0].split()
index = list(range(1, len(result_str_basic_4_login_3) + 1))

for latency in result_str_basic_4_login_3:
    if latency[-2] == 'm':
        result_basic_4_login_3.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_basic_4_login_3.append(float(latency[0: -2]) * 1000)
    else:
        result_basic_4_login_3.append(float(latency[0: -2]) * 0.001)


metadata_basic_1_verify_0 = []
result_str_basic_1_verify_0 = []
result_basic_1_verify_0 = []

with open('./mariadb_basic/basic/1/verify/data0.txt', 'r') as f:
    for line in f:
        metadata_basic_1_verify_0 = list(line.strip(' ').split(','))

result_str_basic_1_verify_0 = metadata_basic_1_verify_0[0].split()
index = list(range(1, len(result_str_basic_1_verify_0) + 1))

for latency in result_str_basic_1_verify_0:
    if latency[-2] == 'm':
        result_basic_1_verify_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_basic_1_verify_0.append(float(latency[0: -2]) * 1000)
    else:
        result_basic_1_verify_0.append(float(latency[0: -2]) * 0.001)



metadata_basic_4_verify_0 = []
result_str_basic_4_verify_0 = []
result_basic_4_verify_0 = []

with open('./mariadb_basic/basic/4/verify/data0.txt', 'r') as f:
    for line in f:
        metadata_basic_4_verify_0 = list(line.strip(' ').split(','))

result_str_basic_4_verify_0 = metadata_basic_4_verify_0[0].split()
index = list(range(1, len(result_str_basic_4_verify_0) + 1))

for latency in result_str_basic_4_verify_0:
    if latency[-2] == 'm':
        result_basic_4_verify_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_basic_4_verify_0.append(float(latency[0: -2]) * 1000)
    else:
        result_basic_4_verify_0.append(float(latency[0: -2]) * 0.001)


metadata_basic_4_verify_1 = []
result_str_basic_4_verify_1 = []
result_basic_4_verify_1 = []

with open('./mariadb_basic/basic/4/verify/data1.txt', 'r') as f:
    for line in f:
        metadata_basic_4_verify_1 = list(line.strip(' ').split(','))

result_str_basic_4_verify_1 = metadata_basic_4_verify_1[0].split()
index = list(range(1, len(result_str_basic_4_verify_1) + 1))

for latency in result_str_basic_4_verify_1:
    if latency[-2] == 'm':
        result_basic_4_verify_1.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_basic_4_verify_1.append(float(latency[0: -2]) * 1000)
    else:
        result_basic_4_verify_1.append(float(latency[0: -2]) * 0.001)


metadata_basic_4_verify_2 = []
result_str_basic_4_verify_2 = []
result_basic_4_verify_2 = []

with open('./mariadb_basic/basic/4/verify/data2.txt', 'r') as f:
    for line in f:
        metadata_basic_4_verify_2 = list(line.strip(' ').split(','))

result_str_basic_4_verify_2 = metadata_basic_4_verify_2[0].split()
index = list(range(1, len(result_str_basic_4_verify_2) + 1))

for latency in result_str_basic_4_verify_2:
    if latency[-2] == 'm':
        result_basic_4_verify_2.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_basic_4_verify_2.append(float(latency[0: -2]) * 1000)
    else:
        result_basic_4_verify_2.append(float(latency[0: -2]) * 0.001)


metadata_basic_4_verify_3 = []
result_str_basic_4_verify_3 = []
result_basic_4_verify_3 = []

with open('./mariadb_basic/basic/4/verify/data3.txt', 'r') as f:
    for line in f:
        metadata_basic_4_verify_3 = list(line.strip(' ').split(','))

result_str_basic_4_verify_3 = metadata_basic_4_verify_3[0].split()
index = list(range(1, len(result_str_basic_4_verify_3) + 1))

for latency in result_str_basic_4_verify_3:
    if latency[-2] == 'm':
        result_basic_4_verify_3.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_basic_4_verify_3.append(float(latency[0: -2]) * 1000)
    else:
        result_basic_4_verify_3.append(float(latency[0: -2]) * 0.001)




metadata_mariadb_1_login_0 = []
result_str_mariadb_1_login_0 = []
result_mariadb_1_login_0 = []

with open('./mariadb_basic/mariadb/1/login/data0.txt', 'r') as f:
    for line in f:
        metadata_mariadb_1_login_0 = list(line.strip(' ').split(','))

result_str_mariadb_1_login_0 = metadata_mariadb_1_login_0[0].split()
index = list(range(1, len(result_str_mariadb_1_login_0) + 1))

for latency in result_str_mariadb_1_login_0:
    if latency[-2] == 'm':
        result_mariadb_1_login_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_mariadb_1_login_0.append(float(latency[0: -2]) * 1000)
    else:
        result_mariadb_1_login_0.append(float(latency[0: -2]) * 0.001)



metadata_mariadb_4_login_0 = []
result_str_mariadb_4_login_0 = []
result_mariadb_4_login_0 = []

with open('./mariadb_basic/mariadb/4/login/data0.txt', 'r') as f:
    for line in f:
        metadata_mariadb_4_login_0 = list(line.strip(' ').split(','))

result_str_mariadb_4_login_0 = metadata_mariadb_4_login_0[0].split()
index = list(range(1, len(result_str_mariadb_4_login_0) + 1))

for latency in result_str_mariadb_4_login_0:
    if latency[-2] == 'm':
        result_mariadb_4_login_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_mariadb_4_login_0.append(float(latency[0: -2]) * 1000)
    else:
        result_mariadb_4_login_0.append(float(latency[0: -2]) * 0.001)


metadata_mariadb_4_login_1 = []
result_str_mariadb_4_login_1 = []
result_mariadb_4_login_1 = []

with open('./mariadb_basic/mariadb/4/login/data1.txt', 'r') as f:
    for line in f:
        metadata_mariadb_4_login_1 = list(line.strip(' ').split(','))

result_str_mariadb_4_login_1 = metadata_mariadb_4_login_1[0].split()
index = list(range(1, len(result_str_mariadb_4_login_1) + 1))

for latency in result_str_mariadb_4_login_1:
    if latency[-2] == 'm':
        result_mariadb_4_login_1.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_mariadb_4_login_1.append(float(latency[0: -2]) * 1000)
    else:
        result_mariadb_4_login_1.append(float(latency[0: -2]) * 0.001)

metadata_mariadb_4_login_2 = []
result_str_mariadb_4_login_2 = []
result_mariadb_4_login_2 = []

with open('./mariadb_basic/mariadb/4/login/data2.txt', 'r') as f:
    for line in f:
        metadata_mariadb_4_login_2 = list(line.strip(' ').split(','))

result_str_mariadb_4_login_2 = metadata_mariadb_4_login_2[0].split()
index = list(range(1, len(result_str_mariadb_4_login_2) + 1))

for latency in result_str_mariadb_4_login_2:
    if latency[-2] == 'm':
        result_mariadb_4_login_2.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_mariadb_4_login_2.append(float(latency[0: -2]) * 1000)
    else:
        result_mariadb_4_login_2.append(float(latency[0: -2]) * 0.001)

metadata_mariadb_4_login_3 = []
result_str_mariadb_4_login_3 = []
result_mariadb_4_login_3 = []

with open('./mariadb_basic/mariadb/4/login/data3.txt', 'r') as f:
    for line in f:
        metadata_mariadb_4_login_3 = list(line.strip(' ').split(','))

result_str_mariadb_4_login_3 = metadata_mariadb_4_login_3[0].split()
index = list(range(1, len(result_str_mariadb_4_login_3) + 1))

for latency in result_str_mariadb_4_login_3:
    if latency[-2] == 'm':
        result_mariadb_4_login_3.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_mariadb_4_login_3.append(float(latency[0: -2]) * 1000)
    else:
        result_mariadb_4_login_3.append(float(latency[0: -2]) * 0.001)


metadata_mariadb_1_verify_0 = []
result_str_mariadb_1_verify_0 = []
result_mariadb_1_verify_0 = []

with open('./mariadb_basic/mariadb/1/verify/data0.txt', 'r') as f:
    for line in f:
        metadata_mariadb_1_verify_0 = list(line.strip(' ').split(','))

result_str_mariadb_1_verify_0 = metadata_mariadb_1_verify_0[0].split()
index = list(range(1, len(result_str_mariadb_1_verify_0) + 1))

for latency in result_str_mariadb_1_verify_0:
    if latency[-2] == 'm':
        result_mariadb_1_verify_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_mariadb_1_verify_0.append(float(latency[0: -2]) * 1000)
    else:
        result_mariadb_1_verify_0.append(float(latency[0: -2]) * 0.001)


metadata_mariadb_4_verify_0 = []
result_str_mariadb_4_verify_0 = []
result_mariadb_4_verify_0 = []

with open('./mariadb_basic/mariadb/4/verify/data0.txt', 'r') as f:
    for line in f:
        metadata_mariadb_4_verify_0 = list(line.strip(' ').split(','))

result_str_mariadb_4_verify_0 = metadata_mariadb_4_verify_0[0].split()
index = list(range(1, len(result_str_mariadb_4_verify_0) + 1))

for latency in result_str_mariadb_4_verify_0:
    if latency[-2] == 'm':
        result_mariadb_4_verify_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_mariadb_4_verify_0.append(float(latency[0: -2]) * 1000)
    else:
        result_mariadb_4_verify_0.append(float(latency[0: -2]) * 0.001)


metadata_mariadb_4_verify_1 = []
result_str_mariadb_4_verify_1 = []
result_mariadb_4_verify_1 = []

with open('./mariadb_basic/mariadb/4/verify/data1.txt', 'r') as f:
    for line in f:
        metadata_mariadb_4_verify_1 = list(line.strip(' ').split(','))

result_str_mariadb_4_verify_1 = metadata_mariadb_4_verify_1[0].split()
index = list(range(1, len(result_str_mariadb_4_verify_1) + 1))

for latency in result_str_mariadb_4_verify_1:
    if latency[-2] == 'm':
        result_mariadb_4_verify_1.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_mariadb_4_verify_1.append(float(latency[0: -2]) * 1000)
    else:
        result_mariadb_4_verify_1.append(float(latency[0: -2]) * 0.001)


metadata_mariadb_4_verify_2 = []
result_str_mariadb_4_verify_2 = []
result_mariadb_4_verify_2 = []

with open('./mariadb_basic/mariadb/4/verify/data2.txt', 'r') as f:
    for line in f:
        metadata_mariadb_4_verify_2 = list(line.strip(' ').split(','))

result_str_mariadb_4_verify_2 = metadata_mariadb_4_verify_2[0].split()
index = list(range(1, len(result_str_mariadb_4_verify_2) + 1))

for latency in result_str_mariadb_4_verify_2:
    if latency[-2] == 'm':
        result_mariadb_4_verify_2.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_mariadb_4_verify_2.append(float(latency[0: -2]) * 1000)
    else:
        result_mariadb_4_verify_2.append(float(latency[0: -2]) * 0.001)


metadata_mariadb_4_verify_3 = []
result_str_mariadb_4_verify_3 = []
result_mariadb_4_verify_3 = []

with open('./mariadb_basic/mariadb/4/verify/data3.txt', 'r') as f:
    for line in f:
        metadata_mariadb_4_verify_3 = list(line.strip(' ').split(','))

result_str_mariadb_4_verify_3 = metadata_mariadb_4_verify_3[0].split()
index = list(range(1, len(result_str_mariadb_4_verify_3) + 1))

for latency in result_str_mariadb_4_verify_3:
    if latency[-2] == 'm':
        result_mariadb_4_verify_3.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_mariadb_4_verify_3.append(float(latency[0: -2]) * 1000)
    else:
        result_mariadb_4_verify_3.append(float(latency[0: -2]) * 0.001)





metadata_redis_1_login_0 = []
result_str_redis_1_login_0 = []
result_redis_1_login_0 = []

with open('./redis/redis/1/login/data0.txt', 'r') as f:
    for line in f:
        metadata_redis_1_login_0 = list(line.strip(' ').split(','))

result_str_redis_1_login_0 = metadata_redis_1_login_0[0].split()
index = list(range(1, len(result_str_redis_1_login_0) + 1))

for latency in result_str_redis_1_login_0:
    if latency[-2] == 'm':
        result_redis_1_login_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_redis_1_login_0.append(float(latency[0: -2]) * 1000)
    else:
        result_redis_1_login_0.append(float(latency[0: -2]) * 0.001)


metadata_redis_4_login_0 = []
result_str_redis_4_login_0 = []
result_redis_4_login_0 = []

with open('./redis/redis/4/login/data0.txt', 'r') as f:
    for line in f:
        metadata_redis_4_login_0 = list(line.strip(' ').split(','))

result_str_redis_4_login_0 = metadata_redis_4_login_0[0].split()
index = list(range(1, len(result_str_redis_4_login_0) + 1))

for latency in result_str_redis_4_login_0:
    if latency[-2] == 'm':
        result_redis_4_login_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_redis_4_login_0.append(float(latency[0: -2]) * 1000)
    else:
        result_redis_4_login_0.append(float(latency[0: -2]) * 0.001)


metadata_redis_4_login_1 = []
result_str_redis_4_login_1 = []
result_redis_4_login_1 = []

with open('./redis/redis/4/login/data1.txt', 'r') as f:
    for line in f:
        metadata_redis_4_login_1 = list(line.strip(' ').split(','))

result_str_redis_4_login_1 = metadata_redis_4_login_1[0].split()
index = list(range(1, len(result_str_redis_4_login_1) + 1))

for latency in result_str_redis_4_login_1:
    if latency[-2] == 'm':
        result_redis_4_login_1.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_redis_4_login_1.append(float(latency[0: -2]) * 1000)
    else:
        result_redis_4_login_1.append(float(latency[0: -2]) * 0.001)


metadata_redis_4_login_2 = []
result_str_redis_4_login_2 = []
result_redis_4_login_2 = []

with open('./redis/redis/4/login/data2.txt', 'r') as f:
    for line in f:
        metadata_redis_4_login_2 = list(line.strip(' ').split(','))

result_str_redis_4_login_2 = metadata_redis_4_login_2[0].split()
index = list(range(1, len(result_str_redis_4_login_2) + 1))

for latency in result_str_redis_4_login_2:
    if latency[-2] == 'm':
        result_redis_4_login_2.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_redis_4_login_2.append(float(latency[0: -2]) * 1000)
    else:
        result_redis_4_login_2.append(float(latency[0: -2]) * 0.001)


metadata_redis_4_login_3 = []
result_str_redis_4_login_3 = []
result_redis_4_login_3 = []

with open('./redis/redis/4/login/data3.txt', 'r') as f:
    for line in f:
        metadata_redis_4_login_3 = list(line.strip(' ').split(','))

result_str_redis_4_login_3 = metadata_redis_4_login_3[0].split()
index = list(range(1, len(result_str_redis_4_login_3) + 1))

for latency in result_str_redis_4_login_3:
    if latency[-2] == 'm':
        result_redis_4_login_3.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_redis_4_login_3.append(float(latency[0: -2]) * 1000)
    else:
        result_redis_4_login_3.append(float(latency[0: -2]) * 0.001)



metadata_redis_1_verify_0 = []
result_str_redis_1_verify_0 = []
result_redis_1_verify_0 = []

with open('./redis/redis/1/verify/data0.txt', 'r') as f:
    for line in f:
        metadata_redis_1_verify_0 = list(line.strip(' ').split(','))

result_str_redis_1_verify_0 = metadata_redis_1_verify_0[0].split()
index = list(range(1, len(result_str_redis_1_verify_0) + 1))

for latency in result_str_redis_1_verify_0:
    if latency[-2] == 'm':
        result_redis_1_verify_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_redis_1_verify_0.append(float(latency[0: -2]) * 1000)
    else:
        result_redis_1_verify_0.append(float(latency[0: -2]) * 0.001)


metadata_redis_4_verify_0 = []
result_str_redis_4_verify_0 = []
result_redis_4_verify_0 = []

with open('./redis/redis/4/verify/data0.txt', 'r') as f:
    for line in f:
        metadata_redis_4_verify_0 = list(line.strip(' ').split(','))

result_str_redis_4_verify_0 = metadata_redis_4_verify_0[0].split()
index = list(range(1, len(result_str_redis_4_verify_0) + 1))

for latency in result_str_redis_4_verify_0:
    if latency[-2] == 'm':
        result_redis_4_verify_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_redis_4_verify_0.append(float(latency[0: -2]) * 1000)
    else:
        result_redis_4_verify_0.append(float(latency[0: -2]) * 0.001)


metadata_redis_4_verify_1 = []
result_str_redis_4_verify_1 = []
result_redis_4_verify_1 = []

with open('./redis/redis/4/verify/data1.txt', 'r') as f:
    for line in f:
        metadata_redis_4_verify_1 = list(line.strip(' ').split(','))

result_str_redis_4_verify_1 = metadata_redis_4_verify_1[0].split()
index = list(range(1, len(result_str_redis_4_verify_1) + 1))

for latency in result_str_redis_4_verify_1:
    if latency[-2] == 'm':
        result_redis_4_verify_1.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_redis_4_verify_1.append(float(latency[0: -2]) * 1000)
    else:
        result_redis_4_verify_1.append(float(latency[0: -2]) * 0.001)


metadata_redis_4_verify_2 = []
result_str_redis_4_verify_2 = []
result_redis_4_verify_2 = []

with open('./redis/redis/4/verify/data2.txt', 'r') as f:
    for line in f:
        metadata_redis_4_verify_2 = list(line.strip(' ').split(','))

result_str_redis_4_verify_2 = metadata_redis_4_verify_2[0].split()
index = list(range(1, len(result_str_redis_4_verify_2) + 1))

for latency in result_str_redis_4_verify_2:
    if latency[-2] == 'm':
        result_redis_4_verify_2.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_redis_4_verify_2.append(float(latency[0: -2]) * 1000)
    else:
        result_redis_4_verify_2.append(float(latency[0: -2]) * 0.001)


metadata_redis_4_verify_3 = []
result_str_redis_4_verify_3 = []
result_redis_4_verify_3 = []

with open('./redis/redis/4/verify/data3.txt', 'r') as f:
    for line in f:
        metadata_redis_4_verify_3 = list(line.strip(' ').split(','))

result_str_redis_4_verify_3 = metadata_redis_4_verify_3[0].split()
index = list(range(1, len(result_str_redis_4_verify_3) + 1))

for latency in result_str_redis_4_verify_3:
    if latency[-2] == 'm':
        result_redis_4_verify_3.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_redis_4_verify_3.append(float(latency[0: -2]) * 1000)
    else:
        result_redis_4_verify_3.append(float(latency[0: -2]) * 0.001)





metadata_chord_dht_1_login_0 = []
result_str_chord_dht_1_login_0 = []
result_chord_dht_1_login_0 = []

with open('./chord-dht/chord-dht/1/login/data0.txt', 'r') as f:
    for line in f:
        metadata_chord_dht_1_login_0 = list(line.strip(' ').split(','))

result_str_chord_dht_1_login_0 = metadata_chord_dht_1_login_0[0].split()
index = list(range(1, len(result_str_chord_dht_1_login_0) + 1))

for latency in result_str_chord_dht_1_login_0:
    if latency[-2] == 'm':
        result_chord_dht_1_login_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_chord_dht_1_login_0.append(float(latency[0: -2]) * 1000)
    else:
        result_chord_dht_1_login_0.append(float(latency[0: -2]) * 0.001)


metadata_chord_dht_4_login_0 = []
result_str_chord_dht_4_login_0 = []
result_chord_dht_4_login_0 = []

with open('./chord-dht/chord-dht/4/login/data0.txt', 'r') as f:
    for line in f:
        metadata_chord_dht_4_login_0 = list(line.strip(' ').split(','))

result_str_chord_dht_4_login_0 = metadata_chord_dht_4_login_0[0].split()
index = list(range(1, len(result_str_chord_dht_4_login_0) + 1))

for latency in result_str_chord_dht_4_login_0:
    if latency[-2] == 'm':
        result_chord_dht_4_login_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_chord_dht_4_login_0.append(float(latency[0: -2]) * 1000)
    else:
        result_chord_dht_4_login_0.append(float(latency[0: -2]) * 0.001)


metadata_chord_dht_4_login_1 = []
result_str_chord_dht_4_login_1 = []
result_chord_dht_4_login_1 = []

with open('./chord-dht/chord-dht/4/login/data1.txt', 'r') as f:
    for line in f:
        metadata_chord_dht_4_login_1 = list(line.strip(' ').split(','))

result_str_chord_dht_4_login_1 = metadata_chord_dht_4_login_1[0].split()
index = list(range(1, len(result_str_chord_dht_4_login_1) + 1))

for latency in result_str_chord_dht_4_login_1:
    if latency[-2] == 'm':
        result_chord_dht_4_login_1.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_chord_dht_4_login_1.append(float(latency[0: -2]) * 1000)
    else:
        result_chord_dht_4_login_1.append(float(latency[0: -2]) * 0.001)


metadata_chord_dht_4_login_2 = []
result_str_chord_dht_4_login_2 = []
result_chord_dht_4_login_2 = []

with open('./chord-dht/chord-dht/4/login/data2.txt', 'r') as f:
    for line in f:
        metadata_chord_dht_4_login_2 = list(line.strip(' ').split(','))

result_str_chord_dht_4_login_2 = metadata_chord_dht_4_login_2[0].split()
index = list(range(1, len(result_str_chord_dht_4_login_2) + 1))

for latency in result_str_chord_dht_4_login_2:
    if latency[-2] == 'm':
        result_chord_dht_4_login_2.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_chord_dht_4_login_2.append(float(latency[0: -2]) * 1000)
    else:
        result_chord_dht_4_login_2.append(float(latency[0: -2]) * 0.001)


metadata_chord_dht_4_login_3 = []
result_str_chord_dht_4_login_3 = []
result_chord_dht_4_login_3 = []

with open('./chord-dht/chord-dht/4/login/data3.txt', 'r') as f:
    for line in f:
        metadata_chord_dht_4_login_3 = list(line.strip(' ').split(','))

result_str_chord_dht_4_login_3 = metadata_chord_dht_4_login_3[0].split()
index = list(range(1, len(result_str_chord_dht_4_login_3) + 1))

for latency in result_str_chord_dht_4_login_3:
    if latency[-2] == 'm':
        result_chord_dht_4_login_3.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_chord_dht_4_login_3.append(float(latency[0: -2]) * 1000)
    else:
        result_chord_dht_4_login_3.append(float(latency[0: -2]) * 0.001)



metadata_chord_dht_1_verify_0 = []
result_str_chord_dht_1_verify_0 = []
result_chord_dht_1_verify_0 = []

with open('./chord-dht/chord-dht/1/verify/data0.txt', 'r') as f:
    for line in f:
        metadata_chord_dht_1_verify_0 = list(line.strip(' ').split(','))

result_str_chord_dht_1_verify_0 = metadata_chord_dht_1_verify_0[0].split()
index = list(range(1, len(result_str_chord_dht_1_verify_0) + 1))

for latency in result_str_chord_dht_1_verify_0:
    if latency[-2] == 'm':
        result_chord_dht_1_verify_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_chord_dht_1_verify_0.append(float(latency[0: -2]) * 1000)
    else:
        result_chord_dht_1_verify_0.append(float(latency[0: -2]) * 0.001)


metadata_chord_dht_4_verify_0 = []
result_str_chord_dht_4_verify_0 = []
result_chord_dht_4_verify_0 = []

with open('./chord-dht/chord-dht/4/verify/data0.txt', 'r') as f:
    for line in f:
        metadata_chord_dht_4_verify_0 = list(line.strip(' ').split(','))

result_str_chord_dht_4_verify_0 = metadata_chord_dht_4_verify_0[0].split()
index = list(range(1, len(result_str_chord_dht_4_verify_0) + 1))

for latency in result_str_chord_dht_4_verify_0:
    if latency[-2] == 'm':
        result_chord_dht_4_verify_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_chord_dht_4_verify_0.append(float(latency[0: -2]) * 1000)
    else:
        result_chord_dht_4_verify_0.append(float(latency[0: -2]) * 0.001)


metadata_chord_dht_4_verify_1 = []
result_str_chord_dht_4_verify_1 = []
result_chord_dht_4_verify_1 = []

with open('./chord-dht/chord-dht/4/verify/data1.txt', 'r') as f:
    for line in f:
        metadata_chord_dht_4_verify_1 = list(line.strip(' ').split(','))

result_str_chord_dht_4_verify_1 = metadata_chord_dht_4_verify_1[0].split()
index = list(range(1, len(result_str_chord_dht_4_verify_1) + 1))

for latency in result_str_chord_dht_4_verify_1:
    if latency[-2] == 'm':
        result_chord_dht_4_verify_1.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_chord_dht_4_verify_1.append(float(latency[0: -2]) * 1000)
    else:
        result_chord_dht_4_verify_1.append(float(latency[0: -2]) * 0.001)


metadata_chord_dht_4_verify_2 = []
result_str_chord_dht_4_verify_2 = []
result_chord_dht_4_verify_2 = []

with open('./chord-dht/chord-dht/4/verify/data2.txt', 'r') as f:
    for line in f:
        metadata_chord_dht_4_verify_2 = list(line.strip(' ').split(','))

result_str_chord_dht_4_verify_2 = metadata_chord_dht_4_verify_2[0].split()
index = list(range(1, len(result_str_chord_dht_4_verify_2) + 1))

for latency in result_str_chord_dht_4_verify_2:
    if latency[-2] == 'm':
        result_chord_dht_4_verify_2.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_chord_dht_4_verify_2.append(float(latency[0: -2]) * 1000)
    else:
        result_chord_dht_4_verify_2.append(float(latency[0: -2]) * 0.001)


metadata_chord_dht_4_verify_3 = []
result_str_chord_dht_4_verify_3 = []
result_chord_dht_4_verify_3 = []

with open('./chord-dht/chord-dht/4/verify/data3.txt', 'r') as f:
    for line in f:
        metadata_chord_dht_4_verify_3 = list(line.strip(' ').split(','))

result_str_chord_dht_4_verify_3 = metadata_chord_dht_4_verify_3[0].split()
index = list(range(1, len(result_str_chord_dht_4_verify_3) + 1))

for latency in result_str_chord_dht_4_verify_3:
    if latency[-2] == 'm':
        result_chord_dht_4_verify_3.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_chord_dht_4_verify_3.append(float(latency[0: -2]) * 1000)
    else:
        result_chord_dht_4_verify_3.append(float(latency[0: -2]) * 0.001)


# 1: login basic, 2: verify basic, 3: login mariadb, 4: verify mariadb, 5: login redis, 6: verify redis, 7: login chord, 8: verify chord
plot_option = 1

if plot_option == 1:
    labels = 'Thread 1', 'Thread 2', 'Thread 3', 'Thread 4'
    plt.boxplot([result_basic_4_login_0[9:], result_basic_4_login_1[9:], result_basic_4_login_2[9:], result_basic_4_login_3[9:]], labels = labels, showmeans=True, sym='' )
    plt.title("Basic - login")
    plt.xlabel('request')
    plt.ylabel('latency/ms')
    plt.show()
elif plot_option == 2:
    labels = 'Thread 1', 'Thread 2', 'Thread 3', 'Thread 4'
    plt.boxplot([result_basic_4_verify_0[9:], result_basic_4_verify_1[9:], result_basic_4_verify_2[9:],
                 result_basic_4_verify_3[9:]], labels=labels, showmeans=True, sym='')
    plt.title("Basic - verify")
    plt.xlabel('request')
    plt.ylabel('latency/ms')
    plt.show()
elif plot_option == 3:
    labels = 'Thread 1', 'Thread 2', 'Thread 3', 'Thread 4'
    plt.boxplot([result_mariadb_4_login_0[9:], result_mariadb_4_login_1[9:], result_mariadb_4_login_2[9:],
                 result_mariadb_4_login_3[9:]], labels = labels, showmeans=True, sym='' )
    plt.title("Mariadb - login")
    plt.xlabel('request')
    plt.ylabel('latency/ms')
    plt.show()
elif plot_option == 4:
    labels = 'Thread 1', 'Thread 2', 'Thread 3', 'Thread 4'
    plt.boxplot([result_mariadb_4_verify_0[9:], result_mariadb_4_verify_1[9:], result_mariadb_4_verify_2[9:],
                 result_mariadb_4_verify_3[9:]], labels=labels, showmeans=True, sym='')
    plt.title("Mariadb - verify")
    plt.xlabel('request')
    plt.ylabel('latency/ms')
    plt.show()
elif plot_option == 5:
    labels = 'Thread 1', 'Thread 2', 'Thread 3', 'Thread 4'
    plt.boxplot([result_redis_4_login_0[9:], result_redis_4_login_1[9:], result_redis_4_login_2[9:],
                 result_redis_4_login_3[9:]], labels = labels, showmeans=True, sym='' )
    plt.title("Redis - login")
    plt.xlabel('request')
    plt.ylabel('latency/ms')
    plt.show()
elif plot_option == 6:
    labels = 'Thread 1', 'Thread 2', 'Thread 3', 'Thread 4'
    plt.boxplot([result_redis_4_verify_0[9:], result_redis_4_verify_1[9:], result_redis_4_verify_2[9:],
                 result_redis_4_verify_3[9:]], labels=labels, showmeans=True, sym='')
    plt.title("Redis - verify")
    plt.xlabel('request')
    plt.ylabel('latency/ms')
    plt.show()
elif plot_option == 7:
    labels = 'Thread 1', 'Thread 2', 'Thread 3', 'Thread 4'
    plt.boxplot([result_chord_dht_4_login_0[9:], result_chord_dht_4_login_1[9:], result_chord_dht_4_login_2[9:],
                 result_chord_dht_4_login_3[9:]], labels = labels, showmeans=True, sym='' )
    plt.title("Chord_dht - login")
    plt.xlabel('request')
    plt.ylabel('latency/ms')
    plt.show()
elif plot_option == 8:
    labels = 'Thread 1', 'Thread 2', 'Thread 3', 'Thread 4'
    plt.boxplot([result_chord_dht_4_verify_0[9:], result_chord_dht_4_verify_1[9:], result_chord_dht_4_verify_2[9:],
                 result_chord_dht_4_verify_3[9:]], labels=labels, showmeans=True, sym='')
    plt.title("Chord_dht - verify")
    plt.xlabel('request')
    plt.ylabel('latency/ms')
    plt.show()
