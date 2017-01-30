#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 18:48:05 2017

@author: immersinn
"""

from pymongo import MongoClient
import pandas

    
class mongo_open:
    
    def __init__(self, db_name, coll_name):
        self.db_name = db_name
        self.coll_name = coll_name
    
    def __enter__(self,):
        self.client = MongoClient()
        self.db = self.client[self.db_name]
        self.coll = self.db[self.coll_name]
        return(self)
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.client.close()        
    
    def query(self, conditions, fields=None):
        return(self.coll.find(conditions, fields))
 
    
def retrieve_game_moments(gid):
    
    with mongo_open('NBASD', 'Moments') as conn:
        moments = [m for m in conn.query({'game_id': gid,
                                         'game_clock_start' : {'$ne' : 'None'}})]
    moments = pandas.DataFrame(moments)
    return(moments)