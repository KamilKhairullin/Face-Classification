# Face Classification Convolutional Neural Network
Project distinguishes Keira Knightley or Natalie Portman in the photo.

#Implementation details

## Creating dataset
With the help of the JS script, I downloaded images from Google Images on request 'Keira Knightley' and 'Natalie Portman'.

## Processing images. Face detection.

Each image was processed and trimmed so that only the face remains.This was done using the library MTCNN.
Examples:
![00000018](https://user-images.githubusercontent.com/54369751/112759831-6fcaed80-8ffd-11eb-8c7f-4bc19701ddca.jpg){:height="500px" width="500px"}
<img src="https://user-images.githubusercontent.com/54369751/112759831-6fcaed80-8ffd-11eb-8c7f-4bc19701ddca.jpg" width="500" height="500">
![2](https://user-images.githubusercontent.com/54369751/112759836-76f1fb80-8ffd-11eb-8eb9-345b64bad382.jpg){:height="500px" width="500px"}
