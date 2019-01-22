def merge_characters(text):
    # note: code explanation based on the example word 'r e c h n u n g'
    # adding an extra item to the list in order to run the while loop later on
    listed_words = text.split(sep=' ') + ['']

    # checking if any item in the e-mail text is a single character
    # if yes it will go to the loop that merges the neighboring single characters
    # if not it will return the e-mail text as it is
    if any(len(x) == 1 for x in listed_words):
        try:
            for word in range(0, len(listed_words)):
                # iterates over words in the e-mail and looks for single-character words
                # initializing the string 'new_word' that will be used for building
                # the new merged word out of the single characters
                new_word = ' '

                if (
                    len(listed_words[word]) == 1
                    and len(listed_words[word + 1]) == 1
                    and listed_words[word] != ' '
                ):
                    # there are two consecutive single-character words the code will enter the while loop
                    # start_index marks where the merged word should be added in the list
                    # end_index shows where the array if single-character items ends
                    start_index = word
                    end_index = word + 1

                    while ((len(listed_words[word]) + len(listed_words[word + 1])) == 2) and (
                        listed_words[word] != '' or listed_words[word + 1] != ''
                    ):
                        # while two consecutive items are single-characters
                        # they will be added to the previously initialized string new_word
                        # with each iteration the last character of the new_word is dropped
                        # because it's and overlapping character of the curren and previous iteration
                        new_word = new_word[:-1] + listed_words[word] + listed_words[word + 1]
                        word += 1
                        end_index = (
                            word
                        )  # updating the end_index as we merge further items of the length == 1

                    # while the merged word will be put in the start_index ('r' of the 'r e c h n u n g')
                    # the indices of 'e', 'c', 'h', 'n', 'u', 'n' 'g' characters will be replaced
                    # with an empty string
                    # this way we don't change the lenngth of the listed_words list while removing
                    # the characters that we don't need anymore
                    listed_words[start_index] = new_word
                    listed_words[start_index + 1 : end_index + 1] = ''
        except IndexError:
            pass
        return ' '.join(listed_words[:-1])  # drops the previously added ['']
    else:
        return (
            text
        )  # in case there were no single-characters in the e-mail it retunrs the original text
