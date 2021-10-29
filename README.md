# blender_principled_bsdf_pytorch
## data 

use blender to render 1000 100*100 pixel image with random bsdf material arg

## save_value.txt
json file 
save every bsdf material arg of image 
every bsdf material have 
```json
bsdf_name:[
  0-1-2-3'Base Color','Base Color','Base Color','Base Color',
  4'Subsurface',
  5'Subsurface Radius',
  6 7 8 9'Subsurface Color','Subsurface Color','Subsurface Color','Subsurface Color',
  10'Metallic',
  11'Specular',
  12'Specular Tint',
  13'Roughness',
  14'Anisotropic',
  15'Anisotropic Rotation',
  16'Sheen',
  17'Sheen Tint',
  18'Clearcoat',
  19'Clearcoat Roughness',
  20'IOR',
  21'Transmission',
  22'Transmission Roughness',
]
```
