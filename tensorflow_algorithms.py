```python
import tensorflow as tf

def train_model(data, labels):
    # Define the model architecture
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    # Compile the model
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    # Train the model
    model.fit(data, labels, epochs=10)

    return model

def predict(model, data):
    # Make predictions using the trained model
    predictions = model.predict(data)

    return predictions
```
