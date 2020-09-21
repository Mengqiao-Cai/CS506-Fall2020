def euclidean_dist(x, y):
    if (len(x) == 0 or len(y) == 0 or len(x) != len(y)):
        return 0
    return ((y[0]-x[0])**2 + (y[1]-x[1])**2) ** (1/2)

def manhattan_dist(x, y):
    if (len(x) == 0 or len(y) == 0 or len(x) != len(y)):
        return 0
    answer = 0
    for i in range(len(x)):
        answer += abs(x[i]-y[i])
    return answer

def jaccard_dist(x, y):
    if (len(x) == 0 or len(y) == 0 or len(x) != len(y)):
        return 0
    answer1 = 0
    for i in range(len(x)):
        if (x[i] != y[i]):
            answer1 += 1
    return answer1/len(x)

def cosine_sim(x, y):
    if (len(x) == 0 or len(y) == 0 or len(x) != len(y)):
        return 0
    ans1 = 0
    ans2 = 0
    ans3 = 0
    for i in range(len(x)):
        ans1 += x[i]*y[i]
        ans2 += x[i]**2
        ans3 += y[i]**2
    return ans1/((ans2**(1/2)) * (ans3**(1/2)))

# Feel free to add more
