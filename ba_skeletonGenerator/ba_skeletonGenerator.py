import pymel.core as pm
from ba_GenericWindow import ba_autoRiggerWindow


class ba_skeletonGenerator(ba_autoRiggerWindow):
    
    spineLocators = []
    armLocators = []
    handLocators = []
    legLocators = []
    spineJoints = []
    footLocators = []
    loc_head = None
    r_hand = []
    r_thumbJoints = []
    r_indexJoints = []
    r_midJoints = []
    r_ringJoints = []
    r_pinkyJoints = []

    def __init__(self):
        ba_autoRiggerWindow.__init__(self)

    def generateSkeleton(self, _numSpineJts, *args):
        self.generateSpine(_numSpineJts)
        self.generateArms()
        self.revFoot = False
        if pm.checkBoxGrp(self.skelModRadio, q=1, value1=1):
            self.revFoot = True        
        self.generateLegs(self.revFoot)
        self.generateHead()
        self.generateHands()

    def generateLocators(self, *args):
        if len(self.spineLocators) > 0:
            del self.spineLocators[:]
        if len(self.armLocators) > 0:
            del self.armLocators[:]
        if len(self.legLocators) > 0:
            del self.legLocators[:]
        if len(self.footLocators) > 0:
            del self.footLocators[:]
        # Spine locators
        self.loc_spine01 = pm.spaceLocator(p=[-2, 15, 1])
        pm.rename(self.loc_spine01, 'loc_neck')
        pm.xform(cp=1)
        self.spineLocators.append(self.loc_spine01)
        self.loc_spine02 = pm.spaceLocator(n='loc_hips', p=[-2, 2, 1])
        self.spineLocators.append(self.loc_spine02)
        pm.xform(cp=1)
        # Right arm locators
        self.loc_r_clav = pm.spaceLocator(n='loc_r_clav', p=[1, 15, 4])
        self.armLocators.append(self.loc_r_clav)
        pm.xform(cp=1)
        self.loc_r_shoulder = pm.spaceLocator(n='loc_r_shoulder', p=[0, 15, 6])
        self.armLocators.append(self.loc_r_shoulder)
        pm.xform(cp=1)
        self.loc_r_elbow = pm.spaceLocator(n='loc_r_elbow', p=[-1, 15, 13])
        self.armLocators.append(self.loc_r_elbow)
        pm.xform(cp=1)
        self.loc_r_wrist = pm.spaceLocator(n='loc_r_wrist', p=[0, 15, 19])
        self.armLocators.append(self.loc_r_wrist)
        pm.xform(cp=1)
        # Right hand locators
        self.loc_r_hand = pm.spaceLocator(n='loc_r_hand', p=[0, 15, 19])
        self.handLocators.append(self.loc_r_hand)
        pm.xform(cp=1)
        self.loc_r_thumbRoot = pm.spaceLocator(n='loc_r_thumbRoot', p=[0, 16, 20])
        self.handLocators.append(self.loc_r_thumbRoot)
        pm.xform(cp=1)
        self.loc_r_thumbEnd = pm.spaceLocator(n='loc_r_thumbEnd', p=[0, 16, 22])
        self.handLocators.append(self.loc_r_thumbEnd)
        pm.xform(cp=1)
        self.loc_r_indexRoot = pm.spaceLocator(n='loc_r_indexRoot', p=[0, 15.5, 21])
        self.handLocators.append(self.loc_r_indexRoot)
        pm.xform(cp=1)
        self.loc_r_indexEnd = pm.spaceLocator(n='loc_r_indexEnd', p=[0, 15.5, 23])
        self.handLocators.append(self.loc_r_indexEnd)
        pm.xform(cp=1)
        self.loc_r_midRoot = pm.spaceLocator(n='loc_r_midRoot', p=[0, 15, 21.5])
        self.handLocators.append(self.loc_r_midRoot)
        pm.xform(cp=1)
        self.loc_r_midEnd = pm.spaceLocator(n='loc_r_midEnd', p=[0, 15, 23.5])
        self.handLocators.append(self.loc_r_midEnd)
        pm.xform(cp=1)
        self.loc_r_ringRoot = pm.spaceLocator(n='loc_r_ringRoot', p=[0, 14.5, 21])
        self.handLocators.append(self.loc_r_ringRoot)
        pm.xform(cp=1)
        self.loc_r_ringEnd = pm.spaceLocator(n='loc_r_ringEnd', p=[0, 14.5, 23])
        self.handLocators.append(self.loc_r_ringEnd)
        pm.xform(cp=1)
        self.loc_r_pinkyRoot = pm.spaceLocator(n='loc_r_pinkyRoot', p=[0, 14, 21])
        self.handLocators.append(self.loc_r_pinkyRoot)
        pm.xform(cp=1)
        self.loc_r_pinkyEnd = pm.spaceLocator(n='loc_r_pinkyEnd', p=[0, 14, 22.5])
        self.handLocators.append(self.loc_r_pinkyEnd)
        pm.xform(cp=1)
        # Right leg locators ---------------------------------------------------
        self.loc_r_hip = pm.spaceLocator(n='loc_r_hip', p=[-2, -1, 6])
        self.legLocators.append(self.loc_r_hip)
        pm.xform(cp=1)
        self.loc_r_knee = pm.spaceLocator(n='loc_r_knee', p=[1, -11, 6])
        self.legLocators.append(self.loc_r_knee)
        pm.xform(cp=1)
        self.loc_r_ankle = pm.spaceLocator(n='loc_r_ankle', p=[-2, -21, 6])
        self.legLocators.append(self.loc_r_ankle)
        pm.xform(cp=1)
        # Right foot locators
        self.loc_r_toeBase = pm.spaceLocator(n='loc_r_toeBase', p=[1, -22, 6])
        self.footLocators.append(self.loc_r_toeBase)
        pm.xform(cp=1)
        self.loc_r_toeEnd = pm.spaceLocator(n='loc_r_toeEnd', p=[3, -22, 6])
        self.footLocators.append(self.loc_r_toeEnd)
        pm.xform(cp=1)
        # Head locator
        self.loc_head = pm.spaceLocator(n='loc_head', p=[-2, 17, 1])
        pm.xform(cp=1)
        
    def generateControlRig(self, *args):
        self.generateHipCtrls()
        self.ikfk = False
        if pm.checkBoxGrp(self.skelModRadio, q=1, value1=3):
            self.ikfk = True
        self.generateCtrls(self.hip_ctrl[0], self.l_legJoints[0:3], 'l', 
                           self.l_leg_ikHandle[0], self.l_footCtrl[0], self.ikfk)
        self.generateCtrls(self.hip_ctrl[0], self.r_legJoints[0:3], 'r', 
                           self.r_leg_ikHandle[0], self.r_footCtrl[0], self.ikfk)
        self.generateShoulderCtrls()
        self.generateHandControls()
        # TODO unfuck this shit:
        # top arms arent generating the hand control properly,
        # or theyre not constraining to the IK properly, investigate 
        self.generateCtrls(self.shoulder_ctrl[0], self.l_armJoints[1:4], 'l', 
                           self.l_arm_ikHandle[0], self.l_hand_ctrl, self.ikfk) 
        self.generateCtrls(self.shoulder_ctrl[0], self.r_armJoints[1:4], 'r', 
                           self.r_arm_ikHandle[0], self.r_hand_ctrl, self.ikfk) 
        
        for i in self.r_leg_ikHandle:
            print i
        for i in self.r_arm_ikHandle:
            print i

# Utility methods -------------------------------------------------------------
    def distanceBetween(self, _objA, _objB):
        # pass this a 3 vector list
        Ax, Ay, Az = _objA
        Bx, By, Bz = _objB
        return ((Ax - Bx)**2 + (Ay - By)**2 + (Az - Bz)**2)**0.5

    def aimAt(self, _target, _source):
        aimConst = pm.aimConstraint(_source, _target)
        pm.delete(aimConst)
        rotVal = _source.rotate.get()
        _source.jointOrient.set(rotVal)
        _source.r.set([0, 0, 0])
        
    def createAlignedControl(self, _handedness, _joint, _name, _offsetXYZ = [0,90,0], _scaleMultiplier = 3):
        #TODO: lock and hide all attrs on the LocAlign_ locators after generation is done
        jPos = pm.PyNode(_joint).getTranslation(space='world')
        loc = pm.spaceLocator(n='LocAlign_'+_handedness+'_'+_name+'_ctrl', p=jPos)
        pm.xform(loc, cp=1)
        oc = pm.orientConstraint(_joint, loc, mo=0)
        pm.delete(oc)
        ctrl = pm.circle(n=_handedness+'_'+_name+'_ctrl', 
                            c=pm.PyNode(_joint).getTranslation(space='world'))
        ctrlShape = pm.listRelatives(ctrl)
        ctrlTrans = pm.listRelatives(ctrlShape, p=1)
        locShape = pm.listRelatives(loc)
        locTrans = pm.listRelatives(locShape, p=1)
        pm.hilite(ctrl)
        pm.parent(ctrlTrans, locTrans, r=0)
        pm.xform(ctrl, cp=1)
        locTrans[0].t.set([0,0,0])
        pm.select(ctrl[0]+'.cv[0:'+str(len(ctrl[0]+'.cv'))+']')
        ctrl[0].rotate.set([0,0,0])
        rad = pm.PyNode(_joint).getRadius()
        pm.xform(ro=(_offsetXYZ), s=(int(rad) * _scaleMultiplier, int(rad) * _scaleMultiplier, int(rad) * _scaleMultiplier))
        pm.makeIdentity(a=1, t=1)
        return ctrl    
#  -----------------------------------------------------------------------------

    def generateSpine(self, _numJoints):
        # TODO: fix the spine joints orienting in the opposite direction
        self.spineJoints = []
        # Generate spine bones -----------------------------------------------
        for i in self.spineLocators:
            delta = i.t.get()
            trans = i.localPosition.get()
            self.spineJoints.append(pm.joint(p=(trans+delta)))
            pm.parent(w=1)
            split = self.spineLocators[
                self.spineLocators.index(i)].split('loc')
            pm.rename(
                self.spineJoints[self.spineLocators.index(i)], 'bind' + split[1])
        # Calculate aim vector and distance between root and end ---------------
        j1Trans = self.spineJoints[0].t.get()
        j2Trans = self.spineJoints[-1].t.get()
        spineAim = pm.datatypes.Vector(j1Trans - j2Trans)
        spineAim.normalize()
        spineLength = self.distanceBetween(j1Trans, j2Trans)
        i = 1
        jtParent = self.spineJoints[1]
        # Create middle joints and orient --------------------------------------
        while i < _numJoints:
            p = spineLength / _numJoints
            val = j2Trans + (spineAim * (p * i))
            newJt = pm.joint(n='bind_spine0' + str(i), p=val)
            spineChain = []
            spineChain.append(newJt)
            self.aimAt(newJt, jtParent)
            pm.parent(newJt, jtParent)
            jtParent = newJt
            i += 1
        # Parent joints --------------------------------------------------------
        pm.parent(self.spineJoints[0], spineChain[-1])
        self.spineJoints[0].jointOrient.set([0, 0, 0])
        for i in spineChain:
            self.spineJoints.append(i)
        delta = self.spineLocators[1].t.get()
        trans = self.spineLocators[1].localPosition.get()
        hipsRotate = pm.joint(n='jDrv_hipsRotate', p=(trans+delta))
        self.spineJoints.append(hipsRotate)
        pm.parent(hipsRotate, self.spineJoints[1])

    def generateHead(self):
        delta = self.loc_head.t.get()
        trans = self.loc_head.localPosition.get()
        self.headJoint = pm.joint(p=(trans+delta), n='bind_head')
        pm.parent(self.headJoint, self.spineJoints[0])
        self.headJoint.jointOrient.set([0, 0, 0])

    def generateLimb(self, _limbSide, _limbName, _limbLocators, _limbJtArray, _rootJt, _mirror = True, _prefix = 'bind'):
        # Pass this the name of the limb, eg. 'r_arm'
        # Pass it the list of locators created for that limb
        # Pass it an empty list, and it will add that limbs bones to the list
        # Generate limb bones -------------------------------------------------
        for i in _limbLocators:
            delta = i.t.get()
            trans = i.localPosition.get()
            splitLocName = str(_limbLocators[_limbLocators.index(i)])[3:]
            newJt = pm.joint(
                p=(trans+delta), n=_prefix + splitLocName)
            _limbJtArray.append(newJt)
            pm.parent(w=1)
        # Orient limb bones --------------------------------------------------
        i = 0
        while i < len(_limbJtArray):
            if i < len(_limbJtArray) - 1:
                # TODO: work out why the reorienting shit doesn't work in the
                # aimAt method
                _limbJtArray[i].jointOrient.set([0, 0, 0])
                self.aimAt(_limbJtArray[i], _limbJtArray[i + 1])
                rotVal = _limbJtArray[i].rotate.get()
                _limbJtArray[i].jointOrient.set(rotVal)
                _limbJtArray[i].r.set([0, 0, 0])
            else:
                _limbJtArray[i].jointOrient.set([0, 0, 0])
            i = i + 1
        # Parent the joints ---------------------------------------------------
        j = 0
        while j < len(_limbJtArray):
            if j < len(_limbJtArray) - 1:
                pm.parent(_limbJtArray[j + 1], _limbJtArray[j])
            j = j + 1
        pm.parent(_limbJtArray[0], _rootJt)
        _limbJtArray[-1].jointOrient.set([0, 0, 0])
        if _mirror:
            pm.mirrorJoint(
                 _limbJtArray[0], mb=1, mxy=1, sr=('_r_', '_' + _limbSide + '_'))

    def generateArms(self):
        self.r_armJoints = []
        self.generateLimb(
            'l', 'r_arm', self.armLocators, self.r_armJoints, self.spineJoints[2], False)

    def generateLegs(self, _revFoot = False):
        self.r_legJoints = []
        self.generateLimb(
            'l', 'r_leg', self.legLocators, self.r_legJoints, self.spineJoints[len(self.spineJoints)-1], False)
        self.r_footJoints = []
        self.generateLimb(
            'l', 'r_foot', self.footLocators, self.r_footJoints, self.r_legJoints[-1], False)
        l_legJoints_raw = pm.mirrorJoint(self.r_legJoints[0], mb=1, mxy=1, sr=('r_', 'l_'))
        i = 2
        self.l_legJoints = l_legJoints_raw[:i+1] 
        l_footJointsRaw = l_legJoints_raw[2+1:]
        self.l_footJoints = []
        for i in l_footJointsRaw:
            if pm.nodeType(i) == 'joint':
                self.l_footJoints.append(i)
        self.l_leg_ikHandle = pm.ikHandle(n='rp_l_ik', sj=self.l_legJoints[0], ee=self.l_legJoints[-1])
        self.r_leg_ikHandle = pm.ikHandle(n='rp_r_ik', sj=self.r_legJoints[0], ee=self.r_legJoints[-1])
        if _revFoot:
            self.r_revFootJoints = []
            self.r_footCtrl = self.generateReverseFoot('r', self.r_footJoints, self.r_legJoints, self.r_revFootJoints, self.r_leg_ikHandle[0])
            self.l_revFootJoints = []
            self.l_footCtrl = self.generateReverseFoot('l', self.l_footJoints, self.l_legJoints, self.l_revFootJoints, self.l_leg_ikHandle[0])
            pm.parent(self.r_revFootJoints[-1], self.r_footCtrl)
            pm.parent(self.l_revFootJoints[-1], self.l_footCtrl)
    
    def generateReverseFoot(self, _handedness, _footJoints, _legJoints, _revFootJoints, _ikHandle):
        jDrv_ankle = pm.duplicate(_legJoints[-1], po=1)
        _revFootJoints.append(jDrv_ankle[0])
        jDrv_toeBase = pm.duplicate(_footJoints[0], po=1)
        _revFootJoints.append(jDrv_toeBase[0])
        jDrv_toeEnd = pm.duplicate(_footJoints[1], po=1)
        _revFootJoints.append(jDrv_toeEnd[0])
        for i in _revFootJoints:
            i.rename(i.name().replace('bind_', 'jDrv_'))
            i.rename(i.name().replace('1', ' '))
            pm.parent(i, w=1)
        pm.parent(jDrv_toeEnd[0], jDrv_toeBase[0])
        pm.parent(jDrv_toeBase[0], jDrv_ankle[0])
        pm.reroot(jDrv_toeEnd[0])
        heelTrans = [pm.PyNode(_legJoints[-1]).getTranslation(space='world')[0], 
                      pm.PyNode(_footJoints[-1]).getTranslation(space='world')[1], 
                      pm.PyNode(_legJoints[-1]).getTranslation(space='world')[2]]
        jDrv_heel = pm.joint(n='jDrv_'+_handedness+'_heel', p=heelTrans)
        pm.parent(jDrv_heel, w=1)
        pm.orientConstraint(_revFootJoints[1], _legJoints[-1], mo=1)
        pm.orientConstraint(_revFootJoints[2], _footJoints[0], mo=1)
        pm.pointConstraint(_revFootJoints[0], _ikHandle, mo=0)
        pm.parent(_revFootJoints[-1], jDrv_heel)
        _revFootJoints.append(jDrv_heel)
        foot_ctrl = self.createAlignedControl(_handedness, _revFootJoints[-1], 'foot')
        pm.makeIdentity(foot_ctrl, a=1, t=1)
        revFoot_ctrls = []
        for i in _revFootJoints:
            ctrl = self.createAlignedControl(_handedness, i, str(i)[7:], [0,0,0], 2)
            revFoot_ctrls.append(ctrl)
            par = pm.listRelatives(ctrl, p=1)
            pm.parent(par, foot_ctrl)
            pm.orientConstraint(ctrl, i, mo=0)
        i = 0
        while i < len(revFoot_ctrls):
            if i < len(revFoot_ctrls) - 1:
                par = pm.listRelatives(revFoot_ctrls[i], p=1)
                pm.parent(par, revFoot_ctrls[i+1])                
            i = i + 1
        for i in revFoot_ctrls:
            pm.makeIdentity(i, a=1, t=1)
        return foot_ctrl
           
    def generateHands(self):
        self.r_hand = []
        self.r_thumbJoints = []
        self.r_indexJoints = []
        self.r_midJoints = []
        self.r_ringJoints = []
        self.r_pinkyJoints = []
        delta = self.loc_r_hand.t.get()
        localPos = self.loc_r_hand.localPosition.get()
        self.r_hand = pm.joint(p=delta+localPos, n='bind_r_hand')
        pm.parent(self.r_hand, self.r_armJoints[-1])
        self.r_thumbJoints = self.generateFinger(self.handLocators[1], self.handLocators[2], 'thumb', 'r', 1)
        self.r_indexJoints = self.generateFinger(self.handLocators[3], self.handLocators[4], 'index', 'r')
        self.r_midJoints = self.generateFinger(self.handLocators[5], self.handLocators[6], 'mid', 'r')
        self.r_ringJoints = self.generateFinger(self.handLocators[7], self.handLocators[8], 'ring', 'r')
        self.r_pinkyJoints = self.generateFinger(self.handLocators[9], self.handLocators[10], 'pinky', 'r')
        pm.parent(self.r_thumbJoints[0], self.r_hand)
        pm.parent(self.r_indexJoints[0], self.r_hand)
        pm.parent(self.r_midJoints[0], self.r_hand)
        pm.parent(self.r_ringJoints[0], self.r_hand)
        pm.parent(self.r_pinkyJoints[0], self.r_hand)
        self.r_arm_ikHandle = pm.ikHandle(n='ik_r_arm', sj=self.r_armJoints[1], ee=self.r_armJoints[3])
        self.l_armJoints = pm.mirrorJoint(self.r_armJoints[0], mb=1, mxy=1, sr=('_r_', '_l_'))
        self.l_arm_ikHandle = pm.ikHandle(n='ik_l_arm', sj=self.l_armJoints[1], ee=self.l_armJoints[3])
        self.l_hand = self.l_armJoints[4]
        
    def generateHandControls(self):
        self.l_hand_ctrl = self.createAlignedControl('l', self.l_hand, 'hand', [0,0,0], 3)
        pm.orientConstraint(self.l_hand_ctrl, self.l_hand)
        pm.pointConstraint(self.l_hand_ctrl, self.l_arm_ikHandle[0])
        self.r_hand_ctrl = self.createAlignedControl('r', self.r_hand, 'hand', [0,0,0], 3)
        pm.orientConstraint(self.r_hand_ctrl, self.r_hand)
        pm.pointConstraint(self.r_hand_ctrl, self.r_arm_ikHandle[0])
    
    def generateFinger(self, _rootLoc, _endLoc, _fingerName, _handedness, _numMidJoints = 2):
        fingerChain = []
        delta = _rootLoc.t.get()
        local = _rootLoc.localPosition.get()
        root = pm.joint(p=delta+local, n='bind_'+_handedness+'_'+_fingerName+'_root')
        pm.parent(root, w=1)
        fingerChain.append(root)
        delta = _endLoc.t.get()
        local = _endLoc.localPosition.get()
        end = pm.joint(p=delta+local, n='bind_'+_handedness+'_'+_fingerName+'_end')
        pm.parent(end, w=1)
        fingerAim = pm.datatypes.Vector(end.getTranslation() - root.getTranslation())
        fingerAim.normalize()
        fingerLength = self.distanceBetween(root.getTranslation(), end.getTranslation())
        positions = []
        p1 = fingerLength * 0.5
        positions.append(p1)
        p2 = fingerLength * 0.75
        positions.append(p2)
        names = ['mid', 'tip']
        i = 0
        while i < _numMidJoints:
            trans = root.getTranslation() + (fingerAim * (positions[i]))
            newJt = pm.joint(p=trans, n='bind_'+_handedness+'_'+_fingerName+'_'+names[i])
            pm.parent(newJt, w=1)
            fingerChain.append(newJt)
            i += 1
        fingerChain.append(end)
        i = 0
        while i < len(fingerChain):
            if i < len(fingerChain) - 1:
                # TODO: work out why the reorienting shit doesn't work in the
                # aimAt method
                fingerChain[i].jointOrient.set([0, 0, 0])
                self.aimAt(fingerChain[i], fingerChain[i + 1])
                rotVal = fingerChain[i].rotate.get()
                fingerChain[i].jointOrient.set(rotVal)
                fingerChain[i].r.set([0, 0, 0])
            else:
                fingerChain[i].jointOrient.set([0, 0, 0])
            i = i + 1
        j = 0
        while j < len(fingerChain):
            if j < len(fingerChain) - 1:
                pm.parent(fingerChain[j + 1], fingerChain[j])
            j = j + 1
        return fingerChain
    
    def generateHipCtrls(self):
        self.hip_ctrl = self.createAlignedControl('main', self.spineJoints[1], 'hip', [0,90,90], 6)
        extra_attrs_div = pm.addAttr(self.hip_ctrl[0], ln='ikfk_div', nn='-', at='enum', en='Xtra Attrs:', k=0, h=0)
        pm.setAttr(self.hip_ctrl[0]+'.ikfk_div', cb=1)
        l_ikfk_attr = pm.addAttr(self.hip_ctrl[0], ln='l_ikfk', nn='L Leg IK/FK', at='enum', en='IK:FK', k=1, h=0)
        r_ikfk_attr = pm.addAttr(self.hip_ctrl[0], ln='r_ikfk', nn='R Leg IK/FK', at='enum', en='IK:FK', k=1, h=0)
        hipsRotate_ctrl = self.createAlignedControl('main', self.spineJoints[-1], 'hipsRotate', [0,90,0], 5)
        hipsRot_cons = pm.orientConstraint(hipsRotate_ctrl[0], self.spineJoints[-1], mo=0)
        
    def generateShoulderCtrls(self):
        self.shoulder_ctrl = self.createAlignedControl('main', self.spineJoints[0], 'shoulder', [0,90,0], 7)
        extra_attrs_div = pm.addAttr(self.shoulder_ctrl[0], ln='ikfk_div', nn='-', at='enum', en='Xtra Attrs:', k=0, h=0)
        pm.setAttr(self.shoulder_ctrl[0]+'.ikfk_div', cb=1)
        l_ikfk_attr = pm.addAttr(self.shoulder_ctrl[0], ln='l_ikfk', nn='L Leg IK/FK', at='enum', en='IK:FK', k=1, h=0)
        r_ikfk_attr = pm.addAttr(self.shoulder_ctrl[0], ln='r_ikfk', nn='R Leg IK/FK', at='enum', en='IK:FK', k=1, h=0)
        pm.orientConstraint(self.shoulder_ctrl, self.spineJoints[-1-1], mo=0)
        print self.spineJoints[-1-1]
    
    def generateCtrls(self, _hierachyControl, _jointChain, _handedness, _ikHandle, _endCtrl, _ikfk = False):
        ctrls = []
        for i in _jointChain[0:2]:
            var = self.createAlignedControl(_handedness, i, str(i)[7:]+'_fk')
            oc = pm.orientConstraint(var, i, mo=0)
            ctrls.append(var)
            pm.makeIdentity(a=1, t=1)
            pm.connectAttr(_hierachyControl+'.'+_handedness+'_ikfk', oc.w0)
            pm.connectAttr(_hierachyControl+'.'+_handedness+'_ikfk', var[0]+'.visibility')
        j = 0
        while j < len(ctrls):
            if j < len(ctrls) - 1:
                par = pm.listRelatives(ctrls[j + 1], p=1)
                pm.parent(par, ctrls[j])                
            j = j + 1  
        for i in ctrls:
            pm.makeIdentity(a=1, t=1)
        if _ikfk:
            parCons = pm.parentConstraint(ctrls[1][0], _endCtrl, mo=1, w=0)
            ik_rev = pm.createNode('reverse', n=_hierachyControl+'_'+_handedness+'_ik_rev')
            pm.connectAttr(_hierachyControl+'.'+_handedness+'_ikfk', parCons.w0)
            pm.connectAttr(_hierachyControl+'.'+_handedness+'_ikfk', ik_rev+'.inputX')
            pm.connectAttr(ik_rev.outputX, _ikHandle.ikBlend)
        return ctrls
    
    # UI -----------------------------------------------------------------------
    def generateLocatorsBtn(self, *args):
        print 'Generate Locators'
        self.generateLocators()

    def generateSkeletonBtn(self, *args):
        print 'Generate Skeleton'
        numSpineJts = pm.intField(self.spineIntField, q=True, v=True)
        self.generateSkeleton(numSpineJts)

    def generateControlRigBtn(self, *args):
        print 'Generate Control Rig'
        self.generateControlRig()
        
ba_skeletonGenerator.showUI()