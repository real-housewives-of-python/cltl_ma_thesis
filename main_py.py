import spacy
import sys
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from sklearn import metrics
from scipy import spatial



def main_py(infile, outfile):

    nlp = spacy.load("en_core_web_lg")

    file = pd.read_csv(infile, delimiter='\t', header=None, skiprows=1) 
    df = pd.DataFrame(file)

    #Convert columns to lists

    Track = df[0].tolist()
    Artist = df[1].tolist()
    Lyrics = df[2].tolist()
    Date = df[3].tolist()
    Gold = df[4].tolist()
    K1 = df[5].tolist()
    K2 = df[6].tolist()
    K3 = df[7].tolist()
    L1 = df[8].tolist()
    L2 = df[9].tolist()
    L3 = df[10].tolist()


    #Knowledge 1

    k1 = []
    for a, b in zip(Gold, K1):
        vector_a = nlp(a).vector
        vector_b = nlp(b).vector

        similarity = 1 - spatial.distance.cosine(vector_a, vector_b)
        roundedsim = round(similarity, 2)

        k1.append(roundedsim)

    #Knowledge 2

    k2 = []
    for a, b in zip(Gold, K2):
        vector_a = nlp(a).vector
        vector_b = nlp(b).vector

        similarity = 1 - spatial.distance.cosine(vector_a, vector_b)
        roundedsim = round(similarity, 2)

        k2.append(roundedsim)

    #Knowledge 3

    k3 = []
    for a, b in zip(Gold, K3):
        vector_a = nlp(a).vector
        vector_b = nlp(b).vector

        similarity = 1 - spatial.distance.cosine(vector_a, vector_b)
        roundedsim = round(similarity, 2)

        k3.append(roundedsim)


    #Lyrics 1

    l1 = []
    for a, b in zip(Gold, L1):
        vector_a = nlp(a).vector
        vector_b = nlp(b).vector

        similarity = 1 - spatial.distance.cosine(vector_a, vector_b)
        roundedsim = round(similarity, 2)

        l1.append(roundedsim)

    #Lyrics 2

    l2 = []
    for a, b in zip(Gold, L2):
        vector_a = nlp(a).vector
        vector_b = nlp(b).vector

        similarity = 1 - spatial.distance.cosine(vector_a, vector_b)
        roundedsim = round(similarity, 2)

        l2.append(roundedsim)

    #lyrics 3

    l3 = []
    for a, b in zip(Gold, L3):
        vector_a = nlp(a).vector
        vector_b = nlp(b).vector

        similarity = 1 - spatial.distance.cosine(vector_a, vector_b)
        roundedsim = round(similarity, 2)

        l3.append(roundedsim)


    dict = {'Track': Track, 'Artist': Artist,'Lyrics': Lyrics, 'Date': Date, 'Gold': Gold, 'K1': K1,
                            'K2': K2, 'K3': K3, 'L1': L1, 'L2': L2, 'L3': L3} 

    df = pd.DataFrame(dict)
    df['Sim K1'] = pd.Series(k1)
    df['Sim K2'] = pd.Series(k2)
    df['Sim K3'] = pd.Series(k3)
    df['Sim L1'] = pd.Series(l1)
    df['Sim L2'] = pd.Series(l2)
    df['Sim L3'] = pd.Series(l3)

    df.to_csv(outfile,sep='\t', index = False)
    
    #Create comparison table
    
    count_k1_1 = 0
    count_k1_2 = 0
    count_k1_3 = 0
    count_k1_4 = 0
    
    count_k2_1 = 0
    count_k2_2 = 0
    count_k2_3 = 0
    count_k2_4 = 0
    
    count_k3_1 = 0
    count_k3_2 = 0
    count_k3_3 = 0
    count_k3_4 = 0
    
    count_l1_1 = 0
    count_l1_2 = 0
    count_l1_3 = 0
    count_l1_4 = 0
    
    count_l2_1 = 0
    count_l2_2 = 0
    count_l2_3 = 0
    count_l2_4 = 0
    
    count_l3_1 = 0
    count_l3_2 = 0
    count_l3_3 = 0
    count_l3_4 = 0
    
    for n in K1:
        if n == '1':
            count_k1_1 += 1
        elif 0.81 <= n <= 1:
            count_k1_2 += 1
        elif 0.61 <= n <= 0.8:
            count_k1_3 += 1
        elif n <= 0.6:
            count_k1_4 += 1
            
    for n in K2:
        if n == '1':
            count_k2_1 += 1
        elif 0.81 <= n <= 1:
            count_k2_2 += 1
        elif 0.61 <= n <= 0.8:
            count_k2_3 += 1
        elif n <= 0.6:
            count_k2_4 += 1
            
            
    for n in K3:
        if n == '1':
            count_k3_1 += 1
        elif 0.81 <= n <= 1:
            count_k3_2 += 1
        elif 0.61 <= n <= 0.8:
            count_k3_3 += 1
        elif n <= 0.6:
            count_k3_4 += 1
            
    for n in L1:
        if n == '1':
            count_l1_1 += 1
        elif 0.81 <= n <= 1:
            count_l1_2 += 1
        elif 0.61 <= n <= 0.8:
            count_l1_3 += 1
        elif n <= 0.6:
            count_l1_4 += 1
            
    for n in L2:
        if n == '1':
            count_l2_1 += 1
        elif 0.81 <= n <= 1:
            count_l2_2 += 1
        elif 0.61 <= n <= 0.8:
            count_l2_3 += 1
        elif n <= 0.6:
            count_l2_4 += 1
            
            
    for n in L3:
        if n == '1':
            count_l3_1 += 1
        elif 0.81 <= n <= 1:
            count_l3_2 += 1
        elif 0.61 <= n <= 0.8:
            count_l3_3 += 1
        elif n <= 0.6:
            count_l3_4 += 1
            
    count = {'Perfect match': [count_k1_1, count_k2_1, count_k3_1, count_l1_1, count_l2_1, count_l3_1],
    'Almost perfect': [count_k1_2, count_k2_2, count_k3_2, count_l1_2, count_l2_2, count_l3_2],
    'Subsantial': [count_k1_3, count_k2_3, count_k3_3, count_l1_3, count_l2_3, count_l3_3],
    'Diff interpretation': [count_k1_4, count_k2_4, count_k3_4, count_l1_4, count_l2_4, count_l3_4]}
            
    dfcount = pd.DataFrame(data, index=['K1',
                               'K2',
                               'K3',
                               'L1',
                               'L2',
                                'L3'])
    dfcount.to_csv('results_count.tsv',sep='\t', index = False)
    
    
    

def main(argv=None):
    
    if argv is None:
        argv = sys.argv
                
    infile = argv[1] 
    outfile = argv[2]
    
    main_py(infile, outfile)
    
    
    
    
if __name__ == '__main__':
    main()