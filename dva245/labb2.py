

import random
import time
import pandas as pd


def max_subsequence1(S):
    maxSum = 0
    # iterate through all possible left indices for subsequences
    for i in range(len(S)):
        # iterate trough all possible right indices for subsequences
        for j in range(i, len(S)):
            # sum from i to j
            testSum = 0
            for k in range(i, j + 1):
                testSum += S[k]
            if testSum > maxSum:
                # store if largest so far
                maxSum = testSum
    return maxSum


def max_subsequence2(S):
    maxSum = 0
    # iterate through all possible left indices for subsequences
    for i in range(len(S)):
        # iterate trough all possible right indices for subsequences,
        # while summing the values
        testSum = 0
        for j in range(i, len(S)):
            # sum from i to j
            testSum += S[j]
            if testSum > maxSum:
                # store if largest so far
                maxSum = testSum
    return maxSum


def max_subsequence3(S):
    maxSum = 0
    testSum = 0
    # iterate through the list
    for i in range(len(S)):
        # sum (test all possible right indices of the list)
        testSum += S[i]
        if testSum > maxSum:
            # store if largest so far
            maxSum = testSum
        # if negative we start with a new left index
        if testSum < 0:
            testSum = 0
    return maxSum


list_lengths1 = [300, 350, 400,650,780,820,920,1050,1200]
list_lengths2 = [5120,6000,7230,8400,9600,1280 * 16]
list_lengths3 = [3000000,4000000,5000000,6000000,7000000,8000000,9000000,10000000,11000000,12000000]


def time_max_subsequence_CPU(function, list_length):  # tests the real-time elapsed
    # time during function execution for each length
    #random.seed(5)  # the results of the timing tests will always be the same, even if you run the tests multiple times,
    # which can make it easier to compare the performance of different algoritms/functrions.
    # this is needed for the sample for the graphs

    # generate a list of the current specified lengths with random numbers
    test_list = random.sample(range(-100000000, 100000001), list_length)
    #  record CPU time
    time_prior = time.process_time()
    #  call function
    function(test_list)
    #  calculates the final CPU time
    time_duration = time.process_time() - time_prior
    #  returns the end time
    return time_duration


# print(time_max_subsequence_real_time(max_subsequence1, list_length))  <--- for one time usage without list of lengths

def time_max_subsequence_list_CPU(fun, list_lengths):  # real-time speed with many lengths in a list
    results = []  # creates the list that will be used to meassure the time of each element
    for length in list_lengths:  # loops through the list with different example of lengths that will be tested
        results.append(time_max_subsequence_CPU(fun, length))  # calls thje function for each length
    return results



results1 = time_max_subsequence_list_CPU(max_subsequence1,list_lengths1)
print("-----------------------------------------")
print("Results from max_subseqeuence1 measuring CPU")
for i in range(len(list_lengths1)):
    print(f"For list of length {list_lengths1[i]}: {results1[i]} seconds")

results2 = time_max_subsequence_list_CPU(max_subsequence2,list_lengths2)
print("-----------------------------------------")
print("Results from max_subseqeuence2 Measuring CPU speed")
for i in range(len(list_lengths2)):
    print(f"For list of length {list_lengths2[i]}: {results2[i]} seconds")

results3 = time_max_subsequence_list_CPU(max_subsequence3, list_lengths3)
print("-----------------------------------------")
print("Results from max_subseqeuence3 Measuring CPU speed")
for i in range(len(list_lengths3)):
    print(f"For list of length {list_lengths3[i]}: {results3[i]} seconds")


#  Merging 2 list variables to 1 Dataframe table and saving as CSV file
df3 = pd.DataFrame({"List length":list_lengths3,"Time(s)":results3})
df3.to_csv("results3.csv", index=False)
df2 = pd.DataFrame({"List length":list_lengths2,"Time(s)":results2})
df2.to_csv("results2.csv", index=False)
df1 = pd.DataFrame({"List length":list_lengths1,"Time(s)":results1})
df1.to_csv("results1.csv", index=False)


