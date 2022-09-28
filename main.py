text=input("Enter a Long text an entire article, a paragraph, a sentence, a poem,whatever you want: ").lower()
letters=[]
letters.append(input("Enter the first letter: ").lower())
letters.append(input("Enter the second letter: ").lower())
letters.append(input("Enter the third letter: ").lower())

print("\n")
print("-----------LETTR REPITATION-------------")

letter1=text.count(letters[0])
letter2=text.count(letters[1])
letter3=text.count(letters[2])

print(f"letter {letters[0]} repeted {letter1} time.\nletter {letters[1]} repeted {letter2} time.\nletter {letters[2]} repeted {letter3} time.\n")
print("----------word Count-----------")
words=text.split()
print(f"The number of words in text is {len(words)}.")

print("\n")
print("--------First and last letter of the index--------------")

first_ltr=text[0]
last_ltr=text[-1]

print(f"The first letter of the text is: {first_ltr}\nThe last letter of the text is: {last_ltr}")

print("\n")
print("--------invert the text--------------")
words.reverse()
inverted_text=' '.join(words)
print(f"If we inverted our text it will look like: {inverted_text}")

print("\n")
print("--------Checking a word in text--------------")

is_python='python' in words
dis={True:'was',False:'was not'}
print(f"The word 'python' {dis[is_python]} in the list.")
