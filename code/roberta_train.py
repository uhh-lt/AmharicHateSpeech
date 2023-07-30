from flair.data import Corpus
from flair.datasets import ClassificationCorpus
from flair.embeddings import TransformerDocumentEmbeddings
from flair.models import TextClassifier
from flair.trainers import ModelTrainer
import flair
import torch

flair.set_seed(42)

data_folder = 'data'
 # 1. get the corpus
    #corpus: Corpus = TREC_6()
flair.device = torch.device('cuda')
    # 2. what label do we want to predict?
label_type = 'hate_class'

    # load corpus by pointing to folder. Train, dev and test gets identified automatically.
corpus: Corpus = ClassificationCorpus(data_folder, label_type=label_type)


        # 3. create the label dictionary
label_dict = corpus.make_label_dictionary(label_type=label_type)

        # 4. initialize transformer document embeddings (many models are available)
document_embeddings = TransformerDocumentEmbeddings('uhhlt/am-roberta', fine_tune=True)

        # 5. create the text classifier
classifier = TextClassifier(document_embeddings, label_dictionary=label_dict, label_type=label_type)

        # 6. initialize trainer
trainer = ModelTrainer(classifier, corpus)

        # 7. run training with fine-tuning
trainer.fine_tune('resources/taggers/hate-classification-with-transformer',
                                  learning_rate=5.0e-5,
                                  mini_batch_size=4,
                                  max_epochs=9,
                                  )
