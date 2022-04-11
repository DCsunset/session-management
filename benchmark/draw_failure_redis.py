import matplotlib.pyplot as plt

metadata_redis_4_login_0 = []
result_str_redis_4_login_0 = []
result_redis_4_login_0 = []

with open('./failure/redis_failure/4/login/data0.txt', 'r') as f:
    for line in f:
        metadata_redis_4_login_0 = list(line.strip(' ').split(','))

result_str_redis_4_login_0 = metadata_redis_4_login_0[0].split()
index_login = list(range(1, len(result_str_redis_4_login_0) + 1))
index_success_login = []
index_failure_login = []
num_login = 1
result_login_success = []
result_login_failure = []

for latency in result_str_redis_4_login_0:
    if latency[0] == '-':
        index_failure_login.append(num_login)

        if latency[-2] == 'm':
            result_login_failure.append(float(latency[1: -2]) * 0.001)
        elif '0' <= latency[-2] <= '9':
            result_login_failure.append(float(latency[1: -2]))
        else:
            result_login_failure.append(float(latency[1: -2]) * 0.000001)

    else:
        index_success_login.append(num_login)

        if latency[-2] == 'm':
            result_login_success.append(float(latency[0: -2]) * 0.001)
        elif '0' <= latency[-2] <= '9':
            result_login_success.append(float(latency[0: -2]))
        else:
            result_login_success.append(float(latency[0: -2]) * 0.000001)

    num_login += 1

    '''if num_login > 100:
        break'''

metadata_redis_4_verify_0 = []
result_str_redis_4_verify_0 = []
result_redis_4_verify_0 = []

with open('./failure/redis_failure/4/verify/data0.txt', 'r') as f:
    for line in f:
        metadata_redis_4_verify_0 = list(line.strip(' ').split(','))

result_str_redis_4_verify_0 = metadata_redis_4_verify_0[0].split()
index_verify = list(range(1, len(result_str_redis_4_verify_0) + 1))
index_success_verify = []
index_failure_verify = []
num_verify = 1
result_verify_success = []
result_verify_failure = []

for latency in result_str_redis_4_verify_0:
    if latency[0] == '-':
        index_failure_verify.append(num_verify)

        if latency[-2] == 'm':
            result_verify_failure.append(float(latency[1: -2]))
        elif '0' <= latency[-2] <= '9':
            result_verify_failure.append(float(latency[1: -2]) * 1000)
        else:
            result_verify_failure.append(float(latency[1: -2]) * 0.001)

    else:
        index_success_verify.append(num_verify)

        if latency[-2] == 'm':
            result_verify_success.append(float(latency[0: -2]))
        elif '0' <= latency[-2] <= '9':
            result_verify_success.append(float(latency[0: -2]) * 1000)
        else:
            result_verify_success.append(float(latency[0: -2]) * 0.001)

    num_verify += 1

    '''if num_verify > 100:
        break'''

# 1: login, 2: verify
plot_option = 1

if plot_option == 1:
    plt.scatter(index_success_login, result_login_success, marker='.')
    plt.scatter(index_failure_login, result_login_failure, marker='x', color='r')
    plt.legend(['success', 'failure'], loc='upper left')
    plt.title("Redis Cluster - login - failure")
    plt.xlabel('request')
    plt.ylabel('latency/s')
    plt.show()

elif plot_option == 2:
    plt.scatter(index_success_verify, result_verify_success, marker='.')
    plt.scatter(index_failure_verify, result_verify_failure, marker='x', color='r')
    plt.legend(['success', 'failure'], loc='upper left')
    plt.title("Redis Cluster - verify - failure")
    plt.xlabel('request')
    plt.ylabel('latency/ms')
    plt.show()