from azure.core.credentials import AzureKeyCredential
#from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.ai.documentintelligence import DocumentIntelligenceClient
from langchain.docstore.document import Document

endpoint = ""
key = ""

#documentUrl = "https://idodata.com/wp-content/uploads/2024/02/MASArticle-scaled.jpg"
#documentUrl = "https://arxiv.org/pdf/2408.15240"
documentUrl = "https://arxiv.org/pdf/2408.15207"
#documentUrl = "https://www.w3.org/WAI/WCAG21/working-examples/pdf-table/table.pdf"

document_analysis_client = DocumentIntelligenceClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

#poller = document_analysis_client.begin_analyze_document("prebuilt-layout", documentUrl)
document_intelligence_client = DocumentIntelligenceClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )
poller = document_intelligence_client.begin_analyze_document("prebuilt-layout", AnalyzeDocumentRequest(url_source=documentUrl))
result = poller.result()

#document_analysis_client.begin_analyze_document()

f = open("output.txt", 'w')
print("--------")
#for paragraph in result.paragraphs:
for paragraph in result.paragraphs:
    #if paragraph.tables:
        #print("Table recognised", file = f)
        #print(f"{paragraph.role}: {paragraph.content}", file = f)
     #   pass
    #else:
    print(f"{paragraph.role}: {paragraph.content}", file = f)
    #print(f"{paragraph.role}: {paragraph.content}")    
    #print(f"{paragraph.content}", file = f)    
    #print(paragraph.content, file = f)

print("paragraph completed ----------------", file = f)
f.close()    

