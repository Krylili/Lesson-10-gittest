#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 18:41:52 2020

@author: Presenter
"""

BASEMATCH_NOERROR = 0
BASEMATCH_CMP_T_AND_U = 1

BASEMATCH_DICT = {"Y": ["C", "T"], "R": ["A", "G"], "N": ["A", "G", "C", "T"]}

def is_base_match(base1: str, base2: str) -> (bool, int):    
    if (base1 == "T" and base2 == "U") or (base2 == "T" and base1 == "U"):
        return False, BASEMATCH_CMP_T_AND_U 
    
    if base1 in BASEMATCH_DICT:
        if base2 in BASEMATCH_DICT[base1]:
            return True, BASEMATCH_NOERROR  

    if base2 in BASEMATCH_DICT:
        if base1 in BASEMATCH_DICT[base2]:
            return True, BASEMATCH_NOERROR         
    

    return base1 == base2, BASEMATCH_NOERROR


if __name__ == "__main__":

    #print(is_base_match("A", "A"))
    #print(is_base_match("C", "C"))
    #print(is_base_match("G", "G"))
    #print(is_base_match("T", "T"))    
    
    print(is_base_match("C", "Y"))  
    print(is_base_match("C", "Y"))  
    print(is_base_match("Y", "C"))  
    print(is_base_match("Y", "T"))
    
    #print(is_base_match("A", "N"), "A matches or not matches any base.")
    #print(is_base_match("X", "N"), "X matches or not matches any base.")
    
    #print(is_base_match("T", "U"), "should be false, but unique case that should not happen anyway.")
    
    #print(is_base_match("A", "T"))
    #print(is_base_match("G", "C"))
    
    