# Sentiment-Analysis
The sentiment analysis project is a Python-based project that allows users to enter any sentence or paragraph and analyzes the sentiment polarity of the text. It uses TextBlob, a Python-based library for processing textual data, to identify whether the text is positive, negative, or neutral. The program then displays the result using a message box.

# Libraries Used
The following libraries were used in this project:
textblob - A library for processing textual data, including sentiment analysis.
newspaper - A Python-based library for web scraping news articles.
tkinter - A standard Python library for creating graphical user interfaces (GUIs).
nltk - A Python-based library for natural language processing.

# Functionality
The program begins by asking the user to enter a sentence or paragraph using a dialog box. Once the user has entered the text, the program uses TextBlob to analyze the sentiment polarity of the text. Sentiment polarity is a score between -1 and 1, where scores greater than 0 indicate positive sentiment, scores less than 0 indicate negative sentiment, and scores equal to 0 indicate neutral sentiment.
The program then displays the result using a message box, which indicates the partiality percentage of the text, along with an emoji to represent the sentiment polarity. If the partiality percentage is greater than 0, the message box displays a positive emoji, indicating positive sentiment. If the partiality percentage is less than 0, the message box displays a negative emoji, indicating negative sentiment. If the partiality percentage is equal to 0, the message box displays a neutral emoji, indicating neutral sentiment.

# Conclusion
Sentiment analysis is a valuable tool for analyzing textual data and identifying patterns and trends in sentiment polarity. This Python-based project demonstrates how TextBlob can be used to analyze the sentiment polarity of text and how tkinter can be used to create a simple graphical user interface for displaying the results. By using this project as a starting point, developers can expand upon the functionality and create more sophisticated sentiment analysis tools for a variety of use cases.
