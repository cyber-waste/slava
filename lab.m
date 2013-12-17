function lab(num,prob,cost,total)
    seq_sys = ones(1,num)
    reliability_data = [calc_reliability(seq_sys,prob)]
    cur_cost = cost
    cur_ind = 1
    while cur_cost <= total
        seq_sys(cur_ind) += 1
        if((cur_ind+1)>num)
            cur_ind = 1
        else
            cur_ind = cur_ind + 1
        endif
        cur_cost += cost
        n = length(reliability_data)
        x = calc_reliability(seq_sys,prob)
        reliability_data(n+1) = x
    endwhile
    
    n = length(reliability_data)
    plot (0:1:(n-1), reliability_data,"+")
endfunction

function res = calc_reliability(seq_sys,prob)
    res = 1
    for n = seq_sys
        res = res * (1 - (1-prob)**n )
    end
endfunction
