### ABSTRACT ###

This thesis focuses on evaluating ChatGPT's ability to perform prompt-guided topic extraction on song lyrics. Prompt-guided topic extraction is the task of guiding ChatGPT to assign topic labels to a given text - in our case, song lyrics.
We compare the performance of currently-available versions of ChatGPT (3.5 and 4) given different factors: the method (whether or not the model is forced to pick from a set list of topic labels), the prompt category (whether or not the prompt includes lyrics) and the year of release of each song (pre-2021 or post-2021), which determines whether or not the song could have been included in ChatGPT's training data. 
The value of this research stems from the fact that - to the best of our knowledge - no previous scientific study has been carried out on ChatGPT's ability to systematically process and extract information from song lyrics.
Our approach consisted of two steps: first, the selection and creation of our own labelled dataset by using the Songfacts database; second, the implementation of the experiments; and third the comparison of results between ChatGPT3.5 and ChatGPT4. According to our experiments, using ChatGPT3.5 and  including the lyrics in the prompt yielded the best results. We also implemented different evaluation methods for ChatGPT given different circumstances, providing initial stepping stones into developing ways to extract information from song lyrics in a (semi-)automatic, scalable way. 

### CODE ###


Here, you will find the following scripts which need to be executed in the following order:

- analyze_distribution.py 
- analyze_informative_features.py
- feature_extraction.py
- ner_system.py
- evaluation.py 
- feature_ablation.py
- crf.py
- crf_evaluation.py  



### DATA ###

The data folder contains all outputs from the abovementioned scripts. 
