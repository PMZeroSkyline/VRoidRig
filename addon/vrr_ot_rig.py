import typing
import bpy
from mathutils import Vector
import math

def set_mode(object, new_mode):
    bpy.context.view_layer.objects.active = object
    bpy.ops.object.mode_set(mode=new_mode)

def add_ik_bone(armature_obj, bone_name, ik_bone_name, size):
    set_mode(armature_obj, 'EDIT')
    armature = armature_obj.data
    root = armature.edit_bones.get("Root")
    bone = armature.edit_bones.get(bone_name)
    ik_bone = armature.edit_bones.new(ik_bone_name)
    ik_bone.head = bone.tail
    ik_bone.tail = bone.tail + Vector((0, size, 0))
    ik_bone.parent = root
    bpy.context.view_layer.update()
    set_mode(armature_obj, 'OBJECT')

def add_ik_target_bone(armature_obj, bone_name, ik_target_bone_name, size, offset):
    set_mode(armature_obj, 'EDIT')
    armature = armature_obj.data
    root = armature.edit_bones.get("Root")
    bone = armature.edit_bones.get(bone_name)
    ik_target_bone = armature.edit_bones.new(ik_target_bone_name)
    ik_target_bone.head = bone.tail + Vector((0, offset, 0))
    ik_target_bone.tail = bone.tail + Vector((0, offset + size, 0))
    ik_target_bone.parent = root
    bpy.context.view_layer.update()
    bpy.ops.object.mode_set(mode='OBJECT')
    set_mode(armature_obj, 'OBJECT')

def add_bone_offset(armature_obj, head_bone_name, tail_bone_name, offset):
    set_mode(armature_obj, 'EDIT')
    armature = armature_obj.data
    head_bone = armature.edit_bones.get(head_bone_name)
    tail_bone = armature.edit_bones.get(tail_bone_name)
    head_bone.head += offset
    tail_bone.tail += offset
    bpy.context.view_layer.update()
    set_mode(armature_obj, 'OBJECT')

def add_ik_constraint(armature_obj, bone_name, ik_bone_name, ik_target_bone_name, pole_angle):
    set_mode(armature_obj, 'POSE')
    pose_bone = armature_obj.pose.bones.get(bone_name)
    ik_constraint = pose_bone.constraints.new(type='IK')
    ik_constraint.target = armature_obj
    ik_constraint.subtarget = ik_bone_name
    ik_constraint.pole_target = armature_obj
    ik_constraint.pole_subtarget = ik_target_bone_name
    ik_constraint.pole_angle = math.radians(pole_angle)
    ik_constraint.iterations = 500
    ik_constraint.chain_count = 2
    ik_constraint.use_tail = True
    ik_constraint.use_stretch = True
    ik_constraint.weight = 1.0
    ik_constraint.use_location = True
    ik_constraint.use_rotation = False
    ik_constraint.influence = 1.0
    bpy.context.view_layer.update()
    set_mode(armature_obj, 'OBJECT')

def set_bone_deform(armature_obj, bone_name, value):
    set_mode(armature_obj, 'EDIT')
    bone = armature_obj.data.edit_bones.get(bone_name)
    bone.use_deform = value
    set_mode(armature_obj, 'OBJECT')
    bpy.context.view_layer.update()

def set_bone_wire(armature_obj, bone_name, value):
    set_mode(armature_obj, 'EDIT')
    bone = armature_obj.data.edit_bones.get(bone_name)
    bone.show_wire = value
    set_mode(armature_obj, 'OBJECT')
    bpy.context.view_layer.update()

def set_bone_shape_to_sphere(armature_obj, bone_name, rotation_euler, scale):
    set_mode(armature_obj, 'EDIT')
    pose_bone = armature_obj.pose.bones.get(bone_name)
    shape_obj = bpy.data.objects.get("BoneShape_Sphere")
    if shape_obj is None:
        bpy.context.scene.cursor.location = (0, 0, 0)
        bpy.ops.mesh.primitive_uv_sphere_add(radius=1, segments=3, ring_count=3, location=(0,0,0))
        shape_obj = bpy.context.object
        shape_obj.name = "BoneShape_Sphere"
        shape_obj.scale = Vector((0,0,0))
    pose_bone.custom_shape = shape_obj
    pose_bone.custom_shape_rotation_euler = Vector(math.radians(angle) for angle in rotation_euler)
    pose_bone.custom_shape_scale_xyz = scale  
    set_mode(armature_obj, 'OBJECT')  
    bpy.context.view_layer.update()

def set_bone_shape_to_cube(armature_obj, bone_name, rotation_euler, scale):
    set_mode(armature_obj, 'EDIT')
    pose_bone = armature_obj.pose.bones.get(bone_name)
    shape_obj = bpy.data.objects.get("BoneShape_Cube")
    if shape_obj is None:
        bpy.context.scene.cursor.location = (0, 0, 0)
        bpy.ops.mesh.primitive_cube_add(size=1, location=(0,0,0))
        shape_obj = bpy.context.object
        shape_obj.name = "BoneShape_Cube"
        shape_obj.scale = Vector((0,0,0))
    pose_bone.custom_shape = shape_obj
    pose_bone.custom_shape_rotation_euler = Vector(math.radians(angle) for angle in rotation_euler)
    pose_bone.custom_shape_scale_xyz = scale
    set_mode(armature_obj, 'OBJECT')  
    bpy.context.view_layer.update()

def set_bone_shape_to_plane(armature_obj, bone_name, rotation_euler, scale):
    set_mode(armature_obj, 'EDIT')
    pose_bone = armature_obj.pose.bones.get(bone_name)
    shape_obj = bpy.data.objects.get("BoneShape_Plane")
    if shape_obj is None:
        bpy.context.scene.cursor.location = (0, 0, 0)
        bpy.ops.mesh.primitive_plane_add(size=1, location=(0,0,0))
        shape_obj = bpy.context.object
        shape_obj.name = "BoneShape_Plane"
        shape_obj.scale = Vector((0,0,0))
    pose_bone.custom_shape = shape_obj
    pose_bone.custom_shape_rotation_euler = Vector(math.radians(angle) for angle in rotation_euler)
    pose_bone.custom_shape_scale_xyz = scale
    set_mode(armature_obj, 'OBJECT')
    bpy.context.view_layer.update()

def set_bone_shape_to_cone(armature_obj, bone_name, rotation_euler, scale):
    set_mode(armature_obj, 'EDIT')
    pose_bone = armature_obj.pose.bones.get(bone_name)
    shape_obj = bpy.data.objects.get("BoneShape_Cone")
    if shape_obj is None:
        bpy.context.scene.cursor.location = (0, 0, 0)
        bpy.ops.mesh.primitive_cone_add(vertices=3 ,location=(0,0,0))
        shape_obj = bpy.context.object
        shape_obj.name = "BoneShape_Cone"
        shape_obj.scale = Vector((0,0,0))
    pose_bone.custom_shape = shape_obj
    pose_bone.custom_shape_rotation_euler = Vector(math.radians(angle) for angle in rotation_euler)
    pose_bone.custom_shape_scale_xyz = scale
    set_mode(armature_obj, 'OBJECT')
    bpy.context.view_layer.update()

def disconnect_bones(armature_obj, bone_name, bone_parent_name):
    set_mode(armature_obj, 'EDIT')
    bpy.ops.armature.select_all(action='DESELECT')
    bone_a = armature_obj.data.edit_bones.get(bone_name)
    bone_b = armature_obj.data.edit_bones.get(bone_parent_name)
    bone_a.select = True
    bone_b.select = True
    bpy.ops.armature.parent_clear(type='DISCONNECT')

class VRR_OT_Rig(bpy.types.Operator):
    bl_idname = "vrr.rig"
    bl_label = "Rig"
    
    def execute(self, context):

        selected_objects = bpy.context.selected_objects
        armature_obj = None
        for obj in selected_objects:
            if obj.type == 'ARMATURE':
                armature_obj = obj
                break


        # disconnect root
        disconnect_bones(armature_obj, "J_Bip_C_Hips", "Root")
        
        # add offset, IK needs some bending to calculate
        add_bone_offset(armature_obj, "J_Bip_L_LowerArm", "J_Bip_L_UpperArm", Vector((0,0.01,0)))
        add_bone_offset(armature_obj, "J_Bip_R_LowerArm", "J_Bip_R_UpperArm", Vector((0,0.01,0)))

        # add IK bone
        add_ik_bone(armature_obj, "J_Bip_L_LowerArm", "IK_Arm_L", 0.2)
        add_ik_bone(armature_obj, "J_Bip_R_LowerArm", "IK_Arm_R", 0.2)
        add_ik_bone(armature_obj, "J_Bip_L_LowerLeg", "IK_Leg_L", 0.2)
        add_ik_bone(armature_obj, "J_Bip_R_LowerLeg", "IK_Leg_R", 0.2)
        add_ik_bone(armature_obj, "J_Bip_C_Neck", "IK_Neck", 0.2)
        add_ik_bone(armature_obj, "J_Bip_C_Chest", "IK_Chest", 0.2)

        # add IK Target
        add_ik_target_bone(armature_obj, "J_Bip_L_UpperArm", "IKT_Arm_L", 0.2, 0.5)
        add_ik_target_bone(armature_obj, "J_Bip_R_UpperArm", "IKT_Arm_R", 0.2, 0.5)
        add_ik_target_bone(armature_obj, "J_Bip_L_UpperLeg", "IKT_Leg_L", -0.2, -0.5)
        add_ik_target_bone(armature_obj, "J_Bip_R_UpperLeg", "IKT_Leg_R", -0.2, -0.5)
        add_ik_target_bone(armature_obj, "J_Bip_C_UpperChest", "IKT_Neck", 0.2, 0.5)
        add_ik_target_bone(armature_obj, "J_Bip_C_Spine", "IKT_Chest", 0.2, 0.5)

        # add IK constraint
        add_ik_constraint(armature_obj, "J_Bip_L_LowerArm", "IK_Arm_L", "IKT_Arm_L", 180)
        add_ik_constraint(armature_obj, "J_Bip_R_LowerArm", "IK_Arm_R", "IKT_Arm_R", 0)
        add_ik_constraint(armature_obj, "J_Bip_L_LowerLeg", "IK_Leg_L", "IKT_Leg_L", -90)
        add_ik_constraint(armature_obj, "J_Bip_R_LowerLeg", "IK_Leg_R", "IKT_Leg_R", -90)
        add_ik_constraint(armature_obj, "J_Bip_C_Neck", "IK_Neck", "IKT_Neck", -90)
        add_ik_constraint(armature_obj, "J_Bip_C_Chest", "IK_Chest", "IKT_Chest", -90)

        # set ik display shape
        set_bone_shape_to_plane(armature_obj, "Root", Vector((90, 0, 0)), Vector((0.5, 0.5, 0.5)))
        set_bone_shape_to_plane(armature_obj, "J_Bip_C_Hips", Vector((90,0,0)), Vector((5, 5, 5)))
        set_bone_shape_to_sphere(armature_obj, "IK_Arm_L", Vector((0,0,-90)), Vector((0.5, 0.5, 0.5)))
        set_bone_shape_to_sphere(armature_obj, "IK_Arm_R", Vector((0,0,90)), Vector((0.5, 0.5, 0.5)))
        set_bone_shape_to_sphere(armature_obj, "IK_Leg_L", Vector((90,0,0)), Vector((0.5, 0.5, 0.5)))
        set_bone_shape_to_sphere(armature_obj, "IK_Leg_R", Vector((90,0,0)), Vector((0.5, 0.5, 0.5)))
        set_bone_shape_to_sphere(armature_obj, "IK_Neck", Vector((0,0,180)), Vector((0.5, 0.5, 0.5)))
        set_bone_shape_to_sphere(armature_obj, "IK_Chest", Vector((0,0,180)), Vector((0.5, 0.5, 0.5)))
        set_bone_shape_to_cone(armature_obj, "IKT_Arm_L", Vector((0,0,30)), Vector((0.2, 0.2, 0.2)))
        set_bone_shape_to_cone(armature_obj, "IKT_Arm_R", Vector((0,0,-30)), Vector((0.2, 0.2, 0.2)))
        set_bone_shape_to_cone(armature_obj, "IKT_Leg_L", Vector((180,0,30)), Vector((0.2, 0.2, 0.2)))
        set_bone_shape_to_cone(armature_obj, "IKT_Leg_R", Vector((180,0,-30)), Vector((0.2, 0.2, 0.2)))
        set_bone_shape_to_cone(armature_obj, "IKT_Neck", Vector((-90,180,0)), Vector((0.2, 0.2, 0.2)))
        set_bone_shape_to_cone(armature_obj, "IKT_Chest", Vector((-90,0,0)), Vector((0.2, 0.2, 0.2)))

        # set controll rig deform
        set_bone_deform(armature_obj, "Root", False)
        set_bone_deform(armature_obj, "IK_Arm_L", False)
        set_bone_deform(armature_obj, "IK_Arm_R", False)
        set_bone_deform(armature_obj, "IK_Leg_L", False)
        set_bone_deform(armature_obj, "IK_Leg_R", False)
        set_bone_deform(armature_obj, "IK_Neck", False)
        set_bone_deform(armature_obj, "IK_Chest", False)
        set_bone_deform(armature_obj, "IKT_Arm_L", False)
        set_bone_deform(armature_obj, "IKT_Arm_R", False)
        set_bone_deform(armature_obj, "IKT_Leg_L", False)
        set_bone_deform(armature_obj, "IKT_Leg_R", False)
        set_bone_deform(armature_obj, "IKT_Neck", False)
        set_bone_deform(armature_obj, "IKT_Chest", False)

        # set controll rig view
        set_bone_wire(armature_obj, "Root", True)
        set_bone_wire(armature_obj, "IK_Arm_L", True)
        set_bone_wire(armature_obj, "IK_Arm_R", True)
        set_bone_wire(armature_obj, "IK_Leg_L", True)
        set_bone_wire(armature_obj, "IK_Leg_R", True)
        set_bone_wire(armature_obj, "IK_Neck", True)
        set_bone_wire(armature_obj, "IK_Chest", True)
        set_bone_wire(armature_obj, "IKT_Arm_L", True)
        set_bone_wire(armature_obj, "IKT_Arm_R", True)
        set_bone_wire(armature_obj, "IKT_Leg_L", True)
        set_bone_wire(armature_obj, "IKT_Leg_R", True)
        set_bone_wire(armature_obj, "IKT_Neck", True)
        set_bone_wire(armature_obj, "IKT_Chest", True)

        # to pose mode
        set_mode(armature_obj, 'POSE')
        return {'FINISHED'}
