Automating text recognition and transliteration of historical documents with weighted convolutional - recurrent architectures



This project aims to develop an automated text recognition and transliteration system for historical Spanish documents from the 17th century. Traditional OCR tools struggle with early printed texts, so this project employs a hybrid CNN-RNN model enhanced with weighted learning techniques and lexicon-based constrained beam search decoding to improve recognition accuracy.

Methods Used
Hybrid CNN-RNN Model: Combines convolutional layers (for feature extraction) with recurrent layers (for sequential text recognition).

Weighted Learning Techniques: Prioritizes rare letterforms, diacritics, and unique symbols found in historical Spanish prints.

Lexicon-Constrained Beam Search Decoding: Uses a renaissance Spanish lexicon to reduce hallucinations and improve word-level accuracy.

Expected Results
A trained machine learning model capable of recognizing non-standard printed text with at least 80% accuracy.

Improved text extraction for historical Spanish documents, making them more accessible for research and study.

Tools & Technologies
Programming Language: Python

Frameworks: TensorFlow/PyTorch

OCR Techniques: CNN-RNN for sequence modeling

Data Processing: Historical Spanish text datasets
