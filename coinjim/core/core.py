# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 14:38:05 2017

@author: dmare
"""
import warnings

class Portfolio(object):
    """A simple portfolio object for managing holdings
    """
    #TODO: Expand/finalize portfolio object roadmap
    def __init__(self):

        self.holdings = dict()        
    def updateHoldings(self, name, amount):
        """Updates portfolio holding
        
           Input:
               name: str, name of holding
               amount: float, amount of holding
        """
        if name not in self.holdings: 
            if amount < 0:
                warnings.warn("Negative Initial Value", UserWarning)
                self.holdings[name] = 0
            else:
                self.holdings[name] = amount
        else:            
            if self.holdings[name]+amount < 0:
                warnings.warn("Amount withdraw too large", UserWarning)
            
            self.holdings[name] += amount
    
    def __str__(self):
        out = ''
        for k in self.holdings.keys():
            out = out + ("%s, %f \n" % (k, self.holdings[k])) 
        return out    
            
            