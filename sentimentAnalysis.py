from flask import Flask, request, render_template
import torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)
# Use a pipeline as a high-level helper
from transformers import pipeline
# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained("NepBERTa/NepBERTa",from_tf=True).to(device)


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    return render_template('main.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the form
    input_data = request.form.to_dict()
    print(input_data)
    # features = ['0', '1', '2'] 
    pipe = pipeline("text-classification", model='TrainedModel')
    output = pipe(input_data["input_text"])
    print(output)

    for i in output:
        if i['label'] =='LABEL_1':
            return f"Positive sentiment Score:{i['score']:.3f}"
        if i['label'] =='LABEL_2':
            return f"Neutral Sentiment Score:{i['score']:.3f}"
        else:
            return f"Negative Sentiment Score: {i['score']:.3f}"

if __name__ == '__main__':
    app.run(debug=True)
