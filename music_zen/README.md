# Overview 

Project for implementing ML model that makes music from input audio files. 

# Procedure 

## GET DATA 

### install pytube 

install pytube using 

`python -m pip install git+https://github.com/nficano/pytube` 

as directly installing from poetry would give give 'StreamingData' errors 

### use pytube 

Youtube using DASH - Dynbamic Adaptive Stream through HTTPS

when querying a url we receive list of streams avaialble 
we would chose audio streams prefereably 
download sample from collected sources and store them
these sample audio file is going to be the training data testing data for our ML model . 

### clean data 

no need to clean data as audio files are just music 

2. CHOSE MODEL 

We are aiming to create a generative audio model that would learn patterns from the audio data set we would use for training, and generate audio with similar characteristics. 

The goal is to use audio model for music compositio and generation. There more data we use the more sophisticated and well tuned to our data the model would be. We would utilize a [Youtube playlist](https://youtube.com/playlist?list=PLHXu9v3Y_fKkS7ljYOGo_0y9FhI2fI-ZS&si=8AEFDOrJlkebCxjT) which would contain all the data we would use for training. 


There are a list of generative models that i would explore in the search of the most compatible and fitting to this particular dataset. 

- Generative Adversarial Networks (like)
- Stable Diffusion Models (dislike)
- Autoregressive models (dislike)
- Variational Autoencoders (like)
- Convolutions GANS (maybe)
- [Wave Net](https://github.com/ibab/tensorflow-wavenet)

## TRAIN MODEL 

## EVALUATE MODEL 

## TEST MODEL

## DEPLOY MODEL 

## MONITOR


