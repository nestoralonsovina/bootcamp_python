import string

def text_analyzer(text = None):
    """
        This function counts the number of upper and lower characters, punctuation and spaces in a given test.
        If the user does not input a text, it will be prompted to insert one through stdin.
    """
    if text is None:
        text = input("What is the text to analyse?")

    upper = sum([1 if c.isalpha() and c.isupper() else 0 for c in text])
    lower = sum([1 if c.isalpha() and c.islower() else 0 for c in text])
    punctuation = sum([1 if c in string.punctuation else 0 for c in text])
    spaces = sum([1 if c.isspace() else 0 for c in text])

    print(f"The text contains {len(text)} characters:")
    print(f"- {upper} upper letters")
    print(f"- {lower} lower letters")
    print(f"- {punctuation} punctuation marks")
    print(f"- {spaces} spaces")