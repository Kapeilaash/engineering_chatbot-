#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("ok")


# In[2]:


get_ipython().run_line_magic('pwd', '')


# In[3]:


import os 
os.chdir("../")


# In[4]:


get_ipython().run_line_magic('pwd', '')


# In[5]:


get_ipython().run_line_magic('pip', 'install -U langchain-community')


# In[6]:


from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


# In[7]:


def load_pdf_files(data):
    loader = DirectoryLoader(
        data,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )

    documents = loader.load()
    return documents


# In[10]:


extracted_data = load_pdf_files("data")


# In[9]:


get_ipython().system('pip install pypdf')


# In[11]:


extracted_data


# In[12]:


len(extracted_data)


# In[13]:


from typing import List
from langchain.schema import Document

def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    """
    Given a list of Document objects, return a new list of Document objects
    containing only 'source' in metadata and the original page_content.
    """
    minimal_docs: List[Document] = []
    for doc in docs:
        src = doc.metadata.get("source")
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source": src}
            )
        )
    return minimal_docs


# In[14]:


minimal_docs = filter_to_minimal_docs(extracted_data)


# In[15]:


minimal_docs


# In[16]:


def text_split(minimal_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20,
    )
    texts_chunk = text_splitter.split_documents(minimal_docs)
    return texts_chunk


# In[17]:


texts_chunk = text_split(minimal_docs)
print(f"Number of chunks: {len(texts_chunk)}")


# In[18]:


texts_chunk


# In[20]:


pip install sentence-transformers


# In[22]:


from langchain.embeddings import HuggingFaceEmbeddings

def download_embeddings():
    """
    Download and return the HuggingFace embeddings model.
    """
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name
    )
    return embeddings

embedding = download_embeddings()


# In[ ]:




