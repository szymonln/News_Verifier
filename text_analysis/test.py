from analyzer import find_keywords

# test case

doc1 = '''
    Researchers have come up with a method for creating realistic-looking — but fake — 
    videos of anyone by using just a single image of them with a trained artificial 
    intelligence system. It's a potentially worrisome capability in the runup to the 
    2020 United States presidential election, as falsified videos of candidates are 
    expected to spread. Researchers at the Samsung AI Center in Moscow and the Moscow-based 
    Skolkovo Institute of Science and Technology explained the feat in a paper published 
    this week to the arXiv, an online academic pre-print service. They said they were able 
    to animate one or several photos of people by first training an AI system on a dataset 
    of videos including many celebrities, so it could learn about key points on the face. 
    After that, the AI system was able to combine that familiarity with one or more images 
    of a person to come up with a convincing "talking head"-style video of them. 
'''

print(find_keywords(doc1))