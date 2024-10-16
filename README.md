# Efficient Data Stream Anomaly Detection

## Overview

This project implements a streaming time series anomaly detection system designed to identify anomalies in continuous data streams, with a specific focus on detecting unusual patterns in floating-point numbers. This system is particularly relevant in contexts such as financial transactions, network traffic monitoring, and various metrics from cloud servers.

The project leverages ARIMA (AutoRegressive Integrated Moving Average) for anomaly detection, a statistical model that captures temporal dependencies and trends in the data. This choice is motivated by ARIMA’s effectiveness in dealing with time series data and its ability to provide accurate predictions based on historical data.

Why Choose ARIMA?

	1.	Suitability for Time Series Data: ARIMA is designed explicitly for univariate time series forecasting, making it suitable for our use case.
	2.	Modeling Trends and Seasonality: ARIMA can handle trends and seasonality in data, allowing for accurate modeling of temporal dependencies.
	3.	Simplicity and Interpretability: Compared to more complex models like LSTM, ARIMA is relatively simpler to implement and interpret, which is beneficial for understanding anomaly detection results.
	4.	Reconstruction Error: By calculating the residuals (differences between actual values and predictions), ARIMA provides a clear method for identifying anomalies based on statistical thresholds.

## Algorithm Details

The ARIMA model is implemented with the following components:

	•	AutoRegressive (AR) Part: Uses past values to predict future values.
	•	Integrated (I) Part: Differencing the data to make it stationary.
	•	Moving Average (MA) Part: Uses past forecast errors to predict future values.

Anomaly Detection Process

	1.	Model Fitting: The ARIMA model is fitted to historical data to learn its underlying patterns.
	2.	Prediction: Using the fitted model, predictions for future values are made.
	3.	Residual Calculation: The residuals are computed as the absolute difference between actual and predicted values.
	4.	Anomaly Flagging: Anomalies are flagged based on thresholds:
	•	Upper Threshold: Set at 1.5, identifying values that significantly exceed normal behavior.
	•	Lower Threshold: Set at -1, identifying values that are significantly below normal behavior.

Technical Details

	•	Input: Univariate time series data in CSV format.
	•	Preprocessing: The data is normalized using StandardScaler for improved model performance.
	•	Anomaly Detection: Anomalies are detected based on calculated residuals, with specified upper and lower thresholds.

## Project Setup

1. Clone the repository:
   ```
   git clone https://github.com/Hurricane0017/Efficient-Data-Stream-Anomaly-Detection.git
   cd Efficient-Data-Stream-Anomaly-Detection
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Prepare your data:
   - Place your time series CSV files in the `time-series/` directory

5. Train the model:
   ```
   python train.py
   ```

6. Run anomaly detection:
   ```
   python main.py
   ```

## Data Stream Simulation

To effectively simulate a real-time data stream, the project incorporates functions that generate synthetic time series data with periodic anomalies. The data includes:

	•	Regular Patterns: Representing normal operational metrics.
	•	Seasonal Elements: To mimic realistic behavior over time.
	•	Random Noise: To introduce variability and complexity into the data.
	•	Anomalies: Deliberately injected into the stream every 20 intervals with large random magnitudes to ensure they stand out against the regular data.


## Visualization
To add visualization of the anomaly detection results, you can modify the `main.py` file to include plotting. Here's an example of how to do this:

Add the following import at the top of `main.py`:
```python
import matplotlib.pyplot as plt
```

Add this function to `main.py`:
```python
def visualize_results(df, filename):
    plt.figure(figsize=(15, 7))
    plt.plot(df['value'], label='Original')
    plt.scatter(df[df['label2'] == 1].index, df[df['label2'] == 1]['value'], color='red', label='Anomaly')
    plt.title(f'Anomaly Detection Results - {filename}')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.savefig(f'./output/{filename}_visualization.png')
    plt.close()
```

In the main loop of `main.py`, after processing each file, add:
```python
visualize_results(result, filename)
```

This will create a visualization for each processed file, showing the original time series and highlighting detected anomalies in red.

## Further Improvements

	•	Experimentation: Test various configurations of the ARIMA model to improve accuracy.
	•	Real-Time Processing: Enhance the system to handle real-time data streams more efficiently.
	•	Multi-Variate Analysis: Extend the detection capability to analyze multiple time series simultaneously.
	•	Active Learning: Implement mechanisms to learn from detected anomalies and adapt the model over time.

## Submission

This project serves as part of the application process for the Graduate Software Engineer role at Cobblestone Energy. If you have any questions or need further clarification, feel free to reach out.

