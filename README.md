# blog_post_openai
Extract the information from the blog post and customise OpenAI model using API

# Environment variables
You have to specify your OpenAI API key
```
export OPENAI_API_KEY="<OPENAI_API_KEY>"
```

# Dependencies
You will need to install some python libraries, such as:
```
requests
langchain
bs4
gradio
```

## Extract the information from the blog post and save it to the text file
```
python extract.py
```


## Customize OpenAI model with the new information
:bangbang: This requires your OPENAI_API_KEY and costs you money.
```
python customize.py
```

## Ask questions about the article
```
python question.py
```
