# input s1 = "danger", s2 = "garden"
# output = True
# Two strings are anagrams if they contain the same characters in the same frequency.

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    freq1 = {}
    freq2 = {}
    for ch in s1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1

    for ch in s2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1

    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
    return True


if __name__ == "__main__":
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")

    if is_anagram(s1, s2):
        print(f'"{s1}" and "{s2}" are anagrams.')
    else:
        print(f'"{s1}" and "{s2}" are not anagrams.')
    
    # Above code allows the user to input 2 strings.   
    # print(is_anagram("garden", "danger"))
   