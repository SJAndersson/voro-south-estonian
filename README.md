# voro-south-estonian
Python and R code for analysing Võro South Estonian (võro kiil')

## Description

This repository contains a series of Python scripts for extracting words from the dictionary "võro-eesti-võro sõnaraamat" compiled by the võro instituut. The scripts begin with a plaintext file derived from the dictionary. They retain words which have associated audio files (anticipating future phonetic work), add inflectional information, and only save words which contain the vowel < i > because of its linguistic properties in the vowel harmony system of the language. The marking of palatalisation is standardised, and the consonantal digraphs are replaced (< ts > by < c > and < ds > by < z >). The final plaintext file output by the script contains 6043 dictionary headwords on each line, many of which contain two additional inflected forms (separated by space).

The repo also contains R code for modality testing with Monte Carlo simulations using Hartigans' dip test statistic. It offers a more reliable way to calculate whether a vector contains uni- or bimodal data in cases where, if the data are bimodal, the means are expected to be close together.

## How to cite

Please cite both the source of the data as well as this GitHub repo. Suggested citations:

Andersson, S. (2024). voro-south-estonian. <https://github.com/SJAndersson/voro-south-estonian> [Accessed YYYY-MM-DD]

Võro instituut. (2002). Võro-eesti-võro sõnaraamat. <https://synaq.org> [Accessed YYYY-MM-DD]
