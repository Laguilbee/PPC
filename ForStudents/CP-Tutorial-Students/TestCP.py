from docplex.cp.model import * 
context.solver.agent = 'local' 
#context.solver.local.execfile = 'Path to the binary cpoptimizer' 
context.solver.local.execfile = '/usr/local/insa/ibm_cplex_studio_2211/cpoptimizer/bin/x86-64_linux/cpoptimizer' 
#context.solver.local.execfile = '/Users/msiala/Applications/CPLEX_Studio2211/cpoptimizer/bin/arm64_osx/cpoptimizer' 
context.params.set_attribute('Presolve', 'Off') 
context.params.set_attribute('Workers', 1)

mdl = CpoModel()

x, y, z = mdl.integer_var_list(3, 1, 3, 'L')

mdl.add(x != y) 
mdl.add(y != z) 
mdl.add(z != x)

sol = mdl.solve() 
sol.print_solution()
