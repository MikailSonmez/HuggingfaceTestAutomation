from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel
from huggingface_hub import login

# Hugging Face API token'ınızı buraya ekleyin

# Hugging Face modelini doğru şekilde başlatmak
token = "***********" 
login(token=token)
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel(),
    additional_authorized_imports=[
        "selenium",
        "selenium.webdriver.common.keys",
        "selenium.webdriver.common.by",
        "selenium.webdriver.support.ui",
        "selenium.webdriver.support.expected_conditions",
        "webdriver_manager",
        "webdriver_manager.chrome"

    ]
)

# Testi çalıştır
agent.run("Write a selenium test to run test in headful mode https://example.com/ perform assert page, and validate title and texts")
