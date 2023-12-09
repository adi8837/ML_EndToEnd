# this is my end to end project

# first initialize the git

```
git init
```

```
git add abc.txt
git add .
```
```
git commit -m "this is my first commit"
```

```

git pull

```

```
bash your_file_name.sh
```

```
python setup.py install
```

# another way you can mention -e . in your requirement file and you can run

```
pip install -r requirements.txt
```


## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### local cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/sunny.savita/fsdsmendtoend.mlflow \
MLFLOW_TRACKING_USERNAME=sunny.savita \
MLFLOW_TRACKING_PASSWORD=3c2c8cd1436ad32b510cfdd84944a528ba4fb650 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/adi8837/ML_EndToEnd.mlflow

export MLFLOW_TRACKING_USERNAME=adi8837

export MLFLOW_TRACKING_PASSWORD=fe1cd7c496de37a1a9f806716a4488c126f66a1d

```


### DVC cmd
- dvc init
- dvc repro
- dvc dag
