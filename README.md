### ABSTRACT ###

This thesis focuses on evaluating ChatGPT's ability to perform prompt-guided topic extraction on song lyrics. Prompt-guided topic extraction is the task of guiding ChatGPT to assign topic labels to a given text - in our case, song lyrics.
We compare the performance of currently-available versions of ChatGPT (3.5 and 4) given different factors: the method (whether or not the model is forced to pick from a set list of topic labels), the prompt category (whether or not the prompt includes lyrics) and the year of release of each song (pre-2021 or post-2021), which determines whether or not the song could have been included in ChatGPT's training data. 
The value of this research stems from the fact that - to the best of our knowledge - no previous scientific study has been carried out on ChatGPT's ability to systematically process and extract information from song lyrics.
Our approach consisted of two steps: first, the selection and creation of our own labelled dataset by using the Songfacts database; second, the implementation of the experiments; and third the comparison of results between ChatGPT3.5 and ChatGPT4. According to our experiments, using ChatGPT3.5 and  including the lyrics in the prompt yielded the best results. We also implemented different evaluation methods for ChatGPT given different circumstances, providing initial stepping stones into developing ways to extract information from song lyrics in a (semi-)automatic, scalable way. 

This repository contains the following:

-- results_CHATGPT3.5 - a tsv file containing the results of using ChatGPT3.5 for prompt-guided topic extraction. 

-- results_CHATGPT4 - a tsv file containing the results of using ChatGPT4 for prompt-guided topic extraction. 

-- main_py.py - a script that calculates the similarity scores and similarity threshold (Perfect Match, Almost Match, Substantial Match, Different Interpretation). Use the files results_CHATGPT3.5 / results_CHATGPT4 as input file.

-- Confusion_matrices.ipynb - a Jupyter Notebook which outputs 4 confusion matrices: ChatGPT4 - Knowledge (Closed), ChatGPT4 - Lyrics (Closed), ChatGPT3.5 - Knowledge (Closed), ChatGPT3.5 - Lyrics (Closed).

-- cosine_CHATGPT3.5 - a tsv file containing the similarity scores for ChatGPT3.5.

-- cosine_CHATGPT4 - a tsv file containing the similarity scores for ChatGPT4.

-- thresholds_ChatGPT3.5 - a tsv file containing the similarity thresholds for ChatGPT3.5.

-- thresholds_ChatGPT4 - a tsv file containing the similarity thresholds for ChatGPT4.


### REQUIREMENTS ###

Jupyter Notebook
