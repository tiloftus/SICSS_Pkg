An example package used for SICSS. The package provides multiple simple functions to be used for text analysis. These functions are count_words, get_top_n_words, and avg_word_length. To run the functions on text files, the functions run_count_words_from_file, run_top_words_from_file, and run_avg_words_from_file are included.

1. Take a look at core.py to see these functions. Also, feel free to look at setup.py and __init__.py while exploring the file structure of the package directory as a whole.

2. Open the file example.ipynb, which is just an empty Python notebook. 

3. In a code cell, install the example package, which is called SICSS_Pkg. In addition to the example package I made, you will also need to install nltk, a popular Python package for working with human language data.
```
!pip install -e .
!pip install nltk
```
After you install the packages, you might have to restart the kernel (Kernel -> Restart Kernel).

4. The directory also includes a file containing a famous speech. Now that the package is installed, import one of its functions and count the number of words in the speech.
```
from SICSS_Pkg.core import run_count_words_from_file
run_count_words_from_file("speech.txt")
```

5. Feel free to also use run_avg_words_from_file on speech.txt by importing it and running it the same way.

6. Import and run run_top_words_from_file to get the most common words in speech.txt.

7. You'll notice the most common words are words like "the", "and", and "be", which get in the way of useful findings. Inside core.py, find the list of stop words and expand it to exclude those common cases. Since you're changing the package, you need to reinstall. After making the changes you'd like to core.py, in example.ipynb, rerun !pip install -e . to reinstall the edited package. You may need to then restart the kernel again. After this, you can redo step 6 and hopefully get better results. 

8. Now that you know how to edit, install, and use a Python package, you can make any edits you please to the package by changing the functions in core.py or adding your own. One idea could be to add a function that counts the number of sentences using punctuation marks. 