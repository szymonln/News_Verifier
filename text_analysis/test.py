from analyzer import find_polish_keywords, find_english_keywords 

# test cases

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

doc2 = '''
    Gdyby szukać analogii w świecie przyrody, to hakerów bez problemu porównać 
    można by było do… mrówek. Potrafią przecisnąć się nawet przez najmniejszą 
    możliwą szczelinę. Gdy tylko dostępna jest okazja, z pewnością ją wykorzystają. 
    Takimi szczelinami, w naszych komputerach są właśnie luki w oprogramowaniach, 
    które otwierają drogę do danych i informacji przechowywanych na dyskach.
    Czym właściwie jest luka? To swego rodzaju „furtka” dla hakerów, umożliwiająca 
    zainfekowanie komputera złośliwym oprogramowaniem. Mówi się o niej, jako o błędzie 
    w kodzie w zabezpieczenia aplikacji. Chociaż definicji jest wiele, wszystkie 
    spójnie wyjaśniają, że luka umożliwia hakerowi wykonywanie czynności na naszym 
    komputerze, uzyskuje on zatem dostęp do danych, podszywając się pod inną jednostkę/program.
'''

print(find_english_keywords(doc1))

print(find_polish_keywords(doc2))