CGDB简介
=======

CGDB是一个基于curses图形库的GNU Debugger（GDB）图形接口。CGDB的目标是变的轻量而且敏捷，而不是拥有很多不必要的功能而变得臃肿。

CGDB的图形接口是参考GDB的文本用户接口设计和实现的，它使用一个分屏显示了当前执行的代码。代码区的界面模仿了Unix经典的文本编辑器：vi。熟悉vi的人对CGDB应该有着宾至如归的感觉。

CGDB中负责和GDB通信的库是Trivial GDB（tgdb或者叫做libtgdb）。使用这个抽象层使得展示代码的UI界面能够独立于调试器，以及极大的简化了CGDB的实现。

