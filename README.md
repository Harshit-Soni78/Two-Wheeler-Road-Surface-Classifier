# Two-Wheeler Road Surface Classifier

Two-Wheeler Road Surface Classifier is an Android app that captures accelerometer and gyroscope data to classify road conditions for two-wheeler rides. It collects motion data and trains an LSTM model to classify surfaces like Kankar, Bitumen, and Concrete roads, plus speed breakers. The dataset can also help detect rash driving, enabling real-time safety alerts. 🚀🏍️

---

## Statement

Create an Android App that captures the readings from motion sensors (accelerometer and gyroscope) in an android phone. Build a dataset using this application that contains the motion characteristics of an average person driving a two-wheeler. Build a LSTM classifier that takes any 3 second sample as input and classifies it as Kankar Road, Bitumen Road, Concrete Road, Single Speed Breaker and Multiple Speed Breakers.

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

###### _(Click to Expand)_

<details>
  <summary  style="font-size: 15px; font-weight: bold; display: flex; justify-content: center;"> 1. Dataset Strategy</summary>

**_App Development with MIT App Inventor to Capture Sensor Data_**

We need an Android app to capture and save motion sensor readings. Use MIT App Inventor to collect data. MIT App Inventor is beginner-friendly but limited in advanced features.

**Steps:**

- Create a New Project: Go to MIT App Inventor, log in, and create a new project.
- Add Sensors: Add accelerometer and gyroscope components.
- Design the Interface: Create buttons for actions like “Start Recording” and “Stop Recording.”
- Save Data: Use the TinyDB or File component to save sensor data locally in CSV format.
- Export Data: Add functionality to send the file to your computer using email or Google Drive or do it manually.

We can use MIT App Inventor for this part.

</details>

---

---

<details>
  <summary  style="font-size: 15px; font-weight: bold; display: flex; justify-content: center;">2. Data Collection & Compilation</summary>

**Prepare Your Environment:**

- Attach the phone securely to the two-wheeler.
- Select diverse routes (kankar, bitumen, concrete roads, etc.).

**Collect Data:**

- Start the app and record sensor readings while driving.
- Manually label the data or use a consistent annotation process during collection.

</details>

---

---

<details>
  <summary  style="font-size: 15px; font-weight: bold; display: flex; justify-content: center;">3. Dataset Labelling and Pre-processing</summary>

- Label the sensor readings with their corresponding road type or event (e.g., speed breaker).
- Pre-process the data:
  - Normalize sensor readings to bring them to the same scale.
  - Segment the data into 200 to 300 rows windows.
  - Compute useful features (e.g., mean, variance, FFT of the signals).

</details>

---

---

<details>
  <summary  style="font-size: 15px; font-weight: bold; display: flex; justify-content: center;">4. Model Architecture</summary>

- Use an **LSTM (Long Short-Term Memory)** network because it excels in time-series data.
- Basic architecture:
  - Input layer: Accepts 3-second sensor data.
  - LSTM layers: Extract temporal patterns.
  - Dense layer: Classifies data into the 5 categories.

</details>

---

---

<details>
  <summary  style="font-size: 15px; font-weight: bold; display: flex; justify-content: center;">5. Model Training</summary>

- Train the LSTM on your dataset with appropriate train-validation splits.
- Use metrics like accuracy and F1-score to evaluate performance.

</details>

---

---

<details>
  <summary  style="font-size: 15px; font-weight: bold; display: flex; justify-content: center;">6. Model Optimization & Comparison</summary>

- Experiment with hyperparameters (e.g., learning rate, number of LSTM layers).
- Compare models with varying feature sets and pre-processing techniques.
- Add dropout layers to prevent overfitting.

</details>

---

---

<details>
  <summary  style="font-size: 15px; font-weight: bold; display: flex; justify-content: center;">7. Bonus Evaluation</summary>
Comming Soon
</details>

---

---

<details>
  <summary  style="font-size: 15px; font-weight: bold; display: flex; justify-content: center;">8. Model Chart Review</summary>
Comming Soon
</details>

---

---

<details>
  <summary  style="font-size: 15px; font-weight: bold; display: flex; justify-content: center;">9. Model Chart Submission</summary>
Comming Soon
</details>

---

---
