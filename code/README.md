# Phish Song Prediction

Code for the Phish Song Prediction application for the Deep Learning project. 

## Data Pipeline

`poetry run python phishDataPipeline.py`

This script will call the [phish.net](https://docs.phish.net/) API to get [setlist](https://phish.net/setlists/phish/) data and write it to `../data/allphishsets.json`. This local copy enables us to not have to call the phish.net API each time we need the same data, per their docs. Read to dataframe via:

```python
pd.read_json('../data/allphishsets.json')
```
