# Sequential Recommendation Systems
Repository for Deep Learning Spring 2022 Project: Sequential Recommendation Systems Using Stochastic Self- Attention Sequential Model

Contributors:
1.  Sankalp Apharande, Columbia University, New York, NY 10027 (Email: spa2138@columbia.edu)

2.  Aarushi Jain, Columbia University, New York, NY 10027 (Email: aj3087@columbia.edu)

3.  Vishweshwar Tyagi, Columbia University, New York, NY 10027 (Email: vt2353@columbia.edu)
    
    
    
**Background:**  
     The existing models fail to incorporate dynamic uncertainty in users’ real-life sequential behavior and also fail to incorporate collaborative transitivity. Another limitation of this model is the failure
to capture collaborative transitivity due to dot-product self-attention. Collaborative transitivity can capture the latent similarity between item-item relationships. For example, if a->b and b->c, the dot
product self-attention mechanism will identify the relationship between items (a,b), and (a, c). But, it would fail to realize the relationship between a and
    
**Problem Statement:**  
     The problem statement is: Given a set of users U and items V and their associated interactions in chronological order, our goal is to recommend topN items as potential next item in the sequence
by incorporating the user’s dynamic uncertainty in choices and collaborative transitivity in item interactions.

**About Code**
1. dataset_insights/h&m _dataset_analysis.ipynb : initial exploratory data analysis of H&M Dataset
2. kaggle_submission_notebooks: to generate submission to be uploaded to Kaggle
   1. GRU4Rec_submission.ipython: Notebook to generate recommendation from trained gru4rec model 
   2. SAS4Rec_submission.ipython: Notebook to generate recommendation from trained SASRec model
   3. stosa.ipython: Notebook for post-processing of generated results from STOSA Model.
3. Models: various models which we implemented
   1. ensemble: contains notebook to generate results for traditional baseline model results and their weighted ensemble
   2. stochastic_self_attention_model: This is the main model of this project. Sequential
Recommendation via Stochastic Self-Attention
   3. GRU4Rec.ipython: Deep Learning model for Session-based Recommendations with Recurrent Neural Networks
   4. SASRec.ipython: Self-Attentive Sequential Recommendation
4. preprocessing: Notebooks for preprocessing:
   1. fetch_data.ipython: Notebook to fetch dataset from Kaggle
   2. generate_sequences.py: Python script to generate sequences from transaction dataset
   3. make_atomic.ipython: Python script to preprocess transction data for GRU4Rec and SASRec models
   4. stosa_preprocessing: Notebook for preprocessing the dataset for STOSA model

**How to Run our model:**
1. First run the notebook preprocessing/fetch_data.ipynb to fetch the dataset from Kaggle
2. Then run the notebook preprocessing/stosa_preprocess.ipynb to generate required sequences for STOSA model
3. Then run the notebook kaggle_submission_notebook/stosa.ipython to train the model
Please note that you may have to set up the directory structure and set up working directory path to run these notebooks successfully.


**Hyperparameters Used for STOSA**

 `hidden_size`: 128
 
 `num_hidden_layers`: 1
 
 `num_attention_heads`: 4
 
 `hidden_act`: gelu
 
 `hidden_dropout_prob`: 0.3
 
 `max_seq_length`: 50
 
 `distance_metric`: wasserstein
 
 `lr`: 0.01
 
 `batch_size`: 4096
 
 `epochs`: 20


For reference, please check this Google Drive folder where we have setup the required directory structure: [Google Drive](https://drive.google.com/drive/folders/1CnLcU39SUHvt1RmG2MGl9bX_JRLYe-8I) 

Processed dataset for GRU4Rec and SASRec - [Google Drive Link](https://drive.google.com/file/d/1-aEgADVM5yhCmIYgZvkmvZCremX5L-Ma/view?usp=sharing)

Processed dataset for STOSA - [Google Drive Link](https://drive.google.com/file/d/1cN9yVLZwxPCopT2h24CH3NfdTXD-N8P7/view?usp=sharing)



**Results:**  
Achieved **MAP@12 of 0.0236** by ensemble of STOSA and [1]. 

**Submission File:**  
STOSA Submission File: [Link](https://drive.google.com/file/d/1-1LMlI-JQbumQ7v_cbQFISMztCK_XIBt/view)  
Current Position on the leaderboard: 394 out of 2,348 teams (as of April 20th 2022)

 **Other Results**
 1. GRU4Rec recommendations submission file: [Link](https://drive.google.com/file/d/1-TyxM0xLUG23IOD2DYTJLSVGkSOiUeH3/view)
 2. SASRec submission file: [Link](https://drive.google.com/file/d/1-9y75BARyo70jLSMjcpYtwdfkNjXtYA-/view?usp=sharing)
 

Reference:
1. For Ensemble Model: https://www.kaggle.com/code/atulverma/h-m-ensembling-with-lstm 

