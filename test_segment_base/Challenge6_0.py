#Function answer(document, searchTerms)
#Input 1: A String with lowercase letters a, b, c... z and spaces "hello world "
#Input 2: A list of words with lowercase letters ex ["hello", "world"]
#Output : The minimum sized (in words) substring that contains all words in input #2
#Method : Keep track of a list [index_word_1, index_word_2, etc...]. Loop through the list once updating the index as we go. Each update we calculate the current substring and compare it to the best.
#Runtime: O(n*log(n))
#Constraints: Behavoir is not defined if there is no substring with all the words in input #2. 
def answer(document, searchTerms):
    #Split up the document into a list for easier processing
    document_list = document.strip().split()
    #Initialize an array with default index of -1 for all searchTerms
    tracking_list = [-1] * len(searchTerms)
    #Initialize the best substring tracking variables
    best_start = -1
    best_end = -1
    #For every word in the document...
    for x_index in range(0, len(document_list)):
        #Try to find the index of the word in the search terms
        try:
            #Initialize the word that is related to the x_index (helper variable)
            x_word = document_list[x_index]
            #This line will fail if the current document-word is not in the search terms
            tracking_list_index = searchTerms.index(x_word)
            #If it is in the search terms
            tracking_list[tracking_list_index] = x_index
            #If we have not found all the search terms yet...
            if (min(tracking_list) == -1):
                #No substring yet
                continue
            else:
                #Find the substring
                start = min(tracking_list)
                end = max(tracking_list)+1
                #Compare its length to the the best length and update if it is better or we have no value to compare to
                if (best_end - best_start > end - start or best_start == -1):
                    best_start = start
                    best_end = end
                continue
        #If it is not in the search terms nothing needs to be updated
        except:
            continue
    #Initialize the output variable
    output_string = ""
    print(best_start)
    print(best_end)
    #Build the output variable from the substring list
    for x in document_list[best_start:best_end]:
        output_string += str(x) + " "
    #Return the output varible after stripping the extra +" "
    return output_string.strip()
