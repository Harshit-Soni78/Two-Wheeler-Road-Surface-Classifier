# Two-Wheeler Road Surface Classifier

Two-Wheeler Road Surface Classifier is an Android app that captures accelerometer and gyroscope data to classify road conditions for two-wheeler rides. It collects motion data and trains an LSTM model to classify surfaces such as Kankar, Bitumen, and Concrete roads, as well as speed breakers. The dataset can also help detect rash driving, enabling real-time safety alerts. 🚀🏍️

---

## Statement

Create an Android App that captures readings from motion sensors (accelerometer and gyroscope) on an Android phone. Build a dataset using this application that contains the motion characteristics of an average person driving a two-wheeler. Build an LSTM classifier that takes any 3-second sample as input and classifies it as Kankar Road, Bitumen Road, Concrete Road, Single Speed Breaker, and Multiple Speed Breakers.

**_Bonus:_** Can we use this dataset to generate alerts when a person is rash driving?

---

## Submission Deadlines

| S. No. | Experiment Title       | Submission Deadline |
| :----: | ---------------------- | :-----------------: |
|  1\.   | Mini Project           |                     |
|        | 1.1 Dataset Submission |     20.02.2025      |
|        | 1.2 Model Submission   |     17.03.2025      |
|        | 1.3 Bonus Submission   |     22.03.2025      |
|        | 1.4 Poster Submission  |     07.04.2025      |
|        | Total Marks            |                     |

| S no. | Work                                | Date        |
| ----- | ----------------------------------- | ----------- |
| a\.   | Dataset Strategy                    | 18 Jan 2025 |
| b\.   | Dataset Collection & Compilation    | 25 Jan 2025 |
| c\.   | Dataset Labelling and Preprocessing | 08 Feb 2025 |
| d\.   | Model Architecture                  | 22 Feb 2025 |
| e\.   | Model Training                      | 08 Mar 2025 |
| f\.   | Model Optimization & Comparison     | 22 Mar 2025 |
| g\.   | Bonus Evaluation                    | 19 Mar 2025 |
| h\.   | Model Chart Review                  | 05 Apr 2025 |
| i\.   | Model Chart Submission              | 12 Apr 2025 |

---

## Steps to do

### 1. Dataset Strategy

**_App Development with MIT App Inventor to Capture Sensor Data_**

We need an Android app to capture and save motion sensor readings. Use MIT App Inventor to collect data. MIT App Inventor is beginner-friendly but limited in advanced features.

**Steps:**

- Create a New Project: Go to MIT App Inventor, log in, and create a new project.
- Add Sensors: Add accelerometer and gyroscope components.
- Design the Interface: Create buttons for actions like “Start Recording” and “Stop Recording.”
- Save Data: Use the TinyDB or File component to save sensor data locally in CSV format.
- Export Data: Add functionality to send the file to your computer using email or Google Drive, or do it manually.

We can use MIT App Inventor for this part.

---

### 2. Data Collection & Compilation

**Prepare Your Environment:**

- Attach the phone securely to the two-wheeler.
- Select diverse routes (kankar, bitumen, concrete roads, etc.).

**Collect Data:**

- Start the app and record sensor readings while driving.
- Manually label the data or use a consistent annotation process during collection.

---

### 3. Dataset Labeling and Pre-processing

- Label the sensor readings with their corresponding road type or event (e.g., speed breaker).
- Pre-process the data:
  - Normalize sensor readings to bring them to the same scale.
  - Segment the data into 200 to 300-row windows.
  - Compute useful features (e.g., mean, variance, FFT of the signals).

---

### 4. Model Architecture

- Use an **LSTM (Long Short-Term Memory)** network because it excels in time-series data.
- Basic architecture:
  - Input layer: Accepts 3-second sensor data.
  - LSTM layers: Extract temporal patterns.
  - Dense layer: Classifies data into the 5 categories.

---

### 5. Model Training

- Train the LSTM on your dataset with appropriate train-validation splits.
- Use metrics like accuracy and F1-score to evaluate performance.

---

### 6. Model Optimization & Comparison

- Experiment with hyperparameters (e.g., learning rate, number of LSTM layers).
- Compare models with varying feature sets and pre-processing techniques.
- Add dropout layers to prevent overfitting.

---

### **6\. Bonus Task: Rash Driving Alert**

Since you have acceleration and gyroscope data, you can detect rash driving.

#### **Approach:**

- If sudden spikes in acceleration/rotation exceed a threshold, classify it as “Rash Driving.”

```python
# Define threshold for rash driving
def detect_rash_driving(row):
    """
    Detects rash driving based on acceleration values.
    If any of the acceleration values (X_Acc, Y_Acc, Z_Acc) exceed the threshold,
    it is considered rash driving.
    """
    if abs(row["X_Acc"]) > 2.5 or abs(row["Y_Acc"]) > 2.5 or abs(row["Z_Acc"]) > 10:
        return "Rash Driving"
    return "Normal"
```

---

### 8. Model Chart Review

This is the report for Models That have been made using these Datasets

## First Iteration

### Model Architecture

```python
model = Sequential([
    LSTM(64, return_sequences=True, input_shape=(chunk_size, 6)),  # chunk_size is 200, 250, 300
    Dropout(0.3),
    LSTM(32),
    Dense(32, activation='relu'),
    Dropout(0.3),
    Dense(4, activation='softmax')  # 4 output classes
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

history = model.fit(X_train, y_train, epochs=30, batch_size=32, validation_data=(X_test, y_test))
```

### Table of Results

|             Model Name             | Accuracy |                                                          Accuracy Curve                                                           |                                                           Confusion Matrix                                                            |
| :--------------------------------: | :------: | :-------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------: |
| **Model_Architecture(CS200-E).h5** |   77%    | ![Accuracy Curve](/05%20Model%20Architecture/Harshit's%20Architecture/result_imgs/Acc_Curve_Harshit_Preprocessed_Data-CS200E.png) | ![Confusion Matrix](/05%20Model%20Architecture/Harshit's%20Architecture/result_imgs/Conf_Matrix_Harshit_Preprocessed_Data-CS200E.png) |
| **Model_Architecture(CS200-U).h5** |   90%    | ![Accuracy Curve](/05%20Model%20Architecture/Harshit's%20Architecture/result_imgs/Acc_Curve_Harshit_Preprocessed_Data-CS200U.png) | ![Confusion Matrix](/05%20Model%20Architecture/Harshit's%20Architecture/result_imgs/Conf_Matrix_Harshit_Preprocessed_Data-CS200U.png) |
| **Model_Architecture(CS250-E).h5** |   64%    | ![Accuracy Curve](/05%20Model%20Architecture/Harshit's%20Architecture/result_imgs/Acc_Curve_Harshit_Preprocessed_Data-CS250E.png) | ![Confusion Matrix](/05%20Model%20Architecture/Harshit's%20Architecture/result_imgs/Conf_Matrix_Harshit_Preprocessed_Data-CS250E.png) |
| **Model_Architecture(CS250-U).h5** |   83%    | ![Accuracy Curve](/05%20Model%20Architecture/Harshit's%20Architecture/result_imgs/Acc_Curve_Harshit_Preprocessed_Data-CS250U.png) | ![Confusion Matrix](/05%20Model%20Architecture/Harshit's%20Architecture/result_imgs/Conf_Matrix_Harshit_Preprocessed_Data-CS250U.png) |
| **Model_Architecture(CS300-E).h5** |   88%    | ![Accuracy Curve](/05%20Model%20Architecture/Harshit's%20Architecture/result_imgs/Acc_Curve_Harshit_Preprocessed_Data-CS300E.png) | ![Confusion Matrix](/05%20Model%20Architecture/Harshit's%20Architecture/result_imgs/Conf_Matrix_Harshit_Preprocessed_Data-CS300E.png) |
| **Model_Architecture(CS300-U).h5** |   75%    | ![Accuracy Curve](/05%20Model%20Architecture/Harshit's%20Architecture/result_imgs/Acc_Curve_Harshit_Preprocessed_Data-CS300U.png) | ![Confusion Matrix](/05%20Model%20Architecture/Harshit's%20Architecture/result_imgs/Conf_Matrix_Harshit_Preprocessed_Data-CS300U.png) |

---

## Second Iteration

### Model Architecture

```python
model = Sequential([
    Bidirectional(LSTM(128, return_sequences=True), input_shape=(200, 6)),
    BatchNormalization(),
    Dropout(0.4),

    Bidirectional(LSTM(64)),
    BatchNormalization(),
    Dropout(0.4),

    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(4, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss=focal_loss(gamma=2., alpha=0.25),
    metrics=['accuracy']
)

model.summary()

# --------------------- Train Model ---------------------

history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=50,
    batch_size=32,
    class_weight=class_weights,
    callbacks=[tf.keras.callbacks.EarlyStopping(patience=6, restore_best_weights=True)]
)
```

### Table of Results

|              Model Name              | Accuracy |                                                            Accuracy Curve                                                            |                                                             Confusion Matrix                                                             |
| :----------------------------------: | :------: | :----------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------: |
| **Model_Architecture(CS200-U)CB.h5** |    81    | ![Accuracy Curve](/05%20Model%20Architecture/Harshit's%20Architecture/result_imgs/Acc_Curve_Harshit_Preprocessed_Data-CS200U-CB.png) | ![Confusion Matrix](/05%20Model%20Architecture/Harshit's%20Architecture/result_imgs/Conf_Matrix_Harshit_Preprocessed_Data-CS200U-CB.png) |
| **Model_Architecture(CS250-U)CB.h5** |    85    | ![Accuracy Curve](/05%20Model%20Architecture/Harshit's%20Architecture/result_imgs/Acc_Curve_Harshit_Preprocessed_Data-CS250U-CB.png) | ![Confusion Matrix](/05%20Model%20Architecture/Harshit's%20Architecture/result_imgs/Conf_Matrix_Harshit_Preprocessed_Data-CS250U-CB.png) |
| **Model_Architecture(CS300-U)CB.h5** |    81    | ![Accuracy Curve](/05%20Model%20Architecture/Harshit's%20Architecture/result_imgs/Acc_Curve_Harshit_Preprocessed_Data-CS300U-CB.png) | ![Confusion Matrix](/05%20Model%20Architecture/Harshit's%20Architecture/result_imgs/Conf_Matrix_Harshit_Preprocessed_Data-CS300U-CB.png) |

---
