def find_cube_pairs(target): #  1) ":" colon is missing 
    solutions = []       # 2) removed semi-colon ";" which is not required 
    max_num = round(target ** (1/3))  # 3) only two "**" asterix symbols are required to raise to power and changed the name "targ" to "target"

    for a in range(1, max_num + 1):      # 4) changed "ranges" to "range" and added a ":" colon
        for b in range(a, max_num + 1):  # 5) changed "ranges" to "range " and added a ":" colon
            if a**3 + b**3 == target:       # 6) only two "**" asterix symbols are required to raise to power and changed the name "targ" to "target"
                solutions.append((a, b)) # 7) changed the name "sol" to "solutions" and removed the semicolon
    return solutions            # 8) changed the name "sol" to "solutions"

pairs = find_cube_pairs(1729) # removed the ,
print("Valid cube pairs for 1729:") # removed , and changed 1728 to 1729 and printf to print 
for a, b in pairs:                       # added colon and changed pair to pairs
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")  # changed 1728 to 1729 and **2 to **3 and printf to print


#   """Submit your response here:  https://forms.office.com/Pages/ResponsePage.aspx?id=vDsaA3zPK06W7IZ1VVQKHFzW4INMf2JMjyL9qPnlPbNUMFU2TjI1WjQyUlczSFNIOFBEWkxTQ0lFQS4u"""
