CYBERBULLYING DETECTION USING A HYBRID RNN-LSTM MODEL
Cyberbullying has become a significant concern in the digital age, with harmful online 
interactions impacting individuals' mental health and well-being. To address this issue, our 
project aims to develop an automated cyberbullying detection system using a combination of 
machine learning and deep learning techniques.  
This project successfully tackles the problem of cyberbullying detection through the following 
comprehensive steps: 
1. Data Collection and Preprocessing: 
We began by collecting comments data, ensuring it was cleaned and structured for 
further analysis. Preprocessing techniques such as tokenization, stopword removal, 
lemmatization, and stemming were applied to standardize the textual data. Sentiment 
labelling was then conducted to classify comments into "cyberbullying" or "non
cyberbullying." 
2. Feature Extraction: 
The textual data was transformed into numerical representations using the TF-IDF 
Vectorizer, allowing machine learning models to process and analyze the comments 
effectively. This step converted human-readable text into a format that is 
computationally understandable. 
3. Dataset Splitting: 
To ensure a fair evaluation of the models, the dataset was split into training and testing 
sets, with the training data used to build the models and the testing data reserved for 
performance validation. 
4. Model Training: 
We employed multiple machine learning algorithms, including Logistic Regression, 
Random Forest Classifier, Multinomial Naive Bayes, and Support Vector Machine 
(SVM). Each model was trained, evaluated, and compared based on metrics such as 
accuracy, precision, recall, and F1-score. 
5. Deep Learning Integration: 
To enhance performance and handle complex sequential data, we trained Neural 
Network models such as LSTM (Long Short-Term Memory) and RNN (Recurrent 
Neural Networks). These models effectively captured the sequential nature of text, 
offering deeper insights into context and sentiment. 
6. Model Saving: 
The best-performing models were saved for future use, ensuring they can be deployed 
without requiring retraining. This step optimizes efficiency and prepares the models for 
real-world application. 
7. GUI Development: 
To make the system accessible and interactive, we developed a user-friendly Graphical 
User Interface (GUI) using Flask. This web application allows users to input comments 
and receive instant predictions about whether the comment constitutes cyberbullying 
or not. 
