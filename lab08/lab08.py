def cumulative_mul(t):
    """Mutates t so that each node's label becomes the product of its own
    label and all labels in the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_mul(t)
    >>> t
    Tree(105, [Tree(15, [Tree(5)]), Tree(7)])
    >>> otherTree = Tree(2, [Tree(1, [Tree(3), Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> cumulative_mul(otherTree)
    >>> otherTree
    Tree(5040, [Tree(60, [Tree(3), Tree(4), Tree(5)]), Tree(42, [Tree(7)])])
    """
    def fuck_y(t) :
        result=1
        if t.is_leaf() :
            return t.label
        else :
            result*=t.label
            for i in t.branches :
                result*=fuck_y(i)
            t.label=result
            return result
    fuck_y(t)

def delete(t, x):
    """Remove all nodes labeled x below the root within Tree t. When a non-leaf
    node is deleted, the deleted node's children become children of its parent.

    The root node will never be removed.

    >>> t = Tree(3, [Tree(2, [Tree(2), Tree(2)]), Tree(2), Tree(2, [Tree(2, [Tree(2), Tree(2)])])])
    >>> delete(t, 2)
    >>> t
    Tree(3)
    >>> t = Tree(1, [Tree(2, [Tree(4, [Tree(2)]), Tree(5)]), Tree(3, [Tree(6), Tree(2)]), Tree(4)])
    >>> delete(t, 2)
    >>> t
    Tree(1, [Tree(4), Tree(5), Tree(3, [Tree(6)]), Tree(4)])
    >>> t = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(2)]), Tree(2, [Tree(6),  Tree(2), Tree(7), Tree(8)]), Tree(4)])
    >>> delete(t, 2)
    >>> t
    Tree(1, [Tree(4), Tree(5), Tree(3, [Tree(6)]), Tree(6), Tree(7), Tree(8), Tree(4)])
    """
    new_branches = []
    for b in t.branches:
        delete(b,x)
        if b.label == x:
            new_branches.extend(b.branches)
        else:
            new_branches.append(b)
    t.branches = new_branches



def convert_link(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> lst = convert_link(link)
    >>> lst
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """

    if link==Link.empty :
        return []

    if isinstance(link.first,Link) :
        return convert_link(link.first)+convert_link(link.rest) 
    else :
        return [link.first]+convert_link(link.rest)

def add_links(link1, link2):
    """Adds two Links, returning a new Link

    >>> l1 = Link(1, Link(2))
    >>> l2 = Link(3, Link(4, Link(5)))
    >>> new = add_links(l1, l2)
    >>> print(new)
    <1 2 3 4 5>
    >>> new2 = add_links(l2,l1)
    >>> print(new2)
    <3 4 5 1 2>
    """

    def duplicate(link) :
        if link==Link.empty :
            return Link.empty
        else :
            return Link(link.first,duplicate(link.rest))

    link1_tem=duplicate(link1)
    link2_tem=duplicate(link2)
    link1_p=link1_tem

    while link1_p.rest!=Link.empty :
        link1_p=link1_p.rest
    
    link1_p.rest=link2_tem
    
    return link1_tem
    

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3))
    >>> b = Link(5, Link(4))
    >>> p1 = multiply_lnks([a, b])
    >>> p1
    Link(10, Link(12))

    >>> c = Link(2, Link(3, Link(5)))
    >>> d = Link(6, Link(4, Link(2)))
    >>> e = Link(4, Link(1, Link(0, Link(2))))
    >>> p2 = multiply_lnks([c, d, e])
    >>> p2
    Link(48, Link(12, Link(0)))
    """
    product = 1
    
    for i in lst_of_lnks:
        if i!=Link.empty:
            product*=i.first
        else :
            return Link.empty
    lst_of_lnks_rests = [x.rest for x in lst_of_lnks]
    return Link(product,multiply_lnks(lst_of_lnks_rests))


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
'''
l1 = Link(1, Link(2))
l2 = Link(3, Link(4, Link(5)))
 
print(add_links(l1,l2))
print(add_links(l2,l1))
'''