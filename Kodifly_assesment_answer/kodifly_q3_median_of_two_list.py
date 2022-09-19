# -*- coding: utf-8 -*-
"""Kodifly_Q3_Median_of_Two_list.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/171IONeDxgTsInIvt7Q9m5PlcpyFcBShe
"""

def median_finder(nums1,nums2):
  # merging two lists and sorting them 
  # Storing the merged list in num_list
  num_list = sorted(nums1 + nums2)
  median = None
  # if the lenght of list is even
  # Then we will find the middle two index 
  # Then add them and divide by 2 to get the mean
  if len(num_list) % 2 == 0:
    middle_val_index_1 = int(len(num_list)/2 - 1) # First index
    middle_val_index_2 = int(len(num_list)/2) # Second Index
    median = (num_list[middle_val_index_1] + num_list[middle_val_index_2]) / 2 # Average the values to find the mean according to general formula
  
  # if the list is odd then getting the length of list and adding 1 into it becasue index starts at 0
  # then dividing by 2 and subtracting 1 to find the middle value which is called median
  else:
    middle_val_index = int((len(num_list)+1)/2 - 1)
    median = num_list[middle_val_index]
  
  return median

nums1 = [1,2]
nums2 = [3,4]

median_finder(nums1,nums2)

