import tensorflow as tf
import numpy as np
import PIL
from matplotlib import pyplot as plt
import pathlib
import random


def entrada(diretorio:str,input_shape:tuple, SEED:int):

    dados_treinamento = tf.keras.utils.image_dataset_from_directory(
        diretorio,
        validation_split=0.2,
        subset='training',
        seed= SEED,
        image_size=(input_size[0], input_size[1]),
        batch_size=32,
        shuffle=True
    )
    
    dados_validacao = tf.keras.utils.image_dataset_from_directory(
        diretorio,
        validation_split=0.2,
        subset='validation',
        seed= SEED,
        image_size=(input_size[0], input_size[1]),
        batch_size=32,
        shuffle=True
    )

    return dados_treinamento, dados_validacao


modelo = tf.keras.Sequential([
        tf.keras.layers.InputLayer(input_shape=input_size),
        tf.keras.layers.Rescaling(1./360),
        tf.keras.layers.Conv2D(16, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(8, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(8, activation='softmax')
    ])


# Compilando o modelo
modelo.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


def my_callback():
    class MyCallback(tf.keras.callbacks.Callback):
        def on_epoch_end(self, epoch, logs=None):
            if logs.get('accuracy') > 0.90:
                print("\nAtingiu 90% de acurácia, interrompendo treinamento!")
                self.model.stop_training = True
    return MyCallback()


historico = modelo.fit(dados_treinamento,validation_data=dados_validacao, epochs=10, validation_split=0.2, verbose=1,callbacks=[my_callback()])



validacao, treinamento = entrada(diretorio, input_size, SEED)

modelo.fit(treinamento, epochs=10, validation_data=validacao, verbose=1)



def predict_image(image_path):
    # Carrega a imagem
    PIL.ImageShow.show(PIL.Image.open(image_path))
    # Abre a imagem usando PIL
    image = PIL.Image.open(image_path)
    # Converte para array numpy e normaliza
    image = np.array(image, dtype=np.float32)
    image = image / 360.0
    # Expande as dimensões para incluir o batch size
    image = np.expand_dims(image, axis=0)
    # Faz a predição
    prediction = modelo.predict(image)
    nome_classe = dados_treinamento.class_names[prediction.argmax(axis=1)[0]]

    # Retorna a classe prevista
    return nome_classe 

predict_image(image_path)