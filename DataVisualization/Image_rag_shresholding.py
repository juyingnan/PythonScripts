import os
from skimage import io, segmentation, color


def get_rag_thresholding_img(original_img):
    labels1 = segmentation.slic(original_img, compactness=30, n_segments=400)
    out1 = color.label2rgb(labels1, original_img, kind='avg')
    return out1


def image_rag_shresholding(root_folder_path):
    os.chdir(root_folder_path)
    count_img = 0
    for website in os.listdir(os.getcwd()):
        web_dir = os.path.join(os.getcwd(), website)
        for img in os.listdir(web_dir):
            img_path = os.path.join(os.getcwd(), website, img)
            img_path = img_path.replace('\\', '//')  # for Windows adjustment
            if os.path.exists(img_path) == -1:
                print("[ERROR] Error while reading")
            img = io.imread(img_path)
            img_rag = get_rag_thresholding_img(img)
            io.imsave(img_path, img_rag)
            count_img += 1
            if count_img % 100 == 0:
                print(count_img)


folder_path = 'C:/Users/bunny/Desktop/images-227_8/'
image_rag_shresholding(folder_path)
