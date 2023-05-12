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

## How it works ? 
Its quite simple actually after taking all the user inputs we take a "reserved" value of necessary matrices note that a numpy array we must use np.copy as regular assignment will be referenced. 

<img width="785" alt="s1" src="https://github.com/malak-crypto/BankersAlgorithm/assets/68809008/59a4370d-0e01-49b2-9a39-e5d81df78ccb">

Then a request is asked for example: process 1 requests 1 unit of process 1. After checking for units validity the numpy arrays are updated.

<img width="528" alt="s2" src="https://github.com/malak-crypto/BankersAlgorithm/assets/68809008/2d65accb-de6a-44f5-9d1a-9164f335d03a">
 
 Here comes the cool part
 <img width="698" alt="s3" src="https://github.com/malak-crypto/BankersAlgorithm/assets/68809008/11c2e7fd-9c4e-4494-ace1-e0e81d13d590">
 - we have a while loop to check whether the entire matrix is set to a certain value (-1 our flag to state that a process is done)
 - then we have a for loop to check on each process
 - if the need resources of this process is less than or equal available then it is safe 
 - the available matrix is updated by adding the current resources of this process to the available 
 - and the row of this process in need matrix is set to -1 (to then avoid in upcoming iterations)
 - else we do nothing we just update an iterator 
 - if the iterator is equal to processes then all processes are unsafe we just exit 
 - now you wonder an infinite loop might occure because what if we never have the entire matrix set to -1 and not all processes are unsafe
 - the counter plays its role here after each for loop we update the counter once we reached equal number of processes we exit
 - the counter also ensures if they don't come in a nice sequence of safe safe safe or unsafe unsafe unsafe if they are random everything will be checked 
 - try this example 
 - total resource <6,5,7,6>
 - available <3,1,1,2>
 - currently allocated <<1,0,3,3>,<1,2,2,1>,<1,2,1,0>>
 - maximum need <<1,2,3,4>,<3,3,2,2>,<1,3,5,0>>
 - not the most efficient approach but it gets the job done ;)

## Few words
- I hope you find this repo helpful for your next project. 
- Contact me anytime for any questions will be glad to help :)
 
 
 
