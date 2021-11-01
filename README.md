# CS112: Discovering Computer Science

## Project 3: Bass Diffusion Model

#### 1 Overview

This project studies the growth and decay models in the context of market adoption of a new product.
We will use the Bass Diffusion model as proposed in the list of projects at the end of Chapter 4.
In this project you will practice skills with program organization, growth and decay models, and
pyplot graphing.
This is a group project. We will randomly assign partners at the start of class. You are to share
equitably the work on this assignment with your partner. Both of you should fully understand all
the parts of the project and be able to answer questions about the project on future quizzes. Your
group should not seek help from other students or people outside of class. Look to the instructor or
the class TAs for help if necessary.
Your project will have two submissions: a python program and a report (pdf). Be sure to follow
the project requirements closely as specified below.

#### 2 Bass Diffusion Models

The Bass Diffusion Models are discuss in ”Project 4.3” on pages 177-180 in the book. I suggest you
start by reading this section of the book carefully, possibly multiple times. You may want to copy
the key difference equations into your notes and review them so that you are sure you understand
them.
Notice the project comes in two parts. I suggest you program the first part, run the suggested
experiments, and then program the second part.

- The book asks you to write a function to implement the primary Bass Diffusion model. In
    the book, they recommend that you have the function itself print the graphs. I ask instead
    that you have your function return the lists of numbers back to main(), and then use the main
    function to make the graphs. This is what we did for the retirement models we built in class.
    The reason for this change is so that you can call the model twice from main() and plot
    BOTH experiments on the same graph. If you were to call the function twice from main
    where it prints its own graphs, then each experiment shows up on its separate graph. For your
    paper, I think you will want the ability to have two separate experiments shown on the same
    graph.
- In the both models, the difference equations operate on fractions of a population – values
    between 0 and 1. In the second model, the graphs you plot will be people, not fractions. I 
    recommend that you keep and build the original list as fractions. Then you write a second loop
    whereby you multiply the fractions in the lists by their population sizes to obtain numbers.

####  3 Experiments

Build the two models (two functions) as outlined in the book. Try all the parameters suggested by
the thought questions. Keep all the code, but comment out the parts that you do not want active.

#### 4 Research Paper

You will write a small research paper that illustrates your main findings.

1. Include an introduction in the paper where you explain the basic bass diffusion model and its
    purpose.
2. Copy the ”thought questions” (4.3.1 through 4.3.5) into your paper.
3. Answer each of these questions. Include a graph from your program for each question/answer.
4. Write a brief conclusion that summarizes your findings of using this model.

#### 5 Details and Requirements

- You will hand in two things: a computer program and a research paper. If you submit multiple
    times, be sure to include BOTH documents in each submission. When I download submis-
    sions, I only get the latest one. So if you have included one of the documents in an earlier
    submission, then I am missing this part.
- Your research paper should be a pdf document (you can print as a pdf in MSWord). Make
    sure your graphs use color and the colors remain in the pdf.
- Your program should follow full commenting conventions. It should follow the proper guide-
    lines for layout. Put both names in the program if you shared the work.
- Leave your program in the state where it produces the final diagram(s) you use in your paper.

# For more information, read Project3_2018.pdf


