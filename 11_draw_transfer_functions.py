#!/usr/bin/env python
# Created by "Thieu" at 16:47, 14/07/2023 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

import matplotlib.pyplot as plt
import numpy as np
from mafese.utils.transfer import vstf_01, vstf_02, vstf_03, vstf_04, sstf_01, sstf_02, sstf_03, sstf_04

print(plt.style.available)
plt.style.use("seaborn-darkgrid")

def draw_v():
    # Generate some data
    x = np.linspace(-8, 8, 100)

    y1 = vstf_01(x)
    y2 = vstf_02(x)
    y3 = vstf_03(x)
    y4 = vstf_04(x)

    # Create a new figure
    plt.figure()

    # Plot the three functions on the same figure
    plt.plot(x, y1, label='V1')
    plt.plot(x, y2, label='V2')
    plt.plot(x, y3, label='V3')
    plt.plot(x, y4, label='V4')

    # Add a legend
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("V-shaped transfer function T(x)")
    plt.savefig("history/vshaped.pdf", bbox_inches='tight')

    # Show the plot
    plt.show()


def draw_s():
    # Generate some data
    x = np.linspace(-8, 8, 100)

    y1 = sstf_01(x)
    y2 = sstf_02(x)
    y3 = sstf_03(x)
    y4 = sstf_04(x)

    # Create a new figure
    plt.figure()

    # Plot the three functions on the same figure
    plt.plot(x, y1, label='S1')
    plt.plot(x, y2, label='S2')
    plt.plot(x, y3, label='S3')
    plt.plot(x, y4, label='S4')

    # Add a legend
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("S-shaped transfer function T(x)")
    plt.savefig("history/sshaped.pdf", bbox_inches='tight')

    # Show the plot
    plt.show()

draw_s()
draw_v()
