from typing import Optional, Union

try:
    import numpy as np
except Exception:
    np = None

ArrayLike = Union[list, "np.ndarray"]

def flow_epe(pred: ArrayLike,
             gt: ArrayLike,
             mask: Optional[ArrayLike] = None,
             max_flow: Optional[float] = None) -> float:
    """
    Compute mean End-Point Error (EPE) between predicted and ground-truth optical flow.

    Args:
        pred, gt: (H, W, 2) lists or NumPy arrays.
        mask: optional (H, W) or broadcastable to (H, W); 1=include, 0=ignore.
        max_flow: optional float; clip per-pixel EPE to this value.

    Returns:
        float: mean EPE over valid pixels. Returns -1 on invalid input or if no valid pixels.
    """
    # Your implementation here
    # m , n = len( pred ) , len( pred[0] ) 
    if isinstance(pred, np.ndarray):
        m , n  , k = pred.shape
    else : 
        m , n , k  = len(pred) , len(pred[0]) , len(pred[1])
    e = np.zeros((m , n ))
    
    for i in range ( m ) : 
        for j in range ( n ) : 
            up , vp = pred[i][j]
            ug, vg = gt[i][j]
            v = [up , vp , ug , vg] 
            if mask is not None: 
                if mask[i][j] < 0.5 : 
                    continue 
            inValid = False 
            for kk in v : 
                if kk == -1 or np.isnan(kk) : 
                    inValid = True 
                    break 
            if inValid : 
                continue 
            e[i][j] =  ((up - ug ) ** 2 + ( vp - vg )**2) ** (1/2) 
            if max_flow != None : 
                e[i][j] = min(e[i][j] , max_flow)
    total  , cnt = 0 , 0 
    for i in range ( m ) :
        for j in range ( n ) : 
            if e[i][j] != 0 : 
                total += e[i][j]
                cnt += 1  
    if total == 0 or cnt == 0 : 
        return -1 
    return total / cnt 
