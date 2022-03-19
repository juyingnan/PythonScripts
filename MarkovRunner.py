import MarkovGenerator as MG
mymarkov = MG.Markov("speech.txt")
mymarkov.generate(250, n=3)