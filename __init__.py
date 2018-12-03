import bpy
import os
import gpu

bl_info = {
  'name': "UE4Rig",
  "author": 'Mack Thompson',
  'version': (0, 0, 1),
  'blender': (2, 80, 0),
  'description': 'Creates rigs using the UE4 skeleton',
  'license': 'MIT',
  'category': 'Animation'
}

class UE4Rig_addrig_operator(bpy.types.Operator):
  """Adds a new rig"""
  bl_label = "Add Rig"
  bl_idname = "ue4rig.add_rig"

  def execute(self, context):

    TemplateFilepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Mannequin.blend")
    Section = "\\Object"
    ObjectName = "SK_Mannequin.001"
    TemplateDirectory = TemplateFilepath + Section

    bpy.ops.wm.append(
        filepath=TemplateFilepath + Section + ObjectName,
        filename=ObjectName,
        directory=TemplateDirectory,
        autoselect=True
      )
    return {'FINISHED'}

class UE4Rig_panel(bpy.types.Panel):
  """UE4Rig Panel"""
  bl_label = "UE4 Rig"
  bl_space_type = "VIEW_3D"
  bl_region_type = 'UI'

  def draw(self, context):
    layout = self.layout

    row = layout.row()
    row.label(text="Setup")
    row = layout.row()
    row.operator("ue4rig.add_rig")

classes = { 
  UE4Rig_panel,
  UE4Rig_addrig_operator
}

def register():
  for cls in classes:
    bpy.utils.register_class(cls)

def unregister():
  for cls in classes:
    bpy.utils.unregister_class(cls)

  if __name__ == "__main__":
    register()