# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lhvOuWklWERBtRjIRSWgZyGbn6nmE8je
"""

from google.colab import files
uploaded = files.upload()

import zipfile
import os

# Define the file name
zip_file = "notable_figures.zip"

# Extract the zip file
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall("notable_figures")

import os

# Verify extracted folders
base_dir = "notable_figures"
categories = os.listdir(base_dir)
print("Categories:", categories)

# List files in a specific category
for category in categories:
    print(f"Files in {category}:")
    print(os.listdir(os.path.join(base_dir, category)))

import os

# Check the contents of the notable_figures directory
base_dir = "notable_figures"
print(os.listdir(base_dir))

# Define path to 445 project folder
project_dir = os.path.join(base_dir, "445 project")
categories = os.listdir(project_dir)
print("Categories:", categories)

from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Create ImageDataGenerator
datagen = ImageDataGenerator(
    rescale=1./255,         # Normalize pixel values
    validation_split=0.2    # Split data into training and validation
)

# Load training data
train_data = datagen.flow_from_directory(
    project_dir,            # Use the path to 445 project
    target_size=(128, 128), # Resize images
    batch_size=32,          # Batch size
    class_mode='categorical',
    subset='training'
)

# Load validation data
val_data = datagen.flow_from_directory(
    project_dir,            # Use the path to 445 project
    target_size=(128, 128),
    batch_size=32,
    class_mode='categorical',
    subset='validation'
)

# List the full structure
for root, dirs, files in os.walk("."):
    print(root, dirs, files)

import tensorflow as tf
from tensorflow.keras import layers

# Define the generator
def build_generator():
    model = tf.keras.Sequential([
        layers.Dense(256, activation="relu", input_shape=(100,)),  # Input: Random noise
        layers.BatchNormalization(),
        layers.Dense(128 * 128 * 3, activation="sigmoid"),
        layers.Reshape((128, 128, 3))  # Output: Image of shape 128x128x3
    ])
    return model

# Define the discriminator
def build_discriminator():
    model = tf.keras.Sequential([
        layers.Flatten(input_shape=(128, 128, 3)),
        layers.Dense(256, activation="relu"),
        layers.Dense(1, activation="sigmoid")  # Output: Probability of being real
    ])
    return model

# Instantiate models
generator = build_generator()
discriminator = build_discriminator()

# Compile discriminator
discriminator.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Build the GAN
gan_input = layers.Input(shape=(100,))
generated_image = generator(gan_input)
discriminator.trainable = False  # Freeze discriminator during generator training
gan_output = discriminator(generated_image)

gan = tf.keras.Model(gan_input, gan_output)
gan.compile(optimizer="adam", loss="binary_crossentropy")

epochs = 1000

import numpy as np  # Import numpy
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Reshape
from tensorflow.keras.optimizers import Adam
# Other imports...

# Define the number of epochs
epochs = 1000  # Example value

for epoch in range(epochs):
    # Get a random batch of real images
    real_images, _ = next(train_data)  # Get real images
    batch_size_actual = real_images.shape[0]  # Dynamically determine actual batch size

    # Adjust real and fake labels dynamically
    real_labels = np.ones((batch_size_actual, 1))  # Match to real batch size
    fake_labels = np.zeros((batch_size_actual, 1))  # Match to real batch size

    # Training loop continues...

import matplotlib.pyplot as plt

# Function to save generated images
def save_generated_images(epoch, generator, examples=10, dim=(1, 10), figsize=(20, 2)):
    noise = generate_random_noise(examples)
    generated_images = generator.predict(noise)
    generated_images = 0.5 * generated_images + 0.5  # Rescale to [0,1]

    plt.figure(figsize=figsize)
    for i in range(examples):
        plt.subplot(dim[0], dim[1], i + 1)
        plt.imshow(generated_images[i].squeeze(), cmap='gray')
        plt.axis('off')
    plt.tight_layout()
    plt.savefig(f"generated_images_epoch_{epoch}.png")
    plt.close()

# Save images every 100 epochs
if epoch % 100 == 0:
    save_generated_images(epoch, generator)

generator.save("generator_model.h5")
print("Generator model saved.")

def save_generated_images(epoch, generator, examples=10, dim=(1, 10), figsize=(20, 2)):
    noise = generate_random_noise(examples)
    generated_images = generator.predict(noise)
    generated_images = 0.5 * generated_images + 0.5  # Rescale to [0,1]

    file_path = f"/content/generated_images_epoch_{epoch}.png"  # Full path
    plt.figure(figsize=figsize)
    for i in range(examples):
        plt.subplot(dim[0], dim[1], i + 1)
        plt.imshow(generated_images[i].squeeze(), cmap='gray')
        plt.axis('off')
    plt.tight_layout()
    plt.savefig(file_path)  # Save with full path
    plt.close()

    print(f"Image saved at {file_path}")

import os
print(os.listdir('/content/'))

plt.savefig('/content/generated_images_epoch_100.png')

from google.colab import files
files.download('/content/generated_images_epoch_100.png')