from langchain_community.document_loaders import WebBaseLoader

def load_webdata():
    urls=[
    "https://paf-iast.edu.pk/eligibilitycriteria/",
"    https://paf-iast.edu.pk/admissionsmeritscheme/",
    "https://paf-iast.edu.pk/paf-iast-need-based-scholarships/",
    "https://paf-iast.edu.pk/paf-iast-merit-scholarship/",
    "https://paf-iast.edu.pk/paf-societies/",
    "https://paf-iast.edu.pk/bachelor-programs/",
    "https://paf-iast.edu.pk/master-programs/",
    "https://paf-iast.edu.pk",
    ]
    loader=WebBaseLoader(urls)
    webdata=loader.load()
    return webdata
