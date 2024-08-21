from haystack.components.builders.prompt_builder import PromptBuilder

def get_prompt_builder():
    prompt_template = """
        Given the following information, answer the question.
        
        Context:
        {% for doc in documents %}
            {{ doc.content }}
        {% endfor %}
        Question: {{query}}
        """
    prompt_builder = PromptBuilder(template=prompt_template)
    return prompt_builder