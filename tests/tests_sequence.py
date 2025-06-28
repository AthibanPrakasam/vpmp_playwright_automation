from pages.sequence_page import Sequencepage



def test_add_sequence(setup_browser):
    pages = setup_browser
    sequence_page = Sequencepage(pages)  
    sequence_page.portallogin()          
    sequence_page.gotoseqmanagement() 



     