word_counts={}

words=input('enter a sentence')

sent=words.split()

for i in sent:
    i=i.lower()
    if i in word_counts:
        word_counts[i]+=1
    else:
        word_counts[i]=1
print(word_counts)
        
