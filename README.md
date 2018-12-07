# California_PageRank

## Dataset
- Source: http://www.cs.cornell.edu/courses/cs685/2002fa/data/gr0.California
- Size: 25814 lines
- Dataset sample:
  - `n 0 http://www.berkeley.edu/` (the page index of http://www.berkeley.edu/ is 0)
  - `e 80 3301` ( there is a link from page 80 to page 3301)

## [Project Structure](https://github.com/ece143-fa18-group10/Wikidata_PageRank/tree/master/project)
### [data](https://github.com/ece143-fa18-group10/Wikidata_PageRank/tree/master/project/data)
The dataset we used in the project and results of dataset preprocessing.

### [source code](https://github.com/ece143-fa18-group10/Wikidata_PageRank/tree/master/project/source%20code)

| file | description |
| - | - |
| PageRank.py | run the PageRank algorithm |
| PageRank_matrix.py | generate the PR matrix |
| build_trans_mat.py | generate the transition matrix |
| preprocessing data.py | preprocess the California dataset |
| background_visualization.py | generate images to introduce the background of the project |

### [visualization](https://github.com/ece143-fa18-group10/Wikidata_PageRank/tree/master/project/visualization)

| folder | description |
| - | - |
| images | includes visualization images |
| [web page](https://ece143-fa18-group10.github.io/Wikidata_PageRank/) | includes files to generate the web page to visualize PageRank |

### [docs](https://github.com/ece143-fa18-group10/Wikidata_PageRank/tree/master/project/docs)
The proposal and the slide of presentation.
