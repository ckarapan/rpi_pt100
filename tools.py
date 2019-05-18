#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Christos Karapanagiotis

"""

def find_nearest(list_,ref_resist): 
    """
    find the element in a list which is closest to a reference value
    """
    resist = list(list_[i][1] for i in range(len(list_)))    
    nearest_value = min(resist, key=lambda x:abs(x-ref_resist))
    list_index = resist.index(nearest_value)
    temperature = list_[list_index][0]
    
    return temperature