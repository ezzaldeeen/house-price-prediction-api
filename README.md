# House Price Prediction API

## Introduction:
A common problem in the real-world which is how we could estimate the **price of houses**, and this is very important issue for both: 
* Seller: The owner of the house.
* Buyer: The one who wants to buy the house.

The data that we want to build our model using it ( Training the model ), It stored on **Kaggle** here is the link of the data and an overview on that dataset.

House Prices Advanced Regression Techniques:

> https://www.kaggle.com/c/house-prices-advanced-regression-techniques

---

## Technical Requirements
+ virtualenv,
+ Docker,
+ The required Python librairies used can be installed from the included *requirements.txt* file:
```bash
virtualenv .venv
source .venv/bin/activate
make init
```
---

## Running the application locally
### Directly
```bash
cd ezzaldeen-mousa
python3 app/run.py
```
---

### On Docker
```bash
cd ezzaldeen-mousa
docker build -t house-price-api .
docker run -p 5000:5000 house-price-api
# or you could just use
make docker-run
```

## Testing the application
Once it is running, the API can be queried using HTTP POST requests. This can be done from the CLI using `curl` or through a GUI REST client like [Postman](https://www.getpostman.com/).


URL: `http://0.0.0.0:5000/api/v1/single_prediction`

Here is a sample query:
```json
{
    "MSZoning": "RL",
    "Street": "Pave",
    "LotShape": "IR1",
    "LandContour": "Lvl",
    "Utilities": "AllPub",
    "OverallQual": 7,
    "YearBuilt": 1959,
    "YearRemodAdd": 1997,
    "MasVnrArea": 0.0,
    "BsmtFinSF1": 1247,
    "TotalBsmtSF": 1501,
    "1stFlrSF": 1801,
    "GrLivArea": 1801,
    "FullBath": 2,
    "TotRmsAbvGrd": 6,
    "Fireplaces": 2,
    "GarageYrBlt": 1959.0,
    "GarageCars": 2,
    "GarageArea": 484
 }
```

The response should look like this:
```json
{
    "predict_value": 298457,
    "success": true
}
```