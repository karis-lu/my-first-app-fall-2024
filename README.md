# my-first-app-fall-2024

## Setup

Create a virtual environment:
```sh
conda create -n reports-env-2024 python=3.10
```
Activate the environment:
```sh
conda activate reports-env-2024
```

Install packages:
```sh
pip install -r requirements.txt
```

[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

Create a ".env" file and add contents like the following (using your own AlphaVantage API Key):

```sh
# this is the ".env" file:
ALPHAVANTAGE_API_KEY="..."
```

## Usage

Run the example script:

```sh
python app/my_script.py
```

Run the unemployment report:

```sh
#ALPHAVANTAGE_API_KEY="..." python app/unemployment.py

#python app/unemployment.py

python -m app.unemployment
```

Run the stocks report:

```sh
#python app/stocks.py

python -m app.unemployment
```


## Testing

Run tests:

```sh
pytest
```









