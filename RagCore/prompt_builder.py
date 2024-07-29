from haystack.components.builders.prompt_builder import PromptBuilder

def get_prompt_builder():
    prompt_template = """
        Given these documents, answer the question.
        Documents:
        {% for doc in documents %}
            {{ doc.content }}
        {% endfor %}
        Question: {{question}}
        Answer:
        """
    prompt_builder = PromptBuilder(template=prompt_template)
    return prompt_builder