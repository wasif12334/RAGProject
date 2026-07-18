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
    "https://paf-iast.edu.pk/school_of_computingsciences/",
    "https://paf-iast.edu.pk/sdaat/",
    "https://paf-iast.edu.pk/department-of-chemical-and-energy-engineering/",
    "https://paf-iast.edu.pk/department-of-materials-science-engineering/",
    "https://paf-iast.edu.pk/ece/",
    "https://paf-iast.edu.pk/deoartments/",
    "https://paf-iast.edu.pk/sbepd/",
    "https://paf-iast.edu.pk/englishdept/",
    "https://paf-iast.edu.pk/department-of-pharmaceuticalsciences/",
    "https://paf-iast.edu.pk/department-of-mechanical-manufacturing-engineering/",
    "https://paf-iast.edu.pk/department-of-biomedical-sciences/",
    ]
    loader=WebBaseLoader(urls)
    webdata=loader.load()
    return webdata
