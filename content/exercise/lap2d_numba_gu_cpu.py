import numba

@numba.guvectorize(['void(float64[:,:],float64[:,:])'],'(m,n)->(m,n)')
def lap2d_numba_gu_cpu(u, unew):

    M = u.shape[0]     
    N = u.shape[1]    
 
    for i in range(1, M-1):
        for j in range(1, N-1):  
            unew[i, j] = 0.25 * ( u[i+1, j] + u[i-1, j] + u[i, j+1] + u[i, j-1] )   