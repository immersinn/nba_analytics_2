#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 00:01:50 2017

@author: immersinn
"""

import pandas


PBP_HEADER = ["GAME_ID",
          "EVENTNUM",
          "EVENTMSGTYPE",
          "EVENTMSGACTIONTYPE",
          "PERIOD",
          "WCTIMESTRING",
          "PCTIMESTRING",
          "HOMEDESCRIPTION",
          "NEUTRALDESCRIPTION",
          "VISITORDESCRIPTION",
          "SCORE",
          "SCOREMARGIN"]


def preprocessPbp(pbp_raw):
    pbp = pbpDict2Df(pbp_raw)
    pbp = addGameClock(pbp)
    return(pbp)


def pbpDict2Df(pbp):
    # Build the play-by-play DataFrame from the pbp dictionary
    p_ord = []
    if 'play_by_play' in list(pbp.keys()):
        for i in sorted([int(k) for k in list(pbp['play_by_play'].keys())]):
                p_ord.append(pbp['play_by_play'][str(i)])
    else:
        for i in sorted([int(k) for k in list(pbp.keys())]):
                p_ord.append(pbp[str(i)])
    pbp = pandas.DataFrame(p_ord,
                           columns=PBP_HEADER)
    pbp = pbp[PBP_HEADER[1:]]

    return(pbp)


def addGameClock(pbp):
    gc = [time2Gc(t) for t in pbp.PCTIMESTRING]
    gc = pandas.DataFrame(data = gc,
                          columns = ['GAMECLOCK'])
    pbp = pbp.join(gc)
    return(pbp)


def time2Gc(time):
    gc = 60 * int(time.split(':')[0]) + int(time.split(':')[1])
    return(gc)