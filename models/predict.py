# import joblib
# import sys
# import numpy as np
# import os  

# # Get the absolute path to the directory containing predict.py
# dir_path = os.path.dirname(os.path.realpath(__file__))

# # Loading the model
# model_path = os.path.join(dir_path, 'hyper_model1.pkl')

# model = joblib.load(model_path)


# # Extracting features from command-line arguments
# features = [float(arg) for arg in sys.argv[1:22]]

# prediction = model.predict(np.array(features).reshape(1, -1))[0]
