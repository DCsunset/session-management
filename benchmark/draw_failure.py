import matplotlib.pyplot as plt

metadata_mariadb_4_login_0 = []
result_str_mariadb_4_login_0 = []
result_mariadb_4_login_0 = []

with open('./failure/mariadb_failure/4/login/data0.txt', 'r') as f:
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

with open('./failure/mariadb_failure/4/login/data1.txt', 'r') as f:
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

with open('./failure/mariadb_failure/4/login/data2.txt', 'r') as f:
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

with open('./failure/mariadb_failure/4/login/data3.txt', 'r') as f:
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



metadata_mariadb_4_verify_0 = []
result_str_mariadb_4_verify_0 = []
result_mariadb_4_verify_0 = []

with open('./failure/mariadb_failure/4/verify/data0.txt', 'r') as f:
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

with open('./failure/mariadb_failure/4/verify/data1.txt', 'r') as f:
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

with open('./failure/mariadb_failure/4/verify/data2.txt', 'r') as f:
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

with open('./failure/mariadb_failure/4/verify/data3.txt', 'r') as f:
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



metadata_chord_dht_4_login_0 = []
result_str_chord_dht_4_login_0 = []
result_chord_dht_4_login_0 = []

with open('./failure/chord-dht_failure/4/login/data0.txt', 'r') as f:
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

with open('./failure/chord-dht_failure/4/login/data1.txt', 'r') as f:
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

with open('./failure/chord-dht_failure/4/login/data2.txt', 'r') as f:
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

with open('./failure/chord-dht_failure/4/login/data3.txt', 'r') as f:
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




metadata_chord_dht_4_verify_0 = []
result_str_chord_dht_4_verify_0 = []
result_chord_dht_4_verify_0 = []

with open('./failure/chord-dht_failure/4/verify/data0.txt', 'r') as f:
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

with open('./failure/chord-dht_failure/4/verify/data1.txt', 'r') as f:
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

with open('./failure/chord-dht_failure/4/verify/data2.txt', 'r') as f:
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

with open('./failure/chord-dht_failure/4/verify/data3.txt', 'r') as f:
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


# 1: login, 2: verify
plot_option = 2

if plot_option == 1:
    plt.plot(index[9:], result_mariadb_4_login_0[9:])
    plt.plot(index[9:], result_chord_dht_4_login_0[9:])
    plt.legend(['mariadb', 'chord_dht'], loc='upper left')
    plt.title("Login - failure")
    plt.xlabel('request')
    plt.ylabel('latency/ms')
    plt.show()
elif plot_option == 2:
    plt.plot(index[9:], result_mariadb_4_verify_0[9:])
    plt.plot(index[9:], result_chord_dht_4_verify_0[9:])
    plt.legend(['mariadb', 'chord_dht'], loc='upper left')
    plt.title("Verify - failure")
    plt.xlabel('request')
    plt.ylabel('latency/ms')
    plt.show()