We need jupyter, CP optimizer (academic version) et docplex 

at insa , CP optimizer is installed in 

/usr/local/insa/ibm_cplex_studio_2211'



CP optimizer is available at https://www.ibm.com/academic/technology/data-science
To finish installation : 
cd $CPLEX_INSTALL/python 

python setup.py install 
ou 
python setup.py install --user 

To test cplex: 
cd cplex/examples/src/python 
python3.10 warehouse.py

To test cpoptimiser: 
python 3.10 TestCP.py 


Pour les note book cplex, il faut d'abord activer l'environnement : 
source activate cplex
