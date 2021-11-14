import math
import random
import pandas as pd
import numpy as np

def rearr_gantt(rnds):
    global time

    def eta(i, j, v):
        x1 = home_cd[i][0]
        y1 = home_cd[i][1]
        x2 = home_cd[j][0]
        y2 = home_cd[j][1]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) / v

    def rearr(rnd):
        global time
        time_ = time
        for t1, t2 in rnd:
            if t1 == bye or t2 == bye:
                delay[t1] = delay[t2] = -(n / 2 - 1) * tq
                continue
            delay[t1] = delay.get(t1, 0) + eta(prev_loc.get(t1, t1), t1, 1)
            delay[t2] = delay.get(t2, 0) + eta(prev_loc.get(t2, t2), t1, 1)
            delay[t1] = delay[t2] = max(delay[t1], delay[t2])
        rnd_rearr = sorted(rnd, key=lambda x: delay.get(x[0], 0))
        remaining_time = (n / 2) * tq
        if bye_exists:
            remaining_time -= tq
        for match in enumerate(rnd_rearr):
            t1 = match[1][0]
            t2 = match[1][1]
            if t1 == bye or t2 == bye:
                continue
            if at.get(t1, None) is None:
                at[t1] = time_ + delay[t1]
                cpft[t1] = max(time, at[t1])
            if at.get(t2, None) is None:
                at[t2] = time_ + delay[t2]
                cpft[t2] = max(time, at[t2])
            time = max(time, time_ + delay[t2]) + tq
            remaining_time -= tq
            ct[t1] = ct[t2] = time
            delay[t1] = delay[t2] = -remaining_time
            prev_loc[t1] = prev_loc[t2] = t1
        return rnd_rearr

    def get_gantt():
        for team in teams:
            if team == bye:
                continue
            tat[team] = ct[team] - at[team]
            wt[team] = tat[team] - bt
            rt[team] = cpft[team] - at[team]
        gantt = pd.DataFrame([at, cpft, ct, tat, wt, rt])
        gantt = gantt.reindex(sorted(gantt.columns), axis=1)
        gantt.index = ['Arrival Time', 'Stadium First Time', 'Completion Time', \
                       'Turn Around Time', 'Waiting Time', 'Response Time']
        gantt = gantt.T
        gantt.insert(1, 'Burst Time', [bt] * len(gantt.index))
        return gantt

    teams = np.unique(np.array(rnds))
    bye = "bye"
    bye_exists = True if bye in teams else False
    n = len(teams)
    boundary = (-10, 10)
    home_cd = dict()
    prev_loc = dict()

    tq = 4
    rnds_rearr = []
    at = dict()
    bt = tq * (n - 2) if bye_exists else tq * (n - 1)
    ct = dict()
    cpft = dict()
    tat = dict()
    wt = dict()
    rt = dict()
    delay = dict()

    for team in teams:
        home_cd[team] = (random.uniform(*boundary), random.uniform(*boundary))

    x = []
    y = []
    for match in enumerate(rnds):
        x.append(match[1])
        if (match[0] + 1) % (n / 2) == 0:
            y.append(x)
            x = []
    rnds = y

    time = 0
    for rnd in enumerate(rnds):
        rnds_rearr.extend(rearr(rnd[1]))

    print(get_gantt().to_string())

    return rnds_rearr