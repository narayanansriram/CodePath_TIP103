from collections import defaultdict
def pair_contestants(scores, k):
    remainder_count = defaultdict(int)
    for score in scores:
        remainder_count[score%k]+=1
    seen = set()
    for remainder in remainder_count:
        if remainder==0 and remainder_count[remainder]%2==0:
            continue
        # if remainder in seen:
        #     continue
        if k-remainder in remainder_count and remainder_count[k-remainder]==remainder_count[remainder]:
            seen.add(remainder)
            seen.add(k-remainder)
        else:
            return False
    return True
        

# Example Usage:

scores1 = [1,2,3,4,5,10,6,7,8,9]
k1 = 5
print(pair_contestants(scores1, k1))

scores2 = [1,2,3,4,5,6]
k2 = 7
print(pair_contestants(scores2, k2))

scores3 = [1,2,3,4,5,6]
k3 = 10
print(pair_contestants(scores3, k3)) 


# Example Output:

# True
# True
# False

student = {"Name":"Emma", "class":9, "grade":'A'}

student.pop("Name")
print(student)

gradebook = {"class":{
    "student":{
        "name":"Mike",
        "grade":{
            "physics":'C',
            "history":"B"
        }
    }
}}

print(gradebook["class"]["student"]["grade"]["history"])

def proc_data(names,scores):
    result = {}
    for i in range(len(names)):
        name =names[i]
        score = scores[i]
        if name not in result:
            result[name]=[]
        result[name].append(score)
    return result

names = ["Alice","Bob","Alice","Bob","Charlie"]
scores = [85,90,95,80,70]
print(proc_data(names,scores))