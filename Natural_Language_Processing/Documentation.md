# Natural Language Processing(NLP)
Natural language processing is a technique which allows us to fetch selective words from our training dataset which are to be used as features to train the model upon. It uses techniques like lemmatization and stemming to segregate meaningful words from the text document. After cleaning out the data and generating features we can use any classifier like naivebayes, support vector machine(svm) ,etc as our model that may be trained against the generated features and be used to make predictions on the testing data.

</br>
<img src="https://storage.googleapis.com/aliz-website-sandbox-strapi-cms/Natural_Language_Processing_03_1_png_1a3c947369/Natural_Language_Processing_03_1_png_1a3c947369.webp" width=500>

</br>   

### Stop Words
These are insignificant words which themselves does not mean anything individually but are used for grammar. Examples-is,are,we,all,why,when etc. These words including the punctuations are needed to be filtered out from the datasets.

### Stemming
This is used to convert all the words into their root form like all words playing, plays, played, playing will be transformed to their root word i.e play, while the word player would not be converted to play. But the drawback with stemming is that for this task it uses a set rules to remove some words from the back of string which often leads to wrong results. For example word caring would be converted to "*car*" instead of *"care"*.

</br>
<img src="https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/BlogImages/04102018020016AM/1.jpg" width=300>

</br>

### Part of speech
It is very important to find in which context does a particular word is being referred to. If it is used as noun, adjective, verb ,etc.

### Lemmatization
Lemmatizer is a more powerful tool than stemming and uses part of speech and takes into account the context in which a particular word is used to transform it to its root form. For example word caring would be converted to "*care*" and not *"car"* as in case of stemming.

</br>

<img src="https://camo.githubusercontent.com/369569beca1e2ddcd4d5ab03afabe27a6015c13a75d662885f91633499b739d3/68747470733a2f2f6d69726f2e6d656469756d2e636f6d2f6d61782f323035302f312a455335627437496f496e49713259696f5170327a63512e706e67" width=400>

</br>

### Code description
our code is written to predict if a given movie review.Though the code contains many functions but it has two main functions:
* clean_review - this fuction lemmatizes and removes all the stopwords including the punctuation from the string passed and return the leftover words.
* get_feature_dict - this function is used to convert the list of riviews into a dictionary containing x<sub>input</sub> values for each feature.

After geting the processed data from the get_feature_dictionary we can apply any classification model on it. In our case we applied two classifiers one naivebayes from nltk itself and another svc from sklearn.