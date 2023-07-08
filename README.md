# Predator-AI
Predator AI is a program that identifies Texas-specific wildlife threats in images and notifies the program user. The program’s functions as an alert system to be used with (non-live feed) security/surveillance cameras to ensure the safety of young children and vulnerable pets when not being supervised. The program is able to detect cougars, coyotes,  various subspecies of foxes common in Texas, alligators, and rattlesnakes in provided input images.


## Algorithm
This program utilizes the pretrained GoogleNet model to classify specified objects found in the input image, find and store the object’s description, and determine and return whether or not a threat has been found (and identify the type of threat if found) based on the classified object’s description.


## Reproducing the Project
### Requirements:
- Jetson Nano
- USB to MicroUSB cable (to connect the Nano to your computer)
- USBC power supply
- Ethernet cable OR USB Wi-Fi adapter and USB extension cord
- PuTTY (must be able to SSH in)
- Visual Studio Code (must be able to SSH in)

### Steps
1. SSH into PuTTY, using the appropriate ip address for your Jetson Nano. If done correctly, you will be prompted to “login as: ”; enter in the username “nvidia”. When prompted for your password, enter it in (keep in mind that the window will not display your password as you type)
2. Install git and cmake by running the commands “sudo apt-get update” and “sudo apt-get install git cmake” separately. (You will be prompted to enter your password)
3. Clone the jetson-inference project by entering “git clone --recursive https://github.com/dusty-nv/jetson-inference”  then enter “cd jetson-inference” followed by “git submodule update --init”
4. Install the python packages and GoogleNet by running the command “sudo apt-get install libpython3-dev python3-numpy” (this command might take a while to finish running)
5. Once finished loading, you should be able to see the command line. Navigate to the jetson-inference directory by running the command “cd \~/jetson-inference” If successful, your command line should have changed “/home” into “~/jetson-inference”
6. Make a build directory by running the command “mkdir build”, then change directories into build by running “cd build”
7. Run make to build the project by running the command “cmake ../” (this command might take a while to finish running)
8. The PuTTY screen will flash to the PyTorch Installer; since you don’t need to install PyTorch, press the spacebar to deselect any selected (starred) PyTorch installation options. (this step might take a while to finish running)
9. After finishing loading, the command line should appear once again. Confirm that you are still in the build directory (if not, refer to step 6). Run the commands “make”,  “sudo make install” and “sudo ldconfig” separately. Once finished, you will be able to run PredatorAI.
10. Download the “predator_AI.py” file, you should be able to see this file in the "Downloads" folder in your file explorer once finished.
11. SSH into Visual Studio Code (enter in your password when prompted) and navigate to the home folder by clicking “File” then “Open Folder” and type “home”, click home in the dropdown menu, enter your password if prompted.
    
     ![home folder](https://github.com/DiaMak-2109/predator-AI/assets/72892433/620de963-63f5-4174-8d00-9d77965ca6e3)

12.  In the Explorer tab (to the left of the VSCode screen) click on the “nvidia” folder to select it (this is where you will move predator_AI.py), then hover over the “HOME [SSH: #############]” folder and click the new folder icon (second icon) and name the folder “predator_AI”

     ![create folder](https://github.com/DiaMak-2109/predator-AI/assets/72892433/4123c5c5-4de4-4d66-9a1a-c9aaa8c931bc)

13. Move the predator_AI.py program from your local computer to the Jetson Nano: Open file explorer on your computer (use the search feature) and navigate to the location where predator_AI.py is located, then drag the predator_AI.py file into the predator_AI folder you created in VSCode
14. Open a new terminal by clicking  “Terminal” then “New Terminal” in the dropdown menu. The command line should show that you are already in the home directory, if not type “cd /home” and press enter to navigate to the directory. Then run the command “cd ~/predator_AI” to navigate to the predator_AI folder
15. Use a browser to search for an image of your liking. Select the image and right click, then select “copy image address”
16. Download the image into the predator_AI folder by running the command “wget ‘image address’”, replacing ‘image address’ with the image address copied to your clipboard (make sure to enclose the address with quotations). You should see a loading bar of the  download progress of the image. Once complete, you should be able to view the command line; the downloaded image will also appear as a file in the predator_AI folder.

      ![wget](https://github.com/DiaMak-2109/predator-AI/assets/72892433/eadf62a5-eaf4-4587-b288-b1ec8375f9cf)
      
17. Run the program: Select and copy the image name embedded in quotations (example: ‘aedafb098a0eb409b689d9d488f21cbce0-koala.jpg’ in the image below) in the last output line and paste it at the end of the command “python3 predator_AI.py “ (make sure to embed the address in quotes after pasting) to run the program on the image of your choice. Below is an example of what the command should look like.
    
      ![run program](https://github.com/DiaMak-2109/predator-AI/assets/72892433/9483a266-67d8-4898-a4c1-4fa5c3d7eeb3)

18. To run the program on other images, repeat steps 15-17

## Model Information
Googlnet is the default pretrained [image classification/recognition](https://github.com/dusty-nv/jetson-inference/blob/master/docs/imagenet-console-2.md) network that impliments the [imageNet](https://rawgit.com/dusty-nv/jetson-inference/master/docs/html/python/jetson.inference.html#imageNet) class. It can be used to classify objects within images, videos, and live camera feeds.

