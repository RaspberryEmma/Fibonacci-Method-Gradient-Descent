# -*- coding: utf-8 -*-
"""
Illustrating the Fibonacci method of gradient descent in action graphically
Emma Tarmey
30/11/20, edits made since
"""

import inspect
import numpy as np
import matplotlib.pyplot as plt
import math as m
import tkinter as tk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

# **********
# NOTE:
# Function input has to be valid python code for a real-valued function.
# When in doubt, write your function, f, as a valid lambda statement.
# Then, use "inspect.getsource(f)" to generate the string that eval() later expects.
# Please examine the included test case for further detail.
# **********

# Handle activating the method
def buttonPressed(ent_f, ent_N, ent_a, ent_b, ent_tol, window):
    print( "\n\n***** Fibonacci Method for Gradient Descent *****")

    f   = lambda x : eval(ent_f.get()) # generates code from user input - dangerous!
    N   = int(ent_N.get())
    a   = float(ent_a.get())
    b   = float(ent_b.get())
    tol = float(ent_tol.get())

    fib_sequence = np.zeros(N+1, float)
    for i in range(0, N+1):
        fib_sequence[i] = fibonacci(i)

    print("\n*** Arguments: ***")
    print("f   = ",    ent_f.get())
    print("N   = ",    ent_N.get())
    print("a   = ",    ent_a.get())
    print("b   = ",    ent_b.get())
    print("tol = ",  ent_tol.get())

    print("\n*** Iterations: ***\n")
    solution = fibonacci_method(f, a, b, fib_sequence, N, tol)
    plot_function(window, f, a, b, solution)

    print("*** Final Solution: ***")
    print("x_1    = ", solution[0])
    print("x_2    = ", solution[1])
    print("f(x_1) = ", f(solution[0]))
    print("f(x_2) = ", f(solution[1]))
   

# Find the nth Fibonacci number
def fibonacci(n):
    a = 1
    b = 1
    for i in range(0, n):
        temp = a
        a    = b
        b    = temp + b
    return a


def print_status(x1, x2, fx1, fx2, a, b, i):
    print("Iteration =", i)
    print("x1    = ", x1)
    print("f(x1) = ", fx1)
    print("x2    = ", x2)
    print("f(x2) = ", fx2)
    print("a     = ", a)
    print("b     = ", b)
    print()


# Thank you to geeksforgeeks for explanation of tkinter
def plot_axis(window, f, a, b, solution):
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5), dpi = 100)
  
    # adding the subplot
    plot1 = fig.add_subplot(111)
  
    # Tkinter canvas contains Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()
  
    # placing canvas on Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
  
    # placing toolbar on Tkinter window
    canvas.get_tk_widget().pack()

    return fig, canvas


def plot_function(window, f, a, b, solution):
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5), dpi = 100)

    # function data
    xs = np.linspace(a, b, num = 100)
    ys = []
    for x in xs:
        ys.append( f(x))
  
    # adding the subplot
    plot1 = fig.add_subplot(111)
  
    # plotting the graph
    plot1.plot(xs, ys)
    plot1.scatter(solution[0], f(solution[0]), s = 50, color = "green", zorder = 2)
    plot1.scatter(solution[1], f(solution[1]), s = 50, color = "green", zorder = 2)
  
    # Tkinter canvas contains Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()
  
    # placing canvas on Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
  
    # placing toolbar on Tkinter window
    canvas.get_tk_widget().pack()


def fibonacci_method(f, a, b, fib_sequence, N, tol = 0.5):
    # count iterations of the method
    i = 0

    # successively refine a,b
    d  = b - a # width of interval
    x1 = (fib_sequence[N-2] / fib_sequence[N]) * (d + a)
    x2 = (fib_sequence[N-1] / fib_sequence[N]) * (d + a)

    while (d > tol):
        fx1 = f(x1)
        fx2 = f(x2)
        N   = N - 1
        i   = i + 1
        print_status(x1, x2, fx1, fx2, a, b, i)

        # decide how to update intervals [a, b] and [x1, x2] based on f(x1), f(x2)
        if (fx2 > fx1):
            b  = x2;
            d  = b - a
            x2 = x1
            x1 = (fib_sequence[N-2] / fib_sequence[N]) * (d + a)
        else:
            a  = x1
            d  = b - a
            x1 = x2
            x2 = (fib_sequence[N-1] / fib_sequence[N]) * (d + a)
    return (a, b)


def main():
    # Setup GUI window
    window = tk.Tk()
    window.title("Fibonacci Method Illustrated")

    # User input for function to be examined, f
    lbl_f = tk.Label(master=window, text = "f(x,y) = ")
    ent_f = tk.Entry(master=window, width=50)
    ent_f.insert(0, "(0.5 * m.exp(x)) + (-2 * m.sin(x))")
    lbl_f.pack()
    ent_f.pack()

    # User input for number of fibonacci numbers to be generated, N
    lbl_N = tk.Label(master=window, text = "N = ")
    ent_N = tk.Entry(master=window, width=50)
    ent_N.insert(0, "5")
    lbl_N.pack()
    ent_N.pack()

    # User input for lower bound of interval, a, in [a, b]
    lbl_a = tk.Label(master=window, text = "a = ")
    ent_a = tk.Entry(master=window, width=50)
    ent_a.insert(0, "0.0")
    lbl_a.pack()
    ent_a.pack()

    # User input for upper bound of interval, b, in [a, b]
    lbl_b = tk.Label(master=window, text = "b = ")
    ent_b = tk.Entry(master=window, width=50)
    ent_b.insert(0, "2.0")
    lbl_b.pack()
    ent_b.pack()

    # User input for termination condition value, tol
    # (solution difference between x1 and x2 <= tol)
    lbl_tol = tk.Label(master=window, text = "tol = ")
    ent_tol = tk.Entry(master=window, width=50)
    ent_tol.insert(0, "0.5")
    lbl_tol.pack()
    ent_tol.pack()

    # button code
    button1 = tk.Button(master  = window,
                       text    = "Run!",
                       command = lambda : buttonPressed(ent_f, ent_N, ent_a, ent_b, ent_tol, window))
    button1.pack()
    
    # do this last for tkinter
    window.mainloop()

main()

