# Selected historical code

step17/model.py retains the original authored population model, initialization, raw scalar-Value prediction, analytic gradients and vector-field functions. Only its import changes from the internal common module to a small public mathematical common module. No loss factor, learning coordinate, clipping policy, initial state or gradient equation is changed.

The integration, execution and packaging drivers are omitted. Importing these functions neither integrates a trajectory nor calls a neural model, reads a dataset, downloads weights or starts training. They are preserved for inspection and explicit mathematical use, not a default historical rerun.

The separate scripts/reproduce_summaries.py implementation reads the published stored arrays/tables. Native training/inference drivers, large gradient histories and uncertain dataset text are not publicly bundled; full historical reruns are outside the validated closeout scope.
