#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 22:49:36 2024

@author: sakinahrosli
"""

# Coursework 2


class DecisionTree:
    def __init__(self, data):
        self.data = data

    # calculate the subset partition
    def subset_part(self, subset):
        count_1 = 0
        count_0 = 0
        # calculate the number of labels in a subset
        for i in range(len(subset)):
            if subset[i][1] == 1:
                count_1 += 1
            if subset[i][1] == 0:
                count_0 += 1

        # calculate portion of labels 0 & 1in a subset
        part_1 = count_1/len(subset)
        part_0 = count_0/len(subset)

        # return the label portion in a subset
        portion = len(subset)/len(self.data) * (1 - (part_1)**2 - (part_0)**2)

        return portion

    # method to check x and y values
    def test_case(self):
        x, labels = zip(*self.data)
        # check x is a number only
        for i in x:
            if (type(i) != int and type(i) != float):
                return False

        # check labels 0 & 1 only
        for i in labels:
            if (type(i) != int):
                return False
            if (i != 0 and i != 1):
                return False

        # check if labels consist of 0 & 1 and not only one labels
        num_labels = list(set(labels))
        # if len is < 2, there's only one label in the dataset. unable to calc midpoint
        if len(num_labels) < 2:
            return False

        # check if x consist of continuous variables
        num_x = list(set(x))
        # if len is < 2, there's only one same value in the dataset. unable to calc midpoint
        if len(num_x) < 2:
            return False

    def _findBestSplit(self):
        if (self.test_case() != False):
            # sort the data by x
            self.data = sorted(
                self.data, key=lambda row: (row[0]), reverse=False)

            # create list to store split index and gini values
            list_gini = []
            split_indexes = []

            for i in (range(len(self.data)-1)):
                # if the next continuous x is different, split and partition to subsets
                if self.data[i][0] != self.data[i+1][0]:

                    # need to calculate each midpoint
                    # split and calculate the midpoint
                    midpoint = (self.data[i][0] + self.data[i+1][0])/2
                    # print('index', i, 'midpoint', midpoint)

                    # partition the data to two subsets
                    subset1 = self.data[0:i+1]
                    subset2 = self.data[i+1:]

                    # calculate the gini from each partition
                    gini = round(self.subset_part(subset1) +
                                 (self.subset_part(subset2)), 4)
                    # print(gini)

                    # store the split index
                    split_indexes.append(i)

                    # store gini value
                    list_gini.append(gini)

            # get the index of minimum gini
            gini = min(list_gini)
            lowest_gini_index = list_gini.index(gini)

            # get split_index of lowest gini
            split_index = split_indexes[lowest_gini_index]

            # use the split_index to access the data and split
            # split is the midpoint
            split = (self.data[split_index][0] + self.data[split_index+1][0])/2
            left = self.data[0:split_index+1]
            right = self.data[split_index+1:]

            return gini, split, left, right

        else:
            return False
