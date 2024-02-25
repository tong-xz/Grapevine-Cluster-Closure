# Qunatifying Grapevine Cluster Closure (QCC)

[toc]

## Environment Configuration
### 1. PaddleSeg

[PaddleSeg](https://github.com/PaddlePaddle/PaddleSeg) is an open-source image segmentation framework based on PaddlePaddle. To install PaddleSeg, you can follow the instructions provided in the PaddleSeg documentation. Here's how you can install it using pip:

Q&A: https://aistudio.baidu.com/projectdetail/1924008

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
Remember to move scripts `train.py`, `val.py`, and `predict.py` under the `./PaddleSeg` directory.
```shell
cd PaddleSeg
python ./train.py --config ../psp2.yml --use_vdl 
```
Then, check the loss curve by using
```shell
visualdl --logdir output/
```
## Model Evaluation
如果output里面有best model，选择best下面的相应模型
```shell
cd PaddleSeg
python ./val.py --config ../psp2.yaml --model_path ./output/iter_10000/model.pdparams
```

## Prediction

```shell
cd PaddleSeg
python ./predict.py --config ../psp2.yaml --model_path <model_path> --image_path ../cab-franc --save_dir ../results
```

