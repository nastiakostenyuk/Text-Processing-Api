import nltk
from nltk.tokenize import word_tokenize


async def tokenize_text(text: str) -> list[str]:
    """
     Tokenize the text into a list of words.

     Args:
         text (str): Text to be tokenized.

     Returns:
         list[str]: A list of strings where each string represents a token.
    """
    return word_tokenize(text)


async def pos_tag_text(text: str) -> list[tuple[str, str]]:
    """
    Function performs Part-of-Speech (POS) tagging on the text.

    Args:
        text (str): Text to be tagged.

    Returns:
        list[tuple[str, str]]: A list of tuples where each tuple contains a word
                                from the input text paired with its corresponding
                                Part-of-Speech tag.
    """

    tokenized_text = await tokenize_text(text)
    return nltk.pos_tag(tokenized_text)


async def ner_text(text: str) -> list[tuple[str, str]]:
    """
    Function performs Named Entity Recognition (NER) on the text.

    Args:
        text (str): Text to be analyzed for named entities.

    Returns:
        list[tuple[str, str]]: A list of tuples, where each tuple contains a named entity label and word.
    """
    pos_text = await pos_tag_text(text)
    chunks = nltk.ne_chunk(pos_text)
    entities = []
    for chunk in chunks:
        if hasattr(chunk, 'label'):
            entities.append((chunk[0][0], chunk.label()))
    return entities
