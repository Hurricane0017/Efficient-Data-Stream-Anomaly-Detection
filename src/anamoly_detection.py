# src/anomaly_detection.py
from sklearn.preprocessing import StandardScaler

class TimeSeriesAnomalyDetectorARIMA:
    def __init__(self, upper_threshold=1.5, lower_threshold=-1):
        self.scaler = StandardScaler()
        self.upper_threshold = upper_threshold  # Z-score upper threshold
        self.lower_threshold = lower_threshold  # Z-score lower threshold

    def detect_anomalies(self, df):
        # Standardize the data
        df['value_scaled'] = self.scaler.fit_transform(df[['value']])
        
        # Calculate Z-scores
        df['z_score'] = df['value_scaled']
        
        # Flag anomalies based on upper and lower thresholds
        df['anomaly'] = ((df['z_score'] > self.upper_threshold) | (df['z_score'] < self.lower_threshold)).astype(int)
        
        return df[['value', 'z_score', 'anomaly']]