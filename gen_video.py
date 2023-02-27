import os
def generate_video(model='s1', outf= '/home/tian/secret/DTVNet-master/checkpoints/DTV_Sky/200708162546/results/test_200_f/07U1fSrk9oI_1'):
	img_path = os.path.join(outf, '0000.png')
	mp4_path = os.path.join(outf, model+ '_video.mp4')
	cmd = ('ffmpeg -loglevel warning -framerate 25 -i ' + img_path +
		' -qscale:v 2 -y ' + mp4_path )
	print(cmd)
	os.system(cmd)
generate_video('s1')