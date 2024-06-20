# from fastapi import FastAPI
# import uvicorn
# import tensorflow
# from utils import cleaned_tokenized
# from tensorflow.keras.models import model_from_json


# app = FastAPI( debug = True)



# @app.get('/predict/{rev}' , status_code=200)
# def predict(rev : str):
#     rev= rev.replace('-',' ')
#     with open(r"E:\collage\graduation project\utils_model_tokenizer_dictionary\first june\model_architecture_testext_fisrtjunee.json", "r") as json_file:
#         loaded_model_json = json_file.read()

#     loaded_model = model_from_json(loaded_model_json)
#     loaded_model.load_weights(r"E:\collage\graduation project\utils_model_tokenizer_dictionary\first june\model_weights_testext_firstjune.h5")
#     result= 1 if loaded_model.predict(cleaned_tokenized(rev)) > .5 else 0
    
#     return {'prediction is' : result}

# #     # Run through terminal
# if __name__== '__test__' :
#     uvicorn.run(app,host='127.0.0.1',port=8000)

'''h5 small'''
from fastapi import FastAPI
import uvicorn
import tensorflow
from utils import cleaned_tokenized

app = FastAPI( debug = True)

model = tensorflow.keras.models.load_model(r'model_testext_may.h5')

@app.get('/predict/{rev}' , status_code=200)
def predict(rev : str):
    rev= rev.replace('-',' ')
    result= 1 if model.predict(cleaned_tokenized(rev)) > .5 else 0
    # (model.predict(cleaned_tokenized(rev)) > .5).astype(int)
    
    return {'prediction is' : result}

    # Run through terminal
if __name__== '__test__' :
    uvicorn.run(app,host='127.0.0.1',port=8000)
