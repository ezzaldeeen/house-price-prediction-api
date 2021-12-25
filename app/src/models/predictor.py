import pickle
import pandas as pd

# load the model
MODEL_PATH = './src/models/pickles/model_v4.pkl'
with open(MODEL_PATH, 'rb') as f:
    MODEL = pickle.load(f)

# load the preprocessor
PREPROCESSOR_PATH = './src/models/pickles/preprocesser_v2.pkl'
with open(PREPROCESSOR_PATH, 'rb') as f:
    PREPROCESSOR = pickle.load(f)


def preprocessing(sample: dict):
    """
        Preprocessing new sample, and make it ready to predict
        by scale the numeric values and encode the category values
        --------
        parameter: sample [dict] sample to transform
        --------
        return: transformed-sample [np.array] pre-processed sample
    """
    # convert the sample from dict to dataframe
    sample = pd.DataFrame.from_dict(sample, orient='index').T
    # transform new sample
    return PREPROCESSOR.transform(sample)


def single_predict(sample: dict) -> int:
    """
        compute the predicted value for this sample,
        -------
        parameter: sample [dict] sample to predict
        -------
        return: predicted_value [int] prediction
    """

    # prepare the new sample for prediction
    sample = preprocessing(sample)

    pred_value = int(MODEL.predict(sample)[0])

    return pred_value
