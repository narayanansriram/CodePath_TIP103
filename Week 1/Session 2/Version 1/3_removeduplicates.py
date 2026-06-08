def remove_dupes(items):
    f = 0
    t = f+1
    b = len(items)-1
    while f<b:
        # print(f"f--->{f};b--->{b};t---->{t}")
        if items[f]==items[t]:
            # print("f==t",f,t,b)
            items[t],items[b]=items[b],items[t]
            b-=1
            f+=1
            t=f+1
        else:
            t+=1
            if t>=b:
                f+=1
                t = f+1
    # print(items,items[:b+1])
    return b+1

# Example Usage

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle"]
print(remove_dupes(items))

# Example Output:

# 4
# 4
