#comentar principios que se esten siguiendo


def get_pref_key(preferences):
    #validar 
    if( len(preferences) != 3 ):
        return None
    else:
        return ((preferences[0]*preferences[1]*preferences[2])%5) + 1
        #hacer asserts / validaciones que pref sea entre 1-5

        