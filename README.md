# tfstyles
tfstyles aims to facilitate the generation of cool images with tensorflow. It is my attempt to provide implementations 
for various neural style transfer algorithms from selected papers discussed in the review paper 
,[Neural Style Transfer: A Review](https://arxiv.org/abs/1705.04058), and organized in the repository,
[Neural-Style-Transfer-Papers](https://github.com/ycjing/Neural-Style-Transfer-Papers).

## Implementations
Implementations for all papers in the image below 
(sourced from [Neural-Style-Transfer-Papers](https://github.com/ycjing/Neural-Style-Transfer-Papers)) are currently 
being attempted, and usage instructions for any completed 
implementation is added underneath.

![taxonomy](https://github.com/ycjing/Neural-Style-Transfer-Papers/raw/master/framework_n5.png)

### A Neural Algorithm of Artistic Style, Gatys *et al* [[paper](https://arxiv.org/pdf/1508.06576.pdf)]
The method used here involves using a content image and a style image to synthesize another image which is similar to 
both the style and content images. This similarity is measured with image features obtained from layers of a deep neural 
network(DNN) and not just directly with the pixels of the image. For the content, the squared error between the desired 
image features and the content image features is used to show the similarity. However, for the style, a
correlation matrix for the features is obtained, to give a notion of texture, and the similarity is measured based on 
the squared error between the correlation matrix of the desired image and that of the style image. This correlation matrix is 
called a gram matrix. This similarity measures, for the content and style, are added up to form the loss which is 
optimized with respect to the pixels of the desired image. More details can be obtained in 
the [paper](https://arxiv.org/pdf/1508.06576.pdf) and several blog posts on the topic. Usage instructions below;

#### usage
```python
from tfstyles import gatys16
config_dict = {
    "content_image_path": "",
    "style_image_path": "",
    "synthesized_image_path": "",
    "iterations": "",
}
gatys16.run(config_dict)
```
The module name, gatys16, is comprised of the author's name and the year of publication.
syle tranfer is performed by calling the run function in the gatys16 module, and supplying a config dictionary, config_dict.<br/>
**descrition of the key-value pairs in config_dict**

key | type | description
--- | --- | ---
content_image_path | str | full path of the content image
style_image_path | str | full path of the style image
synthesized_image_path | str | full path of the synthesized image, which may not exist yet
iterations | int | number of times to iterate through the optimization step of making the synthesized image similar toboth the content and style images.
