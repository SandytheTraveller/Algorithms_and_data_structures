def subListsMaxDiff(num_list, N, k):
    # sort the array in descending order
    num_list.sort(reverse=True)

    # find the largest size of two subsets
    M = max(k, N - k)

    s1 = num_list[0:M] # the largest sub-list will contain the largest numbers
    s2 = num_list[M:]

    max_difference = sum(s1) - sum(s2)
    return s1, s2, max_difference

if __name__ == '__main__':
    num_list = [7, 10, 2, 15, 30, 5, 22]
    N = len(num_list)
    k = 3
    print(subListsMaxDiff(num_list, N, k))