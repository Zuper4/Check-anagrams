print("\nThis program will check if two strings are anagrams.")
print("Two words are anagrams if these words are the same just by rearranging the letters.")
print("For example : pear and reap.")

word1 = str(input("\nWord 1 :"))
word2 = str(input("Word 2 :"))

word1 = word1.lower()
word2 = word2.lower()

if len(word1) == len(word2):

    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)

    if sorted_word1 == sorted_word2:

        print(word1+ " and " +word2+ " are anagrams.")

    else :
        print(word1+ " and " +word2+ " are not anagrams.")

else :
    print(word1+ " and " +word2+ " are not anagrams.")

