from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

def home(request):
    return render(request, 'home.html')

def report(request):
    return render(request, 'report.html')

def predict(request):
    return render(request, 'predict.html')

def predictPost(request):
    # Use request object to extract choice.
    print(request.POST)
    kwarg = {
        'predator': int(request.POST['options-predator']),
        'aquatic': int(request.POST['options-aquatic']),
        'hair': int(request.POST['options-hair']),
        'milk': int(request.POST['options-milk']),
        'classtype': request.POST['options-type'],
        'eggs': int(request.POST['options-eggs']),
        'air': int(request.POST['options-air']),
    }
    return HttpResponseRedirect(reverse('results', kwargs=kwarg,))

import pickle
import sklearn # You must perform a pip install.
import pandas as pd

def results(request, predator, aquatic, hair, milk, classtype, eggs, air):
    print("*** Inside reults()")
    # load saved model
    with open('./model_pkl' , 'rb') as f:
        loadedModel = pickle.load(f)

    # Create a single prediction.
    singleSampleDf = pd.DataFrame([[predator, aquatic, hair, milk, 1 if classtype=='1' else 0, eggs, air]], 
                                columns=['predator', 'aquatic', 'hair', 'milk', 'class_type_1', 'eggs', 'breathes'])
    singlePrediction = loadedModel.predict(singleSampleDf)

    print("Single prediction: " + str(singlePrediction))
    class_types = ['', 'Mammal',
                    'Bird',
                    'Reptile',
                    'Fish',
                    'Amphibian',
                    'Bug',
                    'Invertebrate',
                    ]
    return render(request, 'results.html', {'predator': "YES" if predator else "NO",
                                        'aquatic': "YES" if aquatic else "NO",
                                        'hair': "YES" if hair else "NO",
                                        'milk': "YES" if milk else "NO",
                                        'class_type': class_types[int(classtype)],
                                        'eggs': "YES" if eggs else "NO",
                                        'air': "YES" if air else "NO",
                                        'prediction': "YES" if singlePrediction else "NO"})
