
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np

# from matplotlib import animation, rc
# from IPython.display import HTML
# rc('animation', html='html5')

def animate(data, clim = (-50, 200), roi = None, title = 'Animation', show_frame_nr = False):
    # First set up the figure, the axis, and the plot element we want to animate

    if show_frame_nr:
        blit = False
    else:
        blit = True

    if roi is None:
        n_rows, n_cols = data.shape[1:]
        roi = (slice(0,n_rows, 1), slice(0, n_cols, 1))
    else:
        n_rows, n_cols = data[0][roi].shape
    fig, ax = plt.subplots()
    
    

    ax.set_title(title)

    empty = np.zeros((n_rows,n_cols))
    image = ax.imshow(empty, cmap = 'viridis')
    image.set_clim(clim)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.1)
    plt.colorbar(image, cax=cax)
    

    # initialization function: plot the background of each frame
    def init():
        image.set_data(data[0])
        return (image,)

    # animation function. This is called sequentially
    def animate(i):
        image.set_array(data[i][roi])
        if show_frame_nr:
            ax.set_title(f'{title} {i}')
        return (image,)

    # plt.close() #sometimes needed when working with jupyter notebooks

    # call the animator. blit=True means only re-draw the parts that have changed.
    anim = mpl.animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=len(data), interval=50, blit=blit)

    return anim

def add_colorbar(ax, im):
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.1)
    plt.colorbar(im, cax=cax)