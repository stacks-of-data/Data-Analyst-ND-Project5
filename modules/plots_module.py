import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

sb.set_theme(style='ticks')
plt.style.use("dark_background")
default_plot_color = sb.color_palette("colorblind")[0]
orange_plot_color = sb.color_palette("colorblind")[3]
    
def InitAxesLabels(title, labels):
    plt.title(title)
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    
def SetupCompareBarPlot(values, label1, label2, text):
    bar_colors = [default_plot_color] * values.size
    plot_hatch = [''] * values.size
    is_in_label2 = label1.isin(label2)

    for i in range(is_in_label2.size):
        if is_in_label2[i] == True:
            plot_hatch[i] = 'ooo'
            bar_colors[i] = orange_plot_color
            
    sb.barplot(x=values, y=label1, palette=bar_colors, hatch=plot_hatch, edgecolor='black')
    regular_patch = mpatches.Patch(facecolor=default_plot_color, edgecolor='black', label=text[0])
    hatched_patch = mpatches.Patch(facecolor=orange_plot_color, edgecolor='black', hatch='ooo', label=text[1])
    plt.legend(handles=[hatched_patch, regular_patch], bbox_to_anchor=(1, 1), loc='upper left')