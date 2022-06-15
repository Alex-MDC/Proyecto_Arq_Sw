#comentar principios que se esten siguiendo

#OC: open close principle  -- adding new behaviour with code
#SRP: one reason to change; the business logic of the key generation

class Preference_key_generator:
    #create magic key
    def get_pref_key(self,preferences): 
        if( len(preferences) != 3 ):
            return None
        else:
            return ((preferences[0]*preferences[1]*preferences[2])%5) + 1

        