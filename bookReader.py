import pyttsx3
import PyPDF2

book = open('D:\python\BookReader\sql.pdf', 'rb')   #opening book
pdfReader = PyPDF2.PdfFileReader(book) #reading book
pages = pdfReader.numPages  #getting total pages
print(pages)
speaker = pyttsx3.init()    # initialising text-to-speak
page = pdfReader.getPage(5)
print(page)
text = page.extractText()   #extracting words from page
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)   #changing voice (male to female)
for i in range(5, pages):
   speaker.setProperty('rate', 200)
   speaker.say(text)
   speaker.runAndWait()
book.close()
