def anagram(s1, s2):
     
   
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.") 
    else:
        print("The strings aren't anagrams.")         
         
 
s1 =str(input("Enter the string1:"))
s2 =str(input("Enter the string2:"))
anagram(s1, s2)