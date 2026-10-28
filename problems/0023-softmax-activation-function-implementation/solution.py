import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    mxScore = max(scores)
    lst = []
    total = 0 
    for s in scores : 
        total += math.exp(s-mxScore) 
    for s in scores : 
        lst.append(math.exp(s-mxScore) / total)
    return lst 