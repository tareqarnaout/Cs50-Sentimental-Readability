# function to count letters in the string
def letter_counter(story):
    size = len(story)
    counter = 0
    for i in range(size):
        if ord(story[i].upper()) >= 65 and ord(story[i].upper()) <= 90:
            counter += 1
    return counter


def word_counter(story):
    size = len(story)
    counter = 1
    for i in range(size):
        if ord(story[i]) == 32:
            counter += 1
    return counter


def sent_counter(story):
    size = len(story)
    counter = 0
    for i in range(size):
        if ord(story[i]) == 33 or ord(story[i]) == 46 or ord(story[i]) == 63:
            counter += 1
    return counter


def main():
    paragraph = input("whats the paragraph ")
    numOfLetters = letter_counter(paragraph)
    numOfWords = word_counter(paragraph)
    numOfSentences = sent_counter(paragraph)
    # average of letters for 100 words
    L = (numOfLetters / numOfWords) * 100
    # average of sentences for 100 words
    S = (numOfSentences / numOfWords) * 100
    # calculation
    index = 0.0588 * L - 0.296 * S - 15.8
    index = round(index)
    if index >= 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        for i in range(15):
            if i == index:
                print(f"Grade {i}")


main()
