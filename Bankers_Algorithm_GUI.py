import PySimpleGUI as sg
import numpy as np



sg.theme('Tan')

# take the number of resources and processes from the user
layout = [[sg.Text('Step 1: Enter your parameters', font=("Helvetica", 15))],
          [sg.Text('Number of resources',size=(15,1)), sg.InputText('Ex: 4')],
          [sg.Text('Number of processes',size=(15,1)), sg.InputText('Ex: 3')],
          [sg.Submit(button_text='Next')]]
window = sg.Window('Banker\'s Algorithm', layout)
event, values = window.read()
window.close()
Resources = int(values[0])
Processes = int(values[1])


layout = [[sg.Text('Step 2: Enter your matrices', font=("Helvetica", 15))],
          [sg.Text('Total number of each resource', font=("Helvetica", 10))]]
for i in range(Resources):
    layout.append([sg.Text('Resource ' + str(i+1) + ':'), sg.InputText('Ex: 1')])
layout.append([sg.Text('Available number of each resource', font=("Helvetica", 10))])
for i in range(Resources):
    layout.append([sg.Text('Resource  ' + str(i+1) + ':'), sg.InputText('Ex: 1')])
layout.append([sg.Text('Maximum number of each resource for each process', font=("Helvetica", 10))])
for i in range(Processes):
        layout.append([sg.Text('Process ' + str(i+1) + ':'),sg.InputText('Ex: 1 2 3')])
layout.append([sg.Text('Current number of each resource for each process', font=("Helvetica", 10))])
for i in range(Processes):
        layout.append([sg.Text('Process ' + str(i+1) + ':'),sg.InputText('Ex: 1 2 3')])
layout.append([sg.Submit(button_text='Almost there')])
window = sg.Window('Banker\'s Algorithm', layout)
event, values = window.read()
window.close()
#store the total number of each resource in a numpy array
total_resources = []
for i in range(Resources):
        total_resources.append(int(values[i]))
total_resources_matrix = np.array(total_resources).reshape(1, Resources)
#store the available number of each resource in a numpy array
available_resources = []
for i in range(Resources):
        available_resources.append(int(values[i+Resources]))
available_resources_matrix = np.array(available_resources).reshape(1, Resources)

#store the maximum number of each resource for each process in a numpy array
maximum_matrix_all = np.empty((0, Resources), int)
for i in range(Processes):
        maximum_matrix_all = np.append(maximum_matrix_all, np.array([list(map(int, values[i+2*Resources].split()))]), axis=0)

#store the current number of each resource for each process in a numpy array
current_matrix_all = np.empty((0, Resources), int)
for i in range(Processes):
        current_matrix_all = np.append(current_matrix_all, np.array([list(map(int, values[i+2*Resources+Processes].split()))]), axis=0)

#calculate the need matrix
need_matrix_all = np.subtract(maximum_matrix_all, current_matrix_all)

#store the matrices
reserved_available_resources_matrix = np.copy(available_resources_matrix)
reserved_current_matrix_all = np.copy(current_matrix_all)
reserved_need_matrix_all = np.copy(need_matrix_all)


layout = [[sg.Text('Step 3: Enter your request', font=("Helvetica", 15))],
                [sg.Text('Process number',size=(15,1)), sg.InputCombo(list(range(1, Processes+1)), size=(20, 1))],
                [sg.Text('Resource number',size=(15,1)), sg.InputCombo(list(range(1, Resources+1)), size=(20, 1))],
                [sg.Text('Request',size=(15,1)), sg.Slider(range=(1, 100), orientation='h',size = (20,10), default_value=0)],
                [sg.Button('Check')]]

window = sg.Window('Banker\'s Algorithm', layout)

while True:
   
   event, values = window.read()
   #store the process number
   proc_num = int(values[0])
   #store the resource number
   res_num = int(values[1])
   #store the request
   req = int(values[2])

   proc_num = proc_num - 1
   res_num = res_num - 1

   if event == 'Check':
       #store the process number
       proc_num = int(values[0])
       #store the resource number
       res_num = int(values[1])
       #store the request
       req = int(values[2])

       proc_num = proc_num - 1
       res_num = res_num - 1
       
       if req <= available_resources_matrix[0][res_num]:
          
          available_resources_matrix[0][res_num] = available_resources_matrix[0][res_num] - req
          current_matrix_all[proc_num][res_num] = current_matrix_all[proc_num][res_num] + req
          need_matrix_all[proc_num][res_num] = need_matrix_all[proc_num][res_num] - req

          available_resources_matrix_after_request = np.copy(available_resources_matrix)

          break
       else:
          #display a message that the request is not granted
          sg.popup('Error: The request is bigger than the available resources')
          continue

sg.popup('The request maybe granted \n press ok to simulate')
window.close()


#progress bar per process
layout = [[sg.Text('Step 5: Simulation', font=("Helvetica", 15))],
                [sg.Text('Total number of each resource', font=("Helvetica", 10)), 
                sg.Text('Available number of each resource', font=("Helvetica", 10))],
                [sg.Text(total_resources_matrix,size=(20,1),justification='center'), sg.Text(available_resources_matrix,size=(25,1),justification='center')],
                [sg.Text('Maximum need', font=("Helvetica", 10),size=(20,1),justification = 'left'), sg.Text('Currently allocated', font=("Helvetica", 10),size=(18,1),justification='center')],
                [sg.Text(maximum_matrix_all,size=(20,Processes),justification='center'),
                 sg.Text(current_matrix_all,size=(25,Processes),justification='center')],
                [sg.Text('Need matrix', font=("Helvetica", 10))],
                [sg.Text(need_matrix_all,size=(20,Processes),justification='center')]]
layout.append([sg.Text('Progress bar for each process', font=("Helvetica", 15))])
for i in range(Processes):
        layout.append([sg.Text('Process'+str(i+1)),sg.ProgressBar(100, orientation='h', size=(20, 20), key='progbar'+str(i))])
layout.append([sg.Button('Lets go!'), sg.Button('Done!')])


window = sg.Window('Banker\'s Algorithm', layout)
event, values = window.read()


check = np.full((1, Resources), -1)
check_w = np.full((Processes, Resources), -1)

#breaks when all processes are safe
event, values = window.read()

while True:
        event, values = window.read()
        if event == 'Lets go!':
                count = 0
                itr = 0
                while ((need_matrix_all.all() != check_w.all())):
                        i = 0
                        for i in range (Processes):
                                if (need_matrix_all[i] == check).all():
                                        sg.popup("Process "+str(i+1)+" is safe")
                                        continue
                                else:
                                        if (need_matrix_all[i] <= available_resources_matrix).all():
                                                window['progbar'+str(i)].update_bar(100)
                                                window.refresh()
                                                available_resources_matrix = np.add(available_resources_matrix, current_matrix_all[i])
                                                need_matrix_all[i] = -1
                                                sg.popup(" Enough available resources \n Resources of process " + str(i+1) + " are released \n Available resources are updated!")
                                                continue
                                        else:
                                                sg.popup(" Process "+ str(i+1)+" might be unsafe \n lack of available resources")
                                                itr = itr + 1
                                                continue  

                        #if all processes are unsafe
                        if (itr == Processes):
                                sg.popup("Deadlock. \n System is in an unsafe state")
                                break

                        #if some processes are safe and others are unsafe
                        count = count + 1
                        if (count == Processes):
                                break
        else :
                break

window.close()


if (available_resources_matrix.all() == total_resources_matrix.all()):
   layout = [[sg.Text(' Congratulations! \n System is in a safe state', font=("Helvetica", 15))],
             [sg.Text('Available resources', font=("Helvetica", 10)), sg.Text(available_resources_matrix_after_request,size=(32,1),justification='center')],
             [sg.Text('Currently allocated', font=("Helvetica", 10),size=(18,1),justification='left'),
              sg.Text(current_matrix_all,size=(25,Processes),justification='center')]]
   window = sg.Window('Banker\'s Algorithm', layout)
   event, values = window.read()
   window.close()
   
else:
     layout = [[sg.Text(' Deadlock :( \n System is in an unsafe state.', font=("Helvetica", 15))], 
               [sg.Text('Available resources', font=("Helvetica", 10)),sg.Text(reserved_available_resources_matrix,size=(32,1),justification='center')],
               [sg.Text('Currently allocated', font=("Helvetica", 10),size=(18,1),justification='left'),
               sg.Text(reserved_current_matrix_all,size=(25,Processes),justification='center')]]   
     window = sg.Window('Banker\'s Algorithm', layout)
     event, values = window.read()
     window.close()








      



















