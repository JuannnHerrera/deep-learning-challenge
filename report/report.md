
# Deep Learning Model for Alphabet Soup Charity

## Overview of the Analysis
Hey there! The goal of this analysis is to build a cool binary classifier that predicts the success of applicants for funding based on historical data. Let's dive into the details!

## Data Preprocessing
- **Target Variable**: `IS_SUCCESSFUL`
- **Feature Variables**: Everything else except `EIN` and `NAME`
- **Removed Columns**: `EIN`, `NAME`

## Results
### Data Preprocessing:
We identified our target and features, then cleaned up the data by dropping unnecessary columns and combining rare categories into `Other`. After encoding the categorical variables and scaling the data, we were ready to roll.

### Model Details:
- **Neurons and Layers**: Started with 100 and 50 neurons in the hidden layers.
- **Activation Functions**: `relu` for hidden layers and `sigmoid` for the output.
- **Model Performance**: 
  - Initial model accuracy: 0.73 with a loss of 0.5630.
  - Optimized model accuracy: 0.74 with a loss of 0.5890.

### Optimization Attempts:
We tried a bunch of things like increasing neurons, adding more layers, and tweaking activation functions to boost performance.

## Summary
The optimized model hit an accuracy of about 0.74. There's always room for improvement, so next steps could include trying different models like RandomForest or SVM for potentially better results.

## Alternative Models
Considering the data's complexity and non-linearity, a RandomForest or SVM model might do a better job. These models can handle various data patterns more effectively, making them strong contenders for future attempts.
