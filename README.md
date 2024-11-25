# voro-south-estonian
Python code for extracting data about Võro South Estonian (võro kiil')

## Description

This repository contains a series of Python scripts for extracting words from the dictionary "võro-eesti-võro sõnaraamat" compiled by the võro instituut. The scripts begin with a plaintext file derived from the dictionary. They retain words which have associated audio files (anticipating future phonetic work), add inflectional information, and only save words which contain the vowel <i> because of its linguistic properties in the vowel harmony system of the language. The marking of palatalisation is standardised, and the consonantal digraphs are replaced (<ts> by <c> and <ds> by <z>). The final plaintext file output by the script contains 678 dictionary headwords on each line, many of which contain two additional inflected forms (separated by space).

## How to cite

Please cite both the source of the data as well as this GitHub repo. Suggested citations:

Andersson, S. (2024). voro-south-estonian. <https://github.com/SJAndersson/voro-south-estonian> [Accessed YYYY-MM-DD]

Võro instituut. (2002). Võro-eesti-võro sõnaraamat. <https://synaq.org> [Accessed YYYY-MM-DD]
