import bpy
import mathutils
import os
import sys

def svg_to_fbx(svg_name, input_folder, output_folder):
    # Path to the SVG file
    svg_file_path = os.path.join(input_folder, svg_name)

    # Delete all objects in the scene
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    # Import SVG file
    bpy.ops.import_curve.svg(filepath=svg_file_path)

    # delete SVG
    os.remove(svg_file_path)

    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # Convert curves to meshes and remove original curve objects
    for obj in bpy.data.objects:
        if obj.type == 'CURVE':
            # Create new mesh object
            mesh = bpy.data.meshes.new_from_object(obj)
            new_obj = bpy.data.objects.new(obj.name, mesh)
            new_obj.matrix_world = obj.matrix_world

            # Link new mesh object to the scene
            bpy.context.collection.objects.link(new_obj)

            # Remove original curve object
            bpy.data.objects.remove(obj)

    bpy.ops.object.select_all(action='DESELECT')

    # Select all objects
    bpy.ops.object.select_all(action='SELECT')

    # Get the minimum and maximum X coordinates of the selection
    min_x = float('inf')
    max_x = float('-inf')

    for obj in bpy.context.selected_objects:
        bbox = obj.bound_box

        for vertex in bbox:
            global_vertex = obj.matrix_world @ mathutils.Vector(vertex[:])

            min_x = min(min_x, global_vertex.x)
            max_x = max(max_x, global_vertex.x)

    # Calculate the total width
    total_width = max_x - min_x

    # Calculate the scaling factor
    desired_width = 1.0  # Change this to the desired total width in meters
    scaling_factor = desired_width / total_width

    # Scale the meshes proportionally
    for obj in bpy.context.selected_objects:
        obj.scale *= scaling_factor


    if bpy.context.selected_objects:
        # Switch to edit mode for selected objects
        bpy.context.view_layer.objects.active = bpy.context.selected_objects[0]
        bpy.ops.object.mode_set(mode='EDIT')

        # Select all vertices
        bpy.ops.mesh.select_all(action='SELECT')

        # Extrude all meshes in the Z axis
        bpy.ops.mesh.extrude_region_move(
            TRANSFORM_OT_translate={"value": (0, 0, 0.05)}
        )

        # Exit edit mode
        bpy.ops.object.mode_set(mode='OBJECT')

        file_name = svg_name[:-4] + ".fbx"

        # Select all objects in the scene
        bpy.ops.object.select_all(action='SELECT')

        # Export the scene as an FBX file
        bpy.ops.export_scene.fbx(filepath=os.path.join(output_folder, file_name))

        # Deselect all objects
        bpy.ops.object.select_all(action='DESELECT')

svg_name = sys.argv[4]
input_folder = sys.argv[5]
output_folder = sys.argv[6]

svg_to_fbx(svg_name, input_folder, output_folder)