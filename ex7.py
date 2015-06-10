#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

def find_i(l, elem, f=0, reverse=False):
    "находит елемент в списке" 
    if reverse:
        while i > -1:
            if l[i] == elem:
                return i 
                
            i -= 1
   
    else:
        for i in range(f, len(l)):
            if l[i] == elem:
                return i

    return -1

def biggest_n(l):
    amount = 0
    max_elem = l[0]

    for elem in l[1:]: 
        if elem > max_elem:
            amount += max_elem
            max_elem = elem

        else:
            amount += elem

    return amount
    
def sum_l(l):
    answer = 0
    
    for elem in l:
        answer += elem
     
    return answer

def main(l):
    found = []
    centers = []
    i = 0
    x = 0
    len_l = len(l)    

    while len(l) > i:
        checking = l[i]

        if find_i(found, checking) == -1:
            if find_i(l[i + 1:], checking) != -1:
                found.append(checking) 

            elif len(l) > i + 1 and i - 1 > -1: 
                if l[i - 1] == l[i + 1]:
                    found.append(checking)

                elif i - 1 > 0 and len(found) > 0:
                    if find_i(found, l[i - 1]) == -1 and l[i + 1] == found[-1]:
                        found.append(checking)

        else:
            found.append(checking)
        
        i += 1


    len_found = len(found)
    
    print("len_found: ", len_found)
    print("found: ", found)

    if len_found == 0:
        return len(l) - 1

    i = 0
    palindrome = True

    while len_found > i:
        if found[-i - 1] != found[i]:
            palindrome = False
            break
        
        i += 1
    
    if palindrome:
        return len(l) - len(found)
        
    
    answer = 0 

    
    while len_found > x + 1:
        checking = found[x]
        
        if checking == found[x + 1]:
            j = 1
            length = 2

            while len_found > x + j + 1 and x - j > -1:
                checking = find_i(found, found[x - j], x + j + 1)
                checking1 = find_i(found, found[x + j + 1], x - j, True)
                
                k = checking - (x + j + 1)
                
                
                if found[x + j + 1] == found[x - j]:
                    length += 2
                    
                elif checking != -1:
                    k = checking - (x + j + 1)
                    if k > m:
                        
                    j += k + 1
                    answer += k

                else:
                    break

                print("j: ", j)
                print("length: ", length)
                print("checking: ", checking)
                
                j += 1

            centers.append(length)
        
        elif found[x - 1] == found[x + 1]:
            j = 2
            length = 3

            while len_found > x + j and x - j > -1:
                checking = find_i(found, found[x - j], x + j)
                
                if found[x + j] == found[x - j]:
                    length += 2
                    
                elif checking != -1:
                    j += checking - (x + j - 1)
                    answer += checking - (x + j - 1)
                    
                else:
                    break
                
                print("j: ", j)
                print("length: ", length)
                print("checking: ", checking)

                j += 1

            centers.append(length)

        x += 1
        
        
    answer += biggest_n(centers) + len_l - len_found
    sum_centers = sum_l(centers)
    
    # print(answer) 

    if len_l < sum_centers:
        answer -= (sum_centers - len_found)

    print([l, found, centers])

    return  answer

if __name__ == "__main__":
    print("list of n numbers")
    l = input().split()

    print(main(l))

    input()

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 syntax=python
