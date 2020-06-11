Recently there have been a huge array of online services offering courses that allegedly prepare an individual for a job as a Data Scientist. But it is still difficult for an individual starting out in this field from an unrelated background to make sound deci- sion regarding course choice that will maximize their chances of landing a Data Science related job. The course recommendation system aims to alleviate this problem by providing a list of recommended courses aimed at covering the skills the user is interested in learning for getting a job as a Data Scientist/Analyst, using the Northeastern Univerity course catalog for Data Science and Data Analytics related courses, and the Indeed Job Dataset. This recommendation system is not just based on matching the skills to courses, but also to jobs. In other words, when a user inputs a set of skills, the engine uses K-Means clustering to find which category of Jobs those skills belong to, and finds the list of courses that will cover those topics using cosine similarities. This recommendation system is intended to help users select courses for landing specific Data Science related jobs.


Directions to run course recommender on local system (with an example):

1. navigate to the directory and run python3 main.py from terminal 
2. open app.html in chrome
3. input "python, machine learning, neural networks, artificial intelligence, regression, classification, modeling, supervised" in the input field
4. click button 
