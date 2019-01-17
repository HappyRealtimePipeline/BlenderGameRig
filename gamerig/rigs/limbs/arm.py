#====================== BEGIN GPL LICENSE BLOCK ======================
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#======================= END GPL LICENSE BLOCK ========================

# <pep8 compliant>
import bpy
from rna_prop_ui import rna_idprop_ui_prop_get
from ...utils import MetarigError, copy_bone
from ..widgets import create_hand_widget
from .limb_utils import *

def create_arm( cls, bones ):
    org_bones = cls.org_bones

    bpy.ops.object.mode_set(mode='EDIT')
    eb = cls.obj.data.edit_bones

    ctrl = get_bone_name( org_bones[2], 'ctrl', 'ik' )

    # Create IK arm control
    ctrl = copy_bone( cls.obj, org_bones[2], ctrl )

    # clear parent (so that gamerig will parent to root)
    eb[ ctrl ].parent      = None
    eb[ ctrl ].use_connect = False

    # Parent
    eb[ bones['ik']['mch_target'] ].parent      = eb[ ctrl ]
    eb[ bones['ik']['mch_target'] ].use_connect = False

    if cls.root_bone:
        # add IK Follow feature
        mch_ik_socket = copy_bone( cls.obj, cls.root_bone, mch('socket_' + ctrl) )
        eb[ mch_ik_socket ].length /= 4
        eb[ mch_ik_socket ].use_connect = False
        eb[ mch_ik_socket ].parent = None
        eb[ ctrl    ].parent = eb[ mch_ik_socket ]

        make_constraint( cls, mch_ik_socket, {
            'constraint'   : 'COPY_TRANSFORMS',
            'subtarget'    : cls.root_bone,
            'target_space' : 'WORLD',
            'owner_space'  : 'WORLD',
        })

    # Set up constraints
    # Constrain mch target bone to the ik control and mch stretch

    make_constraint( cls, bones['ik']['mch_target'], {
        'constraint'  : 'COPY_LOCATION',
        'subtarget'   : bones['ik']['mch_str'],
        'head_tail'   : 1.0
    })

    # Constrain mch ik stretch bone to the ik control
    make_constraint( cls, bones['ik']['mch_str'], {
        'constraint'  : 'DAMPED_TRACK',
        'subtarget'   : ctrl,
    })
    make_constraint( cls, bones['ik']['mch_str'], {
        'constraint'  : 'STRETCH_TO',
        'subtarget'   : ctrl,
    })
    if cls.allow_ik_stretch:
        make_constraint( cls, bones['ik']['mch_str'], {
            'constraint'  : 'LIMIT_SCALE',
            'use_min_y'   : True,
            'use_max_y'   : True,
            'max_y'       : 1.05,
            'owner_space' : 'LOCAL'
        })

    pb = cls.obj.pose.bones

    # Modify rotation mode for ik and tweak controls
    pb[bones['ik']['ctrl']['limb']].rotation_mode = 'ZXY'

    pb_master = pb[ bones['fk']['ctrl'][0] ]

    if cls.allow_ik_stretch:
        # Create ik stretch property

        pb_master['ik_stretch'] = 1.0
        prop = rna_idprop_ui_prop_get( pb_master, 'ik_stretch', create=True )
        prop["min"]         = 0.0
        prop["max"]         = 1.0
        prop["soft_min"]    = 0.0
        prop["soft_max"]    = 1.0
        prop["description"] = 'IK Stretch'

        # Add driver to limit scale constraint influence
        b        = bones['ik']['mch_str']
        drv      = pb[b].constraints[-1].driver_add("influence").driver
        drv.type = 'SUM'

        var = drv.variables.new()
        var.name = prop.name
        var.type = "SINGLE_PROP"
        var.targets[0].id = cls.obj
        var.targets[0].data_path = pb_master.path_from_id() + '['+ '"' + prop.name + '"' + ']'

        drv_modifier = cls.obj.animation_data.drivers[-1].modifiers[0]

        drv_modifier.mode            = 'POLYNOMIAL'
        drv_modifier.poly_order      = 1
        drv_modifier.coefficients[0] = 1.0
        drv_modifier.coefficients[1] = -1.0
        
    if cls.root_bone:
        # Add IK Follow property and driver
        pb_master['ik_follow'] = 1.0
        prop = rna_idprop_ui_prop_get( pb_master, 'ik_follow', create=True )
        prop["min"]         = 0.0
        prop["max"]         = 1.0
        prop["soft_min"]    = 0.0
        prop["soft_max"]    = 1.0
        prop["description"] = 'IK Follow'

        drv      = pb[mch_ik_socket].constraints[-1].driver_add("influence").driver
        drv.type = 'SUM'

        var = drv.variables.new()
        var.name = prop.name
        var.type = "SINGLE_PROP"
        var.targets[0].id = cls.obj
        var.targets[0].data_path = pb_master.path_from_id() + '['+ '"' + prop.name + '"' + ']'

    # Create hand widget
    create_hand_widget(cls.obj, ctrl)

    bones['ik']['ctrl']['terminal'] = [ ctrl ]

    return bones
