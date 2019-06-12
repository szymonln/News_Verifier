from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pickle
import os


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


def find_keywords(doc, cv, tfidf_transformer):
    tf_idf_vector = tfidf_transformer.transform(cv.transform([doc]))

    # sort candidates for keywords of tf-idf score
    sorted_items = sort_coo(tf_idf_vector.tocoo())

    feature_names = cv.get_feature_names()
    
    # top 10 results
    keywords = extract_topn_from_vector(feature_names, sorted_items, 10)

    # we can return whole dictionairy as well, with matching score
    return list(keywords.keys()) 


def find_english_keywords(doc):
    # loading trained Vectorizer
    cv = CountVectorizer(decode_error="replace", vocabulary=pickle.load(open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "feature.pkl"), "rb")))
    # loading trained Transformer
    tfidf_transformer = pickle.load(open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "tfidf1.pkl"), "rb"))
    return find_keywords(doc, cv, tfidf_transformer)


def find_polish_keywords(doc):
    # loading trained Vectorizer
    cv = CountVectorizer(decode_error="replace", vocabulary=pickle.load(open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "feature_pol.pkl"), "rb")))
    # loading trained Transformer
    tfidf_transformer = pickle.load(open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "tfidf1_pol.pkl"), "rb"))
    return find_keywords(doc, cv, tfidf_transformer)

if __name__ == "__main__":
    print(find_english_keywords("President Hillary Clinton came today to celebrate a huge victory"))
