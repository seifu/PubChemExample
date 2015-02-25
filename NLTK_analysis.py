__author__ = 'sjc294'


def remove_spaces():
    import get_files

    my_files = get_files.get_files(
        "F:\\Research\\Cheminformatics\\Results\\ChemotherapyResults\\MinedPaperResults\\ChemotherapyOnlyChemicals")

    for fi in my_files:
        # print("F:\\Research\\Cheminformatics\\Results\\ChemotherapyResults\\MinedPaperResults\\ChemotherapyOnlyChemicalsNoSpaces\\"+fi.split('\\')[-1])
        with open(fi, 'r') as f:
            #with open()
            with open(
                            "F:\\Research\\Cheminformatics\\Results\\ChemotherapyResults\\MinedPaperResults\\ChemotherapyOnlyChemicalsNoSpaces\\" +
                            fi.split('\\')[-1], "ab+") as o:
                for l in f.readlines():
                    o.write(bytes(l.replace(" ", ""), 'UTF-8'))


def load_chemical_corpus(root):
    from nltk.corpus import PlaintextCorpusReader, CategorizedPlaintextCorpusReader

    corpus_root = root
    # wordlists = PlaintextCorpusReader(corpus_root, '.*')
    reader = CategorizedPlaintextCorpusReader(root, r'.*\.chem',
                                              cat_file="F:\\Research\\Cheminformatics\\Results\\ChemotherapyResults\\MinedPaperResults\\cats.txt")
    return reader  # wordlists, reader


def analyze_chemical_corpus(corp):
    import nltk

    cfd = nltk.ConditionalFreqDist(
        [(keyword, word.lower())
         for keyword in corp.categories()
         for word in corp.words(categories=keyword)])
    # [print(x, ' ', cfd[x].most_common(5)) for x in corp.categories]
    print('hi')


if __name__ == "__main__":
    readerr = load_chemical_corpus(
        'F:\\Research\\Cheminformatics\\Results\\ChemotherapyResults\\MinedPaperResults\\ChemotherapyOnlyChemicalsNoSpaces')
    analyze_chemical_corpus(readerr)
    #print(len(wordlist.fileids()))