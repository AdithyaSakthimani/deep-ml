import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    # Your code here
    lst = [ i for i in range ( n_samples )]
    nr = np.array(lst)
    if shuffle == True : 
        np.random.shuffle(nr)
    r = nr.tolist()
    size = n_samples // k
    remf = n_samples - ( size * k ) 
    res = []
    for i in range ( 0 , n_samples , size) : 
        if i + size > n_samples : 
            break 
        res.append(r[i:i+size])
    rem = []
    cnt = 0 
    for i in range ( n_samples - 1 , 1 , -1 ) : 
        if cnt < remf : 
            rem.append(r[i])
            cnt += 1 
        else : 
            break 
    res[0].extend(rem)
    ans = []
    for v in res : 
        s = r.copy() 
        for val in v : 
            s.remove(val)
        ans.append((s,v))
    return ans