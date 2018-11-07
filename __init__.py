import bpy

bl_info = {
  'name': "UE4Rig",
  "author": 'Mack Thompson',
  'version': (0, 0, 1),
  'blender': (2, 79, 0),
  'description': 'Creates rigs using the UE4 skeleton',
  'license': 'MIT',
  'category': 'Animation'
}


class UE4Rig_Tools(bpy.types.Panel):
  """UE4Rig Panel"""
  bl_label = "UE4Rig"
  bl_space_type = "VIEW_3D"
  bl_region_type = 'TOOLS'
  bl_category = "UE4Rig"

  def draw(self, context):
    layout = self.layout

def register():
  bpy.utils.register_module(__name__)

def unregister():
  bpy.utils.unregister_module(__name__)

  if __name__ == "__main__":
    register()