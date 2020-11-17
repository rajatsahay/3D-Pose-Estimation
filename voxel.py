import numpy as np

def voxel2mesh(voxels,surface_view):
	cube_verts=[[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
	cube_faces=[[0,1,2],[1,3,2],[2,3,6],[3,7,6],[0,2,6],[0,6,4],[0,5,1],[0,4,5],[6,7,5],[6,5,4],[1,7,3],[1,5,7]]
	cube_verts=np.array(cube_verts)
 	cube_faces=np.array(cube_faces)+1

	scale=0.01
 	cube_dist_scale=1.1
 	verts=[]
 	faces=[]
 	current_vert=0

 	pos=np.where(voxels>0.4)
 	voxels[pos]=1
	for i,j,k in zip(*pos):
	 	if not surface_view or np.sum(voxels[i-1:i+2,j-1:j+2,k-1:k+2])<27:
			verts.extend(scale*(cube_verts+cube_dist_scale*np.array([[i,j,k]])))
			verts.extend(cube_faces+current_vert)
		 	current_vert+=len(cube_verts)

	return np.array(verts),np.array(faces)

def write_obj(filename,verts,faces):
	with open(filename,'w') as f:
		#write verts
		f.write('g\n# %d vertex\n' %len(verts))
	 	for vert in verts:
			 f.write('v %f %f %f\n' %tuple(vert))
		 
		#write faces
		f.write('# %d faces\n' %len(faces))
	  for face in faces:
			f.write("f %d %d %d\n" %tuple(face))
		
def voxel2obj(filename,pred,surface_view=True):
	verts,faces=voxel2mesh(pred,surface_view)
	write_obj(filename,verts,faces)
