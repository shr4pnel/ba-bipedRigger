# ba-bipedRigger
## Bipedal Humanoid Autorigger

###### DISCLAIMER: 

This tool is presented in an as-is state, it is a work in progress and total functionality is not yet guaranteed. If you have problems I will do my best to address them, but I guarantee nothing. See 'LICENSE' for further details.

###### SCOPE: 

A functional bipedal autorigger that generates a clean, correctly oriented rig from user placed locators. The user has the option to generate IK/FK controls, reverse foot setups, limb twist setups.
There is a small UI in which the controls and options are displayed and buttons for executing functions.

###### INSTALLATION: 


Drag ba_GenericWindow.py and ba_skeletonGenerator.py into your Users/user/Documents/maya/version/scripts directory. Import the module and call showUI()

###### INSTRUCTIONS:


Open the UI and press 'Generate Locators' under the 'Locators' header to create the locators that the tool will use for generating the skeleton. The locators are named logically and correspond to key parts of the body.
Note: Only the locators for the right half of the body are generated as the tool mirrors the skeleton that it creates from these locators.
The 'Skeleton' section contains a 'Skeleton Options' section in which the user can specify whether or not they want to include modifiers such as reverse foot, wrist twists and IK/FK switching, and additionally they can specify the number of joins for the spine.
The 'Control Rig' section contains the 'Generate Control Rig' button, which is used for generating the control rig on top of the skeleton.
