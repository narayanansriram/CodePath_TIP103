def arrange_attendees_by_priority(attendees, priority):
    l = []
    m = []
    r = []

    for attendee in attendees:
        if attendee<priority:
            l.append(attendee)
        elif attendee>priority:
            r.append(attendee)
        else:
            m.append(attendee)
    return l+m+r
#     l = 0
#     r = len(attendees)-1
#     mid = 0
#     while mid<=r:
#         if attendees[mid]<priority:
#             attendees[mid],attendees[l]=attendees[l],attendees[mid]
#             l+=1
#             mid+=1
#         elif attendees[mid]>priority:
#             attendees[mid],attendees[r]=attendees[r],attendees[mid]
#             r-=1
#         else:
#             mid+=1
#     return attendees
    


# Example Usage:

print(arrange_attendees_by_priority([9,12,5,10,14,3,10], 10)) 
print(arrange_attendees_by_priority([-3,4,3,2], 2)) 

# Example Output:

# [9,5,3,10,10,12,14]
# [-3,2,4,3]
