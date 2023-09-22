
 [![](../../logo.png)](https://github.com/uhh-lt/amharicmodels/)
# Introduction
The Amharic Hate Speech data is collected using the Twitter API spanning from October 1, 2020 - November 30, 2022, considering the socio-political dynamics of Ethiopia in Twitter space. We used [WEbAnno](http://ltdemos.informatik.uni-hamburg.de/codebookanno-cba/) tool for data annotation; each tweet is annotated by two native speakers and curated by one more experienced adjudicator to determine the gold labels. A total of 15.1k tweets consisting of three class labels namely: Hate, Offensive and Normal are presented. Read our papers for more details about the dataset (see below).

# Amharic Hate Speech Data Annotation: Lab-Controlled Annotation
The dataset is annotated by two annotators and a curator to determine the gold labels.  

For more details, You can read our paper entitled:

## Details of the data
1. train/dev/test.csv

This dataset is ready-made for direct experiments and contains tweet_Id, tweet, and labels for the train/dev/test split datasets. 
   
3. with_annotators_train/test/dev.csv

This dataset is presented with every detail of annotations by two native speakers and the curator for researchers who want to explore our dataset in more detail. 

[Exploring Amharic Hate Speech Data Collection and Classification Approaches](https://www.inf.uni-hamburg.de/en/inst/ab/lt/publications/2023-ayele-et-al-hate-ranlp.pdf)

   
```
@INPROCEEDINGS{9971385,  
author={Ayele, Abinew Ali and Yimam, Seid Muhie and Belay, Tadesse Destaw and Asfaw, Tesfa and  Biemann, Chris},  
booktitle={Proceedings of the 14th Conference on RECENT ADVANCES IN NATURAL LANGUAGE PROCESSING (RANLP 2023},   
title={Exploring Amharic Hate Speech Data Collection and Classification Approaches},   
year={2023},    
location = {Varna, Bulgaria}
}
```



