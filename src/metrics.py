def calculate_metrics(df):
    # Assuming 'label' column is the ground truth and 'anomaly' is the predicted column
    true_positive = len(df[(df['label'] == 1) & (df['anomaly'] == 1)])
    false_positive = len(df[(df['label'] == 0) & (df['anomaly'] == 1)])
    false_negative = len(df[(df['label'] == 1) & (df['anomaly'] == 0)])
    
    precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0
    recall = true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 0
    
    return precision, recall