import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy.linalg as lin
import requests
from io import StringIO

data = pd.read_csv('', low_memory=False, skipinitialspace=True)
print("İlk 5 satır:")
print(data.head())

print("\n" + "="*50 + "\n")

print("Sütun isimleri:")
print(data.columns.tolist())

print("\n" + "="*50 + "\n")

print("Veri bilgisi:")
print(data.info())

print("\n" + "="*50 + "\n")

print(f"Satır sayısı: {data.shape[0]}")
print(f"Sütun sayısı: {data.shape[1]}")
#data=data.dropna()

#print(data.LOCID.unique())