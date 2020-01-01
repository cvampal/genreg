using Combinatorics
using Distributed, SharedArrays

function findsubsets(S,n)
    combinations(S,n)    
end

function boundary_length(n,G,aSet)
    var = 0
    restSet = setdiff(Set([i for i in 0:n-1]), Set(aSet))
    for v in aSet
        for w in G[v] 
            if w in restSet
                var += 1
            end
        end
    end
    return var
end



function get_Cheeger(n,G)
    vertexSet = [i for i in 0:n-1]
    cheeger = 2.0*n
    p = 0
    q = 0
    for i in 1:Int(floor(n/2))
        for aSet in collect(findsubsets(vertexSet,i))
            var = boundary_length(n,G,aSet)
            if var/i < cheeger
                cheeger = var/i
                p = var
                q = i
            end
        end
    end
    return(cheeger,p,q)
end


