from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData,Predictpipeline

from flask import Flask , request , render_template , jsonify

app=Flask(__name__)

@app.route('/')