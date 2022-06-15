#comentar principios que se esten siguiendo

#OC: open close principle  -- adding new behaviour with code
#SRP
def get_pref_key(preferences):
    #validar 
    if( len(preferences) != 3 ):
        return None
    else:
        return ((preferences[0]*preferences[1]*preferences[2])%5) + 1

        