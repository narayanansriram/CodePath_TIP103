def subdomain_visits(cpdomains):
    result = []
    for cpdomain in cpdomains:
        count,domain = cpdomain.split(" ")
        local = []
        local.append(f"{count} {domain}")
        for i in range(len(domain)):
            if domain[i]=='.':
                # print("hit!", domain[i+1:])
                local.append(f"{count} {domain[i+1:]}")
        # print(count,"->",domain)
        result.append(local)
    return result

# Example Usage:

cpdomains1 = ["9001 modern.artmuseum.com"]
cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
              "1 contemporary.gallery.com", "5 medieval.org"]

print(subdomain_visits(cpdomains1))
print(subdomain_visits(cpdomains2))

# Example Output:

# ["9001 artmuseum.com", "9001 modern.artmuseum.com", "9001 com"]

# ["901 gallery.com", "50 impressionism.com", "900 abstract.gallery.com", "5 medieval.org", "5 org",
# "1 contemporary.gallery.com", "951 com"]
