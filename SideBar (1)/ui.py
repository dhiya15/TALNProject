from TkinterSidebar.sidebar import *
from TkinterSidebar.pages.display_pages import *

root = Tk()	# create Window

root.resizable(False, True)
root.geometry("2800x1000")
root.title("ARAcorp")

# create Frame for tab windows
main_frame = Frame(root, bg="white", width=1800, height=1000)
main_frame.place(x=0, y=0)




# create sidebar + buttons + spacers
sidebar = SideBar(root)

sidebar.add_spacer("AP-Corpora")

#sidebar.add_button("Corpus", lambda: Dashboard(main_frame), icon="home.png")

#sidebar.add_spacer("Category")
#sidebar.add_button("HTML & CSS", lambda: Category(main_frame))
sidebar.add_button("Corpus", lambda: CorpusPage(main_frame), icon="icons/corpus.png")
sidebar.add_button("Scrapping", lambda: ScrapPage(main_frame), icon="icons/si.png")
sidebar.add_button("Normalization", lambda: NormalizePage(main_frame), icon="icons/norma.png")
sidebar.add_button("Stemming", lambda: StemmingPage(main_frame), icon="icons/stem.png")

#sidebar.add_spacer("Posts")
#sidebar.add_button("Web Design", lambda: Posts(main_frame))
sidebar.add_button("Similarity", lambda: SimilarityPage(main_frame), icon="icons/si.png")


sidebar.add_button("About", lambda: AboutPage(main_frame), icon="icons/fim.png")

#sidebar.add_spacer("Plugins")
#sidebar.add_button("UI Face", lambda: Category(main_frame))
#sidebar.add_button("Pigments", lambda: TestPage(main_frame))
"""sidebar.add_button("Box Icons", lambda: TestPage(main_frame))

sidebar.add_button("Explore", lambda: Analytics(main_frame), icon="home.png")
sidebar.add_button("History", lambda: Chart(main_frame), icon="home.png")
sidebar.add_button("Setting", lambda: Chart(main_frame), icon="home.png")"""

sidebar.finish()	# finish creation

root.mainloop()
