#Project Sentiment Analysis:
 
# It is a project to recognize the partiality 
# of a sentence or paragraph whether it is a positive or
# a negative comment.
                               


from textblob import TextBlob
from newspaper import Article
from tkinter import simpledialog
from tkinter.messagebox import showinfo
import nltk

# x = input('Enter any sentence to find its partiality:')
# article = Article(url)
answer = simpledialog.askstring('Sentiment Analysis', 'Enter any Sentence:\t\t\t\t')
# print(x)
# article.download()
# article.parse()
# article.nlp()

text =answer
blob = TextBlob(text)
sentiment = blob.sentiment.polarity
y=float(sentiment)
z=str(round(y*100))
z1 = z + "% "

if y > 0: 
    showinfo("Polarity", z1 + " (Its a Positive Sentence 😊)")
elif y < 0:
    showinfo("Polarity", z1 + " (Its a Negative Sentence 😡)")
else:
    showinfo("Polarity", "The given value is either 'Null' or has 'No Partiality' 😐")    

# print(z + "%" + " Partiality")
# if sentiment < 0:
#     print('It is a negative text')
# elif sentiment > 0:
#     print('it is a positive text')
# elif sentiment == 0:
#     print('Its a neutral text')
