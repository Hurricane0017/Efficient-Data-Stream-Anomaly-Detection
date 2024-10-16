from src.anamoly_detection import TimeSeriesAnomalyDetectorARIMA
from src.data_stream import load_data
from src.metrics import calculate_metrics
from src.visualization import plot_results

# Load data
df = load_data('Data/time-series.csv')

# Initialize and run anomaly detection
detector = TimeSeriesAnomalyDetectorARIMA()
anomaly_df = detector.detect_anomalies(df)

# Save results
anomaly_df.to_csv('Output/result.csv', index=True)

# Calculate metrics (assuming you have ground truth labels in the 'label' column)
if 'label' in anomaly_df.columns:
    precision, recall = calculate_metrics(anomaly_df)
    print(f'Precision: {precision:.2f}, Recall: {recall:.2f}')

# Plot the results
plot_results(anomaly_df)