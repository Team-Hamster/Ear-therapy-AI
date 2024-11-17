from keras.models import Sequential
from keras.models import load_model
from keras.layers import Conv2D, MaxPooling2D, Dropout, RepeatVector
# from keras.layers.normalization import BatchNormalization
from keras.layers import BatchNormalization
from keras.layers import Flatten, Dense
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
def get_my_CNN_model_architecture():

    model = Sequential()
    model.add(Conv2D(16, (3, 3), input_shape=(224, 224, 3), kernel_initializer='random_uniform', activation='relu'))

    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.3))

    model.add(Conv2D(256, (5, 5), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Conv2D(512, (5, 5), activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.5))

    model.add(Flatten())

    model.add(Dense(1024, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.7))

    model.add(Dense(110))

    return model

def compile_model(model, optimizer, loss, metrics):
    model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

def train_model(model, X_train, Y_train, epochs, batch_size):
    return model.fit(X_train, Y_train, epochs=epochs, batch_size=batch_size, verbose=1, validation_split=0.2)

def save_model(model, fileName):
    model.save(fileName + '.h5')

from keras.models import load_model

def load_current_model(fileName):
    try:
        # 파일 경로를 직접 넘겨주기 (파일을 직접 열지 않음)
        return load_model(fileName + '.h5')
    except AttributeError as e:
        print(f"Error loading model: {e}")
        return None


def test_model(model, X_test, Y_test):
    preds = model.evaluate(X_test, Y_test)
    print("Loss = " + str(preds[0]))
    print("Test Accuracy = " + str(preds[1]))

def summarize_model(model):
    model.summary()

