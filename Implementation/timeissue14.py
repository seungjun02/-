from itertools import permutations

def solution(n, weak, dist):

    wall = [0] * (2*n)
    dist.sort(reverse=True)

    if dist[0] >= n:
        return 1

    



    for pick in range(1,len(dist)+1):
        
        if pick > len(weak):
            break
            
        
        weak_permu = list(permutations(weak, pick))

        for p in weak_permu:
            for w in range(len(p)):
                wall[p[w]:p[w]+dist[w]+1] = [1] * (dist[w]+1)

            should_continue = False

            for w in weak:
                if wall[w] == 0 and wall[w+n] == 0:
                    should_continue = True
                    break

            wall = [0] * (2*n)

            if should_continue:
                continue

            return pick


    return -1
