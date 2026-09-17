import matplotlib.pyplot as plt

plt.rcParams.update({
	# Figure
	"figure.figsize": (8, 5),
	"figure.dpi": 150,
	"savefig.dpi": 300,

	# Font
	"font.family": "sans-serif",
	"font.sans-serif": ["DejaVu Sans", "Arial", "Helvetica"],
	"font.size": 22,

	# Axes
	"axes.titlesize": 18,
	"axes.labelsize": 16,
	"axes.titleweight": "bold",
	"axes.labelweight": "regular",

	# Tick labels
	"xtick.labelsize": 16,
	"ytick.labelsize": 16,

	# Legend
	"legend.fontsize": 12,
	"legend.title_fontsize": 10,
	"legend.frameon": True,

	# Lines
	"lines.linewidth": 2.0,
	"lines.markersize": 5,

	# Ticks
	"xtick.major.size": 5,
	"ytick.major.size": 5,
	"xtick.major.width": 1.2,
	"ytick.major.width": 1.2,

	# Axes spines
	"axes.linewidth": 1.2,

	# Grid
	"grid.linewidth": 0.7,
	"grid.linestyle": '-.',
	"grid.alpha": 0.3,

	# Better layout
	"figure.constrained_layout.use": True,

	# Figure saving default directory
	"savefig.directory": "results/"
})
