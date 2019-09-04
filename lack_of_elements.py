def check_list(n, alist):
    return list({i for i in range(1, n+1)}.difference(set(alist)))

n=10
input_list=[2,3,7,4,9]

print(check_list(n, input_list))