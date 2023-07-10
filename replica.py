from pywebcopy import save_webpage
 
kwargs = {'project_name': 'site folder'}
 
save_webpage(
   
    # url of the website
    url='http://172.18.10.10:1000/fgtauth?70a7607c3738c29f',
     
    # folder where the copy will be saved
    project_folder=r'S:\Projects\vitap wifi login spoof',
    **kwargs
)