import re

# Mapping dictionary for NLTK to SpaCy conversion
nltk_to_spacy_mapping = {
    r"import nltk": "import spacy\nnlp = spacy.load('en_core_web_sm')",
    
    # Tokenization
    r"from nltk.tokenize import word_tokenize": "import spacy\nnlp = spacy.load('en_core_web_sm')",
    r"word_tokenize\((.*?)\)": "[token.text for token in nlp(\\1)]",
    r"from nltk.tokenize import sent_tokenize": "import spacy\nnlp = spacy.load('en_core_web_sm')",
    r"sent_tokenize\((.*?)\)": "[sent.text for sent in nlp(\\1).sents]",

    # POS Tagging
    r"from nltk import pos_tag": "import spacy\nnlp = spacy.load('en_core_web_sm')",
    r"pos_tag\((.*?)\)": "[(token.text, token.pos_) for token in nlp(' '.join(\\1))]",
    
    # Lemmatization
    r"from nltk.stem import WordNetLemmatizer": "import spacy\nnlp = spacy.load('en_core_web_sm')",
    r"(\w+)\s*=\s*WordNetLemmatizer\(\)": "",  # Capture variable assignment and remove it
    
    # Variable usage for lemmatization
    r"\b\w+\.(lemmatize)\((.*?)\)": "[nlp(\\2)[0].lemma_]",  # Replace lmtzr.lemmatize(word) with nlp(word)[0].lemma_

    # Named Entity Recognition (NER)
    r"from nltk import ne_chunk": "import spacy\nnlp = spacy.load('en_core_web_sm')",
    r"nltk.ne_chunk\((.*?)\)": "[(ent.text, ent.label_) for ent in nlp(\\1).ents]",

    # Stopwords
    r"from nltk.corpus import stopwords": "import spacy\nfrom spacy.lang.en.stop_words import STOP_WORDS",
    r"stopwords.words\('english'\)": "STOP_WORDS",

    # Dependency Parsing
    r"from nltk import DependencyGraph": "import spacy\nnlp = spacy.load('en_core_web_sm')",
    r"DependencyGraph\(\)": "[(token.text, token.dep_, token.head.text) for token in nlp(text)]",

    # Word Similarity
    r"from nltk.corpus import wordnet": "import spacy\nnlp = spacy.load('en_core_web_sm')",
    r"wordnet.synsets\((.*?)\)": "token1.similarity(token2)",

    # n-grams
    r"from nltk import ngrams": "import spacy\nnlp = spacy.load('en_core_web_sm')",
    r"ngrams\((.*?), (.*?)\)": "spacy.util.filter_spans([token.text for token in nlp(text)])[0:int(\\2)]",

    # Sentence Segmentation
    r"from nltk.tokenize import PunktSentenceTokenizer": "import spacy\nnlp = spacy.load('en_core_web_sm')",
    r"PunktSentenceTokenizer\(\).tokenize\((.*?)\)": "[sent.text for sent in nlp(\\1).sents]",

    # Chunking
    r"from nltk.chunk import RegexpParser": "import spacy\nnlp = spacy.load('en_core_web_sm')",
    r"RegexpParser\(grammar\)": "Use SpaCy's dependency parsing to identify similar structures",

    # WordNet Lemmatization
    r"from nltk.corpus import wordnet": "Use external libraries like 'pywordnet' for WordNet-like functionality in SpaCy",

    # Stemming (not available in SpaCy)
    r"from nltk.stem import SnowballStemmer": "Not available in SpaCy (consider using lemmatization instead)",
}

def nltk_to_spacy_converter(input_script):
    # Step 1: Apply the mapping transformations
    for nltk_pattern, spacy_replacement in nltk_to_spacy_mapping.items():
        input_script = re.sub(nltk_pattern, spacy_replacement, input_script)
    
    # Additional changes specific to data structures
    input_script = input_script.replace("df['tokenized']", "df['tokenized']")  # If needed for column renaming
    
    return input_script

# Example usage: Reading from a file and converting the script
def convert_nltk_to_spacy(input_file, output_file):
    with open(input_file, 'r') as file:
        script_content = file.read()

    # Perform conversion
    converted_script = nltk_to_spacy_converter(script_content)

    # Write the converted script to a new file
    with open(output_file, 'w') as file:
        file.write(converted_script)

    print(f"Conversion complete. Converted script saved to {output_file}")

# Example usage:
convert_nltk_to_spacy('target.py', 'spacy_script.py')
