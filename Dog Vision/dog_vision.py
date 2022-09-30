# -*- coding: utf-8 -*-
"""dog-vision.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15PZh9fgXvMCHLLtF637aH0wgsz3Xqkei

# 🐶 End-to-end Multil-class Dog Breed Classification

This notebook builds an end-to-end multi-class image classifier using TensorFlow 2.x and TensorFlow Hub.

## 1. Problem

Identifying the breed of a dog given an image of a dog.

When I'm sitting at the cafe and I take a photo of a dog, I want to know what breed of dog it is.

## 2. Data

The data we're using is from Kaggle's dog breed identification competition.

https://www.kaggle.com/c/dog-breed-identification/data 

## 3. Evaluation

The evaluation is a file with prediction probabilities for each dog breed of each test image.

https://www.kaggle.com/c/dog-breed-identification/overview/evaluation

## 4. Features

Some information about the data:
* We're dealing with images (unstructured data) so it's probably best we use deep learning/transfer learning.
* There are 120 breeds of dogs (this means there are 120 different classes).
* There are around 10,000+ images in the training set (these images have labels).
* There are around 10,000+ images in the test set (these images have no labels, because we'll want to predict them).
"""

# Unzip the uploaded data into Google Drive
# !unzip "/content/drive/MyDrive/Colab Notebooks/Dog Vision/dog-breed-identification.zip" -d "/content/drive/MyDrive/Colab Notebooks/Dog Vision/"

"""### Get our workspace ready

* Import TensorFlow 2.x ✅
* Import TensorFlow Hub ✅
* Make sure we're using a GPU ✅
"""

# # Import TensorFlow into Colab
# import tensorflow as tf
# print("TF version:", tf.__version__)

# # Run this cell if TensorFlow 2.x isn't the default in Colab
# try:
#   # %tensorflow_version only exists in Colab
#   %tensorflow_version 2.x
# except Exception:
#   pass

import tensorflow as tf
import tensorflow_hub as hub
print(f"TF Version: {tf.__version__}")
print(f"TF Version: {hub.__version__}")

# Check for GPU availability
if tf.config.list_physical_devices("GPU"):
  print("GPU Available")
else:
   print("Not Available")

"""## Getting our data ready (turning into Tensors)

With all machine learning models, our data has to be in numerical format. So that's what we'll be doing first. Turning our images into Tensors (numerical representations).

Let's start by accessing our data and checking out the labels.
"""

import pandas as pd
labels_csv = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Dog Vision/labels.csv")
print(labels_csv.describe())
print(labels_csv.head())

labels_csv.head()

# labels_csv["breed"].value_counts()

labels_csv["breed"].value_counts().plot.bar(figsize=(20, 10));

labels_csv["breed"].value_counts().median()

from IPython.display import Image
Image("/content/drive/MyDrive/Colab Notebooks/Dog Vision/train/001513dfcb2ffafc82cccf4d8bbaba97.jpg")

"""
### Getting images and their labels 

Let's get a list of all of our image file pathnames."""

labels_csv.head()

filename = ["/content/drive/MyDrive/Colab Notebooks/Dog Vision/train/" + fname + ".jpg" for fname in labels_csv["id"]]
filename[:10]

import os
os.listdir("/content/drive/MyDrive/Colab Notebooks/Dog Vision/train/")[:10]

import os
if len(os.listdir("/content/drive/MyDrive/Colab Notebooks/Dog Vision/train/")) == len(filename):
  print("Equal length")
else:
  print("Not Equal")

Image(filename[9000])

# labels_csv["id"][9000]
# Image("/content/drive/MyDrive/Colab Notebooks/Dog Vision/train/e20e32bf114141e20a1af854ca4d0ecc.jpg")
labels_csv["breed"][9000]

import numpy as np
labels = labels_csv["breed"]
labels = np.array(labels)
labels

len(labels)

labels_csv.isna().sum()

if len(labels) ==  len(filename):
  print("Matched")
else:
  print("Not Matched")

unique_breed = np.unique(labels)
unique_breed

len(unique_breed)

print(labels[0])
labels[0] == unique_breed

boolean_labels = [label == unique_breed for label in labels]
boolean_labels[:2]

len(boolean_labels)

# example: Turning boolean array into integers
print(labels[0])
print(np.where(labels[0] == unique_breed))
print(boolean_labels[0].argmax())
print(boolean_labels[0].astype(int))

print(labels[2])
print(boolean_labels[2].astype(int))

"""### Creating our own validation set
Since the dataset from Kaggle doesn't come with a validation set, we're going to create our own.
"""

x = filename
y = boolean_labels

len(x), len(y)

"""We're going to start off experimenting with ~1000 images and increase as needed."""

# Set number of images to use for experimenting
NUM_IMAGES = 1000 #@param {type: "slider", min: 1000, max:10000, step:1000}

from sklearn.model_selection import train_test_split
x_train, x_val, y_train, y_val = train_test_split(x[:NUM_IMAGES], y[:NUM_IMAGES], test_size=0.2, random_state=42)

len(x_train), len(y_train), len(x_val), len(y_val)

x_train[:2], y_train[:2]

"""## Preprocessing Images (turning images into Tensors)

To preprocess our images into Tensors we're going to write a function which does a few things:
1. Take an image filepath as input
2. Use TensorFlow to read the file and save it to a variable, `image`
3. Turn our `image` (a jpg) into Tensors
4. Normalize our image (convert color channel values from from 0-255 to 0-1).
5. Resize the `image` to be a shape of (224, 224)
6. Return the modified `image`

Before we do, let's see what importing an image looks like.
"""

from matplotlib.pyplot import imread
image = imread(filename[42])
image.shape

image[:2]

image.max(), image.min()

tf.constant(image)[:2]

tensor = tf.io.read_file(filename[26])
tensor

tensor_rgb = tf.image.decode_jpeg(tensor, channels=3)
tensor_rgb

tensor_01 = tf.image.convert_image_dtype(tensor_rgb, tf.float32)
tensor_01

tensor_01.shape

IMG_SIZE = 224

# Create a function for preprocessing images.
def process_images(image_path):

  # read image
  image = tf.io.read_file(image_path)

  # turn image into numerical Tensor with 3 colours channels (Red, Green, Blue)
  image = tf.image.decode_jpeg(image, channels=3)

  # convert the colour channel values from 0-255 to 0-1 values
  image = tf.image.convert_image_dtype(image, tf.float32)

  # resize image
  image = tf.image.resize(image, size=[IMG_SIZE, IMG_SIZE])

  return image

"""## Turning our data into batches

Why turn our data into batches?

Let's say you're trying to process 10,000+ images in one go... they all might not fit into memory.

So that's why we do about 32 (this is the batch size) images at a time (you can manually adjust the batch size if need be).

In order to use TensorFlow effectively, we need our data in the form of Tensor tuples which look like this: 
`(image, label)`.
"""

# create a simple function to return a tuple (image, label)
def get_image_label(image_path, label):
  image = process_images(image_path)
  return image, label

(process_images(x[42]),tf.constant(y[42]))

"""Now we've got a way to turn our data into tuples of Tensors in the form: `(image, label)`, let's make a function to turn all of our data (`X` & `y`) into batches!"""

# Define the batch size, 32 is a good start
BATCH_SIZE = 32

# Create a function to turn data into batches
def create_data_batches(x, y=None, batch_size=BATCH_SIZE, valid_data=False, test_data=False):
  """
  Creates batches of data out of image (X) and label (y) pairs.
  Shuffles the data if it's training data but doesn't shuffle if it's validation data.
  Also accepts test data as input (no labels).
  """

  # if data is test data set we dont have labels
  if test_data:
    print("Creating test data batches")
    data = tf.data.Dataset.from_tensor_slices(tf.constant(x))
    data_batch = data.map(process_images).batch(BATCH_SIZE)
    return data_batch
  
  # if data is valid data set we dont have need to shuffle it.
  elif valid_data:
    print("Creating valid data batches")
    data = tf.data.Dataset.from_tensor_slices((tf.constant(x), tf.constant(y)))
    data_batch = data.map(get_image_label).batch(BATCH_SIZE)
    return data_batch

  # Need shuffles
  else: 
    print("Creating training data batches.....")
    data = tf.data.Dataset.from_tensor_slices((tf.constant(x), tf.constant(y)))
    # data shuffle
    data = data.shuffle(buffer_size=len(x))
    data_batch = data.map(get_image_label).batch(BATCH_SIZE)
    return data_batch

train_data = create_data_batches(x_train, y_train)
val_data = create_data_batches(x_val, y_val, valid_data=True)

train_data.element_spec, val_data.element_spec

"""## Visualizing Data Batches

Our data is now in batches, however, these can be a little hard to understand/comprehend, let's visualize them!

## Building a model

Before we build a model, there are a few things we need to define:
* The input shape (our images shape, in the form of Tensors) to our model.
* The output shape (image labels, in the form of Tensors) of our model.
* The URL of the model we want to use from TensorFlow Hub - https://tfhub.dev/google/imagenet/mobilenet_v2_130_224/classification/4
"""

import matplotlib.pyplot as plt

def show_32_images(images, labels):

  plt.figure(figsize=(13, 13))

  # loop through 25
  for i in range(32):
    ax = plt.subplot(6, 6, i+1)
    plt.imshow(images[i])
    plt.title(unique_breed[labels[i].argmax()])
    plt.axis("off")

train_data

train_images, train_labels = next(train_data.as_numpy_iterator())
train_images, train_labels

len(train_images), len(train_labels)

train_images, train_labels = next(train_data.as_numpy_iterator())
show_32_images(train_images, train_labels)

val_images, val_labels = next(val_data.as_numpy_iterator())
show_32_images(val_images, val_labels)

"""## Building a model

Before we build a model, there are a few things we need to define:
* The input shape (our images shape, in the form of Tensors) to our model.
* The output shape (image labels, in the form of Tensors) of our model.
* The URL of the model we want to use from TensorFlow Hub - https://tfhub.dev/google/imagenet/mobilenet_v2_130_224/classification/4
"""

IMG_SIZE

len(unique_breed)

# batch, height, width, colour channels
INPUT_SHAPE = [None, IMG_SIZE, IMG_SIZE, 3]

# Setup output shape of our model
OUTPUT_SHAPE = len(unique_breed)

MODEL_URL = "https://tfhub.dev/google/imagenet/mobilenet_v2_130_224/classification/5"

"""Now we've got our inputs, outputs and model ready to go. Let's put them together into a Keras deep learning model!

Knowing this, let's create a function which:
* Takes the input shape, output shape and the model we've chosen as parameters.
* Defines the layers in a Keras model in sequential fashion (do this first, then this, then that).
* Compiles the model (says it should be evaluated and improved).
* Builds the model (tells the model the input shape it'll be getting).
* Returns the model.

All of these steps can be found here: https://www.tensorflow.org/guide/keras/overview
"""

# create a function for keras model

def create_model(input_shape=INPUT_SHAPE, output_shape=OUTPUT_SHAPE, model_url=MODEL_URL):
  print(f"Building Model {model_url}")

  # set up model layers
  model = tf.keras.Sequential([
      hub.KerasLayer(MODEL_URL),    # layer 1 input
      tf.keras.layers.Dense(units=output_shape, activation="softmax")  # layer 2 output
      ])
  
  # compile the model
  model.compile(
      loss=tf.keras.losses.CategoricalCrossentropy(),
      optimizer=tf.keras.optimizers.Adam(),
      metrics=["accuracy"]
  )

  # build the model
  model.build(INPUT_SHAPE)
  return model

model = create_model()
model.summary()

"""## Creating callbacks

Callbacks are helper functions a model can use during training to do such things as save its progress, check its progress or stop training early if a model stops improving.

We'll create two callbacks, one for TensorBoard which helps track our models progress and another for early stopping which prevents our model from training for too long.

### TensorBoard Callback

To setup a TensorBoard callback, we need to do 3 things:
1. Load the TensorBoard notebook extension ✅
2. Create a TensorBoard callback which is able to save logs to a directory and pass it to our model's `fit()` function. ✅
3. Visualize our models training logs with the `%tensorboard` magic function (we'll do this after model training).

https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TensorBoard
"""

# Commented out IPython magic to ensure Python compatibility.
# Load TensorBoard notebook extension
# %load_ext tensorboard

import datetime

# Create a function to build a TensorBoard callback
def create_tensorboard_callback():
  # Create a log directory for storing TensorBoard logs
  logdir = os.path.join("/content/drive/MyDrive/Colab Notebooks/Dog Vision/logs", # Make it so the logs get tracked whenever we run an experiment
                        datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
  return tf.keras.callbacks.TensorBoard(logdir)

"""### Early Stopping Callback

Early stopping helps stop our model from overfitting by stopping training if a certain evaluation metric stops improving.

https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/EarlyStopping
"""

# Create early stopping callback
early_stopping = tf.keras.callbacks.EarlyStopping(monitor="val_accuracy", patience=3)

"""## Training a model (on subset of data)

Our first model is only going to train on 1000 images, to make sure everything is working.
"""

NUM_EPOCHS = 100 #@param {type: "slider", min:10, max:100, step:10}

if tf.config.list_physical_devices("GPU"):
  print("Yes")
else: 
  print("No")

"""Let's create a function which trains a model.

* Create a model using `create_model()`
* Setup a TensorBoard callback using `create_tensorboard_callback()`
* Call the `fit()` function on our model passing it the training data, validation data, number of epochs to train for (`NUM_EPOCHS`) and the callbacks we'd like to use
* Return the model
"""

# Build a function to train and return a trained model

def train_model():
  model = create_model()

  tensorboard = create_tensorboard_callback()

  model.fit(x=train_data, 
            epochs=NUM_EPOCHS, 
            validation_data=val_data, 
            validation_freq=1, 
            callbacks=[tensorboard, early_stopping])
  
  return model

# takes time to run 1000 images
# model = train_model()

"""**Question:** It looks like our model is overfitting because it's performing far better on the training dataset than the validation dataset, what are some ways to prevent model overfitting in deep learning neural networks?

**Note:** Overfitting to begin with is a good thing! It means our model is learning!!!

### Checking the TensorBoard logs

The TensorBoard magic function (`%tensorboard`) will access the logs directory we created earlier and visualize its contents.
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorboard --logdir /content/drive/MyDrive/Colab\ Notebooks/Dog\ Vision/logs

"""## Making and evaluating predictions using a trained model """

val_data

predictions = model.predict(val_data, verbose=1)
predictions

predictions.shape

len(y_val), len(unique_breed)

len(predictions[0])

np.sum(predictions[0])

np.sum(predictions[1])

# first prediction
index = 42
print(predictions[index])
print(f"max value (probability of prediction): {np.max(predictions[index])}")
print(f"sum: {np.sum(predictions[index])}")
print(f"Max index: {np.argmax(predictions[index])}")
print(f"predicted label: {unique_breed[np.argmax(predictions[index])]}")

"""Having the the above functionality is great but we want to be able to do it at scale.

And it would be even better if we could see the image the prediction is being made on!

**Note:** Prediction probabilities are also known as confidence levels.
"""

# Turn prediction probabilities into their respective label (easier to understand)
def get_pred_label(prediction_probability):
  """
  Turns an array of prediction probabilities into a label.
  """
  return unique_breed[np.argmax(prediction_probability)]
pred_label = get_pred_label(predictions[0])
pred_label

"""Now since our validation data is still in a batch dataset, we'll have to unbatchify it to make predictions on the validation images and then compare those predictions to the validation labels (truth labels)."""

val_data

# Create a function to unbatch a batch dataset
def unbatchify(data):
  images = []
  labels = []
  # Loop through unbatched data
  for image, label in data.unbatch().as_numpy_iterator():
    images.append(image)
    labels.append(unique_breed[np.argmax(label)])
  return images, labels

val_images, val_labels = unbatchify(val_data)
val_images[0], val_labels[0]

get_pred_label(val_labels[40])

get_pred_label(predictions[40])

"""Now we've got ways to get get:
* Prediction labels
* Validation labels (truth labels)
* Validation images

Let's make some function to make these all a bit more visaulize.

We'll create a function which:
* Takes an array of prediction probabilities, an array of truth labels and an array of images and an integer. ✅
* Convert the prediction probabilities to a predicted label. ✅
* Plot the predicted label, its predicted probability, the truth label and the target image on a single plot. ✅
"""

def plot_pred(prediction_probabilities, labels, images, n=1):
  """
  View the prediction, ground truth and image for sample n
  """
  pred_prob, true_label, image = prediction_probabilities[n], labels[n], images[n]

  pred_label = get_pred_label(pred_prob)

  plt.imshow(image)
  plt.xticks([])
  plt.yticks([])
  if pred_label == true_label:
    color = "green"
  else:
    color = "red"
  plt.title(f"PRED: {pred_label} {np.max(pred_prob) * 100:.2f}% {true_label}", color=color)

plot_pred(prediction_probabilities=predictions, labels=val_labels, images=val_images, n=77)

"""Now we've got one function to visualize our models top prediction, let's make another to view our models top 10 predictions.

This function will:
* Take an input of prediction probabilities array and a ground truth array and an integer ✅
* Find the prediction using `get_pred_label()` ✅
* Find the top 10:
  * Prediction probabilities indexes ✅
  * Prediction probabilities values ✅
  * Prediction labels ✅
* Plot the top 10 prediction probability values and labels, coloring the true label green ✅
"""

predictions[0]

predictions[0].argsort()[-10:]

predictions[0].argsort()[-10:][::-1]

predictions[0][predictions[0].argsort()[-10:][::-1]]

predictions[0].max()

def plot_pred_conf(prediction_probabilities, labels, n=1):
  """
  Plus the top 10 highest prediction confidences along with the truth label for sample n.
  """
  pred_prob, true_label = prediction_probabilities[n], labels[n]
  pred_label = get_pred_label(pred_prob)

  top_10_pred_indexes = pred_prob.argsort()[-10:][::-1]
  top_10_pred_values = pred_prob[top_10_pred_indexes]
  top_10_pred_label = unique_breed[top_10_pred_indexes]

  top_plot = plt.bar(np.arange(len(top_10_pred_label)), top_10_pred_values, color="grey")
  plt.xticks(np.arange(len(top_10_pred_label)), labels=top_10_pred_label, rotation="vertical")

  if np.isin(true_label, top_10_pred_label):
    top_plot[np.argmax(top_10_pred_label == true_label)].set_color("green")
  else:
    pass

plot_pred_conf(prediction_probabilities=predictions, labels=val_labels, n=9)

"""Now we've got some function to help us visualize our predictions and evaluate our modle, let's check out a few."""

# Let's check out a few predictions and their different values
i_multiplier = 0
num_rows = 3
num_cols = 2
num_images = num_rows * num_cols
plt.figure(figsize=(10*num_cols, 5*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_pred(prediction_probabilities=predictions, labels=val_labels, images=val_images, n=i+i_multiplier)

  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_pred_conf(prediction_probabilities=predictions, labels=val_labels, n=i+i_multiplier)
plt.tight_layout(h_pad=1.0)
plt.show()

"""**Challenge:** How would you create a confusion matrix with our models predictions and true labels?

## Saving and reloading a trained model
"""

def save_model(model, suffix=None):
  """
  Saves a given model in a models directory and appends a suffix (string).
  """
  model_dir = os.path.join("/content/drive/MyDrive/Colab Notebooks/Dog Vision/models", datetime.datetime.now().strftime("%Y%m%d-%H%M%s"))
  model_path = model_dir + "-" + suffix + ".h5"  # save format of model
  print(f"Saving model to: {model_path}")
  model.save(model_path)
  return model_path

def load_model(model_path):
  """
  load saved model
  """
  print(f"loading {model_path}")
  model = tf.keras.models.load_model(model_path, custom_objects={"KerasLayer":hub.KerasLayer})
  return model

"""Now we've got functions to save and load a trained model, let's make sure they work!"""

# Save our model trained on 1000 images
save_model(model, suffix="1000-images-mobilenetv2-Adam")

loaded_1000_image_model = load_model("/content/drive/MyDrive/Colab Notebooks/Dog Vision/models/20220930-06281664519322-1000-images-mobilenetv2-Adam.h5")

# Evaluate the pre-saved model
model.evaluate(val_data)

loaded_1000_image_model.evaluate(val_data)

"""## Training a big dog model 🐶 (on the full data)"""

len(x), len(y)

len(x_train), len(y_train), len(x_val), len(y_val)

# use NUM_EPOCHS = 100 for best result here using 5 to train fast
NUM_EPOCHS = 5 
full_data = create_data_batches(x, y)

full_data

full_model = create_model()

# Create full model callbacks
full_model_tensorboard = create_tensorboard_callback()

# No validation set when training on all the data, so we can't monitor validation accuracy.
full_model_early_stopping = tf.keras.callbacks.EarlyStopping(monitor="accuracy", patience=3)

"""**Note:** Running the cell below will take a little while (maybe up to 30 minutes for the first epoch) because the GPU we're using in the runtime has to load all of the images into memory."""

# # Fit the full model to the full data
# full_model.fit(x=full_data, 
#                epochs=NUM_EPOCHS, 
#                callbacks=[full_model_tensorboard, full_model_early_stopping])

save_model(full_model, suffix="full-image-set-mobilenetv2-Adam")

loaded_full_model = load_model("/content/drive/MyDrive/Colab Notebooks/Dog Vision/models/20220930-10191664533158-full-image-set-mobilenetv2-Adam.h5")

"""## Making predictions on the test dataset

Since our model has been trained on images in the form of Tensor batches, to make predictions on the test data, we'll have to get it into the same format.

Luckily we created `create_data_batches()` earlier which can take a list of filenames as input and convert them into Tensor batches.

To make predictions on the test data, we'll:
* Get the test image filenames. ✅
* Convert the filenames into test data batches using `create_data_batches()` and setting the `test_data` parameter to `True` (since the test data doesn't have labels). ✅
* Make a predictions array by passing the test batches to the `predict()` method called on our model. 
"""

test_path = "/content/drive/MyDrive/Colab Notebooks/Dog Vision/test/"
test_filenames = [test_path + fname for fname in os.listdir(test_path)]
test_filenames[:10]

len(test_filenames)

test_data = create_data_batches(test_filenames, test_data=True)

test_data

"""**Note:** Calling `predict()` on our full model and passing it the test data batch will take a long time to run (about a ~1hr). This is because we have to process ~10,000+ images and get our model to find patterns in those images and generate predictions based on what its learned in the training dataset."""

# test_predictions = loaded_full_model.predict(test_data, verbose=1)
#  39/324 [==>...........................] - ETA: 19:37

# Save predictions (NumPy array) to csv file (for access later)
# np.savetxt("/content/drive/MyDrive/Colab Notebooks/Dog Vision/preds_array.csv", delimiter=",")

test_predictions = np.loadtxt("/content/drive/MyDrive/Colab Notebooks/Dog Vision/preds_array.csv", delimiter=",")

test_predictions[:10]

test_predictions.shape

"""## Preparing test dataset predictions for Kaggle

Looking at the Kaggle sample submission, we find that it wants our models prediction probaiblity outputs in a DataFrame with an ID and a column for each different dog breed.
https://www.kaggle.com/c/dog-breed-identification/overview/evaluation

To get the data in this format, we'll:
* Create a pandas DataFrame with an ID column as well as a column for each dog breed. ✅
* Add data to the ID column by extracting the test image ID's from their filepaths.
* Add data (the prediction probabilites) to each of the dog breed columns.
* Export the DataFrame as a CSV to submit it to Kaggle.
"""

["id"] + list(unique_breed)

preds_df = pd.DataFrame(columns=["id"] + list(unique_breed))
preds_df.head()

test_path

os.path.splitext(filename[0])

test_id = [os.path.splitext(path)[0] for path in os.listdir(test_path)]
test_id

preds_df["id"] = test_id

preds_df.head()

# Add the prediction probabilities to each dog breed column
preds_df[list(unique_breed)] = test_predictions
preds_df.head()

preds_df.to_csv("/content/drive/MyDrive/Colab Notebooks/Dog Vision/Full Model Prediction Kaggle Mobilenetv2.csv", index=False)

"""## Making predictions on custom images

To make predictions on custom images, we'll:
* Get the filepaths of our own images.
* Turn the filepaths into data batches using `create_data_batches()`. And since our custom images won't have labels, we set the `test_data` parameter to `True`.
* Pass the custom image data batch to our model's `predict()` method.
* Convert the prediction output probabilities to predictions labels.
* Compare the predicted labels to the custom images.
"""

custom_path = "/content/drive/MyDrive/Colab Notebooks/Dog Vision/my_dog_photos/"
custom_image_paths = [custom_path + fname for fname in os.listdir(custom_path)]

custom_image_paths

# Turn custom images into batch datasets 
custom_data = create_data_batches(custom_image_paths, test_data=True)
custom_data

custom_preds = loaded_full_model.predict(custom_data)
custom_preds

custom_preds.shape, len(custom_preds)

# Get custom image prediction labels
custom_pred_labels = [get_pred_label(custom_preds[i]) for i in range(len(custom_preds))]
custom_pred_labels

# Get custom images (our unbatchify() function won't work since there aren't labels)
custom_images = []
for image in custom_data.unbatch().as_numpy_iterator():
  custom_images.append(image)

# Check custom image predictions
plt.figure(figsize=(10, 10))
for i, image in enumerate(custom_images):
  plt.subplot(1, 3, i+1)
  plt.xticks([])
  plt.yticks([])
  plt.title(f"{custom_pred_labels[i]}")
  plt.imshow(image)