def correct_string(p):
    if len(p)==0:
        return ''
    
    count_left = 0
    count_right = 0
    correct = True
    
    
    u = ''
    v = ''
    
    for i in range(len(p)):
        if p[i] == '(':
            count_left += 1
            u += '('
            
        elif p[i] == ')':
            count_right += 1
            u += ')'
            
            
        if count_right > count_left:
            correct = False
            
            
        if count_left == count_right:
            v = p[i+1:]
            break
            
            
            
    if correct == True:
        return u+correct_string(v)
    
    else:
        result = ''
        
        for i in u[1:len(u)-1]:
            if i == '(':
                result += ')'
            elif i == ')':
                result += '('
                
        return '('+correct_string(v)+')'+result
                
        
        

def solution(p):
    answer = correct_string(p)
    
    
    return answer
