# for single image file
from imageai.Prediction import ImagePrediction
import os

execution_path=os.getcwd()

prediction = ImagePrediction()

prediction.setModelTypeAsSqueezeNet()

prediction.setModelPath(os.path.join(execution_path, "squeezenet_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()

predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "01sailboat.jpg"), result_count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)


# # multiple image files
# from imageai.Prediction import ImagePrediction
# import os

# execution_path = os.getcwd()

# multiple_prediction = ImagePrediction()
# multiple_prediction.setModelTypeAsSqueezeNet()
# multiple_prediction.setModelPath(os.path.join(execution_path, "squeezenet_weights_tf_dim_ordering_tf_kernels.h5"))
# multiple_prediction.loadModel()

# all_images_array = []

# all_files = os.listdir(execution_path)
# for each_file in all_files:
#     if(each_file.endswith(".jpg") or each_file.endswith(".png")):
#         all_images_array.append(each_file)

# results_array = multiple_prediction.predictMultipleImages(all_images_array, result_count_per_image=5)

# for each_result in results_array:
#     predictions, percentage_probabilities = each_result["predictions"], each_result["percentage_probabilities"]
#     for index in range(len(predictions)):
#         print(predictions[index] , " : " , percentage_probabilities[index])
#     print("-----------------------")