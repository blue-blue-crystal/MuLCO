# Empowering LLMs for Multi-Page Layout Generation via Consistency-Oriented In-Context Learning
![method](/images/main.png)
**Multi-Page Layout Generation via Consistency-Oriented modeling (MuLCO), a data-efficient and training-free multi-page layout generation framework built upon in-context learning.**

## Dataset
![method](/images/dataset.png)
we construct the first dataset MPDoc for multi-page layout generation, which is collected from the arXiv website. Subsequently, leveraging PP-Structure, an intelligent document analysis system developed by the PaddleOCR team 1 , we recognize layouts and annotate the positions and sizes of each element. To promote the identification accuracy, we remove the reference part and perform a manual double check. We divide the dataset into exemplar docs (used for searching nearest neighbor documents) and query docs (used for extracting constraints for LLMs to generate layouts). Finally, as shown in Table 1, we obtain MPDoc dataset with an average page number 𝑁 of 5.8 and an average element number of 9.9

## Results
![method](/images/qualititive_result.png)
*Our task is to predict the position and size of the element based on its category and located page.* Since there is no relevant work on multi-page document layout generation within
our knowledge to compare, we have selected some representative single-page layout generation work in recent years as the baselines and implement these models to generate document layouts page by page, whereas our approach is to regard multi-page layout generation task as a whole. Thus, we compare our method with four strong baselines, including 
 `LayoutTrans`, `LayoutDiffusion`, `LayoutFormer++`, `LayoutPrompter`.
