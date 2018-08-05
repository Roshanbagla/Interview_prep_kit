"""Finding anagrams."""


def anagrams(anagram_list):
    """Finding anagrams."""
    count = 0
    length_list = len(anagram_list)
    for i in range(length_list):
        for j in range(i+1, length_list):
            k1 = sorted(anagram_list[i])
            k2 = sorted(anagram_list[j])
            if ((len(anagram_list[i]) == len(anagram_list[j])) and (k1 == k2)):
                count = count + 1
    return count


def subsets_of_string(string):
    """Find all the subsets of a string."""
    subset_string = []
    length = len(string)
    for i in range(length):
        for j in range(i, length):
            subset_string.append(string[i:j+1])
    return subset_string


subset = subsets_of_string('ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrl'
                           'kpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbe'
                           'lgruel')
print(anagrams(subset))
