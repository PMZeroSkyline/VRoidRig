import bpy

class VRR_PT_Panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_air_panel"
    bl_label = "VRoid Rig"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "VRoidRig"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Welcome !")
        layout.operator("vrr.rig")

