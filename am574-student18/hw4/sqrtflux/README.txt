Using CLAWPACK solve scalar conservation law 
	q_t + f(q)_x = 0
with f(q) = sqrt(q). Consider states q > 0.

	Domain size: xlower = -1, xupper = 9 (clawdata.lower/upper);
	Mesh size: mx = 400 (clawdata.num_cell);
	Tfinal: tfinal = 13 (clawdata.tfinal)
	Limiter: MC (mc);
	Initial condition: 4 (0<x<1), 1 otherwise; 
			   4 (0<x<1), 0.01 otherwise.

The time t_s when the shock and rarefaction wave first begin to interact should be 12.
The numerical solution is a bit earlier. The shock speed is what it should be. The 
left edge of rarefaction wave seems to have a slightly slower speed. Interaction time 
approximates 12 if we do mesh refine. The change of limiter doesn't seem to affect the 
result too much. 

Domain size was chosen so that boundary condition won't affect numerical solution.
Tfinal was chosen so that we can observe all states we expect.
 
