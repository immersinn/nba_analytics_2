#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 20:08:51 2017

@author: immersinn
"""

import numpy


def extract_moment_plays(plays, moment):
    return(plays[plays.apply(lambda x: x['PERIOD'] == moment['quarter'] and \
                  x['GAMECLOCK'] >= numpy.ceil(moment['game_clock_end']) and \
                  x['GAMECLOCK'] <= numpy.floor(moment['game_clock_start']), axis=1)])
    
    
def extract_play_moments(play, moments):
    # Assume we already have all moments for the game queried
    moment_filter = lambda mom: mom['quarter'] == play['PERIOD'] and \
                                play['GAMECLOCK'] >= numpy.ceil(mom['game_clock_end']) and \
                                play['GAMECLOCK'] <= numpy.floor(mom['game_clock_start'])
    return(moments[moments.apply(lambda x: moment_filter(x), axis=1)])