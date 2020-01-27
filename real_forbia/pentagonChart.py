import matplotlib.pyplot as plt
import numpy as np

import apply

labels=['cat', 'clown', 'dog', 'frog', 'spider']
markers = [0, 1, 2, 3, 4, 5]

str_markers = apply.eval_image()

def make_radar_chart(name, stats):

    print(str_markers)
    
    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    stats = np.concatenate((stats,[stats[0]]))
    angles = np.concatenate((angles,[angles[0]]))

    fig= plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, stats, 'o-', linewidth=2)
    ax.fill(angles, stats, alpha=0.25)
    ax.set_thetagrids(angles * 180/np.pi, labels)
    plt.yticks(markers)
    ax.set_title(name)
    ax.grid(True)


    fig.savefig("/home/ubuntu/radarChart/static/images/%s.png" % name)
    #fig.savefig("C:\\Users\\user\\Desktop\\static\\result.png")

    return plt.show()

make_radar_chart("FORBIA", str_markers)