import matplotlib.pyplot as plt


width = 2.2
height = 1.3

plt.style.use('_mpl-gallery')

fig, ax = plt.subplots(figsize=(10, 7))
ax.set(xlim=(-width, width-1.3),
       ylim=(-height, height))
ax.set_xlabel('Real', fontsize=15)
ax.set_ylabel('Imaginary', fontsize=15)
ax.grid(True)
fig.tight_layout()


def draw_mandelbrot_figure(x, y):
    ax.scatter(x, y, s=2) # todo : changer le point size s=2 pour qu'il s'adapte aux nbr de points
    plt.show()


if __name__ == "__main__":
    draw_mandelbrot_figure([1, 2.8], [5, 5.2])
