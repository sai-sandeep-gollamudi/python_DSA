#method to check if the bst is valid or not
def is_valid_bst(self): r=self .dfs_in_order()
    for i in range(1,len( r)):
        if(r[i -1]> = r[ i] ):
            return False
    return True