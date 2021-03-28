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

&nbsp;

<img src="https://user-images.githubusercontent.com/54369751/112760042-4363a100-8ffe-11eb-8074-66595dd94155.jpg" width="400" height="400">
-->>
<img src="https://user-images.githubusercontent.com/54369751/112760058-52e2ea00-8ffe-11eb-8e7b-a5db97622453.jpg" width="200" height="200">
