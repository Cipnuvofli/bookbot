def wordcount(countedstring):
    wordcount = len(countedstring.split())
    return wordcount

def charcounts(targetstring):
    startingstring = targetstring.lower()
    chardict = {}
    for i in startingstring:
        if i in chardict:
            chardict[f"{i}"]+=1
        else:
            chardict[f"{i}"]=1
    return chardict

def makereport(filepath, filecontents):
    print(f"--- Begin report of {filepath} ---\n")
    print(f"{wordcount(filecontents)} words found in the document\n")
    charfrequency = charcounts(filecontents)
    for i in charfrequency:
        print(f"The '{i}' character was found "+str(charfrequency[f"{i}"])+" times")
    print("--- End Report ---")


def main():
    bookpath = "books/frankenstein.txt"
    with open(bookpath) as f:
        file_contents = f.read()
        makereport(bookpath, file_contents)
        

main()