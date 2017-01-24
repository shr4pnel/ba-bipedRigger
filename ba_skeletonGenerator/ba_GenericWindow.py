'''
Created on 3 Jan 2017

@author: BenjiA
'''
import maya.cmds as cmds


class ba_optionsWindow(object):

    @classmethod
    def showUI(cls):
        win = cls()
        win.create()
        return win

    def __init__(self):
        self.window = 'ba_optionsWindow'
        self.title = 'Options Window'
        self.size = (546, 350)
        self.supportsToolAction = False
        self.actionName = 'Apply and Close'
        self.applyBtnName = 'Apply'

    def create(self):
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window, window=True)
        self.window = cmds.window(
            self.window,
            title=self.title,
            widthHeight=self.size,
            menuBar=True
        )
        self.mainForm = cmds.formLayout(nd=100)
        self.commonMenu()
        self.commonButtons()
        self.optionsBorder = cmds.tabLayout(
            scrollable=True,
            tabsVisible=False,
            height=1
        )
        cmds.formLayout(
            self.mainForm, e=True,
            attachForm=(
                [self.optionsBorder, 'top', 0],
                [self.optionsBorder, 'left', 2],
                [self.optionsBorder, 'right', 2]
            ),
            attachControl=(
                [self.optionsBorder, 'bottom', 5, self.applyBtn]
            )
        )
        self.optionsForm = cmds.formLayout(nd=100)
        self.displayOptions()
        cmds.showWindow()

    def commonMenu(self):
        self.editMenu = cmds.menu(label='Edit')
        self.editMenuSave = cmds.menuItem(
            label='Save Settings'
        )
        self.editMenuReset = cmds.menuItem(
            label='Reset Settings'
        )
        self.editMenuDiv = cmds.menuItem(d=True)
        self.editMenuRadio = cmds.radioMenuItemCollection()
        self.editMenuTool = cmds.menuItem(
            label='As Tool',
            radioButton=True,
            enable=self.supportsToolAction
        )
        self.editMenuAction = cmds.menuItem(
            label='As Action',
            radioButton=True,
            enable=self.supportsToolAction
        )
        self.helpMenu = cmds.menu(label='Help')
        self.helpMenuItem = cmds.menuItem(
            label='Help on %s' % self.title,
            command=self.helpMenuCmd
        )

    def commonButtons(self):
        self.commonBtnSize = ((self.size[0] - 18) / 3, 26)
        self.actionBtn = cmds.button(
            label=self.actionName,
            height=self.commonBtnSize[1],
            command=self.actionBtnCmd
        )
        self.applyBtn = cmds.button(
            label=self.applyBtnName,
            height=self.commonBtnSize[1],
            command=self.applyBtnCmd
        )
        self.closeBtn = cmds.button(
            label='Close',
            height=self.commonBtnSize[1],
            command=self.closeBtnCmd
        )
        cmds.formLayout(
            self.mainForm, e=True,
            attachForm=(
                [self.actionBtn, 'left', 5],
                [self.actionBtn, 'bottom', 5],
                [self.applyBtn, 'bottom', 5],
                [self.closeBtn, 'bottom', 5],
                [self.closeBtn, 'right', 5],
            ),
            attachPosition=(
                [self.actionBtn, 'right', 1, 33],
                [self.closeBtn, 'left', 0, 67],
            ),
            attachControl=(
                [self.applyBtn, 'left', 4, self.actionBtn],
                [self.applyBtn, 'right', 4, self.closeBtn]
            ),
            attachNone=(
                [self.actionBtn, 'top'],
                [self.applyBtn, 'top'],
                [self.closeBtn, 'top']
            )
        )

    def helpMenuCmd(self, *args):
        cmds.launch(web='http://maya-python.com')

    def editMenuSaveCmd(self, *args): pass

    def editMenuResetCmd(self, *args): pass

    def editMenuToolCmd(self, *args): pass

    def editMenuActionCmd(self, *args): pass

    def actionBtnCmd(self, *args):
        self.applyBtnCmd()
        self.closeBtnCmd()

    def applyBtnCmd(self, *args): pass

    def closeBtnCmd(self, *args):
        cmds.deleteUI(self.window, window=True)

    def displayOptions(self): pass
    
    
'''
Created on 10 Jan 2017

@author: BenjiA

Class for the UI of ba_autoRigger
'''
import pymel.core as pm


class ba_autoRiggerWindow(object):

    @classmethod
    def showUI(cls):
        win = cls()
        win.create()
        return win

    def __init__(self):
        self.window = 'ba_autoRiggerWindow'
        self.title = 'ba_autoRigger'
        self.size = (300, 231)

    def create(self):
        if(pm.window(self.window, exists=True)):
            pm.deleteUI(self.window, window=True)
        # initialize the window
        self.window = pm.window(
            self.window, title=self.title, wh=self.size, s=0)
        # main form layout
        self.mainForm = pm.formLayout()

        # Locator area --------------------------------------------------------
        # frame for locator generation
        self.locatorFrame = pm.frameLayout(l='Locators', collapsable=1)
        # form layout inside of frame
        self.locatorForm = pm.formLayout()
        # TODO: hook up locator generation to this button
        self.genLoc = pm.button(
            l='Generate Locators', c=self.generateLocatorsBtn, h=32)
        # attach controls in the locator form
        af = []
        af.append([self.genLoc, 'top', 1])
        af.append([self.genLoc, 'left', 2])
        af.append([self.genLoc, 'right', 2])
        af.append([self.genLoc, 'bottom', 1])
        pm.formLayout(
            self.locatorForm, e=True,
            attachForm=af
        )

        # Skeleton area -------------------------------------------------------
        # frame for skeleton generation
        pm.setParent(self.mainForm)
        self.skeletonFrame = pm.frameLayout(l='Skeleton', collapsable=1)
        # skeleton form
        self.skeletonForm = pm.formLayout()
        # TODO: hook up skeleton generation to this button
        self.genSkel = pm.button(
            l='Generate Skeleton', c=self.generateSkeletonBtn, h=32)
        pm.setParent(self.skeletonForm)
        # skeleton modifiers frame
        self.skelModFrame = pm.frameLayout(l='Skeleton Options', collapsable=1)
        self.skelModForm = pm.formLayout()
        # int field for specifying number of spine joints
        self.spineText = pm.text(label='Number of spine joints: ')
        self.spineIntField = pm.intField(ann='Number of spine joints', min=1, v=4)
        # skeleton modifer checkboxes
        self.skelModRadio = pm.checkBoxGrp(
            labelArray3=[
                'Reverse Foot',
                'Wrist Twists',
                'IK/FK'
            ],
            numberOfCheckBoxes=3
        )
        af=[]
        ac=[]
        ac.append([self.spineIntField, 'left', 1, self.spineText])
        ac.append([self.skelModRadio, 'top', 4, self.spineText])
        af.append([self.spineText, 'top', 4])
        af.append([self.spineText, 'left', 3])
        af.append([self.skelModRadio, 'left', 2])
        af.append([self.spineIntField, 'top', 1])
        pm.formLayout(
            self.skelModForm, e=True,
            attachControl=ac,
            attachForm=af
        )
        
        af = []
        ac = []
        ac.append([self.skelModFrame, 'top', 1, self.genSkel])
        af.append([self.skelModFrame, 'right', 2])
        af.append([self.skelModFrame, 'left', 5])
        af.append([self.genSkel, 'top', 1])
        af.append([self.genSkel, 'left', 2])
        af.append([self.genSkel, 'right', 2])
        pm.formLayout(
            self.skeletonForm, e=True,
            attachControl=ac,
            attachForm=af
        )

        # Control rig area ----------------------------------------------------
        # frame for control rig generation
        pm.setParent(self.mainForm)
        self.controlFrame = pm.frameLayout(l='Control Rig', collapsable=1)
        # form layout for control rig
        self.controlForm = pm.formLayout()
        # control rig generation button
        self.genControl = pm.button(
            l='Generate Control Rig', c=self.generateControlRigBtn, h=32)
        af = []
        af.append([self.genControl, 'top', 1])
        af.append([self.genControl, 'left', 2])
        af.append([self.genControl, 'right', 2])
        pm.formLayout(
            self.controlForm, e=True,
            attachForm=af
        )

        # attach frames to main form
        ac = []
        af = []
        ac.append([self.skeletonFrame, 'top', 0, self.locatorFrame])
        ac.append([self.controlFrame, 'top', 0, self.skeletonFrame])
        af.append([self.locatorFrame, 'top', 0])
        af.append([self.locatorFrame, 'left', 0])
        af.append([self.locatorFrame, 'right', 0])
        af.append([self.skeletonFrame, 'left', 0])
        af.append([self.skeletonFrame, 'right', 0])
        af.append([self.controlFrame, 'bottom', 0])
        af.append([self.controlFrame, 'left', 0])
        af.append([self.controlFrame, 'right', 0])
        pm.formLayout(
            self.mainForm, e=True,
            attachControl=ac,
            attachForm=af
        )

        # show the window
        pm.showWindow(self.window)
        # force window size
        pm.window(self.window, e=True, wh=self.size)

    def generateLocatorsBtn(self, *args):
        print 'Generate Locators'

    def generateSkeletonBtn(self, _numSpineJts, *args):
        print 'Generate Skeleton'

    def generateControlRigBtn(self, *args):
        print 'Generate Control Rig'
