# Empowering LLMs for Multi-Page Layout Generation via Consistency-Oriented In-Context Learning
![method](/images/main.png)
**Multi-Page Layout Generation via Consistency-Oriented modeling (MuLCO), a data-efficient and training-free multi-page layout generation framework built upon in-context learning.**

## Dataset
<img src="/images/dataset.png" width="600px">

### Introduction
we construct the first dataset **MPDoc** for multi-page layout generation, which is collected from the arXiv website. Subsequently, leveraging PP-Structure, an intelligent document analysis system developed by the [PaddleOCR team](https://github.com/PaddlePaddle/PaddleOCR), we recognize layouts and annotate the positions and sizes of each element. To promote the identification accuracy, we remove the reference part and perform a manual double check.
### Composition
We divide the dataset into 900 `exemplar docs` (used for searching nearest neighbor documents) and 339 `query docs` (used for extracting constraints for LLMs to generate layouts), which contains five element categories inculuding `text`, `table`, `title`, `figure`, `list`.
### Doc File Structure
* 'labels': A two-dimensional tensor where each entry corresponds to the categories of elements on a page in this document.
* 'bboxes': A three-dimensional tensor where each two-dimensional slice represents the layout data for all elements on a page in this document, with each element described in the form `[Left, Top, Width, Height]`.
```text
{
'doc_name': ['×××'],
'page_num': [7],
'canvas_size': [792, 612],
'labels':tensor([
                 [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 5, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 5, 5, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 2, 2, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 4, 4, 4, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0]
                ]),
'bboxes': tensor([
                  [[0.5212, 0.3472, 0.9167, 0.7487],
                   [0.0866, 0.6540, 0.4820, 0.8902],
                                ...
                   [0.0000, 0.0000, 0.0000, 0.0000]],
                  ...
                  [[0.0866, 0.3409, 0.4820, 0.5492],
                   [0.5212, 0.3346, 0.9150, 0.7083],
                                ...
                   [0.0000, 0.0000, 0.0000, 0.0000]]
                  ])
}
```

## Results
![method](/images/qualititive_result.png)
*Our task is to predict the position and size of the element based on its category and located page.* Since there is no relevant work on multi-page document layout generation within
our knowledge to compare, we have selected some representative single-page layout generation work in recent years as the baselines and implement these models to generate document layouts page by page, whereas our approach is to regard multi-page layout generation task as a whole. Thus, we compare our method with four strong baselines, including 
 `LayoutTrans`, `LayoutDiffusion`, `LayoutFormer++`, `LayoutPrompter`.
