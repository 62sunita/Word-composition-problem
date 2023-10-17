import time

# Function to check if a word can be compounded from a list of words
def is_compounded(word, words_list):
    if word in words_list:
        return True
    for i in range(1, len(word)):
        prefix = word[:i]
        suffix = word[i:]
        if prefix in words_list and suffix in words_list or is_compounded(suffix, words_list):
            return True
    return False

# Function to find the longest and second longest compounded words
def find_longest_compounded_words(words):
    words_set = set(words)
    longest = ""
    second_longest = ""
    for word in words:
        if is_compounded(word, words_set):
            if len(word) > len(longest):
                second_longest = longest
                longest = word
            elif len(word) > len(second_longest):
                second_longest = word
    return longest, second_longest

if __name__ == "__main__":
    start_time = time.time()

    input_files = ["Input_01.txt","Input_02.txt"]
    all_words = []
    for file in input_files:
        with open(file, "r") as f:
            words = [line.strip() for line in f.readlines()]
            all_words.extend(words)
    
    # Find the longest and second longest compounded words
    longest_compounded, second_longest_compounded = find_longest_compounded_words(words)
    
    # Calculate the time taken
    end_time = time.time()
    processing_time = end_time - start_time
    
    # Print the results
    print(f"Longest Compounded Word: {longest_compounded}")
    print(f"Second Longest Compounded Word: {second_longest_compounded}")
    print(f"Time Taken to Process: {processing_time} seconds")
