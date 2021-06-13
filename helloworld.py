import streamlit as st
import numpy as np
import pandas as pd

from scipy.special import perm,comb


st.title("Permutations and Combinations")

total = st.slider('Total balls')

select = st.slider('Selected balls')


#选择排列还是组合
problem_class=st.radio('Permutation or Combination？',('Permutation','Combination'))

#输出排列数或组合数，以及所有结果
if problem_class == 'Permutation':
    st.write('Number of permutations is', int(perm(total,select)))
else:
    st.write('Number of combinations is', int(comb(total,select)))
