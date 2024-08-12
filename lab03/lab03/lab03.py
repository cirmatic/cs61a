LAB_SOURCE_FILE=__file__


def double_eights(n):
    """ Returns whether or not n has two digits in row that
    are the number 8. Assume n has at least two digits in it.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(LAB_SOURCE_FILE, 'double_eights', ['While', 'For'])
    True
    """

    def is_eight(n) :
        if n%10==8 :
           return True
        else :
           return False
    if n==0 or n//10==0 :
       return False
    elif n%10==8 and is_eight(n//10) :
       return True
    else :
       return double_eights(n//10) 
       
def make_onion(f, g):
    """Return a function can_reach(x, y, limit) that returns
    whether some call expression containing only f, g, and x with
    up to limit calls will give the result y.

    >>> up = lambda x: x + 1
    >>> double = lambda y: y * 2
    >>> can_reach = make_onion(up, double)
    >>> can_reach(5, 25, 4)      # 25 = up(double(double(up(5))))
    True
    >>> can_reach(5, 25, 3)      # Not possible
    False
    >>> can_reach(1, 1, 0)      # 1 = 1
    True
    >>> add_ing = lambda x: x + "ing"
    >>> add_end = lambda y: y + "end"
    >>> can_reach_string = make_onion(add_ing, add_end)
    >>> can_reach_string("cry", "crying", 1)      # "crying" = add_ing("cry")
    True
    >>> can_reach_string("un", "unending", 3)     # "unending" = add_ing(add_end("un"))
    True
    >>> can_reach_string("peach", "folding", 4)   # Not possible
    False
    """
    def can_reach(x, y, limit):
        if limit < 0:
            return False
        elif x == y:
            return True
        else:
            return can_reach(f(x), y, limit - 1) or can_reach(g(x), y, limit - 1)
    return can_reach


def mario_number(level):
    """Return the number of ways that Mario can perform a sequence of steps
    or jumps to reach the end of the level without ever landing in a Piranha
    plant. Assume that every level begins and ends with a space.

    >>> mario_number(' P P ')   # jump, jump
    1
    >>> mario_number(' P P  ')   # jump, jump, step
    1
    >>> mario_number('  P P ')  # step, jump, jump
    1
    >>> mario_number('   P P ') # step, step, jump, jump or jump, jump, jump
    2
    >>> mario_number(' P PP ')  # Mario cannot jump two plants
    0
    >>> mario_number('    ')    # step, jump ; jump, step ; step, step, step
    3
    >>> mario_number('    P    ')
    9
    >>> mario_number('   P    P P   P  P P    P     P ')
    180
    """
    if len(level)>2 : 
       level1=level[1:]
       level2=level[2:]
    else :
       level1=level[1:]
       level2='P'
    if level[0]=='P':
       return 0
    elif  len(level)==1 :
       return 1
    else :
       return mario_number(level1)+mario_number(level2)

def max_subseq(n, t):
    """
    Return the maximum subsequence of length at most t that can be found in the given number n.
    For example, for n = 2012 and t = 2, we have that the subsequences are
        2
        0
        1
        2
        20
        21
        22
        01
        02
        12
    and of these, the maxumum number is 22, so our answer is 22.

    >>> max_subseq(2012, 2)
    22
    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """


    arrange=[] 
    str_n=str(n)
    for char in str_n :
        arrange.append(int(char))

    def sub_seq(num,bit,arrange) : 
        res=0
        k=num
        new_num=0
        if bit>1 :
           for i in arrange[num:1-bit] :
            if i>res :
               new_num=k+1
               res=i
            k+=1
           return res,new_num 
        elif bit==1 :
            for i in arrange[num:] :
             if i>res :
               new_num=k+1
               res=i
             k+=1
            return res,new_num 

    bit=0
    while n//(10**bit)!=0 :
          bit+=1
    tem=0
    i=1
    num=0
    bit_tem=t
    result=0
    if t>=bit :
       return n
    else :
       while i<=t :
             tem,num=sub_seq(num,bit_tem,arrange)
             result+=tem*(10**(t-i))
             bit_tem-=1
             i+=1
    return result

def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
   
    def nis_division(n,d_n) :
        if d_n==1 :
           return True
        elif n%d_n==0 :
           return False
        else :
           return nis_division(n,d_n-1)
    if n==1 :
       return False
    else :
       return nis_division(n,n-1) 
