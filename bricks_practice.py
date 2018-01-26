def make_bricks(small, big, goal):
    big_total = big *5
    if big_total < 5:
        n_times = 0
    else:
        if big_total <= goal:
            n_times = math.floor(big_total/5)
        else:
            n_times = math.floor(goal/5)

    if (big_total == 0 and small ==0) or (goal==0):
        return False
    else:
        if big_total == goal or small == goal:
            return True
        if (n_times*5) > goal:
            if ((goal%5)==0):
                return True
            else:
                return False
        else:
            if small >=0:
                if small >=(goal-(n_times*5)):
                    return True
                else:
                    return False
            else:
                return False  
