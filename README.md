# Amharic Hate Speech: Datasets and Classification Models
### In this page we are introducing two datasets on Amharic hate speech detection and classification models:

## Title: The 5js in Ethiopia: Amharic Hate Speech Data Annotation Using Toloka Crowdsourcing Platform

ICT4D-2022 Dataset: This dataset is a Crowdsourced dataset of 5.3k tweets collected for our paper entittled <span style="color:red">**The 5js in Ethiopia: Amharic Hate Speech Data Annotation Using Toloka Crowdsourcing Platform.**</span> and presented in The 4th ICT4DA Conference 2022, Bahir Dar, Ethiopia. Each tweet in the datset is annotated with three annotatotrs on Yandex Toloka Crowdsourcing plantform
   
   ### Abstract
   This paper presents an Amharic hate speech annotation using the Yandex Toloka crowdsourcing platform. The dataset for this paper is collected from 5 consecutive years in Ethiopia (5Js), namely from 2018-2022, following the ‘June’ events in Ethiopia. Every June for the last five years, some events put the country in violence. Accordingly, we annotate 5,267 tweets, nearly 1k tweets every year. We explore the main challenges of crowdsourcing annotation for Amharic hate speech data collection using Toloka. We attain a Fliess kappa score of 0.34 using three independent annotators that annotate the tweets and the gold label is determined using majority voting. Using the datasets, we build different classification models using classical machine learning and deep learning approaches. The classical machine learning algorithms, LR and SVM, achieve an F1 score of 0.49, while NB archives an F1 score of 0.46. The deep learning algorithms (LSTM, BiLSTM, and CNN) achieve a similar F1 score, that is 0.44, which is the lowest performance of all models. The contextual embedding models, Am-FLAIR and Am-RoBERTa achieve F1 scores of 0.48 and 0.50 respectively. We publicly release the dataset, source code, and models with a permissive license.

   **Please read our paper for the details**
   

##  Title: Exploring Amharic Hate Speech Data Collection and Classification Approaches

RANLP-2023 Dataset: This dataset is collected with WebAnno annotation tool in controlled environment for the paper entittled <span style="color:red"> **Exploring Amharic Hate Speech Data Collection and Classification Approaches.**</span> and presented in Recent Advances in Natural Languages Processing-RANLP2023, Varna, Bulgaria. The datset consists of 15.1k tweets, each tweet annotated with two native speakers and the gold labels are determined with more experienced curators. 


### Abstract

In this paper, we present a study of efficient data selection and annotation strategies for Amharic hate speech. We also build various classification models and investigate the challenges of hate speech data selection, annotation, and classification for the Amharic language. From a total of over 18 million tweets in our Twitter corpus, 15.1k tweets are annotated by two independent native speakers, and a Cohen's kappa score of 0.48 is achieved. A third annotator, a curator, is also employed to decide on the final gold labels. We employ both classical machine learning and deep learning approaches, which include fine-tuning AmFLAIR and AmRoBERTa contextual embedding models. Among all the models, AmFLAIR achieves the best performance with an F1-score of 72%. We publicly release the annotation guidelines, keywords/lexicon entries, datasets, models, and associated scripts with a permissive license. 

**Please read our paper for the details**

Content
1. [Train Model](/code/README.md)
2. [Dataset]()
