import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# ========================
# Plot รูปภาพตัวอย่าง
# ========================
def plot_images(images, labels=None, class_names=None, nrow=4):
    plt.figure(figsize=(12, 8))
    for i in range(len(images)):
        plt.subplot(nrow, len(images)//nrow + 1, i+1)
        plt.imshow(images[i].permute(1,2,0))
        if labels is not None and class_names is not None:
            plt.title(class_names[labels[i]])
        plt.axis('off')
    plt.show()

# ========================
# บันทึกสถิติลง CSV สำหรับ Dashboard
# ========================
def save_statistic(animal_type, disease, output_csv='web/static/statistics.csv'):
    if os.path.exists(output_csv):
        df = pd.read_csv(output_csv)
    else:
        df = pd.DataFrame(columns=['animal', 'disease'])

    df = pd.concat([df, pd.DataFrame({'animal':[animal_type], 'disease':[disease]})], ignore_index=True)
    df.to_csv(output_csv, index=False)

# ========================
# Metric ตัวอย่าง Accuracy
# ========================
def calculate_accuracy(y_true, y_pred):
    correct = sum([yt==yp for yt, yp in zip(y_true, y_pred)])
    return correct / len(y_true)