#To find if a word is an anagram
def isAnagram(original,test):
    if len(original) ==len(test):
        count= [0]* ord('z')
        for c in original:
            count[ord(c)] +=1
            for c in test:
                if count[ord(c)]==0:
                    return False
                else:
                    count[ord(c)]-=1
                    return True
                return False
            original= raw_input("enter first dtring:")
            test = raw_input("enter second string:")
            print
            print ("%s and %s are %s") %(original,test,"anagrams" if (isAnagram(original, test)) else "not anagrams")
            
            
