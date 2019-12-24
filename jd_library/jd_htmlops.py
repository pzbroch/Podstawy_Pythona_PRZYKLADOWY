##############################
#     jd_htmlops library     #
#----------------------------#
#  Various HTML Operations   #
#============================#
# Ver. 0.3 (2019-12-24)      #
# (C) 2019 Przemyslaw Zbroch #
##############################





################################################################################
#                                                                              #
# buildHtmlPage(pageTitle, bodyContent)                                        #
#                                                                              #
# Function that generates HTML website that includes title and body provided.  #
#                                                                              #
# Returns website as a multiline string.                                       #
#                                                                              #
# Parameters:                                                                  #
#   - pageTitle - any string for the title of the website                      #
#                 (will be put between <title> tags of the final html code)    #
#   - pageContent - any string representing the html website content           #
#                   (will be put between <body> tags of the final html code)   #
#                                                                              #
# Required source files:                                                       #
#   - pagebase.html from jd_library - a file that contains the html code       #
#                   which will be filled with title and body. This file also   #
#                   includes the use of style.css sheet to be placed           #
#                   in the main project folder with the following path:        #
#                   /[project_folder]/static/css/style.css                     #
#                                                                              #
################################################################################



def buildHtmlPage(pageTitle, bodyContent):
    tmpFile = open('jd_library/pagebase.html','rt')
    pageBase = tmpFile.read(4096)
    tmpFile.close()
    return pageBase.format(pageTitle, bodyContent)
