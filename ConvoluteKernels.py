import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from skimage import data, util, filters, color
from scipy.ndimage import correlate

class ConvoluteKernels:
    """
    30/04/25 Jacques Bourg
    """
    # def __init__(self):
    #     self.l = 5
    #     self.kernel_list = self.create_kernels()
    #     self.image = self.create_image()
    #     self.ind = 0
    #     self.actual_kernel = self.kernel_list[self.ind]
    #     self.fig, self.axes = plt.subplots(1, 3, figsize=(15, 5))
    #     plt.subplots_adjust(bottom=0.25)
    #     self.ax_img1, self.ax_img2, self.ax_img3 = self.axes
    #     self.setup_plot()
    #     self.setup_slider()
    #     self.setup_button()

    # def create_kernels(self):
    #     kernel = np.zeros((11,11))
    #     kernel[5-self.l:5+self.l+1,5] = 1
    #     kernel[5,5-self.l:5+self.l+1] = 1

    #     kernel2 = np.zeros((11,11))
    #     kernel2[5,5] = 1

    #     kernel3 = np.zeros((11,11))
    #     kernel3[4:7,4:7] = 1

    #     kernel4 = np.zeros((11,11))
    #     kernel4[:,5] = 1

    #     kernel5 = np.zeros((13,13))
    #     kernel5[5:8, 5:8] = -1/8
    #     kernel5[6,6] = 1

    #     kernel6 = np.zeros((11,11))
    #     kernel6[3:8,3:8] = -9/12
    #     kernel6[4:7,4:7] = 1

    #     kernel7 = np.zeros((13,13))
    #     lp = 6
    #     kernel7[6-lp:6+lp+1,5] = -21/48
    #     kernel7[6-lp:6+lp+1,6] = -21/48
    #     kernel7[6-lp:6+lp+1,7] = -21/48
    #     kernel7[5,6-lp:6+lp+1] = -21/48
    #     kernel7[6,6-lp:6+lp+1] = -21/48
    #     kernel7[7,6-lp:6+lp+1] = -21/48 
    #     kernel7[6-self.l:6+self.l+1,6] = 1
    #     kernel7[6,6-self.l:6+self.l+1] = 1

    #     kernel8 = np.zeros((11,11))
    #     kernel8[:,3:8] = 1
    #     kernel8[:,4:7] = -22/33

    #     kernel9 = np.zeros((15,15))
    #     lpp = 7
    #     kernel9[7-lpp:7+lpp+1,5] = -69/56
    #     kernel9[7-lpp:7+lpp+1,6] = -69/56
    #     kernel9[7-lpp:7+lpp+1,7] = -69/56
    #     kernel9[7-lpp:7+lpp+1,8] = -69/56
    #     kernel9[7-lpp:7+lpp+1,9] = -69/56

    #     kernel9[5,7-lpp:7+lpp+1] = -69/56
    #     kernel9[6,7-lpp:7+lpp+1] = -69/56
    #     kernel9[7,7-lpp:7+lpp+1] = -69/56
    #     kernel9[8,7-lpp:7+lpp+1] = -69/56  
    #     kernel9[9,7-lpp:7+lpp+1] = -69/56

    #     lp = 6
    #     kernel9[7-lp:7+lp+1,6] = 1
    #     kernel9[7-lp:7+lp+1,7] = 1
    #     kernel9[7-lp:7+lp+1,8] = 1
    #     kernel9[6,7-lp:7+lp+1] = 1
    #     kernel9[7,7-lp:7+lp+1] = 1
    #     kernel9[8,7-lp:7+lp+1] = 1

    #     kernel10 = np.zeros((15,15))
    #     lpp = 7
    #     kernel10[7-lpp:7+lpp+1,5] = -21/104
    #     kernel10[7-lpp:7+lpp+1,6] = -21/104
    #     kernel10[7-lpp:7+lpp+1,7] = -21/104
    #     kernel10[7-lpp:7+lpp+1,8] = -21/104
    #     kernel10[7-lpp:7+lpp+1,9] = -21/104

    #     kernel10[5,7-lpp:7+lpp+1] = -21/104
    #     kernel10[6,7-lpp:7+lpp+1] = -21/104
    #     kernel10[7,7-lpp:7+lpp+1] = -21/104
    #     kernel10[8,7-lpp:7+lpp+1] = -21/104  
    #     kernel10[9,7-lpp:7+lpp+1] = -21/104

    #     lp = 5
    #     kernel10[7-lp:7+lp+1,7] = 1
    #     kernel10[7,7-lp:7+lp+1] = 1

    #     return [kernel, kernel2, kernel3, kernel4, kernel5, kernel6, kernel7, kernel8, kernel9, kernel10]

    # def create_image(self):
    #     image = np.zeros((100,100))
    #     image[20:40,20:40] = 1
    #     image[20:40,20:40] = 1
    #     image[60,20]       = 7
    #     image[80,20]       = 2

    #     l = 5
    #     image[80-l:80+l+1,80] = 1
    #     image[80,80-l:80+l+1] = 1

    #     image[20-l:20+l+1,80] = 3
    #     image[20,80-l:80+l+1] = 3

    #     image[80, 50] = 3
    #     image[80-4, 50] = 3

    #     return image

    # def add_gaussian_noise(self, image, var=0.01):
    #     noisy_image = image + var*np.random.rand(np.shape(image)[0], np.shape(image)[1])
    #     return noisy_image

    # def apply_convolution(self, image, kernel):
    #     return correlate(image, kernel)

    # def setup_plot(self):
    #     a = np.max(np.abs(self.actual_kernel))
    #     cm_k = self.custom_color_map(pow=1, nb_points= 256, max = a)
    #     self.img1 = self.ax_img1.imshow(self.actual_kernel, cmap=cm_k, vmin=-a, vmax= a)
    #     self.fig.colorbar(self.img1, ax=self.ax_img1)

    #     self.img2 = self.ax_img2.imshow(self.image, cmap='gray')
    #     self.fig.colorbar(self.img2, ax=self.ax_img2)

    #     conv_im = self.apply_convolution(self.image, self.actual_kernel)
    #     b = np.max(np.abs(conv_im))
    #     cm_l = self.custom_color_map(pow=1, nb_points= 256, max = 1)

    #     self.img3 = self.ax_img3.imshow(conv_im, vmin = -b, vmax = b, cmap=cm_l)
    #     self.fig.colorbar(self.img3, ax=self.ax_img3)

    #     self.ax_img1.set_title('Kernel')
    #     self.ax_img2.set_title('Image + Noise')
    #     self.ax_img3.set_title('Convolution Result')

    # def setup_slider(self):
    #     self.ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
    #     self.slider = Slider(self.ax_slider, 'Noise Level', 0.0, 5, valinit=0.01)
    #     self.slider.on_changed(self.update)

    # def setup_button(self):
    #     self.ax_button = plt.axes([0.8, 0.025, 0.1, 0.04])
    #     self.button = Button(self.ax_button, 'Change Kernel')
    #     self.button.on_clicked(self.change_kernel)

    # def update(self, val):
    #     noise_level = self.slider.val
    #     noisy_image = self.add_gaussian_noise(self.image, var=noise_level)
    #     self.img2.set_data(noisy_image)

    #     conv_im = self.apply_convolution(noisy_image, self.actual_kernel)
    #     b = np.max(np.abs(conv_im))    
    #     self.img3.set_data(conv_im)
    #     self.img3.set_clim([-b, b])
    #     self.fig.canvas.draw_idle()

    # def change_kernel(self, event):
    #     self.ind = self.ind + 1
    #     ind_vec = self.ind % len(self.kernel_list)
    #     actual_kernel = self.kernel_list[ind_vec]

                                 
                                 
                                 
 

    #     a = np.max(np.abs(actual_kernel))    
    #     img1.set_data(actual_kernel)  
    #     img1.set_clim([-a, a])

    # noise_level = slider.val
    # noisy_image = add_gaussian_noise(image, var=noise_level)
    # img2.set_data(noisy_image)
    
    
    # conv_im = apply_convolution(noisy_image, actual_kernel)
    # b = np.max(np.abs(conv_im))    

    # img3.set_data(conv_im)
    # img3.set_clim([-b, b])

    # fig.canvas.draw_idle()