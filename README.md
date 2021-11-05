# Face Classification Convolutional Neural Network
Project distinguishes Keira Knightley or Natalie Portman in the photo.

# Implementation details

## Creating dataset
With the help of the JS script, I downloaded images from Google Images on request 'Keira Knightley' and 'Natalie Portman'.

## Processing images. Face detection.

Each image was processed and trimmed so that only the face remains.This was done using the library MTCNN.  <br />
Examples:  <br />  <br />
<img src="https://user-images.githubusercontent.com/54369751/112759831-6fcaed80-8ffd-11eb-8c7f-4bc19701ddca.jpg" width="200" height="200">
---->>>
<img src="https://user-images.githubusercontent.com/54369751/112759836-76f1fb80-8ffd-11eb-8eb9-345b64bad382.jpg" width="200" height="200">
<p float="left">
<img src="https://user-images.githubusercontent.com/54369751/112760042-4363a100-8ffe-11eb-8074-66595dd94155.jpg" width="200" height="200">
---->>>
<img src="https://user-images.githubusercontent.com/54369751/112760058-52e2ea00-8ffe-11eb-8e7b-a5db97622453.jpg" width="200" height="200">
 </p>
 
 ## Fitting CNN
 We fit results into CNN with VGG16 pretrained layers. Output of fitting is below
Epoch 25/25 <br />
69/69 [==============================] - 17s 242ms/step - loss: 0.0201 - accuracy: 0.9954 - val_loss: 0.0699 - val_accuracy: 0.9896 <br />

## Results
<p float="left">
<img src="https://user-images.githubusercontent.com/54369751/112760315-1fed2600-8fff-11eb-953b-781e247c9b56.png" width="400" height="400">
<img src="https://user-images.githubusercontent.com/54369751/112760322-29768e00-8fff-11eb-90c8-8ef930095aa0.png" width="400" height="400">
<img src="https://user-images.githubusercontent.com/54369751/112760326-2ed3d880-8fff-11eb-9aa8-f84caf8ba75b.png" width="400" height="400">
</p>
<p float="left">
<img src="https://user-images.githubusercontent.com/54369751/112760373-693d7580-8fff-11eb-8793-ed6fcb511c93.png" width="350" height="350">
<img src="https://user-images.githubusercontent.com/54369751/112760378-6b9fcf80-8fff-11eb-828f-b9a3012e8b69.png" width="350" height="350">
<img src="https://user-images.githubusercontent.com/54369751/112760380-6d699300-8fff-11eb-9aac-d3a05d9be738.png" width="350" height="350">
</p>

# Link to model
https://drive.google.com/file/d/1uJRyz3YkAYZ18tf-vJI3g8wg6PHLBV_1/view?usp=sharing
