# Qunatifying Grapevine Cluster Closure (QCC)

[toc]

## Environment Configuration
### 1. PaddleSeg

[PaddleSeg](https://github.com/PaddlePaddle/PaddleSeg) is an open-source image segmentation framework based on PaddlePaddle. To install PaddleSeg, you can follow the instructions provided in the PaddleSeg documentation. Here's how you can install it using pip:


```shell
git clone https://github.com/PaddlePaddle/PaddleSeg.git
```

### 2. Dev Environment 
`requirements.txt` file clearly list all the packages needed. If you want to use GPU to train the model, remember to use
`paddleseg-gpu` version.
```shell
pip install -r requirements.txt
```

## Model Training
```shell
cd PaddleSeg
python tools/train.py --config ../dataset/psp2.yaml
```

## Model Evaluation

```shell
python tools/train.py --config configs/pspnet/pspnet.yaml --model_path ./output/iter_10000/model.pdparams
```

## Prediction

```shell
python tools/inference.py --config <config_path> --model_path <model_path> --image_path data/example.jpg --save_dir results
```



Step 2: Copy the code to the installed PaddleSeg folder
After installing PaddleSeg, you need to copy the code provided in the Segmentation folder to the installed PaddleSeg folder. You can do this by navigating to the PaddleSeg installation folder and copying the files to the Segmentation folder.

Step 3: Train the algorithm
Once you have installed PaddleSeg and copied the code to the Segmentation folder, you can train the PSPNet model on your dataset. To do this, you need to run the train.py script provided in the Segmentation folder. You will need to specify the path to your dataset, the number of epochs to train for, and other hyperparameters. The script will save the trained model to the models directory.


Step 4: Run the algorithm on your collected images
After training the PSPNet model, you can use it to perform cluster segmentation on your collected images. To do this, you need to run the inference.py script provided in the Segmentation folder. You will need to specify the path to your input image and the path to the trained model. The script will generate a segmented image, which you can then use for further analysis.
```python 
python inference.py --config configs/pspnet/pspnet.yaml --model_path models/pspnet/best_model/model.pdparams --image_path data/example.jpg --save_dir results
```

## Image thresolding

To quantify the Cluster Closure (%CC) using the code provided in the repository, you need to use the script named "Calculating_Cluster_Closure". Before running the script, you need to adjust the path parameter according to the location of your input images. You may also need to toggle the contrast enhancement parameter (named 'cultivar') if required.

Here's how you can adjust the parameters:

Step1 : path: This parameter specifies the path to the input images that you want to analyze. You need to set this parameter to the path of your input image directory.

Step 2: cultivar - This parameter is used to toggle contrast enhancement on or off. If you want to apply contrast enhancement, set this parameter to 1. Otherwise, set it to 0.

Step 3: After adjusting the parameters, you can run the script to calculate the Cluster Closure (%CC) for your input images. The script will save the results in a CSV file.

## Stat Analysis

Use stats_Plot.py file to calculate basic stats and Asymptotic.R script to fit regression and calculate the time of cluster closure.

