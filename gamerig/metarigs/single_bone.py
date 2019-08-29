import bpy


from mathutils import Color


def create(obj):
    # generated by gamerig.utils.write_metarig
    bpy.ops.object.mode_set(mode='EDIT')
    arm = obj.data

    arm.gamerig.rig_ui_template = 'ui_template'


    for i in range(6):
        arm.gamerig.colors.add()

    arm.gamerig.colors[0].name = "Root"
    arm.gamerig.colors[0].active = Color((0.5490196347236633, 1.0, 1.0))
    arm.gamerig.colors[0].normal = Color((0.4352940022945404, 0.18431399762630463, 0.4156860113143921))
    arm.gamerig.colors[0].select = Color((0.31372547149658203, 0.7843138575553894, 1.0))
    arm.gamerig.colors[0].standard_colors_lock = True
    arm.gamerig.colors[1].name = "IK"
    arm.gamerig.colors[1].active = Color((0.5490196347236633, 1.0, 1.0))
    arm.gamerig.colors[1].normal = Color((0.6039220094680786, 0.0, 0.0))
    arm.gamerig.colors[1].select = Color((0.31372547149658203, 0.7843138575553894, 1.0))
    arm.gamerig.colors[1].standard_colors_lock = True
    arm.gamerig.colors[2].name = "Special"
    arm.gamerig.colors[2].active = Color((0.5490196347236633, 1.0, 1.0))
    arm.gamerig.colors[2].normal = Color((0.9568629860877991, 0.7882350087165833, 0.04705899953842163))
    arm.gamerig.colors[2].select = Color((0.31372547149658203, 0.7843138575553894, 1.0))
    arm.gamerig.colors[2].standard_colors_lock = True
    arm.gamerig.colors[3].name = "Tweak"
    arm.gamerig.colors[3].active = Color((0.5490196347236633, 1.0, 1.0))
    arm.gamerig.colors[3].normal = Color((0.03921600058674812, 0.21176500618457794, 0.5803920030593872))
    arm.gamerig.colors[3].select = Color((0.31372547149658203, 0.7843138575553894, 1.0))
    arm.gamerig.colors[3].standard_colors_lock = True
    arm.gamerig.colors[4].name = "FK"
    arm.gamerig.colors[4].active = Color((0.5490196347236633, 1.0, 1.0))
    arm.gamerig.colors[4].normal = Color((0.11764699965715408, 0.5686269998550415, 0.035294000059366226))
    arm.gamerig.colors[4].select = Color((0.31372547149658203, 0.7843138575553894, 1.0))
    arm.gamerig.colors[4].standard_colors_lock = True
    arm.gamerig.colors[5].name = "Extra"
    arm.gamerig.colors[5].active = Color((0.5490196347236633, 1.0, 1.0))
    arm.gamerig.colors[5].normal = Color((0.9686279892921448, 0.2509799897670746, 0.09411799907684326))
    arm.gamerig.colors[5].select = Color((0.31372547149658203, 0.7843138575553894, 1.0))
    arm.gamerig.colors[5].standard_colors_lock = True

    for i in range(30):
        arm.gamerig.layers.add()

    arm.gamerig.layers[0].name = "Face"
    arm.gamerig.layers[0].row = 1
    arm.gamerig.layers[0].selset = False
    arm.gamerig.layers[0].group = 5
    arm.gamerig.layers[1].name = "Face (Primary)"
    arm.gamerig.layers[1].row = 2
    arm.gamerig.layers[1].selset = False
    arm.gamerig.layers[1].group = 2
    arm.gamerig.layers[2].name = "Face (Secondary)"
    arm.gamerig.layers[2].row = 2
    arm.gamerig.layers[2].selset = False
    arm.gamerig.layers[2].group = 3
    arm.gamerig.layers[3].name = "Torso"
    arm.gamerig.layers[3].row = 3
    arm.gamerig.layers[3].selset = False
    arm.gamerig.layers[3].group = 3
    arm.gamerig.layers[4].name = "Torso (Tweak)"
    arm.gamerig.layers[4].row = 4
    arm.gamerig.layers[4].selset = False
    arm.gamerig.layers[4].group = 4
    arm.gamerig.layers[5].name = "Fingers"
    arm.gamerig.layers[5].row = 5
    arm.gamerig.layers[5].selset = False
    arm.gamerig.layers[5].group = 6
    arm.gamerig.layers[6].name = "Fingers (Tweak)"
    arm.gamerig.layers[6].row = 6
    arm.gamerig.layers[6].selset = False
    arm.gamerig.layers[6].group = 4
    arm.gamerig.layers[7].name = "Arm.L (IK)"
    arm.gamerig.layers[7].row = 7
    arm.gamerig.layers[7].selset = False
    arm.gamerig.layers[7].group = 2
    arm.gamerig.layers[8].name = "Arm.L (FK)"
    arm.gamerig.layers[8].row = 8
    arm.gamerig.layers[8].selset = False
    arm.gamerig.layers[8].group = 5
    arm.gamerig.layers[9].name = "Arm.L (Tweak)"
    arm.gamerig.layers[9].row = 9
    arm.gamerig.layers[9].selset = False
    arm.gamerig.layers[9].group = 4
    arm.gamerig.layers[10].name = "Arm.R (IK)"
    arm.gamerig.layers[10].row = 7
    arm.gamerig.layers[10].selset = False
    arm.gamerig.layers[10].group = 2
    arm.gamerig.layers[11].name = "Arm.R (FK)"
    arm.gamerig.layers[11].row = 8
    arm.gamerig.layers[11].selset = False
    arm.gamerig.layers[11].group = 5
    arm.gamerig.layers[12].name = "Arm.R (Tweak)"
    arm.gamerig.layers[12].row = 9
    arm.gamerig.layers[12].selset = False
    arm.gamerig.layers[12].group = 4
    arm.gamerig.layers[13].name = "Leg.L (IK)"
    arm.gamerig.layers[13].row = 10
    arm.gamerig.layers[13].selset = False
    arm.gamerig.layers[13].group = 2
    arm.gamerig.layers[14].name = "Leg.L (FK)"
    arm.gamerig.layers[14].row = 11
    arm.gamerig.layers[14].selset = False
    arm.gamerig.layers[14].group = 5
    arm.gamerig.layers[15].name = "Leg.L (Tweak)"
    arm.gamerig.layers[15].row = 12
    arm.gamerig.layers[15].selset = False
    arm.gamerig.layers[15].group = 4
    arm.gamerig.layers[16].name = "Leg.R (IK)"
    arm.gamerig.layers[16].row = 10
    arm.gamerig.layers[16].selset = False
    arm.gamerig.layers[16].group = 2
    arm.gamerig.layers[17].name = "Leg.R (FK)"
    arm.gamerig.layers[17].row = 11
    arm.gamerig.layers[17].selset = False
    arm.gamerig.layers[17].group = 5
    arm.gamerig.layers[18].name = "Leg.R (Tweak)"
    arm.gamerig.layers[18].row = 12
    arm.gamerig.layers[18].selset = False
    arm.gamerig.layers[18].group = 4
    arm.gamerig.layers[19].name = ""
    arm.gamerig.layers[19].row = 1
    arm.gamerig.layers[19].selset = False
    arm.gamerig.layers[19].group = 0
    arm.gamerig.layers[20].name = ""
    arm.gamerig.layers[20].row = 1
    arm.gamerig.layers[20].selset = False
    arm.gamerig.layers[20].group = 0
    arm.gamerig.layers[21].name = ""
    arm.gamerig.layers[21].row = 1
    arm.gamerig.layers[21].selset = False
    arm.gamerig.layers[21].group = 0
    arm.gamerig.layers[22].name = ""
    arm.gamerig.layers[22].row = 1
    arm.gamerig.layers[22].selset = False
    arm.gamerig.layers[22].group = 0
    arm.gamerig.layers[23].name = ""
    arm.gamerig.layers[23].row = 1
    arm.gamerig.layers[23].selset = False
    arm.gamerig.layers[23].group = 0
    arm.gamerig.layers[24].name = ""
    arm.gamerig.layers[24].row = 1
    arm.gamerig.layers[24].selset = False
    arm.gamerig.layers[24].group = 0
    arm.gamerig.layers[25].name = ""
    arm.gamerig.layers[25].row = 1
    arm.gamerig.layers[25].selset = False
    arm.gamerig.layers[25].group = 0
    arm.gamerig.layers[26].name = ""
    arm.gamerig.layers[26].row = 1
    arm.gamerig.layers[26].selset = False
    arm.gamerig.layers[26].group = 0
    arm.gamerig.layers[27].name = ""
    arm.gamerig.layers[27].row = 1
    arm.gamerig.layers[27].selset = False
    arm.gamerig.layers[27].group = 0
    arm.gamerig.layers[28].name = ""
    arm.gamerig.layers[28].row = 1
    arm.gamerig.layers[28].selset = False
    arm.gamerig.layers[28].group = 0
    arm.gamerig.layers[29].name = "Root"
    arm.gamerig.layers[29].row = 14
    arm.gamerig.layers[29].selset = False
    arm.gamerig.layers[29].group = 1

    bones = {}

    bone = arm.edit_bones.new('Bone')
    bone.head[:] = 0.0000, 0.0000, 0.0000
    bone.tail[:] = 0.0000, 1.0000, 0.0000
    bone.roll = 0.0000
    bone.use_connect = False
    bone.use_deform = False
    bones['Bone'] = bone.name

    bpy.ops.object.mode_set(mode='OBJECT')
    pbone = obj.pose.bones[bones['Bone']]
    pbone.gamerig.name = 'root'
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (False, False, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'QUATERNION'
    pbone.bone.layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False]

    bpy.ops.object.mode_set(mode='EDIT')
    for bone in arm.edit_bones:
        bone.select = False
        bone.select_head = False
        bone.select_tail = False
    for b in bones:
        bone = arm.edit_bones[bones[b]]
        bone.select = True
        bone.select_head = True
        bone.select_tail = True
        arm.edit_bones.active = bone

    arm.layers = [(x in [29]) for x in range(32)]

if __name__ == "__main__":
    create(bpy.context.active_object)
