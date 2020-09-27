# Quelques exemples d'usage de la librairie matplotlib
# De nombreux exemples supplémentaires à cette adresse: https://matplotlib.org/gallery/index.html
# Remarque : N'oubliez pas plt.close()! après chaque figure

import matplotlib.pyplot as plt
import numpy             as np

if __name__ == '__main__':

	## function
	#############################################
	x = np.linspace(0, 2, 100)           # Generate evenly spaced numbers

	fig, ax = plt.subplots()             # Create a figure and an axis.
	ax.plot(x, x, label='linear')        # Plot some data on the axes.
	ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
	ax.plot(x, x**3, label='cubic')      # ... and some more.
	ax.set_xlabel('x label')             # Add an x-label to the axes.
	ax.set_ylabel('y label')             # Add a y-label to the axes.
	ax.set_title("Simple Plot")          # Add a title to the axes.
	ax.legend()                          # Add a legend.
	#plt.show()                           # Display the plot (close to continue)
	plt.savefig('mpl_plot.png')          # Save the plot on the HD (current directory)
	plt.close()                          # Close the fig


	## scatter data
	#############################################
	data1, data2 = np.random.randn(2, 100)  # Draw random samples

	fig, ax = plt.subplots(1, 1)            # Create a figure and an axis.
	ax.plot(data1, data2, marker='x')       # Scatter plot
	plt.savefig('mpl_scatter.png')          # Save the plot on the HD
	plt.close()                             # Close the fig


	## error bar
	# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.errorbar.html
	#############################################
	x = np.linspace(0, 10, 50)
	dy = 0.8
	y = np.sin(x) + dy * np.random.randn(50)

	plt.errorbar(x, y, yerr=dy, fmt='o', color='black', ecolor='lightgray', elinewidth=3, capsize=0);
	plt.savefig('mpl_errorbar.png')
	plt.close()


	## histogram (avec personalisation)
	# https://matplotlib.org/3.3.1/api/_as_gen/matplotlib.pyplot.hist.html
	#############################################
	x = np.random.randn(1000)

	plt.style.use('classic')
	fig=plt.figure(figsize=(5,3))
	ax = plt.axes(facecolor='#E6E6E6')
	# Afficher les ticks en dessous de l'axe
	ax.set_axisbelow(True)
	# Cadre en blanc
	plt.grid(color='w', linestyle='solid')

	# Cacher le cadre
	# ax.spines contient les lignes qui entourent la zone où les 
	# données sont affichées.
	for spine in ax.spines.values():
	    spine.set_visible(False)
	# Cacher les marqueurs en haut et à droite
	ax.xaxis.tick_bottom()
	ax.yaxis.tick_left()

	# Nous pouvons personnaliser les étiquettes des marqueurs
	# et leur appliquer une rotation
	marqueurs = [-3, -2, -1, 0, 1, 2]
	xtick_labels = ['A', 'B', 'C', 'D', 'E', 'F']
	plt.xticks(marqueurs, xtick_labels, rotation=30)

	# Changer les couleur des marqueurs
	ax.tick_params(colors='gray', direction='out')
	for tick in ax.get_xticklabels():
	    tick.set_color('gray')
	for tick in ax.get_yticklabels():
	    tick.set_color('gray')
	    
	# Changer les couleurs des barres
	ax.hist(x, edgecolor='#E6E6E6', color='#EE6666')
	plt.savefig('mpl_histopersonalise.png')
	plt.close()

