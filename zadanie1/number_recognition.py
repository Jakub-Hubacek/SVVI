import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import img_to_array, array_to_img

###- trenovacia mnozina a musi trenovat na vsetkych cisliciach ; pouzit SoftMax aspon v jednom ako aktivacnu funkciu


# Načítanie MNIST datasetu
mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()


# Normalizácia hodnôt pixelov na rozsah [0, 1]
X_train = X_train / 255.0
X_test = X_test / 255.0

# Funkcia na zmenšenie obrázku na 4x7
def resize_image(image, target_size=(4, 7)):
    # Konverzia 28x28 obrázku na cieľovú veľkosť 4x7
    img = array_to_img(image.reshape(28, 28, 1))  # Zobrazenie ako obraz
    img_resized = img.resize(target_size)  # Zmenšenie na 4x7
    img_resized = img_to_array(img_resized).reshape(-1)  # Prevzatie do tvaru (28,)
    return img_resized

# Aplikácia funkcie na celý dataset
X_train_resized = np.array([resize_image(img) for img in X_train])
X_test_resized = np.array([resize_image(img) for img in X_test])

# Konverzia výstupov na one-hot encoding
y_train_onehot = tf.keras.utils.to_categorical(y_train, 10)
y_test_onehot = tf.keras.utils.to_categorical(y_test, 10)

# Rozdelenie tréningových dát na tréningový a validačný set
X_train_resized, X_val_resized, y_train_onehot, y_val_onehot = train_test_split(
    X_train_resized, y_train_onehot, test_size=0.2, random_state=42)

# Výpis tvarov datasetu na overenie
print(f"Tréningové dáta tvar: {X_train_resized.shape}")
print(f"Validačné dáta tvar: {X_val_resized.shape}")
print(f"Testovacie dáta tvar: {X_test_resized.shape}")
# Ukážka jedného obrázku a jeho labelu
import matplotlib.pyplot as plt

plt.imshow(X_train[1], cmap="gray")
plt.title(f"Označenie obrázku: {y_train[1]}")
plt.show()

## TRENING MODELU

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Vytvorenie neurónovej siete
model = Sequential()
model.add(Dense(32, input_shape=(28,), activation="relu"))  # Vstupná a skrytá vrstva
model.add(Dense(10, activation="softmax"))  # Výstupná vrstva

# Kompilácia modelu
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# Tréning modelu
model.fit(
    X_train_resized,
    y_train_onehot,
    epochs=20,
    batch_size=32,
    validation_data=(X_val_resized, y_val_onehot),
)

# Vyhodnotenie modelu na testovacom sete
test_loss, test_accuracy = model.evaluate(X_test_resized, y_test_onehot)
print(f"Testovacia presnosť: {test_accuracy * 100:.2f}%")


## Použitie modelu na predikciu
# Príklad predikcie jednej číslice
sample_digit = X_test_resized[2].reshape(1, -1)  # Vyberie prvý testovací vzor
sample_digit = np.array(
    [0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0]
)
sample_digit = sample_digit.reshape(1, -1)
print("Sample digit shape:", sample_digit)
predicted_digit = np.argmax(model.predict(sample_digit))
print("Predicted digit:", predicted_digit)
