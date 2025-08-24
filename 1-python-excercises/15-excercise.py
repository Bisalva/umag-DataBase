# FUNCTION FROM Base de datos 2 Workclass


text = "Python es un lenguaje de programación. Python es fácil de aprender."

def text_analysis(text):

    words = text.replace(".", "").replace(",", "").split()
    unique_words = set(w for w in words if w != "")
    longest_word = max(words, key=len) if words else ""

    return {
        "total_palabras": len(words),
        "palabras_unicas": len(unique_words),
        "palabra_mas_larga": longest_word,
    }

print(text_analysis(text))