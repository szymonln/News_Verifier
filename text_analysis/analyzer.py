from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pickle

def get_stop_words(stop_file_path):
    """load stop words """
    with open(stop_file_path, 'r', encoding="utf-8") as f:
        stopwords = f.readlines()
        stop_set = set(m.strip() for m in stopwords)
        return frozenset(stop_set)


def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)


def extract_topn_from_vector(feature_names, sorted_items, topn=10):
    """get the feature names and tf-idf score of top n items"""
    
    # we take only 'topn' best results
    sorted_items = sorted_items[:topn]
 
    score_vals = []
    feature_vals = []
    
    # index and tf-idf score
    for idx, score in sorted_items:
        
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])
 
    results= {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]]=score_vals[idx]
    
    return results


def find_keywords(doc):
    # loading trained Vectorizer
    cv = CountVectorizer(decode_error="replace",vocabulary=pickle.load(open("feature.pkl", "rb")))

    # loading trained Transformer
    tfidf_transformer = pickle.load(open("tfidf1.pkl", 'rb'))
    
    tf_idf_vector = tfidf_transformer.transform(cv.transform([doc]))

    # sort candidates for keywords of tf-idf score
    sorted_items = sort_coo(tf_idf_vector.tocoo())

    feature_names = cv.get_feature_names()
    
    # top 10 results
    keywords = extract_topn_from_vector(feature_names, sorted_items, 10)

    # we can return whole dictionairy as well, with matching score
    return list(keywords.keys()) 
