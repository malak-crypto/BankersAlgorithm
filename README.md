# BankersAlgorithm

The Banker's algorithm is an algorithm used in operating systems to avoid the deadlock situation by making sure that all the processes will get the resources they need to complete execution. 
This implementation of the Banker's algorithm is written in Python using PySimpleGUI and NumPy libraries.

## Prerequisites 
The following libraries are required to run the code:

- PySimpleGUI
- NumPy

These libraries can be easily installed using pip. Open your terminal and run the following command:
- pip install PySimpleGUI
- pip install numpy

## How to use ?
- Run the bankers_algorithm.py file in a Python environment (e.g. IDLE, Jupyter Notebook, etc.)
- The application will start and you will be prompted to enter the number of resources and processes.
- Enter the required parameters and click on the Next button.
-
 <img width="364" alt="Window1" src="https://github.com/malak-crypto/BankersAlgorithm/assets/68809008/01f5fd4b-b82b-4cb5-b32d-e8a2112c638e">
 
 - Enter the required matrices (total number of each resource, available number of each resource, maximum number of each resource for each process, current number of each resource for each process) and click on the Almost there button.

<img width="331" alt="window2" src="https://github.com/malak-crypto/BankersAlgorithm/assets/68809008/215825fb-5510-4ce5-af8f-401ea853f918">

- Enter the process number, resource number, and the request. Then click on the Check button to check whether the request can be granted or not.

<img width="259" alt="window3" src="https://github.com/malak-crypto/BankersAlgorithm/assets/68809008/86fc3755-c7ad-4aac-915f-2ade3116e413">

- If request can be granted user can start simulation else user must enter valid number of resources required.

<img width="317" alt="window4" src="https://github.com/malak-crypto/BankersAlgorithm/assets/68809008/3cf9dfdb-27f4-4d1e-83a4-82633a62bdaa">

- When simulation starts user can observe the different progress bars updating and popup messages inducating current state.

<img width="319" alt="Window5" src="https://github.com/malak-crypto/BankersAlgorithm/assets/68809008/8710a687-9f64-4465-aeba-300eef08524e">

- When done a popup message appears 

<img width="313" alt="window6" src="https://github.com/malak-crypto/BankersAlgorithm/assets/68809008/aaa86add-f5c7-456e-8db5-8c08d98b5796">

- Now try a deadlock case to see the other popup messages :)
