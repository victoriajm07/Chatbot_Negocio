import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from keras.api.models import load_model

lemmatizer = WordNetLemmatizer() # Instanciar la class
# Cargar el archivo JSON
intents = json.loads(open('training.json', 'r', encoding='utf-8').read())

# Carga el modelo
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')

def clean_up_sentence(sentence): # Traducción al lenguaje natural
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence) # Almacen de palabras proporcionadas por el usuario
    bag = [0] * len(words) # Crea una lista con las palabras
    for w in sentence_words: 
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    bow = np.array([bow])
    print(f"🔍 Bag of Words (entrada): {bow.shape}")  # Verifica el tamaño del input
    res = model.predict(bow)[0]
    print(f"🔍 Resultados crudos: {res}")
    ERROR_THRESHOLD = 0.1  # Reducir umbral
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    print(f"🎯 Resultados después del umbral: {results}")  # Verifica si hay predicciones
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = [{'intent': classes[r[0]], 'probability': str(r[1])} for r in results]
    print(f"✅ Predicciones finales: {return_list}")
    return return_list


def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tags'] == tag:
            result = random.choice(i['responses'])
            break
    return result

