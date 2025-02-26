import nltk
from nltk.stem import WordNetLemmatizer
import json
import pickle
import numpy as np
from keras._tf_keras.keras.models import Sequential
from keras._tf_keras.keras.layers import Dense, Dropout
from keras.api.optimizers import SGD
from keras.api.optimizers.schedules import ExponentialDecay
import random

nltk.download('punkt_tab')
nltk.download('wordnet')

# Cargar el archivo JSON
data_file = open('training.json', 'r', encoding='utf-8').read()
intents = json.loads(data_file)

lemmatizer = WordNetLemmatizer()

words = []
classes = []
documents = []
ignore_words = ["?", "!", ".", ","]

# Tokenizar y procesar las palabras en los patrones
for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent["tags"]))
        if intent["tags"] not in classes:
            classes.append(intent["tags"])

# Lematizar y limpiar palabras
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(set(words))
classes = sorted(set(classes))

# Guardar palabras y clases en archivos pickle
pickle.dump(words, open("words.pkl", "wb"))
pickle.dump(classes, open("classes.pkl", "wb"))

# Crear datos de entrenamiento
training = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    word_patterns = doc[0]
    word_patterns = [lemmatizer.lemmatize(w.lower()) for w in word_patterns]
    for w in words:
        bag.append(1 if w in word_patterns else 0)
    
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])

# Mezclar y convertir a NumPy arrays
random.shuffle(training)
train_x = np.array([row[0] for row in training])
train_y = np.array([row[1] for row in training])

# Crear la red neuronal
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation="softmax"))

# Configurar el optimizador
sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss="categorical_crossentropy", optimizer=sgd, metrics=["accuracy"])

# Entrenar el modelo
hist = model.fit(train_x, train_y, epochs=200, batch_size=5, verbose=1)

# Guardar el modelo entrenado
model.save("chatbot_model.h5")

print("✅ Modelo entrenado y guardado como 'chatbot_model.h5'")