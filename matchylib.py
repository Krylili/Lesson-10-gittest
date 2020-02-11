#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 18:41:52 2020

@author: Presenter
"""

BASEMATCH_NOERROR = 0
BASEMATCH_CMP_T_AND_U = 1

def is_base_match(base1: str, base2: str) -> (bool, int):    
    if (base1 == "T" and base2 == "U") or (base2 == "T" and base1 == "U"):
        return False, BASEMATCH_CMP_T_AND_U 

    return base1 == base2, BASEMATCH_NOERROR


if __name__ == "__main__":

    print(is_base_match("A", "A"))
    print(is_base_match("C", "C"))
    print(is_base_match("G", "G"))
    print(is_base_match("T", "T"))
    
    
    print(is_base_match("T", "U"), "should be false, but unique case that should not happen anyway.")
    
    print(is_base_match("A", "T"))
    print(is_base_match("G", "C"))
    
    