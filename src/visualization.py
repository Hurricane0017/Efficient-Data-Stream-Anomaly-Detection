import matplotlib.pyplot as plt
import os

def plot_results(df, title='Anomaly Detection in Time Series', filename='anomaly_detection_plot.png'):
    # Create an output directory if it doesn't exist
    output_dir = 'images'
    os.makedirs(output_dir, exist_ok=True)

    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df['value'], label='Values')
    plt.scatter(df.index[df['anomaly'] == 1], df['value'][df['anomaly'] == 1], color='red', label='Anomalies')
    
    # Set the plot title and labels
    plt.title(title)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()

    # Save the plot
    plt.savefig(os.path.join(output_dir, filename), bbox_inches='tight')
    
    # Add title below the plot
    plt.figtext(0.5, -0.1, title, ha='center', fontsize=12)
    
    plt.show()  # Display the plot