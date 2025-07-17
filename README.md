# Picky-Autoencoder-Image-Categorization-Research

Here is the the catch.

Can I use autoencoders and tricks in the latent space to categorize data without the explicit use of categorical labels.

A few definitions:
    1) There are m number of models. 
    2) There's a batch size of b.
    3) There's a latent space of l dimensions. 
    4) There's around x different classes that follow a somewhat uniform distribution. 

How it works:
    a) Train each of the m models to recreate images. 
    b) In the latent space enforce each of the model's representation of images to be confined to a given 'space' that is located along a hypersphere in the latent space. We will maximize the space between the differnent model clusters or enforce this by precalculating equidistant points that we enforce the different points of the model to go to. 


Then:
    a) Once the models have converged above, then we will swap the loss function with one that will enforce the different compressed representation of the images of the models to gain proximity in the latent space and lose proximity to the other images in the latent space. If there is a large number of categories that have implicit intraclass similarities then we can maximize. 

The hope:
    1) The model will learn to identify relevant semantic features of the images and when we get to grouping similar images together, it will implicitly group images that are more like each other. 