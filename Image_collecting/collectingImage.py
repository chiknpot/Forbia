from google_images_download import google_images_download
response = google_images_download.googleimagesdownload()

arguments={"keywords":"scenary","limit":500,"print_urls":True, "chromedriver":"chromedriver.exe"}
paths = response.download(arguments)
print(paths)
