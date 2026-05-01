from src.states.blogstate import BlogState

class BlogNode:
    """
    A class to represent the blog node
    """
    
    def __init__(self,llm):
        self.llm = llm
        
    def title_creation(self,state:BlogState):
        """
        Create the title of the blog
        """    