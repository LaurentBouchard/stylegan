# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
# Copyright (c) 2019, Laurent Bouchard. The modifications made in this file were made by myself and are not endorsed by NVlabs0
# The original work can be found here: https://github.com/NVlabs/stylegan
# 
# This work is licensed under the Creative Commons Attribution-NonCommercial
# 4.0 International License. To view a copy of this license, visit
# http://creativecommons.org/licenses/by-nc/4.0/ or send a letter to
# Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

"""Minimal script for generating an image using pre-trained StyleGAN generator."""

import os
import pickle
import numpy as np
import PIL.Image
import dnnlib
import dnnlib.tflib as tflib
import config
import sys

def main():
    if (len(sys.argv) != 4):
        print("Usage: python", str(sys.argv[0]), "<name of the round> <psi> <number of images>\n Name of the round can be any string and psi should be a number between 0.0 and 1.0 and the number of image can be any integer")
        exit(1)
    
    # Pick parameters.
    round = str(sys.argv[1])
    psi = float(sys.argv[2])
    nb_images = int(sys.argv[3])

    # Initialize TensorFlow.
    tflib.init_tf()
    
    # Load pre-trained network.
    _G, _D, Gs = pickle.load(open("./2019-02-26-stylegan-faces-network-02048-016041.pkl", "rb"))

    os.makedirs(config.result_dir, exist_ok=True)
    os.makedirs(os.path.join(config.result_dir, round))
    fmt = dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True)
    rnd = np.random.RandomState(None)
    
    print("Generating images...\n")
    for i in range(0,nb_images):
        latents = rnd.randn(1, Gs.input_shape[1])

        # Generate image.
        images = Gs.run(latents, None, truncation_psi=psi, randomize_noise=True, output_transform=fmt)
    
        # Save image.
        png_filename = os.path.join(config.result_dir, round, str(i)+'.png')
        PIL.Image.fromarray(images[0], 'RGB').save(png_filename)
    
    print("\nImages generation done. They can be found in", "./results/"+round+"/")

if __name__ == "__main__":
    main()
