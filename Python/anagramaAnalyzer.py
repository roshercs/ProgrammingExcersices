##########################
#   Evaluate if two strings are anagrams 
#   Two words are anagrams if they are made up of exactly the same characters (in appearance and repetition) but vary in the position of at least two
#   letters . Equal strings are not anagrams.
#   Author: Rogelio Hernandez
#   Date: 06/Enero/2024
##########################

#Evaluate two strings, count and evaluate if they have the same number of the same chars.
#Args string 1, string 2: strings in LOWER CASE
def searchAnagram(string1,string2):
    #Evaluate if the strings are the same, in the true case, end function
    if string1==string2:
        print("Las cadenas son iguales, no es anagrama")
        return
    dic={}
    # Creation of dictionary. Keys are the chars, values the count of apparition of each one
    for i in string1:
        #If doesnt exist in the dictionary, inster as new value with count 1, else inc the count nombre of the value
        if i not in dic:
            dic[i]=1
        else:
            dic[i]=dic[i]+1

    #For each char in the second string, it search in the dictionary, if at least one doesnt exist, end function. If the char exists, decrements the count of the value
    for i in string2:
        if i in dic:
            dic[i]=dic[i]-1
        else:
            print("No son anagramas")
            return
    #If all chars in second string are in the first one, it searches if the first string have at least one more char (value!=0)
    for i in dic.values():
        if i!=0:
            print("No son anagramas")
            return
    print("Son anagramas: ", string1,string2)


#Reading strings, should convert them in lower case
s1=input("Cadena 1: ").lower()
s2=input("Cadena 2: ").lower()
searchAnagram(s1,s2)
