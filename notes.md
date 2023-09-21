# Course Notes

## Guidelines for formatting prompts[](https://www.educative.io/courses/master-chatgpt-prompt-engineering/basics-of-prompting#Guidelines-for-formatting-prompts)

Here are a few guidelines to keep in mind while prompting:

- Be clear and specific about the task or question.
- Provide sufficient context to help the model understand the prompt.
- Use explicit examples or input data to guide the model’s understanding.
- Control response length by defining boundaries or experimenting with token counts.
- Utilize system-level instructions to set tone or behavior (temperature or top-k and top-p values).
- Iterate and refine prompts based on feedback and results.

Prompt formatting is a crucial aspect of interacting with language models effectively. By structuring prompts with clear instructions, relevant context, input data, and output indicators, we can guide the model to generate accurate and contextually appropriate responses. Following the guidelines for prompt formatting will help us achieve the desired outcomes when working with language models like ChatGPT.

# Course Notes

## Table of Contents

[ChatGPT Under The Hood](#chatgpt-under-the-hood)

[ChatGPT Usage](#chatgpt-usage)

[Basics of Prompting](#basics-of-prompting)

[Iterative Refinement](#iterative-refinement)

[Inferring with ChatGPT](#inferring-with-chatgpt)

[Transforming with ChatGPT](#transforming-with-chatgpt)

[Expanding with ChatGPT](##expanding-with-chatgpt)

[Formatting Output with ChatGPT](#formatting-output-with-chatgpt)

[Best Practices for Prompting](#best-practices-for-prompting)

## Basics of Prompting

## Introduction

### Summary: LLMs & Why ChatGPT Stands Out

#### Key Points:

1. **What are LLMs?**
   - Large Language Models (LLMs) are a critical development in Natural Language Processing (NLP).
2. **ChatGPT's Rapid Growth**

   - Gained 100 million users in just over two months after its launch, outpacing TikTok and Instagram.
   - Attracts significant investment, including $10 billion from Microsoft.

3. **Other Notable LLMs**

   - OpenAI GPT-3: Known for human-like text and diverse tasks.
   - BERT: Excel in context understanding and text classification.
   - RoBERTa: An optimized version of BERT with improved performance.
   - PaLM 2: Combines multiple models for reliable results.

4. **ChatGPT vs. Other LLMs**

   - Investors were disappointed with Alphabet's Bard, showing the market's high expectations around ChatGPT.

5. **Strengths and Weaknesses**

   - GPT-3: Highly accurate but needs substantial computational resources.
   - BERT: Struggles with out-of-context queries.
   - RoBERTa: Computationally intensive.
   - PaLM 2: Needs more resources due to multiple model combination.

6. **Applications**

   - GPT-3: Language translation, virtual assistants.
   - BERT: Search engines, sentiment analysis.
   - RoBERTa: Text classification, machine translation.
   - PaLM 2: Text analysis, sentiment analysis.

7. **Why ChatGPT?**
   - **General-purpose**: Can handle various NLP tasks.
   - **High Accuracy**: Trained on diverse data sources.
   - **Ease of Use**: Requires fewer resources than others.
   - **Conversational Proficiency**: Fine-tuned for high-quality responses.

#### Highlights:

- ChatGPT is a major player, showing unprecedented growth and investment interest.
- Various LLMs have different strengths, weaknesses, and application areas.
- ChatGPT is preferred for its versatility, accuracy, and lower resource requirements.

#### Main Points:

- Importance of well-structured prompts
- Components of a good prompt: Instructions, Context, Input Data, Output Indicators
- Guidelines for formatting prompts

## ChatGPT Under The Hood

#### Overview

- Focuses on the features, architecture, and training data of ChatGPT.
- Developed by OpenAI for generating human-like text responses.

#### ChatGPT Model

- Built on GPT-3 architecture, uses autoregressive language modeling.
- Contextualizes input text to generate appropriate text-based responses.

#### Response Mechanism

- Input is verified for safety and ethical guidelines.
- Breaks down input into tokens, predicts the next word, and forms a full response.
- Can be fine-tuned for domain-specific needs like language translation.

#### Training Data

- Trained on a diverse dataset including books, articles, and online forums.
- Uses over 45 terabytes of text from various genres, languages, and time periods.

#### Key Features

- **Versatility**: Useful for multiple NLP tasks, can be fine-tuned.
- **Accuracy**: High performance in several NLP benchmarks.
- **Human-like Responses**: Ideal for chatbot development.
- **Large Model Size**: Over 6 billion parameters, enhances context understanding.

#### ChatGPT 3.5 vs. ChatGPT 4.0

- **ChatGPT 3.5 Turbo**: Faster, more efficient, ideal for real-time responses.
- **ChatGPT 4**: Better at long-form text, improved accuracy, and naturalness.

#### Takeaways

- Highly versatile and accurate, ideal for various NLP applications including chatbots.
- Specific version choice should be based on project requirements.

---

#### Instructions:

- Be explicit and clear about what you want the model to do.
- Specify the desired format or actions.
- Include any constraints or limitations.

**Example**: When creating a chatbot for pizza delivery, specify available toppings, desired format for orders, and a limit on the number of toppings.

#### Context:

- Set the scene with relevant background.
- Include details that might influence the model's understanding.

**Example**: When asking for directions in a foreign country, specify that context so the model knows to translate into the appropriate language.

#### Input Data:

- Use examples or references related to the task.
- Make sure the data is relevant to the prompt’s objective.

**Example**: When asking to summarize an article, provide the article title and summary to guide the response.

#### Output Indicators:

- Specify the expected format or structure of the response.
- Guide the model’s response with specific output requirements.

**Example**: If you want to fill in a sentence template, provide the template as an output indicator.

#### General Guidelines:

- Be clear and specific.
- Provide sufficient context.
- Use explicit examples or input data.
- Control response length (token count).
- Use system-level instructions for tone or behavior (temperature, top-k, top-p).
- Iterate and refine prompts based on feedback.

By carefully crafting your prompts, you'll get more accurate and contextually appropriate responses from ChatGPT.
## ChatGPT Usage

### ChatGPT Usage: Summary

#### Key Sections
- General Usage
- Summarization
- Text Extraction
- Translation
- Generating Structured Output
- Creative Writing

#### Major Points

**1. General Usage:**  
- ChatGPT is versatile, capable of tasks beyond chat interactions. Used for summarization, text extraction, translation, structured outputs, and creative writing.

**2. Summarization:**  
- Effective for condensing long texts into shorter summaries. Great for creating executive summaries, research paper abstracts, etc.

**3. Text Extraction:**  
- Automates the process of pulling out key info from unstructured text. Useful for data extraction and information retrieval.

**4. Translation:**  
- Capable of accurate language translation tasks, beneficial for multilingual chatbots and language learning.

**5. Generating Structured Output:**  
- Can produce responses adhering to specific formats/templates, helping in automating repetitive tasks and streamlining workflows.

**6. Creative Writing:**  
- Also used for generating creative text like stories and poetry, offering a creative companion for writers.

#### Takeaways
- ChatGPT is a multi-faceted tool not just limited to chatbot interactions. It has practical applications in various fields, making it a robust utility for tasks requiring human-level language understanding.

## Iterative Refinement

Iterative refinement is the practice of progressively improving and adjusting prompts to obtain more accurate and tailored responses from ChatGPT. The process involves modifying instructions, context, or constraints to guide the model better.

#### Benefits

1. Allows for more specific, detailed instructions, leading to precise outputs.

2. Enables the incorporation of additional context or specific requirements for more contextually appropriate responses.

3. Gives users greater control over the output, enabling them to steer the model’s responses toward desired outcomes.

#### Tips for Refinement

1. **Include Constraints**: Be specific in the prompt, like specifying dietary restrictions when asking for a recipe.

2. **Offer Examples**: Providing examples can help ChatGPT understand the desired format or structure.

3. **Adjust Format**: Mention the need for lists or other specific formats if necessary.

4. **Refine Context**: Gradually add or modify context to make the prompts more relevant.

5. **Test and Iterate**: Experiment with different prompt variations and refine based on results.

#### Workflow

The iterative refining workflow is a cyclical process involving testing, evaluation, and prompt adjustments to gradually hone the model's responses.

#### Example

The example provided showcases how a basic travel recommendation prompt can be refined over three iterations to offer increasingly personalized travel suggestions. Each refinement incorporates more specific details like the type of vacation, couple’s interests, timing, and weather preferences, resulting in a highly tailored recommendation.

In essence, iterative refinement helps users tap into the full potential of ChatGPT by continually improving the prompts, enabling more accurate and contextually relevant outputs.

## Inferring with ChatGPT

Sure thing, Nick! Here's a summarized outline of the page about "Inferring with ChatGPT":

---

### Summary: Inferring with ChatGPT

- Overview of how ChatGPT uses inference to understand implicit information and generate personalized responses.

#### Inference

- Definition: Deduction of unstated information based on context and background knowledge.

#### Benefits of Inferring

- Grasps the context for better, more relevant responses.
- Resolves ambiguities and clarifies vague queries.
- Bridges information gaps for a smooth conversation.

#### Use Cases of Inference

- Enhances responses with conversation history and contextual cues.
- Understands user intents when details are missing.
- Provides tailored suggestions.
- Maintains coherent and relevant conversations.
- Clarifies and resolves uncertainties.

#### Examples

1. **What time is the movie?**

   - Inference: Refers to a movie being discussed or relevant to the current context.

2. **Can you recommend a good restaurant nearby?**

   - Inference: Based on the user's current location or context.

3. **How long does it take to fly from New York to London?**
   - Inference: Duration of a non-stop flight, assuming no delays.

4A. **Height Comparisons (John, Bob, Andrew, Sid)**

- Inference: John is the tallest.

4B. **Is Andrew taller than John?**

- Inference: John is tallest, so Andrew can't be taller.

#### Strategies for Leveraging Inferring

- **Context Awareness**: Provide context to help ChatGPT make better inferences.
- **Clarity in Prompts**: Create prompts that give clear cues for better inference.
- **Test and Iterate**: Evaluate and refine ChatGPT responses to improve accuracy.

#### Conclusion

- Understanding and utilizing inference in ChatGPT enables richer and more meaningful interactions.

---

You can use this summary as a quick reference for understanding how ChatGPT uses inference to better interact with users.

## Transforming with ChatGPT

#### What is Transforming?

- Transforming in ChatGPT means rewriting text, reframing ideas, summarizing information, translating languages, and generating new content.
- It enables the user to tailor ChatGPT's responses to suit specific contexts and audiences, thereby enhancing its versatility.

#### Significance:

- Allows users to explore different perspectives and generate unique text variations.
- Adapts responses to suit different contexts, audience types, or formatting requirements.

#### Applications and Examples:

1. **Text Rewriting**: ChatGPT can rewrite an email from casual to formal tone.
2. **Idea Reframing**: It can provide different article title variations for the topic "The Importance of Education."
3. **Summarization**: Capable of summarizing long articles into short summaries.
4. **Language Translation**: Translates text between languages.
5. **Content Generation**: Can generate story continuations, creative writing prompts, and product descriptions.

#### Strategies for Effective Transforming:

- Be specific with your instructions and guidelines.
- Consider the context and purpose for which you're asking the transformation.
- Iteratively refine your prompts to get better results.

This page essentially lays out the power of transforming capabilities in ChatGPT, detailing its applications and how to leverage it effectively. The aim is to help users craft better prompts and explore creative possibilities.

Hope this helps you grasp the capabilities of ChatGPT's transforming feature! Let me know if you have any more questions or need further clarifications.

## Expanding with ChatGPT

#### Key Points:

1. **What is Expanding?**: Expanding with ChatGPT refers to the process of adding more detail and context to an initial idea or question, aiming to provide comprehensive and informative answers.

2. **Importance of Expanding**:

- Enables in-depth exploration of concepts.
- Offers well-rounded, background-supported responses.
- Enhances user experience with informative and comprehensive replies.

3. **Use Cases and Examples**:

- **Detailed Explanations**: ChatGPT can break down complex subjects into simpler terms.
- **Supporting Evidence**: Adds credibility by presenting facts, studies, or expert opinions.
- **Elaborating on Examples**: Gives more details and context around provided examples.
- **Historical Context**: Can offer background history for a better understanding of a topic.

4. **Strategies for Effective Expansion**:

- Be specific in your prompts.
- Align the context and purpose of the expansion.
- Use iterative refinement of prompts to obtain more accurate and detailed outputs.

5. **Iterations for Refinement**:

- **Example 1**: Starts with a broad prompt like "Expand on the topic of dogs" and refines it to focus on specific traits and living conditions.
- **Example 2**: Further refines the prompt to request information on five popular dog breeds and their exercise routines.

By using the expansion feature effectively, ChatGPT can offer richer and more detailed conversations, catering to a wide range of topics and user needs.

Keep this as a quick reference for effectively leveraging the 'expanding' capability of ChatGPT to generate more detailed and insightful content.

## Formatting Output with ChatGPT

### Summary: Formatting Output with ChatGPT

**Key Topics:**

- Understanding format and sequence requirements
- Adapting output to tabular formats
- Handling sequential output
- Incorporating headers or titles
- Formatting lists or bullet points
- Incorporating emphasis or styling

**Overview:**

This guide discusses best practices for formatting and structuring output when working with language models like ChatGPT. By tweaking the input prompts, you can tailor the generated output to match various formats and sequences.

**Key Points:**

1. **Format and Sequence Requirements**: Carefully analyze the input prompt to discern any specific format or sequence requirements. Align your output accordingly.

2. **Tabular Formats**: When a table is required, format the output into clearly separated columns and rows. This is especially useful for scientific data representation.

3. **Sequential Output**: For prompts needing a sequential answer, make sure that each part follows logically from the one before it. This is handy for step-by-step guides.

4. **Headers or Titles**: Include clear headers for sections or data points to provide context and structure, useful in reports or segmented information.

5. **Lists and Bullet Points**: If a list is required, mention it in the prompt. Use bullet points for easy readability.

6. **Emphasis and Styling**: Use techniques like bold, italics, or underlining for emphasizing key terms or sections.

This guide helps you create outputs that are not only informative but also easy to read and well-structured, making the information more comprehensible.

## Best Practices for Prompting

#### Key Points:

1. **Detailed Description**: Offering specific details while prompting ChatGPT improves the accuracy and relevance of generated responses.

   - _Example_: Instead of "recommend a book," specify preferred genres or themes.

2. **Contextual Understanding**: Providing context allows ChatGPT to generate responses that better align with the situation or topic.

   - _Example_: Don't just ask "What's the weather like?" Say, "I'm planning a beach outing; what's the weather like?"

3. **Incorporating Specific Examples**: Using concrete examples helps in getting more practical and tailored advice.

   - _Example_: Instead of asking for general programming advice, provide a specific code snippet.

4. **Rich Language & Sensory Details**: Descriptive language makes for more engaging and appropriate responses.

   - _Example_: Instead of asking for a simple recipe, provide specific tastes and cooking techniques you're interested in.

5. **Iterative Prompt Refinement**: Continuously tweaking and refining prompts can lead to more precise and desired outputs.
   - _Example_: Start with "Write a poem about love," and refine to "Write a poem about enduring love, inspired by a couple’s 50th anniversary."

#### Takeaway:

Effective prompting with ChatGPT involves multiple layers: detailed description, context, specific examples, rich language, and prompt refinement. These elements collectively enable better communication and more relevant outputs for various tasks.
