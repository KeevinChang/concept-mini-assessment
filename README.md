# Concept Mini Assessment

## To Run
1. Download/clone the repo from GitHub
2. Run the command: pip install -r requirements.txt in terminal
3. Run the command: py manage.py migrate (makemigrations unnecessary migration file included in repo)
4. You are now ready to deploy the application! Deploy at any point using the command: py manage.py runserver


## AI Collaboration
Tools used: ChatGPT, Google Gemini

**Example Prompts:** <br>
Prompt: Which Django models field lends itself best to creative fields as tags? <br>
Prompt: If I have a Navbar in my base.html how would I make changes to what buttons are available on it based on the page? <br>
Prompt: How can I implement a lifting hover effect over card elements on my Django template?

**Scenarios where AI was helpful**
* Identifying where a bug may have occurred based on and interpreting the meaning of a debug statement
* Suggesting modules to implement specific pieces of functionality
* Completing code for simple tasks like template skeletons and models for databasing

**Scenarios where AI was less useful**
* Actual debugging, especially complex bugs. I found that in cases where the first suggested solution did not work,
AI would exclusively add more code rather than consider possible mistakes in previous solutions, bloating the codebase
* Making small adjustments to features. AI often would often suggest many changes when all I wanted to do was make a small changes