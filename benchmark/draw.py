import matplotlib.pyplot as plt

metadata_basic_1_login_0 = []
result_str_basic_1_login_0 = []
result_basic_1_login_0 = []

with open('./mariadb_basic/basic/1/login/data0.txt', 'r') as f:
    for line in f:
        metadata_basic_1_login_0 = list(line.strip(' ').split(','))

result_str_basic_1_login_0 = metadata_basic_1_login_0[0].split()

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

for latency in result_str_basic_4_login_0:
    if latency[-2] == 'm':
        result_basic_4_login_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_basic_4_login_0.append(float(latency[0: -2]) * 1000)
    else:
        result_basic_4_login_0.append(float(latency[0: -2]) * 0.001)


metadata_basic_1_verify_0 = []
result_str_basic_1_verify_0 = []
result_basic_1_verify_0 = []

with open('./mariadb_basic/basic/1/verify/data0.txt', 'r') as f:
    for line in f:
        metadata_basic_1_verify_0 = list(line.strip(' ').split(','))

result_str_basic_1_verify_0 = metadata_basic_1_verify_0[0].split()

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

for latency in result_str_basic_4_verify_0:
    if latency[-2] == 'm':
        result_basic_4_verify_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_basic_4_verify_0.append(float(latency[0: -2]) * 1000)
    else:
        result_basic_4_verify_0.append(float(latency[0: -2]) * 0.001)




metadata_mariadb_1_login_0 = []
result_str_mariadb_1_login_0 = []
result_mariadb_1_login_0 = []

with open('./mariadb_basic/mariadb/1/login/data0.txt', 'r') as f:
    for line in f:
        metadata_mariadb_1_login_0 = list(line.strip(' ').split(','))

result_str_mariadb_1_login_0 = metadata_mariadb_1_login_0[0].split()

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

for latency in result_str_mariadb_4_login_0:
    if latency[-2] == 'm':
        result_mariadb_4_login_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_mariadb_4_login_0.append(float(latency[0: -2]) * 1000)
    else:
        result_mariadb_4_login_0.append(float(latency[0: -2]) * 0.001)


metadata_mariadb_1_verify_0 = []
result_str_mariadb_1_verify_0 = []
result_mariadb_1_verify_0 = []

with open('./mariadb_basic/mariadb/1/verify/data0.txt', 'r') as f:
    for line in f:
        metadata_mariadb_1_verify_0 = list(line.strip(' ').split(','))

result_str_mariadb_1_verify_0 = metadata_mariadb_1_verify_0[0].split()

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

for latency in result_str_mariadb_4_verify_0:
    if latency[-2] == 'm':
        result_mariadb_4_verify_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_mariadb_4_verify_0.append(float(latency[0: -2]) * 1000)
    else:
        result_mariadb_4_verify_0.append(float(latency[0: -2]) * 0.001)





metadata_redis_1_login_0 = []
result_str_redis_1_login_0 = []
result_redis_1_login_0 = []

with open('./redis/redis/1/login/data0.txt', 'r') as f:
    for line in f:
        metadata_redis_1_login_0 = list(line.strip(' ').split(','))

result_str_redis_1_login_0 = metadata_redis_1_login_0[0].split()

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

for latency in result_str_redis_4_login_0:
    if latency[-2] == 'm':
        result_redis_4_login_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_redis_4_login_0.append(float(latency[0: -2]) * 1000)
    else:
        result_redis_4_login_0.append(float(latency[0: -2]) * 0.001)



metadata_redis_1_verify_0 = []
result_str_redis_1_verify_0 = []
result_redis_1_verify_0 = []

with open('./redis/redis/1/verify/data0.txt', 'r') as f:
    for line in f:
        metadata_redis_1_verify_0 = list(line.strip(' ').split(','))

result_str_redis_1_verify_0 = metadata_redis_1_verify_0[0].split()

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

for latency in result_str_redis_4_verify_0:
    if latency[-2] == 'm':
        result_redis_4_verify_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_redis_4_verify_0.append(float(latency[0: -2]) * 1000)
    else:
        result_redis_4_verify_0.append(float(latency[0: -2]) * 0.001)





metadata_chord_dht_1_login_0 = []
result_str_chord_dht_1_login_0 = []
result_chord_dht_1_login_0 = []

with open('./chord-dht/chord-dht/1/login/data0.txt', 'r') as f:
    for line in f:
        metadata_chord_dht_1_login_0 = list(line.strip(' ').split(','))

result_str_chord_dht_1_login_0 = metadata_chord_dht_1_login_0[0].split()

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

for latency in result_str_chord_dht_4_login_0:
    if latency[-2] == 'm':
        result_chord_dht_4_login_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_chord_dht_4_login_0.append(float(latency[0: -2]) * 1000)
    else:
        result_chord_dht_4_login_0.append(float(latency[0: -2]) * 0.001)



metadata_chord_dht_1_verify_0 = []
result_str_chord_dht_1_verify_0 = []
result_chord_dht_1_verify_0 = []

with open('./chord-dht/chord-dht/1/verify/data0.txt', 'r') as f:
    for line in f:
        metadata_chord_dht_1_verify_0 = list(line.strip(' ').split(','))

result_str_chord_dht_1_verify_0 = metadata_chord_dht_1_verify_0[0].split()

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

for latency in result_str_chord_dht_4_verify_0:
    if latency[-2] == 'm':
        result_chord_dht_4_verify_0.append(float(latency[0: -2]))
    elif '0' <= latency[-2] <= '9':
        result_chord_dht_4_verify_0.append(float(latency[0: -2]) * 1000)
    else:
        result_chord_dht_4_verify_0.append(float(latency[0: -2]) * 0.001)


# 1: login thread 1, 2: verify thread 1, 3: login thread 4, 4: verify thread 4
plot_option = 3

if plot_option == 1:
    index_basic = list(range(1, len(result_basic_1_login_0) + 1))
    index_mariadb = list(range(1, len(result_mariadb_1_login_0) + 1))
    index_redis = list(range(1, len(result_redis_1_login_0) + 1))
    index_chord_dht = list(range(1, len(result_chord_dht_1_login_0) + 1))
    plt.plot(index_basic[9:], result_basic_1_login_0[9:])
    plt.plot(index_mariadb[9:], result_mariadb_1_login_0[9:])
    plt.plot(index_redis[9:], result_redis_1_login_0[9:])
    plt.plot(index_chord_dht[9:], result_chord_dht_1_login_0[9:])
    plt.legend(['Basic', 'MariaDB Galera Cluster', 'Redis Cluster', 'Chord_dht'], loc = 'upper left')
    plt.title("Login - 1 thread")
    plt.xlabel('request')
    plt.ylabel('latency/ms')
    plt.show()
elif plot_option == 2:
    index_basic = list(range(1, len(result_basic_1_verify_0) + 1))
    index_mariadb = list(range(1, len(result_mariadb_1_verify_0) + 1))
    index_redis = list(range(1, len(result_redis_1_verify_0) + 1))
    index_chord_dht = list(range(1, len(result_chord_dht_1_verify_0) + 1))
    plt.plot(index_basic[9:], result_basic_1_verify_0[9:])
    plt.plot(index_mariadb[9:], result_mariadb_1_verify_0[9:])
    plt.plot(index_redis[9:], result_redis_1_verify_0[9:])
    plt.plot(index_chord_dht[9:], result_chord_dht_1_verify_0[9:])
    plt.legend(['Basic', 'MariaDB Galera Cluster', 'Redis Cluster', 'Chord_dht'], loc='upper left')
    plt.title("Verify - 1 thread")
    plt.xlabel('request')
    plt.ylabel('latency/ms')
    plt.show()
elif plot_option == 3:
    index_basic = list(range(1, len(result_basic_4_login_0) + 1))
    index_mariadb = list(range(1, len(result_mariadb_4_login_0) + 1))
    index_redis = list(range(1, len(result_redis_4_login_0) + 1))
    index_chord_dht = list(range(1, len(result_chord_dht_4_login_0) + 1))
    plt.plot(index_basic[9:], result_basic_4_login_0[9:])
    plt.plot(index_mariadb[9:], result_mariadb_4_login_0[9:])
    plt.plot(index_redis[9:], result_redis_4_login_0[9:])
    plt.plot(index_chord_dht[9:], result_chord_dht_4_login_0[9:])
    plt.legend(['Basic', 'MariaDB Galera Cluster', 'Redis Cluster', 'Chord_dht'], loc='upper left')
    plt.title("Login - 4 threads")
    plt.xlabel('request')
    plt.ylabel('latency/ms')
    plt.show()
elif plot_option == 4:
    index_basic = list(range(1, len(result_basic_4_verify_0) + 1))
    index_mariadb = list(range(1, len(result_mariadb_4_verify_0) + 1))
    index_redis = list(range(1, len(result_redis_4_verify_0) + 1))
    index_chord_dht = list(range(1, len(result_chord_dht_4_verify_0) + 1))
    plt.plot(index_basic[9:], result_basic_4_verify_0[9:])
    # plt.plot(index_mariadb[9:], result_mariadb_4_verify_0[9:])
    plt.plot(index_redis[9:], result_redis_4_verify_0[9:])
    plt.plot(index_chord_dht[9:], result_chord_dht_4_verify_0[9:])
    plt.legend(['Basic', 'Redis Cluster', 'Chord_dht'], loc='upper left')
    plt.title("Verify - 4 threads")
    plt.xlabel('request')
    plt.ylabel('latency/ms')
    plt.show()