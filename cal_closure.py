import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from matplotlib.backends.backend_pdf import PdfPages
from  pathlib import Path

def find_png_files(root_dir):
    png_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith('.png'):
                png_files.append(os.path.join(dirpath, file))
    return png_files

def process_images(png_files, output_path):
    df = pd.DataFrame(columns=['Date','Treatment', 'Rep', 'CC Value'])
    with PdfPages(os.path.join(output_path, 'count.pdf')) as pdf_pages:
        for file_path in png_files:
            img = cv2.imread(file_path)
            # 假设img为灰度图，如果不是，先转换为灰度图
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # 创建基于特定值的掩模
            mask_38 = img_gray == 38
            mask_75 = img_gray == 75

            # 可以根据需要处理这两个掩模
            # 例如，计算每个掩模的像素数量
            count_38 = np.sum(mask_38)
            count_75 = np.sum(mask_75)
            CC_value = count_38 / (count_38 + count_75) * 100

            # 更新DataFrame
            print(file_path)
            date_parts = file_path.split('\\')[2].split('-')
            date = '-'.join(part for part in date_parts if part.isdigit())
            treatment = file_path.split('\\')[3][:2]
            rep = file_path.split('\\')[3][-1]
            df = df._append({'Date': date,  'Treatment':treatment, 'Rep': rep,'CC Value': CC_value}, ignore_index=True)
                
            fig, axs = plt.subplots(1, 2, figsize=(10, 5))
            axs[0].imshow(img_gray * mask_38, cmap='gray')
            axs[1].imshow(img_gray * mask_75, cmap='gray')
            fig.suptitle(f' Date: {date} - Treatment:{treatment} - Rep: {rep} - CC Value: {CC_value:.2f}% - File: {os.path.basename(file_path)}')
            pdf_pages.savefig(fig)
            plt.close(fig)


    # 保存DataFrame到CSV文件
    df.to_csv(os.path.join(output_path, 'result.csv'), index=False)
    print("ALL DONE!!!")

# 设置你的根目录和输出路径
root_dir = ".\\vignoles_output"
output_path = ".\\"
png_files = find_png_files(root_dir)
process_images(png_files, output_path)
