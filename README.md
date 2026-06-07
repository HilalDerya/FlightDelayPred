# Flight Delay Prediction Based on Weather
A machine learning project that predicts whether a flight will be delayed by based on weather conditions and flight metadata.

## Overview
Using a dataset of ~195,000 U.S. domestic flights from 2022, four classification models were trained and evaluated. The best-performing model, XGBoost, achieved 79.58% accuracy on the test set.

## Dataset
The dataset combines two sources:

**Flight data** — U.S. Bureau of Transportation Statistics (BTS): departure times, airlines, origin/destination airports, delay labels
**Weather data** — Historical weather API: temperature (max/min), precipitation, wind speed, weather code

### Key details:
Raw records: ~194,917 flights
After filtering cancelled/diverted flights and dropping null weather values: ~190,981 records
Target variable: DepDel15 — binary label indicating a 15+ minute departure delay
Class distribution: 75.2% on-time / 24.8% delayed

## Features Used
FeatureDescriptionMonth, DayofMonth, DayOfWeekTemporal featuresCRSDepTimeScheduled departure timeDistanceFlight distanceOrigin_encoded, Dest_encodedOrigin/destination airports (label encoded)Airline_encodedOperating airline (label encoded)temp_max, temp_minMax/min temperature on departure dayprecipitationDaily precipitationwindspeed_maxMaximum wind speedweather_codeWMO weather condition code

## Models & Results
Four models were trained using an 80/20 train-test split (stratified):
ModelTrain AccuracyTest AccuracyLogistic Regression76.71%76.76%Random Forest79.76%79.18%Gradient Boosting79.76%79.57%XGBoost79.69%79.58% ✅
**XGBoost — Detailed Performance**
              precision    recall    f1-score   support

   On-time       0.81      0.95      0.88     28,707
   Delayed       0.69      0.33      0.44      9,490

  accuracy                           0.80     38,197

**Confusion Matrix:**

Correctly predicted on-time: 27,308
Correctly predicted delayed: 3,090
False positives (predicted delayed, was on-time): 1,399
False negatives (predicted on-time, was delayed): 6,400


<img width="1489" height="1189" alt="indir" src="https://github.com/user-attachments/assets/c66365b2-0c9a-465f-badd-6216dc26fefc" />

## Tech Stack

- **Language:** Python 3
- **Platform:** Google Colab
- **Libraries:** pandas, numpy, scikit-learn, xgboost, matplotlib, seaborn
