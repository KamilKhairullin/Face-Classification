# Face Classification Convolutional Neural Network
Project distinguishes Keira Knightley or Natalie Portman in the photo.

#Implementation details

## Creating dataset
With the help of the JS script, I downloaded images from Google Images on request 'Keira Knightley' and 'Natalie Portman'.

## Processing images. Face detection.

Each image was processed and trimmed so that only the face remains.This was done using the library MTCNN.
Examples:
<img src="https://user-images.githubusercontent.com/54369751/112759831-6fcaed80-8ffd-11eb-8c7f-4bc19701ddca.jpg" width="400" height="200">
---->>>
<img src="https://user-images.githubusercontent.com/54369751/112759836-76f1fb80-8ffd-11eb-8eb9-345b64bad382.jpg" width="200" height="200">
<p float="left">
<img src="https://user-images.githubusercontent.com/54369751/112760042-4363a100-8ffe-11eb-8074-66595dd94155.jpg" width="400" height="400">
---->>>
<img src="https://user-images.githubusercontent.com/54369751/112760058-52e2ea00-8ffe-11eb-8e7b-a5db97622453.jpg" width="200" height="200">
 </p>
 
 ## Fitting CNN
 We fit results into CNN with VGG16 pretrained layers. Output of fitting is below
Epoch 1/25
2/69 [..............................] - ETA: 7s - loss: 0.7251 - accuracy: 0.5000
69/69 [==============================] - 18s 266ms/step - loss: 0.6687 - accuracy: 0.5902 - val_loss: 0.4861 - val_accuracy: 0.7604
Epoch 2/25
69/69 [==============================] - 17s 248ms/step - loss: 0.4652 - accuracy: 0.7732 - val_loss: 0.2536 - val_accuracy: 0.8958
Epoch 3/25
69/69 [==============================] - 17s 250ms/step - loss: 0.3015 - accuracy: 0.8761 - val_loss: 0.1622 - val_accuracy: 0.9167
Epoch 4/25
69/69 [==============================] - 17s 248ms/step - loss: 0.2142 - accuracy: 0.9098 - val_loss: 0.1541 - val_accuracy: 0.9271
Epoch 5/25
69/69 [==============================] - 17s 247ms/step - loss: 0.1626 - accuracy: 0.9317 - val_loss: 0.1197 - val_accuracy: 0.9479
Epoch 6/25
69/69 [==============================] - 17s 246ms/step - loss: 0.1315 - accuracy: 0.9490 - val_loss: 0.1094 - val_accuracy: 0.9688
Epoch 7/25
69/69 [==============================] - 17s 248ms/step - loss: 0.0886 - accuracy: 0.9663 - val_loss: 0.0855 - val_accuracy: 0.9583
Epoch 8/25
69/69 [==============================] - 17s 247ms/step - loss: 0.0925 - accuracy: 0.9590 - val_loss: 0.1178 - val_accuracy: 0.9583
Epoch 9/25
69/69 [==============================] - 17s 247ms/step - loss: 0.0875 - accuracy: 0.9690 - val_loss: 0.0435 - val_accuracy: 0.9896
Epoch 10/25
69/69 [==============================] - 17s 246ms/step - loss: 0.0488 - accuracy: 0.9827 - val_loss: 0.0555 - val_accuracy: 0.9688
Epoch 11/25
69/69 [==============================] - 17s 245ms/step - loss: 0.0485 - accuracy: 0.9818 - val_loss: 0.0228 - val_accuracy: 1.0000
Epoch 12/25
69/69 [==============================] - 17s 245ms/step - loss: 0.0605 - accuracy: 0.9809 - val_loss: 0.1438 - val_accuracy: 0.9688
Epoch 13/25
69/69 [==============================] - 17s 247ms/step - loss: 0.0570 - accuracy: 0.9772 - val_loss: 0.0563 - val_accuracy: 0.9792
Epoch 14/25
69/69 [==============================] - 17s 246ms/step - loss: 0.0187 - accuracy: 0.9927 - val_loss: 0.0066 - val_accuracy: 1.0000
Epoch 15/25
69/69 [==============================] - 17s 246ms/step - loss: 0.0586 - accuracy: 0.9845 - val_loss: 0.0812 - val_accuracy: 0.9896
Epoch 16/25
69/69 [==============================] - 17s 246ms/step - loss: 0.0364 - accuracy: 0.9909 - val_loss: 0.0917 - val_accuracy: 0.9896
Epoch 17/25
69/69 [==============================] - 17s 249ms/step - loss: 0.0141 - accuracy: 0.9936 - val_loss: 0.0514 - val_accuracy: 0.9896
Epoch 18/25
69/69 [==============================] - 17s 247ms/step - loss: 0.0171 - accuracy: 0.9954 - val_loss: 0.0652 - val_accuracy: 0.9896
Epoch 19/25
69/69 [==============================] - 17s 246ms/step - loss: 0.0258 - accuracy: 0.9927 - val_loss: 0.0409 - val_accuracy: 0.9896
Epoch 20/25
69/69 [==============================] - 17s 244ms/step - loss: 0.0201 - accuracy: 0.9954 - val_loss: 0.0602 - val_accuracy: 0.9896
Epoch 21/25
69/69 [==============================] - 17s 243ms/step - loss: 0.0158 - accuracy: 0.9936 - val_loss: 0.0827 - val_accuracy: 0.9896
Epoch 22/25
69/69 [==============================] - 17s 243ms/step - loss: 0.0171 - accuracy: 0.9964 - val_loss: 0.0467 - val_accuracy: 0.9792
Epoch 23/25
69/69 [==============================] - 17s 242ms/step - loss: 0.0121 - accuracy: 0.9982 - val_loss: 0.0933 - val_accuracy: 0.9896
Epoch 24/25
69/69 [==============================] - 17s 244ms/step - loss: 0.0244 - accuracy: 0.9918 - val_loss: 0.1313 - val_accuracy: 0.9896
Epoch 25/25
69/69 [==============================] - 17s 242ms/step - loss: 0.0201 - accuracy: 0.9954 - val_loss: 0.0699 - val_accuracy: 0.9896

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
