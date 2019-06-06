[x] Profile ARA* from smpl_test using google-profiler.

Instructions
============

1. To enable the profiler, set the environment variable ``CPUPROFILE`` to the file name you want to save the output in.
2. By default, this file will be saved in ``.ros`` folder.
3. Interpret this file using ``pprof``.

Results
=======

Analysis of the call stack shows clearly that the ``GetSuccs`` function is the most expensive operation in the whole pipeline accounting for roughly ``41%`` of calls. In particular, the ``checkAction`` function that finds the successors and does collision-checking is the most expensive operation.

The results agree with my intuition that collision checking is expensive. An important point is that ``checkAction`` is called for every action, irrespective of whether it ends by being valid/invalid or useful/not-useful. In this context work on partial expansion of nodes, lazy collision checking and minimizing edge evaluations are relevant.
