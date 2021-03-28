from FaceDetection.FaceDetector import FaceDetector 
from FaceClassification.CNN import ConvolutionalNeuralNetwork
from Test.test import Tester


#detector = FaceDetector();
#image = detector.detect_face('faces/jd2.jpg')
#if image is not None:
#    plt.imshow(image)
#    plt.show()

#a = ConvolutionalNeuralNetwork(vgg16_path = 'vgg16_weights_tf_dim_ordering_tf_kernels_notop.h5')
#a.fit_data('faces/test/', 'faces/train/')


b = Tester("faces/test/Kiera", 'model.h5')
b.run_test(200, 200)
