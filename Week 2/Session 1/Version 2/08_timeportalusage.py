from collections import defaultdict, Counter
def display_time_portal_usage(usage_records):
    access = defaultdict(list)
    timesList = set()
    for _,portal,time in usage_records:
        access[portal].append(time)
        timesList.add(time)
    result = []
    header = ["Portal"]
    timesList = (list(timesList))
    timesList.sort()
    header.extend(timesList)
    result.append(header)
    timeIndices = {time:idx+1 for idx,time in enumerate(timesList)}
    sortedAccess = sorted(access.items(),key=lambda x:int(x[0]))
    for portal,times in sortedAccess:
        timesCt = Counter(times)
        curr = [portal]
        for time,timeIdx in timeIndices.items():
            if time in timesCt:
                curr.append(str(timesCt[time]))
            else:
                curr.append('0')
        result.append(curr)
    return result

    

# Example Usage:

usage_records1 = [["David","3","10:00"],
                  ["Corina","10","10:15"],
                  ["David","3","10:30"],
                  ["Carla","5","11:00"],
                  ["Carla","5","10:00"],
                  ["Rous","3","10:00"]]
usage_records2 = [["James","12","11:00"],
                  ["Ratesh","12","11:00"],
                  ["Amadeus","12","11:00"],
                  ["Adam","1","09:00"],
                  ["Brianna","1","09:00"]]
usage_records3 = [["Laura","2","08:00"],
                  ["Jhon","2","08:15"],
                  ["Melissa","2","08:30"]]

print(display_time_portal_usage(usage_records1))
print(display_time_portal_usage(usage_records2))
print(display_time_portal_usage(usage_records3))

# Example Output:

# [['Portal','10:00','10:15','10:30','11:00'],['3','2','0','1','0'],['5','1','0','0','1'],
#  ['10','0','1','0','0']]
# [['Portal','09:00','11:00'],['1','2','0'],['12','0','3']]
# [['Portal','08:00','08:15','08:30'],['2','1','1','1']]
