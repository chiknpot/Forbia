'''
Created on Mar 26, 2012

@author: sotuzun
'''
import settings
import web
import os
import requests as req

urls = (
    '/upload', 'Upload',
    '/result', 'Result'
)

app = web.application(urls, globals())

render = web.template.render(settings.TEMPLATE_FOLDER, base=settings.BASE_TEMPLATE_NAME)


class Upload(object):
	def GET(self):
		return render.upload()

	def POST(self):
		try:
			print(os.system ('rm dir_video/*'))
			print(os.system ('rm dir_picture/*'))
			x = web.input(myfile={})
			filedir = os.getcwd()+'/dir_video' # change this to the directory you want to store the file in.
			if 'myfile' in x: # to check if the file-object is created
				#filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
				filepath=x.myfile.filename
				filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
				with open(filedir +'/'+ filename,'wb') as fout:# creates the file where the uploaded file should be stored
					fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
			print(os.system ('python3 video_cut.py'))
			print(os.system ('python3 /home/ubuntu/real_forbia/pentagonChart.py'))
			raise web.seeother('/result')
		except:
			return render.upload()

class Result:
	def GET(self):
		return render.result()

if __name__ == '__main__':
	app.run()
