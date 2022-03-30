import matplotlib.patches as patches
import matplotlib.pyplot as plt
from PIL import Image
import json


if __name__ == '__main__':
    preds_path = './data/hw01_preds'
    data_path = './data/RedLights2011_Medium'

    f = open(f'{preds_path}/preds.json')
    img_2_bboxes = json.load(f)

    fig, ax = plt.subplots()

    for img_name in img_2_bboxes:
        bboxes = img_2_bboxes[img_name]
        img = Image.open(f'{data_path}/{img_name}')

        for bbox in bboxes:
            height = abs(bbox[2] - bbox[0])
            width = abs(bbox[3] - bbox[1])
            ax.imshow(img)
            # negative height so that corner is top left
            rect = patches.Rectangle((bbox[0], bbox[1]),
                                     width,
                                     -height,
                                     linewidth=1,
                                     edgecolor='m',
                                     facecolor='none')

            # Add the patch to the Axes
            ax.add_patch(rect)

        plt.savefig(f'{preds_path}/{img_name}_pred.jpg')

        plt.cla()